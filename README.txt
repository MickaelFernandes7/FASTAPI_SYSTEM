FASTAPI System

Descrição do Sistema: O Sistema é uma base de consulta, inserção, e deleção de produtos de uma loja de conveniência.

Estrutura do Sistema – Campos e Sua Descrição:

- Estoque: Consultamos a quantidade de produtos da loja. (HTTP: GET, SQL: SELECT)
Aqui também podemos adicionar produtos aos estoques. (HTTP:POST, SQL: INSERT)
Aqui podemos atualizar produtos que foram vendidos. (HTTP: PUT, SQL: UPDATE)
Podemos apagar os produtos que já não são mais vendidos. (HTTP: DELETE, SQL: DELETE OU TRUNCATE)

- Vendas: Aqui vamos colocar um campo que adiciona os produtos vendidos e Seus valores. (POST, INSERT, GET)

- Compras: Aqui vamos listar as compras que fizemos dos produtos adquiridos. (HTTP: POST, GET) 

- Criar um método para de entrada de usuário para conceder a permissão de consultar, e inserir, e deletar produtos aos campos.

Produto: O produto deve conter: Nome, Descrição, Quantidade, e Preço.

Métodos HTTP/FASTAPI:
- GET:    Para consultar os produtos, nos campos Compras, e Vendas, e Estoque.
- POST:  Inserir produtos nos campos de Compras e Vendas, e Estoque, os produtos, entradas e saídas.
- PUT:    Para Atualizar os produtos campos de Vendas, Compras e Estoque.
- DELETE:  Para apagar os produtos que não são mais vendidos do campo Estoque.

Como Usar o Sistema:

Campo Estoque:

Campo Compras:

Campo Vendas: