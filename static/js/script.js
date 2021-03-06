document.addEventListener('DOMContentLoaded', () => {

    // Begin hamburger menu script
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
            el.addEventListener('click', () => {

                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        });
    }
    // End hamburger menu script

    // Begin notification script
    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
        const $notification = $delete.parentNode;

        $delete.addEventListener('click', () => {
            $notification.parentNode.removeChild($notification);
        });
    });
    // End notification script

    // Begin scroll to content script
    window.scrollToCards = () => {
        const cardsSection = document.getElementById('cards-section');

        // scrollTo(0, cardsSection.offsetTop);
        scrollTo({
            top: cardsSection.offsetTop,
            behavior: 'smooth'
        })
    }
    // End scroll to content script
});