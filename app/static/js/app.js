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
      document.cookie = "latitude="+String(startPos.coords.latitude);
      document.cookie = "longitude="+String(startPos.coords.longitude);
    };

    var geoError = function(error) {
      console.log('Error occurred. Error code: ' + error.code);
    }; 
  
    navigator.geolocation.getCurrentPosition(geoSuccess, geoError, geoOptions);
}

const modal = document.querySelector(".modal");
const openbtn = document.querySelector(".check");
const closebtn = document.querySelector(".close");

openbtn.addEventListener('click',function(){
  modal.classList.add("open-modal");
  console.log("run");
})


closebtn.addEventListener('click',function(){
  modal.classList.remove("open-modal");
})
