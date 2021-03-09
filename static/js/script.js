$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });


// The following password validation method was found: https://codepen.io/diegoleme/pen/surIK

var password = document.getElementById("password")
  , confirm_password = document.getElementById("password_confirm");

function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;