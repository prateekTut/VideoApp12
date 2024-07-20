// Handle tab switching
function openCategory(evt, categoryName) {
  var i, tabcontent, tablinks;

  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  document.getElementById(categoryName).style.display = "block";
  evt.currentTarget.className += " active";
}

// Display the first category by default
document.addEventListener("DOMContentLoaded", function () {
  document.getElementsByClassName("tablink")[0].click();
});

// Form handling and redirection (mockup, replace with actual logic)
document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();
  // Perform login logic
  window.location.href = "home.html"; // Redirect to home page
});

document.getElementById("signupForm").addEventListener("submit", function (e) {
  e.preventDefault();
  // Perform signup logic
  window.location.href = "login.html"; // Redirect to login page
});
