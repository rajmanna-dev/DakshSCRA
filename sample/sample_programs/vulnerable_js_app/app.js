const express = require('express');
const bodyParser = require('body-parser');
const fileUpload = require('express-fileupload');
const { exec } = require('child_process');
const path = require('path');
const app = express();

// Hardcoded secret key
const SECRET_KEY = 'hardcoded_secret';

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(fileUpload());
app.use(express.static('uploads'));

// Home Route (XSS Vulnerability)
app.get('/', (req, res) => {
  const message = req.query.message || 'Welcome to the Vulnerable Node App!';
  res.render('index', { message });
});

// Command Injection Vulnerability
app.post('/run', (req, res) => {
  const command = req.body.command;
  exec(command, (error, stdout, stderr) => {
    if (error) {
      res.send(`Error: ${stderr}`);
    } else {
      res.send(`Output: ${stdout}`);
    }
  });
});

// Insecure File Upload
app.post('/upload', (req, res) => {
  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send('No files were uploaded.');
  }

  const file = req.files.file;
  const uploadPath = path.join(__dirname, 'uploads', file.name);

  // No validation of file type
  file.mv(uploadPath, err => {
    if (err) {
      return res.status(500).send(err);
    }
    res.send('File uploaded!');
  });
});

app.listen(3000, () => {
  console.log('App running on http://localhost:3000');
});
