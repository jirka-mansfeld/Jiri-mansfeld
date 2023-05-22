const result = document.querySelector(".user-list")
const input = document.querySelector(".input-filter")
const userList = []

getData()

input.addEventListener("input", (event) => {
    dataFilter(event.target.value)
})

// async funkce se spusti, ale kod hned pokracuje dal, neceka se na jeji dokonceni(funguje za behu)
async function getData() {
    // v podstate znamena pockej, dokud se nenacte tech nasich 50 uzivatelu a az poto to uloz do allUsers
    const allUsers = await fetch("https://randomuser.me/api?results=50")

    //json prevede nahrana data na citelna pro nas
    const data = await allUsers.json()
    console.log(data)

    //vycisti seznam uzivatelu
    result.innerHTML = ""


    //musime vytvorit HTML Li pro kazdeho uzivatele
    data.results.forEach((onePerson) => {
        const li = document.createElement("li")
        li.innerHTML = `
        <img src="${onePerson.picture.large}" alt="${onePerson.name.first}"
        <div class="user-info">
            <h3>${onePerson.name.first} ${onePerson.name.last}</h3>
            <p>${onePerson.location.city}, ${onePerson.location.country}</p>
        </div>
        `

        //pridame do resultu
        result.appendChild(li)

        // a ulozime do userListu
        userList.push(li)
    })
    
}

//porovnávání uživatelů
function dataFilter(input) {
    userList.forEach((oneUser) => {
        if (oneUser.innerText.toLowerCase().includes(input.toLowerCase())) {
            oneUser.classList.remove("hide")
        } else {
            oneUser.classList.add("hide")
        }
    })
}