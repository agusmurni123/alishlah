const btnmenu = document.querySelector('.menu');
const btnbar = document.querySelector('.fa-bars');

btnbar.addEventListener('click',function() {
    btnmenu.classList.toggle('menuaktive');
});