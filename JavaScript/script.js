const container = document.querySelector('.container')
const botao = document.querySelector('#botao')
let botao_bool = false



function on_off(){
    container.classList.toggle('on')

    if(botao_bool) {
        botao.textContent = "ACENDER"
        botao_bool = false
    } else {
        botao.textContent = "APAGAR"
        botao_bool = true
    }
}


