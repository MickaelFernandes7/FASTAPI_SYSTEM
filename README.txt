FASTAPI System

Descrição do Sistema: O Sistema é uma base de consulta, inserção, e deleção de produtos de uma loja de conveniência.

Métodos HTTP/FASTAPI:
- GET:    Para consultar os produtos, nos campos Compras, e Vendas, e Estoque.
- POST:  Inserir produtos nos campos de Compras e Vendas, e Estoque, os produtos, entradas e saídas.
- PUT:    Para Atualizar os produtos campos de Vendas, Compras e Estoque.
- DELETE:  Para apagar os produtos que não são mais vendidos do campo Estoque.

Como Usar o Sistema:

Início: Todos os campos precisam de um login de usuário para liberar o acesso dos campos.

Campo Usuário:

Atributos Usuário:
nome: string(texto)
email: string(texto)
password: string(texto)

Campos:

Create User (Criar Usuário):Esse campo cria um usuário.

Get User (Receber Usuário): Esse campo exibe um usuário criado com base no seu e-mail.

Update User (Atualizar Usuário): Esse campo atualiza os dados de um usuário com base no seu e-mail.
Observação: Caso esse campo seja atualizado a criptografia será alterada, e a senha será visível nas consultas posteriores.

Delete User (Deletar Usuário): Esse campo deleta um usuário com base no seu e-mail.
--------------------------------------------------------------------------------------------------------------------------
Campo Autenticação:

Atributos Login:
username: string(texto)
password: string(texto)

Campos:

Campo Login: Esse campo realiza o login e cria um token de acesso para um usuário já criado.
Observação: Ao usar esse campo digitar apenas o Username e a Senha. Digitar o E-mail no atributo Username. 
--------------------------------------------------------------------------------------------------------------------------
Campo Estoque:

Atributos Estoque:
nome: string(texto)
descricao: string(texto)
preco: int(numero inteiro)
quantidade": int(numero inteiro)

Campos:

All Inventory(Todo o Estoque): Esse campo consulta todos os produtos no estoque da loja.

Create Inventory(Criar Estoque): Esse campo insere um produto no estoque da loja.

Show Inventory(Mostrar Estoque): Esse campo exibe um produto específico por seu nome.

Update Inventory(Atualizar Estoque): Esse campo atualiza um produto específico do estoque, por seu nome.

Delete Inventory(Deletar Estoque): Esse campo deleta um produto do estoque, por seu nome.  
--------------------------------------------------------------------------------------------------------------------------
Campo Compras:

Atributos Compras:
nome: string(texto)
preco: int(numero inteiro)
quantidade: int(numero inteiro)
mes_compra: string(texto)
valor_gasto: int(numero inteiro)

Campos:
All Buy(Todas as compras): Esse campo consulta todas as compras de produtos realizadas pela loja.

Create Buy(Crie a Compra): Esse campo cria uma compra realizada pela loja e calcula o valor gasto pela quantidade e preço dos produtos.
Observação: Não é necessário preencher o atributo "valor_gasto" pois o sistema já o faz automaticamente.

Update Buy(Atualizar Compra): Esse campo atualiza uma compra já feita pela loja.
Observação: Quando usar esse campo passar o valor total gasto manualmente.
Quando usar esse campo, passar também o valor total da compra no atributo valor_gasto.

Delete Buy(Deletar Compra): Esse campo deleta uma compra feita pela loja, com base no nome da compra do produto.

Show Month Buy(Mostrar Compra do Mês): Esse campo exibe as compras realizadas em um determinado mês.
--------------------------------------------------------------------------------------------------------------------------Campo Vendas:

Atributos Vendas:
nome: string(texto)
preco: int(numero inteiro)
quantidade: int(numero inteiro)
mes_venda: string(texto)
valor_recebido: int(numero inteiro)

Campos:
All Sell(Todas as Vendas): Esse campo consulta todas as vendas de produtos realizadas pela loja.

Create Sell(Crie a Venda): Esse campo cria uma venda realizada pela loja e calcula o valor gasto pela quantidade e preço dos produtos.
Observação: Não é necessário preencher o atributo "valor_recebido" pois o sistema já o faz automaticamente.

Update Sell(Atualizar Venda): Esse campo atualiza uma venda já feita pela loja.
Observação: Quando usar esse campo passar o valor total recebido manualmente.
Quando usar esse campo, passar também o valor total da venda no atributo valor_gasto.

Delete Sell(Deletar Venda): Esse campo deleta uma venda feita pela loja, com base no nome da compra do produto.

Show Month Sell(Mostrar Venda do Mês): Esse campo exibe as vendas realizadas em um determinado mês.