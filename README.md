# desafio-back-end
>
Parsear este arquivo de [texto(CNAB)](https://github.com/Angelmzm/desafio-back-end/blob/main/CNAB.txt) e salvar suas informações(transações financeiras) em uma base de dados com as seguintes informações: 
>
-Tipo da transação
>
-Data da ocorrência
>
-Valor da movimentação
>
-CPF do beneficiário
>
-Cartão utilizado na transação
>
-Hora da ocorrência atendendo ao fuso de UTC-3
>
-Nome do representante da loja
>
-Nome da loja
>

## Passos de instalação:
>
1- Crie o ambiente virtual:
```
python -m venv venv
```
>
2- Ative o venv:
>
linux:
```
  source venv/bin/activate
 ```
windows:
 ```
  .\venv\Scripts\activate
 ```
 >
 3- Instale os pacotes necessário:
```
pip install -r requirements.txt
```   
## Passos para execução em ambiente de desenvolvimento:
>
1- Configurar o dotenv:
>
criar uma pasta chamada .env igual a pasta .env.examplo e preencher as informações
>
 2- Fazer as migrações:
```
python manage.py makemigrations
```
3- Rodar as migrações:
```
python manage.py migrate
```
4- Colocar o servidor para rodar:
```
python manage.py runserver  
```
5- Abrir o navegador
>
ctrl + click no link 
>
## Tecnologias utilizadas:
>
- Python
>
- Django
>
- Dotenv
>
