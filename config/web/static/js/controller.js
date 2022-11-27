// validaremos el ancho de nuestra panntalla para poder cambiar la immagen de portada
if (window.screen.availWidth < 540) {
    console.log('si sr')
}

let toping = document.getElementById('support')

toping.addEventListener('click', () => window.scrollTo({ top: 0, left: 0, behavior: 'smooth' })) 