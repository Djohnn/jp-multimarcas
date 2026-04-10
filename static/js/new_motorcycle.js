// ================================
// MODAL DE MARCA
// ================================
const modal = document.getElementById('modal-brand');
const btnOpen = document.getElementById('btn-add-brand');
const btnClose = document.getElementById('btn-close-modal');
const overlay = document.getElementById('modal-overlay');

btnOpen.addEventListener('click', () => {
    modal.classList.add('modal--open');
    overlay.classList.add('modal--open');
});

function closeModal() {
    modal.classList.remove('modal--open');
    overlay.classList.remove('modal--open');
}

btnClose.addEventListener('click', closeModal);
overlay.addEventListener('click', closeModal);

// Fechar com ESC
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
});