// ================================
// DROPDOWN DO USUÁRIO
// ================================

document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
    const btn = dropdown.querySelector('.nav-dropdown__btn');
    const menu = dropdown.querySelector('.nav-dropdown__menu');

    btn.addEventListener('click', (e) => {
        e.stopPropagation();
        // Fecha os outros antes de abrir
        document.querySelectorAll('.nav-dropdown__menu').forEach(m => {
            if (m !== menu) m.classList.remove('dropdown--open');
        });
        menu.classList.toggle('dropdown--open');
    });
});

// Fecha ao clicar fora
document.addEventListener('click', () => {
    document.querySelectorAll('.nav-dropdown__menu').forEach(m => {
        m.classList.remove('dropdown--open');
    });
});


// const dropdownBtn = document.getElementById('dropdown-btn');
// const dropdownMenu = document.getElementById('dropdown-menu');

// if (dropdownBtn) {
//     dropdownBtn.addEventListener('click', (e) => {
//         e.stopPropagation();
//         dropdownMenu.classList.toggle('dropdown--open');
//     });

//     document.addEventListener('click', () => {
//         dropdownMenu.classList.remove('dropdown--open');
//     });

//     document.addEventListener('keydown', (e) => {
//         if (e.key === 'Escape') dropdownMenu.classList.remove('dropdown--open');
//     });
// }