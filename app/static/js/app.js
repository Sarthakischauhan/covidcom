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
const openbtn = document.querySelectorAll(".check");
const closebtn = document.querySelectorAll(".close");
const vaccine = document.querySelector(".vaccine-modal");
const oxygen = document.querySelector(".oxygen-modal");
const plasma = document.querySelector(".plasma-modal");


openbtn.forEach(function(btn){
  btn.addEventListener('click',function(){
    modal.classList.add("open-modal");
    if (btn.classList.contains("vaccine")){
      vaccine.style.display="flex";
    }
    else if (btn.classList.contains("oxygen")){
      oxygen.style.display="flex";
    }
    else if (btn.classList.contains("plasma")){
      plasma.style.display = "flex";
    } 
  })
})
closebtn.forEach(function(btn){
  btn.addEventListener('click',function(){
    modal.classList.remove("open-modal");
    if (btn.classList.contains("vaccine")){
      vaccine.style.display="none";
    }
    else if (btn.classList.contains("oxygen")){
      oxygen.style.display="none";
    }
    else if (btn.classList.contains("plasma")){
      plasma.style.display = "none";
    } 
  })
})






closebtn.addEventListener('click',function(){
  modal.classList.remove("open-modal");
})
