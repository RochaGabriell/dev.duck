var modal = document.getElementById("deleteModal");
var closeButton = document.getElementsByClassName("close")[0];
var deleteButton = document.getElementById("deleteButton");

deleteButton.onclick = function () {
    modal.style.display = "block";
}

closeButton.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}