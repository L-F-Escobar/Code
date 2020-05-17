const fs = require('fs-extra')

fs.copy('frontend', 'local', function (err) {
    if (err) {
      console.error(err);
    } else {
      console.log("success!");
    }
}); //copies directory, even if it has subdirectories or files