const url = require('url')
const AWS = require('aws-sdk')
const S3 = new AWS.S3()


module.exports.handle_shortener = (event, context, callback) => {
  console.log("event --> " + JSON.stringify(event));
  console.log("event --> " + JSON.stringify(JSON.parse(event.body)));

  let longUrl = JSON.parse(event.body).url || '';
  console.log("Longurl --> " + longUrl);

  validate(longUrl)
    .then(function () {
      console.log('ONE')
      return getPath()
    })
    .then(function (path) {
      console.log('TWO')
      let redirect = buildRedirect(path, longUrl)
      return saveRedirect(redirect)
    })
    .then(function (path) {
      console.log('THREE')
      let response = buildResponse(200, 'success', path)
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
  let characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  let position = Math.floor(Math.random() * characters.length)
  let character = characters.charAt(position)

  if (path.length === 7) {
    return path
  }

  return generatePath(path + character)
}


function isPathFree (path) {
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
  console.log('IN buildRedirect')
  console.log('process.env.BUCKET --> ' + process.env.BUCKET)
  let redirect = {
    // 'Bucket': config.BUCKET,
    'Bucket': process.env.BUCKET,
    'Key': path
  }

  if (longUrl) {
    redirect['WebsiteRedirectLocation'] = longUrl
    console.log('redirect --> ' + redirect)
  }

  return redirect
}
// value="http://example.com"

function getPath () {
  return new Promise(function (resolve, reject) {
    let path = generatePath()
    console.log("Path --> " + path);
    isPathFree(path)
      .then(function (isFree) {
        console.log("isFree --> " + isFree);
        return isFree ? resolve(path) : resolve(getPath())
      })
  })
}


function saveRedirect (redirect) {
  return S3.putObject(redirect).promise()
    .then(() => Promise.resolve(redirect['Key']))
    .catch(() => Promise.reject({
      statusCode: 500,
      message: 'Error saving redirect'
    }))
}







// // split into another file
// module.exports.handle_upload = (event, context, callback) => {
//   console.log("event --> " + JSON.stringify(event));

//   let response = buildResponse(200, 'success')

//   // const response = {
//   //   headers: {
//   //     'Access-Control-Allow-Origin': '*'
//   //   },
//   //   statusCode: 200,
//   //   body: "From api gateway"
//   // }
//   console.log("response --> " + JSON.stringify(response));
//   callback(null, response);
// }