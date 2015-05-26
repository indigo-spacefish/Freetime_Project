document.addEventListener("DOMContentLoaded", function() {

    var carousel = document.getElementById('carousel');
    var currentImage = document.getElementById('c1');
    var forwardBtn = document.getElementById('forwardArrow');
    var backBtn = document.getElementById('backArrow');


    function carouselForward() {
        currentImage.classList.add('hide');
        currentImage.classList.remove('show');
        if (currentImage == document.getElementById('c4')) {
            var nextImage = document.getElementById('c1')
        }
        else {
            nextImage = currentImage.nextElementSibling;
        }
        nextImage.classList.remove('hide');
        nextImage.classList.add('show');
        currentImage = nextImage;
    }


    function carouselBack() {
        currentImage.classList.add('hide');
        currentImage.classList.remove('show');
        if (currentImage == document.getElementById('c1')) {
            var prevImage = document.getElementById('c4');
        }
        else {
            prevImage = currentImage.previousElementSibling;
        }
        prevImage.classList.remove('hide');
        prevImage.classList.add('show');
        currentImage = prevImage;
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