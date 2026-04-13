const modal = document.getElementById('modal-lead');
const btnOpen = document.getElementById('btn-lead');
const btnClose = document.getElementById('btn-close-lead');
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

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
});