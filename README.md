Django 1.7
==========

Exemplo mínimo de um projeto Django baseado no site [djangoproject.com][0].

O site mostra uma *Intro to Django* em [Get started with Django][1]. Então veremos aqui como instalar um **virtualenv**, instalar o *Django 1.7* nele e criar um projeto baseado em *Intro to Django*.

| ![YouTube](http://pythonclub.com.br/images/regisdasilva/youtube_logo.png) | ![PythonClub](http://res.cloudinary.com/diu8g9l0s/image/upload/v1400201393/pythonclub/logo_275x130.png) |
|------------------------------|------------------------------|
| [YouTube][6]          	   | [PythonClub][7]                  |


Veja o video no [Youtube][6] e o post no [PythonClub][7].

### Instalando alguns programas

* **[VirtualEnv][2]**
 
Para instalar o *virtualenv* abra o terminal e digite

	$ sudo apt-get install -y virtualenv

* **[Pip][3]**
 
Para instalar o *pip* digite

	$ sudo apt-get install -y python-pip

### Criando a ambiente

Vamos criar um ambiente usando o **Python 3**, então digite

	$ virtualenv -p /usr/bin/python3 django1.7

onde ``django1.7`` é o nome do ambiente.

Entre na pasta

	$ cd django1.7

e *ative o ambiente*

	$ source bin/activate

Para diminuir o caminho do prompt digite
	
	$ PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ "

### Instalando [Django 1.7][0] + [django-bootstrap3][4]

	$ pip install django==1.7.2 django-bootstrap3

*Dica*: se você digitar ``pip freeze`` você verá a versão dos programas instalados.

### Criando o projeto

Para criar o projeto digite

	$ django-admin.py startproject mysite .

repare no ponto no final do comando, isto permite que o arquivo ``manage.py`` fique nesta mesma pasta *django1.7*.

### Criando a app

Agora vamos criar a *app* **bands**, mas vamos deixar esta *app* dentro da pasta *mysite*. Então entre na pasta

	$ cd mysite

e digite

	$ python ../manage.py startapp bands

A intenção é que os arquivos tenham a seguinte hierarquia nas pastas:

	.
	├── fixtures.json
	├── manage.py
	├── mysite
	│   ├── bands
	│   │   ├── admin.py
	│   │   ├── forms.py
	│   │   ├── models.py
	│   │   ├── templates
	│   │   │   ├── bands
	│   │   │   │   ├── band_contact.html
	│   │   │   │   ├── band_detail.html
	│   │   │   │   ├── band_form.html
	│   │   │   │   ├── band_listing.html
	│   │   │   │   ├── member_form.html
	│   │   │   │   └── protected.html
	│   │   │   ├── base.html
	│   │   │   ├── home.html
	│   │   │   └── menu.html
	│   │   ├── tests.py
	│   │   └── views.py
	│   ├── settings.py
	│   ├── urls.py


Agora permaneça sempre na pasta *django1.7*

	$ cd ..

e digite

	$ python manage.py migrate

para criar a primeira *migração* e

	$ python manage.py runserver

e veja que o projeto já está funcionando.

### Video no YouTube

Agora assista o video no [youtube][6] e também leia [PythonClub][7].

### Carregando dados de um **json**

Se você digitar o comando abaixo alguns dados já serão carregados no banco de dados.

	$ python manage.py loaddata fixtures.json

Mas é claro que isso é só no final de tudo.

Boa sorte!

[0]: https://www.djangoproject.com/
[1]: https://www.djangoproject.com/start/
[2]: https://virtualenv.pypa.io/en/latest/
[3]: http://pip.readthedocs.org/en/latest/
[4]: http://django-bootstrap3.readthedocs.org/en/latest/
[5]: https://docs.djangoproject.com/en/1.7/intro/tutorial01/
[6]: https://www.youtube.com/watch?v=OayIF9Pz7rE
[7]: http://pythonclub.com.br/tutorial-django-17.html