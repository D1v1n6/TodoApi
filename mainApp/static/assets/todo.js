function myFunction() {
    let x = document.getElementById("email").value;

    let text;
    if (x === '') {
        text = "Please Input An Email";
    } else {
        text = "Email OK!";
    }
    document.getElementById("check").innerHTML = text;
}