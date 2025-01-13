python packages:
https://docs.python.org/3/tutorial/modules.html#tut-packages

a module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

The __init__.py files are required to make Python treat directories containing the file as packages 

__all__ : if defined, all submodules will be imported from the parent packaging when douin from package import *

1. Create a project: 
django-admin startproject mysite

2. Create an app:
python manage.py startapp polls

3. Add the view with the name (the endpoint).if "" as first argument, it is the default view

4. Add the url to the app

5. Add the url to the project

6. create and migrate  all the apps with database (list in installed apps in settings.py) with the command python manage.py migrate

7. check the database. if SQLite, use the command python manage.py dbshell

8. once in the shell, you can use SQL commands to check the database (e.g. .tables to see the tables)

9. create a model in the app

10. create the migration file with the command
' python manage.py makemigrations polls (makemigration = update)'

Other commands:
 'python manage.py check' = check for problems in the project without making migrations'
 'python manage.py sqlmigrate polls 0001' = check the SQL code that will be executed
 'python manage.py shell' = open the python shell

11. create an admin superuser
'python manage.py createsuperuser'

12. add the model to the admin interface (in the app admin.py)


## Django Template Language (DTL): ##

Tags¶
Tags provide arbitrary logic in the rendering process.

This definition is deliberately vague. For example, a tag can output content, serve as a control structure e.g. an “if” statement or a “for” loop, grab content from a database, or even enable access to other template tags.

Tags are surrounded by {% and %} like this:

{% %} : Balises de contrôle (logique).
{{ }} : Balises d'affichage des variables ou résultats.

{% csrf_token %} template tag. This is used to prevent Cross Site Request Forgerie (in french: protection contre les requêtes intersites) attacks.

## summary vmt model ##
1. View: a function that handle the http request, interacts with the model and send a response http, usually rendered with a template

2. model: a representation of a table in a database. it defines the database structure that we want to stock and manipulate

3. template: a file that contains the html code that will be rendered by the view

use the PRG (Post/Redirect/Get) pattern:
use httpresponseRedirect to avoid the form to be sent twice if the user refresh the page after submitting the form (the browser will send the form again)



todo:
migration when mouting the docker
make all dockers up

