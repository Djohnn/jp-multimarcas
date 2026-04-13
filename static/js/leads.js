const modal = document.getElementById('modal-lead');
const btnOpen = document.getElementById('btn-lead');
const btnClose = document.getElementById('btn-close-lead');
const overlay = document.getElementById('modal-overlay');

if (btnOpen) {
    btnOpen.addEventListener('click', () => {
        modal.classList.add('modal--open');
        overlay.classList.add('modal--open');
    });
}

function closeModal() {
    modal.classList.remove('modal--open');
    overlay.classList.remove('modal--open');
}

if (btnClose) btnClose.addEventListener('click', closeModal);
if (overlay) overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
});