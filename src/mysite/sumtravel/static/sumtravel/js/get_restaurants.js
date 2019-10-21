//devuelve una alerta si la url es incorrecta para el scrapeo

function init_alert() {
    var is_alert = document.querySelector("div.alert")
    alert = is_alert.getAttribute("alert")
    console.log(alert)

    if(alert === "True"){
        alert("Error: introduce una url de restaurantes válida de tripadvisor donde haya reviews")
    }

}

init_alert()




