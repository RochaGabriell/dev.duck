var djangoLista = 'poo'
var materiaSelect = document.getElementById("only-subjects");

materiaSelect.addEventListener("change", function () {
    if (djangoLista.includes(materiaSelect.value)) {
        document.getElementById("subjects-language").style.display = "block";
    }
    else {
        document.getElementById("subjects-language").style.display = "none";
        document.getElementById("subjects-language").value = "0"
    }
});