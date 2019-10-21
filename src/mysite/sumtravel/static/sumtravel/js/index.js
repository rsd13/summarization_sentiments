
function checkText(){
    var inputs = document.querySelectorAll("input")

    var restaurante = inputs[0].value
    var ciudad = inputs[1].value
    check_restaurante = (restaurante === "")
    check_ciudad = (ciudad === "")

    if (check_restaurante && check_ciudad){
        alert("Error, falta rellenar el texto de restaurante y ciudad")
        return false
    }else if(check_ciudad){
        alert("Error, falta rellenar el texto de ciudad")
        return false
    }else if(check_restaurante){
        alert("Error, falta rellenar el texto de restaurante")
        return false
    }
}

function init_alert() {
    var boton = document.querySelectorAll("input")[2]
    boton.addEventListener("click",checkText);
}
//init_alert()
