document.addEventListener("DOMContentLoaded", function() {

    var carousel = document.getElementById('carousel');
    var currentImage = document.getElementsByClassName('show');

    function carouselForward () {
        currentImage.nextSibling.classList.add('show')
    }

});