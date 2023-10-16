const fs = require('fs')
const { parse } = require('csv-parse')

const sqlite3 = require('sqlite3').verbose()
let init = true

if (fs.existsSync('webapp.db')) {
    init = false
}

const db = new sqlite3.Database('./webapp.db')
if (init) {
    process.exit(0)
}
// https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.76.zip
if (!fs.existsSync('worldcities.csv')) {
    console.log('Downloading worldcities.csv')
    const fetch = require('node-fetch')
    const {pipeline} = require('stream')
    const {promisify} = require('util')
    const {createWriteStream} = require('fs')
    const decompress = require('decompress')

    const streamPipeline = promisify(pipeline)
    fetch('https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.76.zip')
        .then(response => {
            if (!response.ok) throw new Error('Download failed')
            console.log('Donwload completed')

            streamPipeline(response.body, createWriteStream('./worldcities.zip'))
                .then(() => {
                    decompress('worldcities.zip', 'world')
                        .then(() => {
                            fs.renameSync('./world/worldcities.csv', './worldcities.csv')

                            db.exec('CREATE TABLE cities (name VARCHAR(250), country VARCHAR(250), population INT)', (err) => {
                                console.log(err)
                            })
                        
                            fs.createReadStream("./worldcities.csv")
                                .pipe(parse({ delimiter: ',', from_line: 2}))
                                .on("data", function (row) {
                                    db.serialize(function () {
                                        db.run(
                                            'INSERT INTO cities VALUES (?, ?, ?)',
                                            [row[0], row[4], row[9]],
                                            function (error) {
                                                console.log(this.lastID)
                                            }
                                        )
                                    })
                                })
                                .on("end", function () {
                                    console.log("finished.")
                                })
                                .on("error", function (error) {
                                    console.error(error.message)
                                })
                        
                            db.exec('CREATE TABLE flag (name VARCHAR(250))', (err) => {
                                console.log(err)
                            })
                        
                            db.run('INSERT INTO flag VALUES ("BTU{SQL_INJECTION_FLAG}")')
                        })
                })
        })
}