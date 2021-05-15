window.onload = function() {
    getLocation()
};
  

function getLocation(){
    var startPos;
    var geoOptions = {
       timeout: 10 * 1000
    }
  
    var geoSuccess = function(position) {
      startPos = position;
    //   document.getElementById('startLat').innerHTML = startPos.coords.latitude;
    //   document.getElementById('startLon').innerHTML = startPos.coords.longitude;
      console.log(startPos.coords.latitude);
      console.log(startPos.coords.longitude);
      document.cookie = "latitude="+String(startPos.coords.latitude);
      document.cookie = "longitude="+String(startPos.coords.longitude);
    };

    var geoError = function(error) {
      console.log('Error occurred. Error code: ' + error.code);
      // error.code can be:
      //   0: unknown error
      //   1: permission denied
      //   2: position unavailable (error response from location provider)
      //   3: timed out
    }; 
  
    navigator.geolocation.getCurrentPosition(geoSuccess, geoError, geoOptions);
}

