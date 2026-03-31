window.addEventListener("load", () => {
    window.addEventListener("click", windowClickEvent => {
        const dropdownContent = document.querySelector(".dropdown-content");
        const dropdown = document.querySelector(".dropdown-box");
        const selectedItem = document.querySelector(".selected-item");

        if(dropdown.classList.contains("active")){
            if(!dropdownContent.contains(windowClickEvent.target)){
            closeDropdown();
            }
        }
        else if(selectedItem.contains(windowClickEvent.target)){
            openDropdown();
        }    
    })

    const dropdownItems = document.querySelectorAll(".dropdown-item");

    dropdownItems.forEach(dropdownItem => {
        dropdownItem.addEventListener("click", () =>{
            dropdownItems.forEach(innerDropdownItem => {
            innerDropdownItem.classList.remove("active");
        })

        dropdownItem.classList.add("active");
        
        const selectedItemInput =  document.querySelector(".selected-item input");

        selectedItemInput.value =  dropdownItem.innerHTML; 
        closeDropdown();

        })
    })
    
    const searchInput = document.querySelector(".search-input input");


    searchInput.addEventListener("keyup", () => { 
        const filter = searchInput.value.toLocaleLowerCase();
        console.log(dropdownItems)
        dropdownItems.forEach(dropdownItem => {
            if (dropdownItem.textContent.toLocaleLowerCase().includes(filter)){
                console.log(dropdownItem)   
                dropdownItem.classList.remove("hide");
            }
            else{
                dropdownItem.classList.add("hide");
                console.log(dropdownItem)
            }
        })
    })

})

function openDropdown(){
    const dropdown = document.querySelector(".dropdown-box");
    dropdown.classList.add("active");
}

function closeDropdown(){
    const dropdown = document.querySelector(".dropdown-box");
    dropdown.classList.remove("active");
}