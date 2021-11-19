alert('Script is working');
let phoneArray = document.getElementsByClassName("dropdown-item");

alert(phoneArray);
alert(phoneArray.length);

let choosePhone = function(){
    alert('In function');
    let phoneId=this.getAttribute('id');
    alert(phoneId);

//    let phoneDiv = document.getElementById("phone-selected");
    document.getElementById("h2-phone-selected").innerHTML = "Чехлы для телефона " + phoneId;

//    let phoneNameLabel = document.createElement("h2");
//    phoneNameLabel.innerHTML = "Чехлы для телефона " + phoneId;
//    phoneDiv.append(phoneNameLabel);

}

for (let i = 0;i < phoneArray.length; i++){
    phoneArray[i].addEventListener('click', choosePhone);
}