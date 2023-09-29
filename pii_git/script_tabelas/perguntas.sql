create database jogo;
use jogo;

CREATE TABLE perguntas (
    pergunta    VARCHAR(512),
    alt1    VARCHAR(512),
    alt2    VARCHAR(512),
    alt3    VARCHAR(512),
    alt4    VARCHAR(512),
    resposta    int(1),
    materia    VARCHAR(512)
);

INSERT INTO perguntas (pergunta, alt1, alt2, alt3, alt4, resposta, materia) VALUES
	('A forma correta de comentar uma linha de código: ', '1 - // Comentário', '2 - /* Comentário */', '3 - # Comentário', '4 - <!-- Comentário -->', '3', 'Python'),
	('Qual tipo de dado é imutável? ', '1 - List', '2 - Tuple', '3 - Set', '4 - Dictionary', '2', 'Python'),
	('Função usada para obter o comprimento de uma lista:', '1 - count()', '2 - length()', '3 - size()', '4 - len()', '4', 'Python'),
	('O operador usado para concatenar duas strings: ', '1 - *', '2 - %', '3 - +', '4 - &', '3', 'Python'),
	('Método usado para remover um elemento de um conjunto: ', '1 - discard()', '2 - remove()', '3 - delete()', '4 - pop()', '1', 'Python'),
	('A saída do seguinte código, print(2 ** 3), é:', '1 - 5', '2 - 8', '3 - 16', '4 - 23', '2', 'Python'),
	('Módulo usado para trabalhar com arquivos? ', '1 - sys', '2 - os', '3 - math', '4 - time', '2', 'Python'),
	('Função usada para ler entrada do usuário?', '1 - input()', '2 - get()', '3 - read()', '4 - scan()', '1', 'Python'),
	('Método usado para ordenar uma lista?', '1 - sort()', '2 - sorted()', '3 - order()', '4 - arrange() ', '1', 'Python'),
	('A função do operador ""==""? "', '1 - Verificar se dois valores são idênticos', '2 - Realizar uma atribuição de valor', '3 - Incrementar uma variável', '4 - Multiplicar dois números', '1', 'Python'),
	('Forma correta de declarar uma variável é?', '1 - nome_variavel = valor', '2 - var nome_variavel = valor ', '3 - let nome_variavel = valor ', '4 - const nome_variavel = valor', '1', 'Python'),
	('Estrutura para repetir um bloco de código enquanto uma condição for verdadeira:', '1 - for loop', '2 - if statement', '3 - while loop', '4 - switch case', '3', 'Python'),
	('Método utilizado para converter uma string em letras minúsculas:', '1 - lower()', '2 - capitalize() ', '3 - upper()', '4 - swapcase()', '1', 'Python'),
	('Tipo de dado utilizado para representar números inteiros: ', '1 - int', '2 - float', '3 - str', '4 - bool', '1', 'Python'),
	('Método para verificar se uma determinada chave existe em um dicionário: ', '1 - find()', '2 - contains() ', '3 - exists() ', '4 - in', '4', 'Python'),
	('Função utilizada para arredondar um número para o inteiro mais próximo em:','1 - round()', '2 - ceil()', '3 - floor() ', '4 - abs()', '1', 'Python'),
	('Método para dividir uma string em substrings com base em um caractere de separação? ', '1 - split() ', '2 - join() ', '3 - replace()', '4 - slice()', '1', 'Python'),
	('Método para adicionar um elemento no final de uma lista em: ', '1 - insert() ', '2 - append() ', '3 - extend() ', '4 - push()', '2', 'Python'),
	('O operador lógico utilizado para verificar se duas condições são verdadeiras? ', '1 - && ', '2 - ||', '3 - and', '4 - !', '3', 'Python'),
	('Dado utilizado para representar uma sequência imutável de elementos? ', '1 - list', '2 - dictionary', '3 - set', '4 - tuple', '4', 'Python'),
	('Qual o método utilizado para obter o valor absoluto de um número? ', '1 - round()', '2 - abs() ', '3 - sqrt()', '4 - pow()', '2', 'Python'),
	('Qual a função utilizada para encontrar o valor máximo em uma lista? ', '1 - min()', '2 - sort()', '3 - sum()', '4 - max()', '4', 'Python'),
	('Função para executar um bloco de código caso uma condição seja verdadeira e outra seja falsa em Python?', '1 - if-else statement', '2 - while loop', '3 - for loop', '4 - switch case', '1', 'Python'),
	('Qual o método utilizado para converter um número em uma string? ', '1 - int()', '2 - str()', '3 - float()', '4 - convert()', '2', 'Python'),
	('Qual é o operador utilizado para realizar a concatenação de strings?', '1 - /', '2 - -', '3 - +', '4 - *', '3', 'Python'),
	('Modificador de acesso para tornar um atributo ou método visível apenas dentro da mesma classe: ', '1 - private', '2 - protected', '3 - public', '4 - default', '1', 'Java'),
	('O tipo de dado para representar números de ponto flutuante de precisão dupla? ', '1 - int', '2 - float', '3 - double', '4 - decimal', '3', 'Java'),
	('Qual é a palavra-chave utilizada para criar uma instância de uma classe? ', '1 - new', '2 - this', '3 - class', '4 - instance', '1', 'Java'),
	('Qual o operador para realizar uma comparação de igualdade entre dois valores? ', '1 - =', '2 - ==', '3 - !=', '4 - ===', '2', 'Java'),
	('O modificador de acesso para tornar um atributo/método visível para todas as classes? ', '1 - private', '2 - protected', '3 - public', '4 - default', '4', 'Java'),
	('Qual é o método utilizado para obter o tamanho de um array?', '1 - count()', '2 - sort()', '3 - length() ', '4 - size()', '3', 'Java'),
	('Qual é o método utilizado para ler a entrada do usuário? ', '1 - input()', '2 - print() ', '3 - read() ', '4 - Scanner.nextLine()', '4', 'Java'),
	('O operador utilizado para realizar uma multiplicação entre dois valores? ', '1 - +', '2 - -', '3 - *', '4 - /', '3', 'Java'),
	('Qual a palavra-chave para definir uma classe pai de outra classe? ', '1 - super', '2 - parent', '3 - this', '4 - extends', '4', 'Java'),
	('Qual é o método utilizado para converter uma string em um número inteiro? ', '1 - convertToInt()', '2 - parseInt() ', '3 - toInt() ', '4 - toInteger()', '2', 'Java'),
	('Qual é o tipo de dado utilizado para representar valores booleanos? ', '1 - boolean', '2 - int', '3 - double', '4 - char', '1', 'Java'),
	('Estrutura de controle utilizada para executar um bloco de código para um conjunto finito de valores? ', '1 - for loop', '2 - while loop', '3 - do-while loop', '4 - switch case', '1', 'Java'),
	('Qual é a classe base de todas as classes do pacote java.lang? ', '1 - Object', '2 - String', '3 - System', '4 - Math', '1', 'Java'),
	('Método para verificar se um objeto é uma instância de uma determinada classe: ', '1 - isInstance()', '2 - instanceOf() ', '3 - isClass() ', '4 - getClass()', '2', 'Java'),
	('Qual é o operador utilizado para realizar uma concatenação de strings? ', '1 - +', '2 - -', '3 - *', '4 - /', '1', 'Java'),
	('Qual é o método utilizado para remover um elemento de um ArrayList? ', '1 - remove() ', '2 - delete()', '3 - erase() ', '4 - pop()', '1', 'Java'),
	('Qual é a palavra-chave utilizada para indicar que um método não retornará nenhum valor? ', '1 - void', '2 - null', '3 - empty', '4 - none', '1', 'Java'),
	('Qual é o método utilizado para imprimir uma mensagem no console? ', '1 - print() ', '2 - println() ', '3 - log()', '4 - write()', '2', 'Java'),
	('Qual é o comando utilizado para criar um novo banco de dados?', '1 - CREATE', '2 - INSERT', '3 - UPDATE', '4 - SELECT', '1', 'Banco de Dados (SQL)'),
	('Qual é o comando utilizado para selecionar todos os registros de uma tabela? ', '1 - SELECT * ', '2 - SELECT ALL', '3 - SELECT ROWS', '4 - SELECT TABLE', '1', 'Banco de Dados (SQL)'),
	('Qual o operador para combinar múltiplas condições em uma cláusula WHERE? ', '1 - OR', '2 - XOR', '3 - NOT', '4 - AND', '4', 'Banco de Dados (SQL)'),
	('Qual é o comando usado para inserir dados em uma tabela?', '1 - INSERT INTO ', '2 - UPDATE', '3 - ADD INTO', '4 - SET VALUES', '1', 'Banco de Dados (SQL)'),
	('Qual é o comando para atualizar dados em uma tabela? ', '1 - ALTER TABLE', '2 - UPDATE', '3 - MODIFY TABLE', '4 - REPLACE INTO', '2', 'Banco de Dados (SQL)'),
	('Qual é o comando utilizado para excluir uma tabela? ', '1 - DELETE', '2 - TRUNCATE', '3 - REMOVE', '4 - DROP', '4', 'Banco de Dados (SQL)'),
	('Qual é o tipo de dados usado para armazenar valores monetários?', '1 - INTEGER', '2 - CHAR', '3 - DECIMAL', '4 - VARCHAR', '3', 'Banco de Dados (SQL)'),
	('Qual é o comando utilizado para renomear uma tabela? ', '1 - RENAME TABLE ', '2 - ALTER TABLE ', '3 - MODIFY TABLE', '4 - UPDATE TABLE', '1', 'Banco de Dados (SQL)'),
	('Operador utilizado para ordenar os resultados de uma consulta em ordem decrescente? ', '1 - DESC', '2 - ASC', '3 - ORDER BY DESC', '4 - SORT DESC', '1', 'Banco de Dados (SQL)'),
	('Comando para criar uma chave primária em uma tabela? ', '1 - PRIMARY KEY', '2 - KEY', '3 - INDEX', '4 - UNIQUE', '1', 'Banco de Dados (SQL)'),
	('Qual é o comando utilizado para criar uma tabela? ', '1 - INSERT', '2 - CREATE TABLE', '3 - UPDATE', '4 - SELECT', '2', 'Banco de Dados (SQL)'),
	('Qual é o comando usado para adicionar uma nova coluna a uma tabela existente? ', '1 - ALTER TABLE', '2 - UPDATE TABLE', '3 - ADD COLUMN', '4 - MODIFY TABLE', '1', 'Banco de Dados (SQL)'),
	('Qual o operador para buscar um padrão específico em uma consulta SELECT? ', '1 - LIKE', '2 - WHERE', '3 - MATCH', '4 - IN', '1', 'Banco de Dados (SQL)'),
	('Qual o comando para realizar uma junção (join) entre duas ou mais tabelas? ', '1 - MERGE', '2 - UNION', '3 - JOIN', '4 - CONCAT', '2', 'Banco de Dados (SQL)'),
	('Qual comando é usado para fazer uma cópia de segurança (backup) de um banco de dados?', '1 - BACKUP DATABASE', '2 - SAVE DATABASE', '3 - EXPORT DATABASE', '4 - myBanco de Dados (SQL)dump', '4', 'Banco de Dados (SQL)'),
	('Qual o tipo de dados para armazenar valores de data e hora? ', '1 - DATE', '2 - TIME', '3 - DATETIME', '4 - TIMESTAMP', '3', 'Banco de Dados (SQL)'),
	('Qual o comando para limitar o número de registros retornados por uma consulta SELECT? ', '1 - SET LIMIT', '2 - TOP', '3 - LIMIT', '4 - COUNT', '3', 'Banco de Dados (SQL)'),
	('Qual é o operador utilizado para verificar se um valor está dentro de uma lista de valores? ', '1 - BETWEEN', '2 - IN', '3 - EXISTS', '4 - IS NULL', '2', 'Banco de Dados (SQL)'),
	('Qual é o comando utilizado para conceder privilégios a um usuário? ', '1 - GRANT', '2 - ALLOW', '3 - SET PRIVILEGES', '4 - GIVE', '1', 'Banco de Dados (SQL)'),
	('Qual é o comando utilizado para revogar privilégios de um usuário? ', '1 - REVOKE', '2 - DENY', '3 - REMOVE PRIVILEGES', '4 - TAKE AWAY', '1', 'Banco de Dados (SQL)');

SELECT * FROM perguntas;

drop table perguntas;
