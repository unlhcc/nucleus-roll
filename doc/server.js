#!/usr/bin/env node

var path = require('path');
var swaggerSuite = require('swagger-suite');  // you can just use require('swagger-suite') in your apps

//
// Load the Swagger file
// ----------------------------------------
var server = swaggerSuite(path.join(__dirname, 'api.yaml'));


// This an Express error-handler middleware (notice the extra "err" parameter).
// It will only be called if an error occurs.  See http://expressjs.com/guide/error-handling.html
server.use(function(err, req, res, next) {
  // Return all errors as a custom "errorModel" object
  var errorModel = {
    code: err.status || 500,
    message: err.message || 'Unknown Error'
  };

  res.status(errorModel.code).json(errorModel);
});


//
// Start listening for requests
// ----------------------------------------
server.start();

