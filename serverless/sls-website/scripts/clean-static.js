'use strict'

const exec = require('child_process').exec

const BUCKET = "recallmaster-sls-url-shortener.com"
const REGION = 'us-east-1'

let command = `aws s3 rm s3://${BUCKET} --recursive --exclude favicon.png --exclude index.html --exclude jquery-3.2.1.min.js --exclude paper.min.css`

exec(command, function (error, stdout, stderr) {
  if (stderr) {
    console.error('Clean static bucket error')
    console.error('---')
    console.error(stderr)
  } else {
    console.log('Cleaned static bucket')
    console.log(`http://${BUCKET}.s3-website-${REGION}.amazonaws.com/`)
    console.log('---')
    console.log(stdout)
  }
})

