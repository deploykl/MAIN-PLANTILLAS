let nextBtn = document.querySelector('.next');
let prevBtn = document.querySelector('.prev');
let slider = document.querySelector('.slider');
let sliderList = slider.querySelector('.list');
let thumbnail = document.querySelector('.slider .thumbnail');
let thumbnailItems = thumbnail.querySelectorAll('.item');

// Agregar el primer ítem del thumbnail al final
thumbnail.appendChild(thumbnailItems[0]);

// Función para mover el slider hacia adelante ('next')
function moveSliderNext() {
    let sliderItems = sliderList.querySelectorAll('.item');
    let thumbnailItems = document.querySelectorAll('.thumbnail .item');
    
    sliderList.appendChild(sliderItems[0]);
    thumbnail.appendChild(thumbnailItems[0]);
    slider.classList.add('next');
    
    slider.addEventListener('animationend', function() {
        slider.classList.remove('next');
    }, {once: true}); // Remove the event listener after it's triggered once
}

// Función para mover el slider hacia atrás ('prev')
function moveSliderPrev() {
    let sliderItems = sliderList.querySelectorAll('.item');
    let thumbnailItems = document.querySelectorAll('.thumbnail .item');
    
    sliderList.prepend(sliderItems[sliderItems.length - 1]);
    thumbnail.prepend(thumbnailItems[thumbnailItems.length - 1]);
    slider.classList.add('prev');
    
    slider.addEventListener('animationend', function() {
        slider.classList.remove('prev');
    }, {once: true}); // Remove the event listener after it's triggered once
}

// Event listeners para los botones de next y prev
nextBtn.onclick = function() {
    moveSliderNext();
};

prevBtn.onclick = function() {
    moveSliderPrev();
};

// Cambiar automáticamente cada 2 segundos
setInterval(function() {
    moveSliderNext();
}, 8000);
