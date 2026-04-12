

const slider = document.getElementById('price-slider');
const priceValue = document.getElementById('price-value');

if (slider) {
    slider.addEventListener('input', () => {
        priceValue.textContent = 'R$ ' + parseInt(slider.value).toLocaleString('pt-BR');
    });
}

