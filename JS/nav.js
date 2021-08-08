document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.querySelector(".menu-btn");
    const navContent = document.querySelector(".nav-collapse-content")
    let menuOpen = false;
    const body = document.querySelector("body")
    const nav = document.querySelector("nav")

    menuBtn.addEventListener("click", () => {
        if (!menuOpen) {
            menuBtn.classList.add("open");
            menuOpen = true;
            navContent.classList.add("flex");
            body.style.overflow = "hidden";

        } else {
            menuBtn.classList.remove("open");
            menuOpen = false;
            navContent.classList.remove("flex");
            body.style.overflow = "initial";
        }
    });
});