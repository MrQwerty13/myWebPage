document.addEventListener('DOMContentLoaded', function() {
    const brandSelect = document.getElementById('brandSelect');
    const volumeSelect = document.getElementById('volumeSelect');
    const tasteSelect = document.getElementById('tasteSelect');

    // Используем глобальную переменную
    const data = window.brandData || {};

    brandSelect.addEventListener('change', function() {
        const brand = this.value;
        // Очищаем списки
        volumeSelect.innerHTML = '<option value="">Select Volume</option>';
        tasteSelect.innerHTML = '<option value="">Select Taste</option>';

        if (brand && data.volumes && data.tastes) {
            const volumes = data.volumes[brand] || [];
            const tastes = data.tastes[brand] || [];

            volumes.forEach(function(v) {
                const opt = document.createElement('option');
                opt.value = v;
                opt.textContent = v + ' L';
                volumeSelect.appendChild(opt);
            });

            tastes.forEach(function(t) {
                const opt = document.createElement('option');
                opt.value = t;
                opt.textContent = t;
                tasteSelect.appendChild(opt);
            });
        }
    });
});

function openModal() {
    document.getElementById('addModal').style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    document.getElementById('addModal').style.display = 'none';
    document.body.style.overflow = '';
}

window.onclick = function(event) {
    const modal = document.getElementById('addModal');
    if (event.target === modal) {
        closeModal();
    }
};

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal();
    }
});

function confirmDelete() {
    return confirm('Are you sure you want to delete this drink?');
}