
console.log(window.data)
function historial(){
    grafico_pos = window.data.grafica_positiva
    grafico_neg = window.data.grafica_negativa
    grafico_neu = window.data.grafica_neutra

    new Chart("q1", {
        type: 'bar',
        data: {
            labels: grafico_pos.map(character => character.año),
            datasets: [{
                label: 'positivo',
                data: grafico_pos.map(character => character.cantidad),
                borderColor: 'rgba(0, 50, 250, .7)',
                borderWidth: 1,
                backgroundColor: 'rgba(0, 250, 50, .2)'
            },{
                label: 'negativo',
                data: grafico_neg.map(character => character.cantidad),
                borderColor: 'rgba(0, 50, 250, .7)',
                borderWidth: 1,
                backgroundColor: 'rgba(255,101,80,0.4)'
            },{
                label: 'neutro',
                data: grafico_neu.map(character => character.cantidad),
                borderColor: 'rgba(0, 50, 250, .7)',
                borderWidth: 1,
                backgroundColor: 'rgba(191,191,191,0.4)'
            }

            ]
        }
    })
}

function freq_noun_pos() {
    grafico_pos = window.data.conteo_noun_pos
    console.log(grafico_pos)
    new Chart("q2", {
        type: 'horizontalBar',
        data: {
            labels: grafico_pos.map(eachCharacter => eachCharacter.nombre),
            datasets: [{
                label: 'Sustantivos',
                data: grafico_pos.map(eachCharacter => eachCharacter.frecuencia),
                borderWidth: 1,
                borderColor: 'rgba(0,50,250,.7)',
                backgroundColor: 'rgba(0,250,50,.2)'
            }]
        }
    })
}

function freq_adj_pos() {
    grafico_pos = window.data.conteo_ajd_pos
    console.log(grafico_pos)
    new Chart("q3", {
        type: 'horizontalBar',
        data: {
            labels: grafico_pos.map(eachCharacter => eachCharacter.nombre),
            datasets: [{
                label: 'Adjetivos',
                data: grafico_pos.map(eachCharacter => eachCharacter.frecuencia),
                borderWidth: 1,
                borderColor: 'rgba(0,50,250,.7)',
                backgroundColor: 'rgba(0,250,50,.2)'
            }]
        }
    })
}

function freq_noun_neg() {
    grafico_pos = window.data.conteo_noun_neg
    console.log(grafico_pos)
    new Chart("q4", {
        type: 'horizontalBar',
        data: {
            labels: grafico_pos.map(eachCharacter => eachCharacter.nombre),
            datasets: [{
                label: 'Sustantivos',
                data: grafico_pos.map(eachCharacter => eachCharacter.frecuencia),
                borderWidth: 1,
                borderColor: 'rgba(0,50,250,.7)',
                backgroundColor: 'rgba(255,101,80,0.4)'
            }]
        }
    })
}


function freq_adj_neg() {
    grafico_pos = window.data.conteo_ajd_neg

    new Chart("q5", {
        type: 'horizontalBar',
        data: {
            labels: grafico_pos.map(eachCharacter => eachCharacter.nombre),
            datasets: [{
                label: 'Adjetivos',
                data: grafico_pos.map(eachCharacter => eachCharacter.frecuencia),
                borderWidth: 1,
                borderColor: 'rgba(0,50,250,.7)',
                backgroundColor: 'rgba(255,101,80,0.4)'
            }]
        }
    })
}

function insert_graficos(){
    historial()
    freq_noun_pos()
    freq_adj_pos()
    freq_adj_neg()
    freq_noun_neg()
}

insert_graficos()
