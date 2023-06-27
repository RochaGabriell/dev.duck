const person_button = document.getElementsByClassName('person-button')[0];
const dropdown = document.getElementById('dropdown');

person_button.addEventListener('click', () => {
    dropdown.style.display = 'block';
    person_button.setAttribute('aria-expanded', 'true');
});

document.addEventListener('click', (event) => {
    if (!person_button.contains(event.target) && !dropdown.contains(event.target)) {
        dropdown.style.display = 'none';
        person_button.setAttribute('aria-expanded', 'false');
    }
});