console.log('lol')
function CallJSON() {
    console.log('called')
    let x = document.forms["Assignment11"]["x-js"].value;
    let add = "https://reqres.in/api/users/" + x
    fetch(add)
        .then(response => response.json())
        .then(responseJSON => {
            let userData = document.getElementById("UserData")
            console.log(responseJSON)
            console.log(userData)
            userData.innerHTML = JSON.stringify(responseJSON)
        })
        .catch(err => console.log(err));
    return false;
}
