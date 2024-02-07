function register(){
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("pass").value;
    var confirmPass = document.getElementById("con_pass").value;
    var message = document.getElementById("message").value;

    if(password !== confirmPass){
        message.innerHTML = "Passwords do not match.";
        message.style.color = "red";
    }else {
        message.innerHTML = "Registration successful";
        message.style.color = "green";
    }

    message.classList.remove("hidden");
}
