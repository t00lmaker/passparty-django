## Setup

### Ambiente virtual Python

Criar o ambiente virutal Python para não poluir o ambiente do SO:

```sh
python -m venv .venv 
```

Esse ambiente virtual é uma "copia" do ambiente python e permite que você instale bibliotecas de forma independente, sem correr o risco de quebrar as libs do sistema. Mas antes de tudo é necessário ativar o venv:

```sh
source .venv/bin/activate
```

Pronto agora todas as suas libs serão instaladas localmente no seu projeto. A primeira lib pode ser instalada: 

```sh
pip install django
```

No momento de deploy da aplicação é possível gerar a lista de dependencias por meio do comando:

```sh
pip freeze > requirements.txt
```

A partir desse arquivo é possivel instalar em outra maquina as dependencias de seu projeto com o commando: 

```sh
pip install -r requirements.txt
```


## Iniciando um novo Django Project 


Um projeto Django é formado por diversas aplicações que iteragem entre si. Uma app é permite segregar tudo de um determinado contexto em uma unidade lógica apartada.  
Abaixo o comando para gerar um projeto: 

```sh
django-admin startproject core .
```

Esse comando ira criar uma pasta core que contém as configurações gerais do projeto, o nome é indiferente, pode ser o nome do projeto, setup, core etc ... Além disso, cria um arquivo chamado manager.py que é o entrypoint para os scripts de geranciamento da aplicação Django: 


```sh
python manager.py runserver
```

Esse comando roda o servidor da aplicação utilizando o manager e a expoe na porta 8000 do localhost. 

Para gerar uma app chamada job, podemos usar o seguinte comando:

```sh
python manage.py startapp job
```

Uma vez gerada a app, é necessário adiciona-la no projeto, isso é feito por adiciona-la na constante _INSTALLED_APPS_ do arquivo __settings.py__ do projeto: 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'job.apps.JobConfig' # aqui foi add a nova app
]
```

### Migrações de Banco de dados

As aplicações contidas no django de inicio ja possuem um conjunto de tabelas que são criadas com o comando abaixo:

```sh
python manage.py migrate
```

A saida deve ser algo como : 

```sh
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

Quando você cria ou modifica um model você precisa executar o comando em seguida para gerar a migração: 

```sh
python manage.py makemigrations
```
A saída deve ser algo como: 

```sh
Migrations for 'job':
  job/migrations/0001_initial.py
    - Create model Job
    - Create model Image
```
Note que ele deve mostrar os modulos que você alterou e criar uma pasta migrations com um arquivo para a alteração. Ness caso por mais que tenha feito duas alterações, ele gera apenas um aquivo.

O próximo passo é de fato aplicar a migração no banco de dados, com o mesmo commando usado anteriormente: 

```sh
python manage.py migrate
```
Mas agora a saída mostra apenas a migration gerada sendo aplicada:

```sh
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, job, sessions
Running migrations:
  Applying job.0001_initial... OK
```

Note que na lista aplicações que indica que todas as migrations foram aplicadas foi adicionado a app job. 

Outra coisa a se notar é que as tabelas são criadas com o nome da aplicação na frente do nome da tabela. 

## Admin 


Você pode criar um usuario super admin

```sh
python3 manage.py createsuperuser
```

Será utilizado para entrar no admin do django em locahost:8000/admin.


## Heroku Deploy

1. Create files: 
  - Procfile
  - Atualize requirements.txt
  - runtime.txt 

2. Altere Settings conforme [esse modelo](https://github.com/heroku/python-getting-started/blob/main/gettingstarted/settings.py)

3. Add add on de database postgres.
 
```sh
 heroku addons:create heroku-postgresql:mini
```
4. Entre no dyno e rode os scripts de criação de tabelas de banco

```sh
 heroku run bash
```sh


## MTV - Model Template View

Esse padrão utilizado pelo Django para seu fluxo de aplicação.


