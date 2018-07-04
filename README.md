
# Catálogo
Essa aplicação feita em Python utilizando o framework Flask é um catálogo de produtos. A página inicial apresenta as categorias dos produtos, ao acessar uma categoria você é apresentado aos itens presentes nesse grupo e em cada ítem é mostrado um imagem, preço e breve apresentação do protudo utilizando texto.

## Instalação
Abaixo temos os passos necessários para conseguir rodar esta aplicação:

1. **Instalar os pacotes utilizados no projeto** - utilizando o `pip` instale os seguintes pacotes mostrados abaixo:
    * `$ pip install Flask`
    * `$ pip install sqlalchemy`
    * `$ pip install passlib`
    * `$ pip install flask-httpauth`
    * `$ pip install httplib2`
    * `$ pip install psycopg2`
    * `$ pip install psycopg2-binary`
    * `$ pip install requests`
    * `$ pip install oauth2client`

2. **Download do projeto** - basta fazer um clone, fork ou download desse projeto, direto para sua máquina.
3. **Criar o banco de dados** - utilizando o comando `python database_setup.py` será criado o banco de dados chamado `catalogo.db`.
4. **Levantando a aplicação** - execute o comando `python app.py` para rodar a aplicação.
5. **Abrindo no navegador web** - escolha um navegador web e digite na `http://localhost:5000` na barra de navegação e aplicação será apresentada.


## Como utilizar a aplicação
Antes de utilizar a aplicação certifique-se de que executou os passos 4 e 5 do item anterior.

### Tela inicial
Abaixo é apresentado a tela inicial. Na imagem abaixo vemos algumas categorias, no entanto no seu caso não se preocupe caso não apareça os campos com as categorias isso está acontecendo porque no seu caso não foram cadastradas nenhuma categoria ainda.
![Tela Inicial](static/images/readme/tela_inicial.png)

### Fazer login
Para fazer login basta clicar no canto superior direito, sobre a palavra `Login` e a tela abaixo será apresentada. Para se logar basta clicar no botão azul escrito `Fazer login`. Ao clicar sobre o botão uma tela de autenticação do Google será aberta e apresentará pelo menos uma conta do Google (caso tenha cadastro no Google), escolha sua conta e você será redirecionado para a plataforma Catálogo.
![Fazer Login](static/images/readme/tela_login.png)

### Dentro da plataforma - Logout, Nova Categoria, Editar Categoria, Deletar Categoria
Lembrando novamente, para você não aparecerá os cards com as categorias porque você não cadastrou nada ainda. Nessa tela você poderá fazer logout apenas clicando sobre a palavra `Logout` no canto superior direito e será levado a tela da primeira imagem. Para criar uma nova categoria basta clicar no botão `Nova Categoria` uma tela para preenchimento dos dados será apresentada (essa tela será mostrada abaixo). Fazer a edição de uma categoria já inserida é só clicar no botão azul claro que fica no canto esquerdo inferior, com isso você será levado para uma tela de edição dos dados da categoria (essa tela também será apresentada na sequência). Excluir uma categoria também é bem simples, é só clicar no botão com ícone de lixeira e uma página pedindo a confirmação será aberta.
![Logado](static/images/readme/dentro_plataforma_inicio.png)

### Nova categoria
A seguir temos a tela com os campos para criar uma nova categoria.
![Nova categoria](static/images/readme/nova_categoria.png)

### Editar categoria
A seguir temos a tela com os campos para editar uma categoria.
![Editar categoria](static/images/readme/editar_categoria.png)

### Deletar categoria
A seguir temos a tela com os campos para excluir uma categoria.
![Deletar categoria](static/images/readme/delete_categoria.png)

### Itens de uma categoria
Apresentar os itens criados de cada categoria é só clicar sobre o nome ou imagem de uma categoria e a tela abaixo será apresentada. Nessa tela podemos criar um novo item dessa categoria bastando para isso clicar no botão `Novo Item`. Se precisar editar um item basta clicar no botão verde no canto inferior esquerdo. Caso queira excluir o item clique no botão com ícone de lixeira. Assim com acontecia na categoria, ao clicar nos botões editar ou excluir você será levado para uma tela de edição ou exclusão. No canto esquerdo há uma lista com as categorias cadastradas, ao clicar em uma delas será mostrado os itens dessa categoria.
![Itens de uma categoria](static/images/readme/tela_itens.png)

### Descrição de um item específico
Ao clicar sobre o nome ou imagem de um item específico será apresentado um tela semelhante à mostrada abaixo.
![Itens de uma categoria](static/images/readme/desc_item.png)

## Utilizar a API
Na documentação a seguir utilizaremos o `curl` para apresentar os exemplos da utilização da API.

### Requisitar dados dos usuários
#### Todos os usuários
Utilizando o comando abaixo será retornado um JSON com os dados de todos os usuários cadastrados na plataforma.

`$ curl -X GET http://localhost:5000/user/api`


#### Usuário específico
Utilizando o comando abaixo será retornado um JSON com os dados de um usuário específico.

`$ curl -i -X GET http://localhost:5000/user/api/1`


### Requisitar dados das categorias

#### Todas as categorias
Com a linha abaixo será retornado todas as categorias presentes na plataforma

`$ curl -X GET http://localhost:5000/category/api`


#### Nova categoria
Para criar uma nova categoria basta utilizar a estrutura do exemplo abaixo.

`$ curl -i -X POST -H "Content-Type: application/json" -d '{"category_name":"Outra Categoria", "category_description":"Uma descrição qualquer aqui"}' http://localhost:5000/category/api/1`

#### Categoria específica
Retorna os dados de uma categoria específica

`$ curl http://localhost:5000/category/api/1`

#### Editar categoria
Para editar uma categoria basta utilizar a estrutura do exemplo abaixo.

`$ curl -X PUT -H "Content-Type: application/json" -d '{"category_name":"Tasaki", "category_description":"Categoria alterada para Tasaki"}' http://localhost:5000/category/api/1`

#### Deletar categoria
Para excluir uma categoria basta utilizar a estrutura do exemplo abaixo.

`$ curl -i -X DELETE http://localhost:5000/category/api/1`

### Requisitar dados dos itens

#### Todos os itens
Retorna todos os itens cadastrados na plataforma.

`$ curl -X GET http://localhost:5000/item/api`


#### Todos os itens de uma determinada categoria
Retorna todos os itens de uma determinada categoria.

`$ curl -X POST http://localhost:5000/item/api/1`

#### Atualizar um item específico
Para atualizar um item específico basta utilizar a estrura do exemplo abaixo.

`$ curl -X PUT -H "Content-Type: application/json" -d '{"item_name":"Tasaki", "item_long_description":"Uma descrição longa aqui.", "item_short_description":"Uma descrição curta aqui.", "price":"70.00"}' http://localhost:5000/item/api/1`


#### Exclui um item específico
Para excluir um item específico basta utilizar a estrutura do exemplo abaixo.

`$ curl -X DELETE http://localhost:5000/item/api/1`

## Licença
O projeto Análise de Logs foi lançado com a licença [MIT
license](https://github.com/atom-community/markdown-preview-plus/blob/master/LICENSE.md).