function CallJSON() {
    console.log('called')
    let x = document.forms["Assignment11"]["x-js"].value;
    let add = "https://reqres.in/api/users/" + x
    fetch(add)
        .then(response => response.json())
        .then(responseJSON => {
            let user = responseJSON.data
            console.log(user)
            let userData = document.getElementById("UserData")
            userData.innerHTML = `
            <p>User Data</p>
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
                <span>${user.first_name} ${user.last_name}</span>
                <br>
                <a href="mailto:${user.email}">Send Email<a/>
            </div>
            `;
        })
        .catch(err => console.log(err));
    return false;
}
