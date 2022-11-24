// validaremos el ancho de nuestra panntalla para poder cambiar la immagen de portada
if (window.screen.availWidth < 540) {
    console.log('si sr')
}
// prevenimos el recargo de pagina 

const button = document.getElementById('btn-form')
button.addEventListerner('click',(e)=> e.preventDefault())