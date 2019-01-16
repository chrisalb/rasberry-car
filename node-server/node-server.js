const express = require('express')
const app = express()
const port = 3000
const fs = require('fs')

app.engine('ntl', function (filePath, options, callback) { // define the template engine
  fs.readFile(filePath, function (err, content) {
    if (err) return callback(err)
    var rendered = content.toString().replace('#title#', '<title>' + options.title + '</title>')
        .replace('#message#', '<h1>' + options.message + '</h1>')
    return callback(null, rendered)
  })
})

app.set('views', './views')
app.set('view engine', 'ntl')
app.use('/assets', express.static('assets'))

app.get('/', (req, res) =>
    res.render('index', {}))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))



