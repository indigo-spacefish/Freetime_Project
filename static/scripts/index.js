var text1 = "Finish writing that novel or make a dent in your to-read pile.";
var text2 = "Learn new skills or discover different ways to adventure.";
var text3 = "Want to know how much time you aren't spending at the gym?";
var text4 = "Stop letting your time slip away and get outdoors.";
var textArray = [text1, text2, text3, text4];


document.addEventListener("DOMContentLoaded", function() {

    var carousel = document.getElementById('carousel');
    var currentImage = document.getElementById('c1');
    var currentText = document.getElementById('carousel_text');
    var currentTextIndex = 0;
    var forwardBtn = document.getElementById('forwardArrow');
    var backBtn = document.getElementById('backArrow');


    function carouselForward() {
        currentImage.classList.add('hide');
        currentImage.classList.remove('show');
        if (currentImage == document.getElementById('c4')) {
            var nextImage = document.getElementById('c1');
            currentText.innerHTML = textArray[0];
            currentTextIndex = 0;
        }
        else {
            nextImage = currentImage.nextElementSibling;
            currentTextIndex += 1;
            currentText.innerHTML = textArray[currentTextIndex];
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
            currentText.innerHTML = textArray[3];
            currentTextIndex = 3;
        }
        else {
            prevImage = currentImage.previousElementSibling;
            currentTextIndex -= 1;
            currentText.innerHTML = textArray[currentTextIndex];
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