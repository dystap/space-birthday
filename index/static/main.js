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
})

function openDropdown(){
    const dropdown = document.querySelector(".dropdown-box");
    dropdown.classList.add("active");
}

function closeDropdown(){
    const dropdown = document.querySelector(".dropdown-box");
    dropdown.classList.remove("active");
}