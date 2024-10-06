function verificaA() { 
  // Captura a string inserida pelo usuário
  let string = document.getElementById("imput").value;
  
  // Contador de ocorrências da letra 'a'
  let countA = 0;
  
  // Percorre a string e conta quantas vezes a letra 'a' aparece
  for (let i = 0; i < string.length; i++) {
      if (string[i] === 'a' || string[i] === 'A') {
          countA++;
       }
     }


 // Exibe o resultado na página
 let resultado = document.getElementById("resultado");
 if (countA > 0) {
     resultado.textContent = `A letra "a/A" ocorre ${countA} vezes na string.`;
 } else {
     resultado.textContent = 'A letra "a" não foi encontrada na string.';
 }
}
