const eggImage = document.getElementById('egg-image');
const eggCrackSound = document.getElementById('egg-crack-sound');

eggImage.addEventListener('click', function () {
    eggCrackSound.play();
});