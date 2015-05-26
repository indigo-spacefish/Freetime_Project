document.addEventListener("DOMContentLoaded", function() {

    var carousel = document.getElementById('carousel');
    var currentImage = document.getElementsByClassName('show');
    var forwardBtn = document.getElementById('forwardArrow');
    var backBtn = document.getElementById('backArrow');


    function carouselForward() {
        currentImage.style.display = 'none';
        currentImage = currentImage.nextElementSibling;
        currentImage.style.display = 'inline-block';
    }


    function carouselBack() {
        currentImage.style.display = 'none';
        currentImage = currentImage.previousElementSibling;
        currentImage.style.display = 'inline-block';
    }


    forwardBtn.addEventListener('click', function (event) {
        console.log(event);
        console.log(this);
        carouselForward();
    });


    backBtn.addEventListener('click', function (event) {
        console.log(event);
        console.log(this);
        carouselBack();
    });

});