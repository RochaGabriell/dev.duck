const selectElement = document.querySelectorAll('#select-subjects');
selectElement.forEach(selectElement => {
    selectElement.addEventListener('change', (event) => {
        event.target.form.submit();
    });
});