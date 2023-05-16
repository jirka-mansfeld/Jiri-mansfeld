const heading = document.querySelector("#text")
const speedOr = document.querySelector("#speed")
const text = "Jirka"
let idLettter = 1
let delay = 500 / speedOr.value

function printText() {
    heading.textContent = text.slice(0, idLettter)
    idLettter++

    if (idLettter > text.length) {
        idLettter = 1
    }

    // spusti funkci printtext se zpozdenim delay
    setTimeout(printText, delay)
}

printText()

speedOr.addEventListener("input", (event) => {
    delay = 500 / event.target.value
})