const url = require('url')
const AWS = require('aws-sdk')
const S3 = new AWS.S3()


module.exports.handle_website = (event, context, callback) => {
  console.log("event --> " + JSON.stringify(event));
  console.log("event.body --> " + JSON.stringify(event.body));
  console.log("(event.body).url --> " + JSON.parse(event.body).url);
  console.log("(event.body).vanity --> " + JSON.parse(event.body).vanity);

  let longUrl = JSON.parse(event.body).url || '';
  console.log("Longurl --> " + longUrl);

  validate(longUrl)
    .then(function () {
      console.log('ONE')
      return getPath()
    })
    .then(function (path) {
      console.log('TWO')
      console.log("path --> " + path);
      let redirect_code = buildRedirect(path, longUrl)
      return saveRedirect(redirect_code)
    })
    .then(function (path) {
      console.log('THREE')
      console.log("path --> " + path);
      let response = buildResponse(200, 'success', path)
      console.log("response --> " + JSON.stringify(response));
      return Promise.resolve(response)
    })
    .catch(function (err) {
      console.log('pre FOUR - ERROR')
      let response = buildResponse(err.statusCode, err.message)
      return Promise.resolve(response)
    })
    .then(function (response) {
      console.log('FIVE - pre-RESPONSE')
      callback(null, response)
    })
}


function buildResponse (statusCode, message, path = false) {
  let body = { message }
  if (path) body['path'] = path

  console.log(`\nIn buildResponse`)
  console.log(`body --> ${body}`)

  return {
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
    statusCode: statusCode,
    body: JSON.stringify(body)
  }
}


function validate (longUrl) {
  if (longUrl === '') {
    return Promise.reject({
      statusCode: 400,
      message: 'URL is required'
    })
  }

  let parsedUrl = url.parse(longUrl)
  if (parsedUrl.protocol === null || parsedUrl.host === null) {
    return Promise.reject({
      statusCode: 400,
      message: 'URL is invalid'
    })
  }

  return Promise.resolve(longUrl)
}


function generatePath (path = '') {
  /*
  Recursive function. Appends {path} one at a time till its 7 
  random characters long.

  Returns:
  - path (str) : 7 random characters.
  */
  console.log("generatePath");
  let characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  let position = Math.floor(Math.random() * characters.length)
  let character = characters.charAt(position)

  if (path.length === 7) {
    console.log("generatePath is finished --> " + path);
    return path
  }

  return generatePath(path + character)
}


// https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#headObject-property
function isPathFree (path) {
  /*
  Function looks for a bucket object {buildRedirect(path)}. If object is found,  
  path is not free. Throws an error if the object is not found, catch not found error
  and reject all others.

  Returns
  - bool : False = path is not free.
           True = path is free.
  */
  console.log('IN isPathFree')
  return S3.headObject(buildRedirect(path)).promise()
    .then(() => Promise.resolve(false))
    .catch(function (err) {
      console.log('IN isPathFree CATCH')
      if (err.code == 'NotFound') {
        console.log('IN isPathFree CATCH IF')
        return Promise.resolve(true)
      } else {
        console.log('IN isPathFree CATCH ELSE')
        return Promise.reject(err)
      }
    })
}


function buildRedirect (path, longUrl = false) {
  let redirect = {
    'Bucket': process.env.BUCKET,
    'Key': path
  }

  if (longUrl) {
    redirect['WebsiteRedirectLocation'] = longUrl
  }

  console.log('redirect object --> ' + JSON.stringify(redirect))

  return redirect
}


function getPath () {
  /*
  Function will execute until it resolves with a valid 7 character path.
  First, generate a 7 character path, then check if the path already exists in 
  S3. If the path exists, run the function again.

  Returns
  - path (str) : path appened to shortened endpoint.
  */
  console.log("In getPath");
  return new Promise(function (resolve, reject) {
    let path = generatePath()
    console.log("Back in getPath after generatePath");
    isPathFree(path)
      .then(function (isFree) {
        console.log("isFree --> " + isFree);
        console.log("path --> " + path);
        console.log("End getPath");
        return isFree ? resolve(path) : resolve(getPath())
      })
  })
}

// https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#putObject-property
function saveRedirect (redirect) {
  return S3.putObject(redirect).promise()
    .then(() => Promise.resolve(redirect['Key']))
    .catch(() => Promise.reject({
      statusCode: 500,
      message: 'Error saving redirect'
    }))
}
