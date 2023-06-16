let myToDos = [{
    text: "Vynést koš",
    competion: false
}, {
    text: "Dojít nakoupit",
    competion: false
}, {
    text: "Uklidit",
    competion: true
}, {
    text: "Nakrmit psa",
    competion: true
}, {
    text: "Nakrmit kočku",
    competion: false
}]

// vypisujeme toDos do stránky
myToDos.forEach((oneToDo) =>{
    let ToDoP = document.createElement("p")
    ToDoP.textContent = oneToDo.text
    document.querySelector(".ukoly").appendChild(ToDoP)
})

//zachytáváme klinutí tlačítka
document.querySelector(".myBtn").
addEventListener("click", (event) =>{
    console.log(event)
})

//ukládáme text z políčka
const filters = {
    searchingText: ""
}

// obecna filtrovaci fce
let comparison = (array, searchText) =>{
    let arrayResults = array.filter((oneObject) =>{
        return oneObject.text.toLowerCase().includes
        (searchText.searchingText.toLowerCase())
        
    })

    document.querySelector(".toDoLeft").innerHTML = ""

    //pocitame ukoly ke splneni
    let leftToDos = arrayResults.filter((oneResult) =>{
        return oneResult.competion === false
    })
    
    let paragraph = document.createElement("p")
    paragraph.textContent = (`Počet úkolů ke splnění: ${leftToDos.length}`)
    document.querySelector(".toDoLeft").appendChild(paragraph)

    // maže úkoly pri kazdem prepisu
    document.querySelector(".ukoly").innerHTML = ""
     
    //vypisuje úkoly pri prepisu
    arrayResults.forEach((oneObject) =>{
        let paragraph = document.createElement("p")
        paragraph.textContent = `${oneObject.text}`
        document.querySelector(".ukoly").appendChild(paragraph)
    })
} 

// načítáme text z políčka
let searchText = document.querySelector("#search-text")
searchText.addEventListener("input", (event) =>{
    filters.searchingText = event.target.value

    // volame filtrovaci funkci
    comparison(myToDos, filters)
})

