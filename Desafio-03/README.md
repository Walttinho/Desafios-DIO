## Descrição

Para este desafio, vamos aplicar outros conceitos fundamentais de programação, agora, criaremos um programa que calcule a soma dos números pares em um intervalo específico. Dessa forma, desenvolva uma solução clara, simples e organizada, você pode criar **variáveis** com nomes representativos, como `limiteInferior`, `limiteSuperior` e `somaPares`. Utilize uma **estrutura de controle de fluxo**, como o `for` para percorrer todos os números no intervalo definido pelos `limiteInferior` e o `limiteSuperior`. Dentro desse loop, crie uma **estrutura condicional** `if` para verificar se cada número é par e se o resto da divisão por 2 é igual a zero (`i % 2 == 0`). Se a condição for verdadeira, o número é somado à **variável** `somaPares`.

## Entrada

Será as informações de `limiteInferior` e `limiteSuperior`, sendo eles dois números inteiros (`int`).

## Saída

A saída deverá informar uma String com o resultado final: `"A soma dos números pares de {limiteInferior} a {limiteSuperior} e: {somaPares}"`.

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saída |
| ------- | ----- |
| 30<br>60 | A soma dos numeros pares de 30 a 60 e: 720 |
| 1<br>32 | A soma dos numeros pares de 1 a 32 e: 272 |
| 10<br>20 | A soma dos numeros pares de 10 a 20 e: 90 |



## Lógica Utilizada na Resolução do Código

Aqui está a explicação da lógica passo a passo:

1. **Leitura dos limites inferiores e superiores:** O programa solicita ao usuário que insira os valores para os limites inferior e superior. Esses valores são lidos através de `Console.ReadLine()` e armazenados nas variáveis `limiteInferior` e `limiteSuperior`, respectivamente.

2. **Inicialização da variável de soma de pares:** É declarada e inicializada a variável `somaPares` com o valor zero. Essa variável será utilizada para acumular a soma dos números pares no intervalo.

3. **Loop para percorrer os números no intervalo:** Utiliza-se um loop `for` com a variável `i` iniciando em `limiteInferior` e continuando até `limiteSuperior`. O loop percorre cada número no intervalo definido.

4. **Verificação de números pares:** Dentro do loop, há uma verificação com `if (i % 2 == 0)`. Esta condição verifica se o número `i` é par (ou seja, se o resto da divisão por 2 é igual a zero).

5. **Acumulação da soma dos números pares:** Se o número verificado for par, ou seja, se a condição do `if` for verdadeira, esse número é adicionado à variável `somaPares`.

6. **Exibição do resultado:** Após o término do loop, o programa exibe a soma dos números pares no intervalo definido pelo usuário utilizando `Console.WriteLine()` e a formatação de string (`$"A soma dos numeros pares de {limiteInferior} a {limiteSuperior} e: {somaPares}"`).

Basicamente, esse programa calcula a soma dos números pares dentro de um intervalo específico definido pelo usuário, utilizando um loop `for`, uma estrutura condicional `if` para verificar números pares e acumulando o resultado na variável `somaPares`. Por fim, exibe o resultado da soma.