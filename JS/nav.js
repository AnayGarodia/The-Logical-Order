var $blip = $('.blip');

$('#page-nav>a').on('mouseover', function() {
    $blip.css({
        left: $(this).offset().left -
            $(this).parent().offset().left +
            $(this).width() / 2 -
            20 // 20 is one half of .blip's width
    });
});

$('#page-nav').on('mouseout', function() {
    $('.blip').css({ left: -100 });
});


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