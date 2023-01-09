# SeazoneCodeChallenge

Olá, Meu nome é João Teixeira de Loiola Netto e o intuito deste repositório é apresentar minha resolução ao desafio solicitado.

Espero que gostem :)
	
# Carregar Bibliotecas
Baixe as bibliotecas para executar esse projeto usando o comando:
> $ pip install -r requirements.txt
	
# Criar banco de dados

> $ py manage.py makemigrations api

> $ py manage.py migrate


# Cadastrar dados ao banco (Fixtures)

> $ py manage.py loaddata fixtures/imoveis.json --app api.Imovel
> $ py manage.py loaddata fixtures/anuncios.json --app api.Anuncio
> $ py manage.py loaddata fixtures/reservas.json --app api.Reserva


# Rodar aplicação
> $ py manage.py runserver

