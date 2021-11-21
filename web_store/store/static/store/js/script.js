let phoneArray = document.getElementsByClassName("dropdown-item");

let choosePhone = function(){
    let phoneId=this.getAttribute('id');
//    let phoneDiv = document.getElementById("phone-selected");
    document.getElementById("h2-phone-selected").innerHTML = "Чехлы для телефона " + phoneId;
    document.getElementById("side-bar-phone-name").innerHTML = phoneId;
    document.getElementById("h2-phone-unselected").setAttribute(id="h2-phone-selected");
//    let phoneNameLabel = document.createElement("h2");
//    phoneNameLabel.innerHTML = "Чехлы для телефона " + phoneId;
//    phoneDiv.append(phoneNameLabel);
}

for (let i = 0;i < phoneArray.length; i++){
    phoneArray[i].addEventListener('click', choosePhone);
}