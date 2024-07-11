## Descrição

Neste desafio, aplicaremos conceitos essenciais de programação. Seu objetivo é desenvolver uma solução simulando o registro de usuário em uma aplicação. Assegure que o código tenha uma **sintaxe** clara e organizada, com nomenclaturas significativas para **variáveis** como `email`, `nomeUsuario`, `senha` que será o local de armazenamento das informações de registro. Escolha **tipos de dados** apropriados, como o `String` para representar o `email`, `nomeUsuario` e `senha`. Certifique-se de tratar senha como strings para operações específicas.

## Entrada

Como entrada, receberemos três informações referentes ao `emailCadastro` (String), `nomeUsuario` (String) e `senha` (String).

## Saída

Construa uma mensagem de saída formatada corretamente, como nesta estrutura: '`registroNome` + ", verifique o email: " + `registroEmail` + " para ativar." '

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                 | Saída                                                    |
|-------------------------|----------------------------------------------------------|
| anavaz@email.com        | Ana, verifique o email: anavaz@email.com para ativar.    |
| Ana                     |                                                          |
| 2323                    |                                                          |
| joaocarlos@email.com    | Joao, verifique o email: joaocarlos@email.com para ativar.|
| Joao                    |                                                          |
| 3232                    |                                                          |
| shaula@email.com        | Shaula, verifique o email: shaula@email.com para ativar. |
| Shaula                  |                                                          |
| 8989                    |                                                          |


## Lógica Utilizada na Resolução do Código

Aqui está a explicação passo a passo da lógica implementada:

1. **Declaração das variáveis:** São declaradas três variáveis do tipo `string`: `registroEmail`, `registroNome` e `registroSenha`. Essas variáveis serão usadas para armazenar as informações inseridas pelo usuário.

2. **Leitura de dados de entrada:** Utiliza-se o método `Console.ReadLine()` para receber os dados de entrada do usuário. O programa espera que sejam inseridos, nesta ordem, o email, o nome do usuário e a senha. Cada valor é armazenado nas variáveis correspondentes.

3. **Saída formatada:** A saída é exibida no console usando `Console.WriteLine()`. Utiliza-se a interpolação de strings (`$"{variavel}"`) para formatar a mensagem de saída conforme especificado. O programa mostra a mensagem "registroNome, verifique o email: registroEmail para ativar.", onde `registroNome` e `registroEmail` são os valores inseridos pelo usuário anteriormente.

Essencialmente, este programa realiza a leitura de informações do usuário e as exibe de volta em uma mensagem formatada no console.
