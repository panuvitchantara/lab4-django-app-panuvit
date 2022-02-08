# lab4-django-app-panuvit

For this lab, I create a docker with images from Django and Postsql. 

To do this task, I use the command 'docker-compose'. 

====== STEPS ========

1. Create a directory called 'django' to get things in a structure. 
2. Create a dockerfile. 
3. Create a 'requirements.txt' where I select the Django version and psycopg2. 
3.1 psycopg2 is an essential tool to integrate the Django to use Postgresql as the database.
4. Create a docker compose file, which this file will tell docker to select the image of Postgresql as the database, and django with a specific configuration.
4.1 The configuration is the volume which attaches to the image from the folder '/app/' (local) into '/app' (on docker).
4.2 The database configuration, I give an instruction to the docker to use the database named 'db' where it uses the Postgresql's docker image. 
5. Run the command 'docker-compose' which it is telling the docker instruction to build a particular image.

My commands:
$ docker-compose run web django-admin startproject panuvit .
//// after it is finished /////
$ docker-compose up 
//// this will run the docker to make sure that our Django is running. ////


After I got the Django runs on Docker completely. I use 'docker-compose down' command to shut down the operation. Then, I continue working with Django set-up.

The Django part. 
1. Create an app called 'staticSite' with 'docker-compose run web django-admin startapp staticSite 
2. In the staticSite's folder, I create a function to return HTTPRespond with "Hello from Panuvit SAD2022". 
3. In the staticSite's folder, I also create a 'urls.py' to create own routing for the app.
4. Change the main url.py with 'include' the path from our app. 
5. Run the docker again with 'docker-compose up'.

/// Finish The lab /////
