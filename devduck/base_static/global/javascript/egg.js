function startShakeAnimation() {
    var imgElement = document.getElementById('egg-effect');
    imgElement.classList.add('shake-animation');
}

function stopShakeAnimation() {
    var imgElement = document.getElementById('egg-effect');
    imgElement.classList.remove('shake-animation');
}

setInterval(function () {
    startShakeAnimation();
    setTimeout(stopShakeAnimation, 5000);
}, 10000);