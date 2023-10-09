const express = require('express')
const app = express()

const sqlite3 = require('sqlite3').verbose()
const db = new sqlite3.Database('./webapp.db')

app.get('/search', async (req, res) => {
    const city = req.query.city

    const result = await db.all(`SELECT *
                                 FROM cities
                                 WHERE name LIKE "${city}"`, [], (_, rows) => {
        console.log(rows)
        res.send(rows)
    })
})

app.use(express.static('./public'))

app.listen(8080)