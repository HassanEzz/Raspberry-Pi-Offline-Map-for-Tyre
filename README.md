# Raspberry-Pi-Offline-Map-for-Tyre
Offline Map for Tyre

This project helps tourists find their destination in Tyre without Internet.

Participants are:

	Ibrahim Shahine

	Diana Alkouraeye

	Mohammad Kaiin

	Mohammad AlSamra

A database is used to complete the project that has two GUI created using python and many 
library like MySQLdb and Tkinter:

			•	One GUI that has many buttons, every one leads to a map.

			•	The second helps to insert another map. 

in this project we have two python files and a sql file:

 "map.py": this will create a GUI that contains several buttons; every one open a map by clicking on it. this GUI is connected
            database "map" that has a table named "tyr" every record has two feilds 'name' and 'image'.
            
 "entry.py": this will create a GUI that contains two entry and a button; this let us enter a new record to the database "map"
               in the table "tyr" the name of the map and an image of it.
               
 "map.sql": this file is the database "map" of the project; 
            for importing this database you use this instruction in the terminal:
     (mysqldump -u root -p map < map.sql) where root is your mysql username and map the name of the database

