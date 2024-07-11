## Descrição

Agora, focaremos em outro conceito fundamental de programação para desenvolver um algoritmo que possua como objetivo a simulação de um Sistema de Gerenciamento de Tarefas. Dessa forma, crie **variáveis** como, `titulo`, `descricao` e `dataVencimento` para guardar as informações das tarefas. Após isso, implemente uma **estrutura condicional** `if/else` para verificar se a descrição da tarefa excede 50 caracteres. Caso a descrição exceda 50 caracteres, trataremos essa condição exibindo uma mensagem adequada. Lembrando que as **estruturas condicionais** são fundamentais para o controle de fluxo dos programas, pois realizam verificações precisas com base em condições específicas predefinidas, neste caso, é o limite de 50 caracteres.

## Entrada

A entrada será as `Strings` com o título da tarefa, a descrição e a data de vencimento.

## Saída

Será exibida a tarefa que foi adicionada com o título, descrição e data de vencimento. Mas, caso a descrição tenha mais de 50 caracteres, deverá ser informado: `O Valor da descrica excede a quantidade de caracteres permitido`.

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saída |
|---------|-------|
| Backup Noturno<br>Executar backup automático de servidores às 2h da madrugada | Descrição ultrapassa limite de caracteres. |
| Monitoramento de Rede<br>Configurar alertas para tráfego em tempo real<br>18/12 | Configurar alertas para tráfego em tempo real até 18/12 |
| Atualização de Software<br>Aplicar patches<br>22/12 | Aplicar patches até 22/12 |


## Lógica Utilizada na Resolução do Código

Aqui está a explicação da lógica passo a passo:

1. **Declaração das variáveis:** São declaradas três variáveis do tipo `string`: `titulo`, `descricao` e `dataVencimento`. Elas serão utilizadas para armazenar informações sobre uma tarefa.

2. **Leitura de dados de entrada:** O programa utiliza `Console.ReadLine()` para receber os dados de entrada do usuário. O primeiro dado inserido é considerado como o título da tarefa e o segundo como a descrição. Essas entradas são armazenadas nas variáveis correspondentes.

3. **Verificação de limite de caracteres:** O programa utiliza uma estrutura condicional `if/else` para verificar se a descrição da tarefa excede 50 caracteres. Se a quantidade de caracteres na descrição for maior que 50, o programa exibe a mensagem "Descricao ultrapassa limite de caracteres." no console.

4. **Saída formatada:** Caso a descrição não ultrapasse o limite de caracteres, o programa continua pedindo a entrada da data de vencimento da tarefa através do console. Após a inserção dessa data, o programa exibe a descrição da tarefa e a data de vencimento, concatenando-as na formatação adequada, utilizando o método `Console.WriteLine()`.

Basicamente, esse programa solicita ao usuário informações sobre uma tarefa (título, descrição e data de vencimento), verifica se a descrição excede o limite de caracteres e, se não ultrapassar, exibe os dados da tarefa inserida.