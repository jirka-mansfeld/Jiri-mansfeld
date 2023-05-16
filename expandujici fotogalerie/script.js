const slides = document.querySelectorAll(".slide")

slides.forEach((oneSlide) => {
    oneSlide.addEventListener("click", (event) => {

        // active vymaze vsem
        deleteActiveClass()
        
        // prida active classu slidu na ktery se kliklo
        oneSlide.classList.add("active")
    })
})

// vymaze vsem slidum tridu active
function deleteActiveClass(){
    slides.forEach((oneSlide) => {
        oneSlide.classList.remove("active")
    })
}