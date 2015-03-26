![University of Glasgow](http://www.agripa.com/media/27266/glasgow_545x409.jpg)


----------


# What's On
What's On is a project for Web Application Development 2 at The University of Glasgow. What's on is a cross platform calender which enables the user to add multiple calenders, each particular to specific events, such as a university schedule or workout schedule to one manageable calender interface.


----------


## Instructions to run application
To run this application clone into this repository and then install the required packages onto your system:

        $ pip install -U django==1.7
        $ pip install django-mathfilters
        $ pip install django-datetime-widget

You will then have to setup the database with the following commands:

        $ python manage.py makemigrations
        $ python manage.py migrate

To insert test data into your database execute this command:

        $ python populate_whatson.py

Default login credentials:

        username = test
        password = test


----------


## Features

Task  | Status | Priority
------------- | ------------- | -------------
HTML / CSS | Complete - Alan | High
Premade Calendar Integrated  | Complete - Alan | High
Calendar / Events Model  | Complete - Alan | High
Calendar / Events View | Complete - Alan | High
Add / Edit Calendars | Complete - Alan | High
Add / Edit Events | Complete - Alan | High
Public Events | In Progress - Alan | Low
Registration / Login | Complete - Alan | High
Export to 3rd party | Complete - Nick | Low
Add About page | Complete - Nick | Low
Population Script | Complete - Alan | High
Test Cases | In Progress - Ross | High
Import Calendar | Complete - Nick| Medium
Making Import Calendar Modal | In Progress - Ross | Medium
Validate HTML | Complete - Nick | High