document.addEventListener("DOMContentLoaded", function() {
    const backToTopButton = document.getElementById("backToTop");

    window.onscroll = function() {
        if (document.body.scrollTop > 100 || 
            document.documentElement.scrollTop > 100) {
            backToTopButton.style.display = "block";
        } else {
            backToTopButton.style.display = "none";
        }
    };

    // When the user clicks the button, it will scroll right to the top
    backToTopButton.addEventListener("click", function() {
        window.scrollTo({ behavior: "smooth", top: 0 });
    });
});