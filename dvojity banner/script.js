const containerSlider = document.querySelector(".container-slider")
const slideLeft = document.querySelector(".slide-left")
const slideRight = document.querySelector(".slide-right")
const arrowDown = document.querySelector(".arrow-down")
const arrowUp = document.querySelector(".arrow-up")
// pocet divu
const slidesLength = slideRight.querySelectorAll("div").length

let numberActiveSlide = 0

// posun slidu na spravnou barvu k obrazku
slideLeft.style.top = `-${(slidesLength - 1) * 100}vh`

arrowUp.addEventListener("click", (event) => {
    changeSlide("up")
})

arrowDown.addEventListener("click", (event) => {
    changeSlide("down")
})

function changeSlide(direction) {
    // zjistujeme vysku aktualniho slideru pomoci fnkce clientHeight
    const sliderHeight = containerSlider.clientHeight

    if (direction === "up") {
        numberActiveSlide++
        if (numberActiveSlide > slidesLength - 1) {
            numberActiveSlide = 0
        }
    } else {
        numberActiveSlide--
        if (numberActiveSlide < 0) {
            numberActiveSlide = slidesLength - 1
        }
    }

    slideRight.style.transform = `translateY(-${sliderHeight * numberActiveSlide}px)`
    slideLeft.style.transform = `translateY(${sliderHeight * numberActiveSlide}px)`
}