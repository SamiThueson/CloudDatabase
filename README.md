# Overview

As a learning software engineer I want to further my knowledge and learn to code better and efficiently. I decided to research and create my own cloud database to help further my knowledge.

I created my own cloud database by using Google Firestore. From there I used Python to integrate the database and manipulate it. I created a bunch of different functions to display, insert, and delete from the database. It is quite simply to understand and use. 

Below is a link to a demo and walkthrough of my cloud database.

[Software Demo Video](https://youtu.be/ZFfuOeGQSoU)

# Cloud Database

I used Google Firestore which is a cloud database. It is a NoSQL database meaning it is not a relational database, but a key/value pair database. It stores data into maps that can be queried in different ways.  

The database that I created has one table in it called 'places'. Within the table you can store cities that you would like to visit someday. The cities have different fields such as, 'latitude', 'longitude', and 'where to go' that you can store values into. 

# Development Environment

The tools I used to create the cloud database were Firebase/Google Firestore. In order to use Firestore you have to create an account and then create the database. In order to connect to the database you have to authenticate it by using a private key from your account. 

I used Python as my programming language to be able to read and write to the database. Within python I used the library firebase_admin to be able to connect to the database and authenticate that I do own the database and can manipulate it. 

# Useful Websites

* [Information About What Firebase Is](https://firebase.google.com/docs/firestore)
* [Quick Start for Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart)
* [Google Cloud Help With Authentication](https://cloud.google.com/docs/authentication/getting-started)
* [Helpful Tutorial Using Python and Firestore](https://towardsdatascience.com/nosql-on-the-cloud-with-python-55a1383752fc)
* [Videos On Getting To Know Cloud Firestore](https://www.youtube.com/playlist?list=PLl-K7zZEsYLluG5MCVEzXAQ7ACZBCuZgZ)

# Future Work

* Make the documents display prettily
* Add more ways of querying items
* Fix the add_field function so that you can't add the same field multiple times
* Create another table that is related to the current table