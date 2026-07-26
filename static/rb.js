// Open the modal
function openModal() {
  document.getElementById('addModal').style.display = 'block';
}

// Close the modal
function closeModal() {
  document.getElementById('addModal').style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function (event) {
  const modal = document.getElementById('addModal');
  if (event.target === modal) {
    modal.style.display = 'none';
  }
};

// rb.js – добавить функцию confirmDelete

function confirmDelete() {
  return confirm('Are you sure you want to delete this can?');
}