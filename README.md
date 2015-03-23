![University of Glasgow](http://www.agripa.com/media/27266/glasgow_545x409.jpg)


----------


# What's On
What's on is a cross platform calender which enables the user to add multiple calenders, each particular to specific events, such as a university schedule or workout schedule to one manageable calender interface.


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

Default login details:

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
Add / Edit Calendars | In Progress - Alan | High
Add / Edit Events | In Progress - Alan | High
Public Events | To Do | Low
Registration / Login | Complete - Alan | High
Import Calendar | To Do | Medium
Share Calendar | To Do | Medium
Export to 3rd party | To Do | Low
Add About page | Complete - Nick | Low
Population Script | Complete - Alan | High
Test Cases | To Do | High
