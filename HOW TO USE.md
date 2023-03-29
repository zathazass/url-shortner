A. clone repository and change it as current working directory.

$ git clone https://github.com/zathazass/url-shortner.git


B. create your virtual environment

$ virtualenv env


C. install pre-dependencies

pip install -r requirements.txt


D. run local server

python manage.py runserver


E. now you can use application in browser

http://localhost:8000


F. you can consume REST API

http://localhost:8000/api/v1/