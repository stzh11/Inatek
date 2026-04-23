document.addEventListener('DOMContentLoaded', () => {
    const burgerBtn = document.getElementById('burger-btn');
    const navMenu = document.getElementById('nav-menu');

    if (!burgerBtn || !navMenu) {
        return;
    }

    const closeMenu = () => {
        navMenu.classList.remove('show');
        burgerBtn.setAttribute('aria-expanded', 'false');
    };

    burgerBtn.setAttribute('aria-expanded', 'false');

    burgerBtn.addEventListener('click', () => {
        const isOpen = navMenu.classList.toggle('show');
        burgerBtn.setAttribute('aria-expanded', String(isOpen));
    });

    navMenu.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', closeMenu);
    });

    document.addEventListener('click', (event) => {
        if (!navMenu.contains(event.target) && !burgerBtn.contains(event.target)) {
            closeMenu();
        }
    });

    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            closeMenu();
        }
    });
});
