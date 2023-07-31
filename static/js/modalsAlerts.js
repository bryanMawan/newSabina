    
    // Get all alert elements
    const alerts = document.querySelectorAll('.alert');

    // Add event listener to each alert for the close button
    alerts.forEach(alert => {
        const closeButton = alert.querySelector('.btn-close');
        closeButton.addEventListener('click', () => {
            alert.classList.add('fade');
            setTimeout(() => {
                alert.remove();
            }, 500); // Delay the removal to allow the fade-out animation to complete
        });
    });

    function showModal(modalId) {
    document.addEventListener('DOMContentLoaded', function () {
        var myModal = new bootstrap.Modal(document.getElementById(modalId), {
            keyboard: false
        });
        var myButton = document.querySelector(`button[data-bs-target="#${modalId}"]`);
        myButton.addEventListener('click', function () {
            myModal.show();
        });
    });
    }

    showModal('pathModal');
    showModal('passwordModal'); 

    

