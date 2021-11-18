alert('Script is working');
let phoneArray = document.getElementsByClassName("dropdown-item");

alert(phoneArray);
alert(phoneArray.length);

let choosePhone = function(){
    alert('In function');
    let phoneDiv = document.getElementById("phone-selected");
    alert('hello!');
    let phoneNameLabel = document.createElement("h2");
    phoneNameLabel.innerHTML = "Телефон";
    phoneDiv.append(phoneNameLabel);

}

for (let i = 0;i < phoneArray.length; i++){
    phoneArray[i].addEventListener('click', choosePhone);
}