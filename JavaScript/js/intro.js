const paragrafo = document.querySelector('p');

paragrafo.addEventListener('click', updateName);


function updateName(){
    let name = prompt('Inserisci il nuovo player');
    paragrafo.textContent = 'Player 1: ' + name;
}