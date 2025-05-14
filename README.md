# ml-engineer-assignment
This project is a take home assignment for a machine learning engineering role. It requires uploading a CSV file into a postgres SQL database and a couple python functions to work with the data. 

I did not have any issues with this assignment, however, I did change the CSV file since it had an issue with record #17 having 6 columns as opposed to 5 due to the client name being spilt into first and last names. After much thought I decided to fix the CSV as opposed to code a work around because this would be how a CSV file would normally be handled. Usually source files have data standards to ensure all records have an equal number of columns. In the event someone made a customm CSV with a mistake usually the solution would involved fixng the CSV as opposed to changing the data pipeline.

To run ths assignment please use the following steps:
1. open the psql terminal
2. run the command "\i Desktop/RBC/create_user.sql" to create a role named "bank"
3. run the command "\i Desktop/RBC/create_database.sql" to create a database name "clientdb"
4. run the command "\c clientdb bank" to change into the new database with the new role
5. run the command "\i Desktop/RBC/create_database_objects.sql" to create the necessary schema and tables
6. run the command "\i Desktop/RBC/insert_data.sql" to insert the data
7. open python
8. run the script create_sql_function.py to locally test the different functions

Important Notes:
1. You will need to change the filepath in insert_data.sql to accomendate the CSVs location your compurter
2. You may need to change some information in the yaml file to accomendate your postgres settings

Thank you and I hope you enjoy my code.



