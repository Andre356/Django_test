# PGS_test

"Zadanie rekrutacyjne

Przygotuj aplikację z wykorzystaniem ORM pozwalającą stworzyć i zapisać w bazie danych dwa typy obiektów: User oraz Group. Modele te mają być w realacji wiele do wielu, jeden użytkownik może należeć do wielu grup, grupa może zawierać wielu użytkowników. Przygotuj dwa endpointy zgodne z REST pozwalające na wykonanie wszystkich operacji CRUD na tych modelach. Dodatkowo endpointy powinny umożliwiać wyświetlenie na żądanie powiązanych obiektów, tj. użytkownika wraz z grupami lub grupy wraz z użytkownikami.

Do projektu należy dołączyć plik Readme.md opisujący w jaki sposób uruchomić aplikację oraz plik pozwalajacy zainstalować wszystkie zależności (requirements.txt lub setup.py)."

# Tech!
This project uses a number of open source projects to work properly:
  - Python 3.x
  - Django 2.1.2
  - DjangoRestFramework 3.8.2
  - Bootstrap 4

# Installation

This application requires Python 3.6.5 to run.
Copy all files to a directory.

Install the dependencies and start the server:
### For Windows (cmd):
```sh
virtualenv myvnv
myvnv\Scripts\activate.bat
pip install -r requirements.txt
cd test_PGS_project
python manage.py runserver
```
### For Unix (Debian):
```sh
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
virtualenv myenv
```
Download the project to a proper dir and follow this steps
```sh
source myenv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

### How to start?
If local server is running just go to this url and test:
```sh
http://127.0.0.1:8000/main/home
```
# REST API
Endpoint for User model:
```sh
http://127.0.0.1:8000/main/usersset/
```
Endpoint for Group model:
```sh
http://127.0.0.1:8000/main/groupsset/
```
License
----
**Free Software, Hell Yeah!**