const module_select = document.getElementById('module');
const subjects_select = document.getElementById('subjects');
const language_select = document.getElementById('subjects-language');

const djangoLista = [
    "Algoritmo e Programação", "Programação Orientada a Objetos", "Estrutura de Dados I",
    "Estrutura de Dados II", "Programação para Internet I", "Programação para Internet II",
    "Tópicos Especiais em Programação", "Programação para Dispositivos Móveis", "Analise e Projeto de Sistemas",
    "Tópicos Especiais em Sistema de Informação", "Lesgislação Aplciada a Tecnologia da Informação", "Banco de Dados I",
    "Banco de Dados II"
]

module_select.addEventListener('change', () => {
    const module_id = module_select.options[module_select.selectedIndex].value;

    subjects_select.style.display = 'block';
    for (let i = 0; i < subjects_select.options.length; i++) {
        const subject = subjects_select.options[i];

        if (subject.id == module_id) {
            subject.style.display = 'block';

        } else {
            subject.style.display = 'none';
            subject.value = 0;
        }
    }
});

subjects_select.addEventListener("change", function () {
    if (djangoLista.includes(subjects_select.options[subjects_select.selectedIndex].innerText)) {
        language_select.style.display = "block";
    }
    else {
        language_select.style.display = "none";
        language_select.value = "0"
    }
});