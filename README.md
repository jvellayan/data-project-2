# data-project-2

Data Project 1

Jaya Vellayan

## Setting up a Database
I decided to host a MySQL database in Docker. To do this I ran two commands in terminal:

The command simply creates a new directly on your computer. The combination of these two commands allow you to save the changes you made to the database even after you stop running Docker. This means you won't have to repopulation the table every time you load Docker again.

**$mkdir /tmp/datadir**

This command runs a Docker container and sets it up to be mounted with the directory we created in the previous command.

**$docker run -p 4000:3306 -e MYSQL_ROOT_PASSWORD=Abc123  --mount type=bind,src=/tmp/datadir,dst=/var/lib/mysql mysql:5.7**

After these commands finish running, we have a MySql environment set up. We now need to create a database. 

The first step is the open a new tab or window in terminal. Then run a few commands: 

First we run the command below in order to get the container ID.

**docker container ls**

Once we have the container ID, we run the below command (switching 2ec5a94f5095 to the container id displayed by the previous command) to login.

**docker exec -it 2ec5a94f5095 /bin/bash**

Then we run the command below, so that we are able to code in MySQL directly in the terminal window that we logged into Docker. The command below will prompt you for the password, which is Abc123 if exact docker run command was used.

**mysql -u root -p**
 
We then run the next two commands to create a database, and then use that database.

**create database project2;
use project2;**

Now the database is set up and ready for use!

## Uploading to the Database

The first step to getting the database ready for uploading the API information is create the table. To create a table, we run the command below in the terminal we logged into docker in.

**CREATE TABLE final ( 
	factor INT, 
	pi DECIMAL (50,25), 
	time DATETIME, 
PRIMARY KEY (factor));**

Once that is done, we use the python packages requests, schedule and mysql.connector to create a python file that will pull data from the API each minute and upload into the a MySQL table. The python package requests allows us to easily pull the information directly from the API. The package schedule allows us to easy make sure our code executes every minute at the exact same second. Finally, mysql.connector allows us to connect the python file to the database and run MySQL commands.

We use mysql.connecter.connect() to connect to the database. The parameter are as follows:

**host="127.0.0.1",
  user="root",
  password="Abc123",
  database="project2"**

In the function add_data_to_db(), we are getting data in JSON form directly from the API. Then, we are separating the data and putting it into variables. These variables are used to write the MySQL command, which is also executed every minute. There is an if statement in the code that needs to be manually updated with a time in which you want the code to stop executing. However, it is not required to update this statement because factor is the primary key in the MySQL table, and factor repeats after the hour is over. Hence, the code will stop itself when the next hour starts because the a duplicate primary would attempt to be added to the table, which does not work.

The variable job utilizes the schedule package, specifically schedule.every().minute.at(":00") to invoke the add_data_to_db() every minute at the same time. The while loop at the bottom of the code ensures that the code does not quit before it finishes executing completely. 

After an hour, when the code is done executing, we see this printed from the python file.

<img width="682" alt="Screen Shot 2021-05-04 at 2 01 45 PM" src="https://user-images.githubusercontent.com/50887095/117076180-fd3be480-ad03-11eb-8672-95efc2c1900d.png">

In the terminal running docker, we run this command to see the entire MySQL table.

**SELECT * FROM final;**

<img width="525" alt="Screen Shot 2021-05-04 at 2 00 52 PM" src="https://user-images.githubusercontent.com/50887095/117076263-1ba1e000-ad04-11eb-9c77-466c82e5b387.png">


## Analysis

Now that our table is fully populated, we can run many MySQL commands (in the terminal running Docker) to get a better understanding of the data. To start, we already know that the API repeats the same factor and pi values every hour, but that is about it. Additionally, all these commands can be found inside the commands.sql file.

I first started by gathering general information about the data and seeing if that gave me any insight on the data.

If we start by looking at pi commands and their outputs only:

**SELECT AVG(pi) FROM final;** 

The averge for the pi column is : 3.15448112351675831864406779661.


**SELECT MIN(pi) FROM final;** 

The minimum for the pi column is: 3.017071817071818.

**SELECT MAX(pi) FROM final;** 4.0

The maximum for the pi column is: 4.0.

Based on these first three statistics, we can see that there is a very small range in the pi column.

**SELECT DISTINCT pi from final;**

When this command is run, we can see that the number of pi values is still the same as the original table. Hence, every value of pi for the hour is distinct. There are no repeat values of pi.

**SELECT STD(pi) FROM final;** 0.112316521179452

**SELECT VARIANCE(pi) FROM final;** 

The standard deviation for pi is 0.112316521179452 and the variance is 0.01261500092985429, which are very small numbers. This further supports the idea that the column pi has a very small range.

**SELECT POWER(pi,(1/3)) FROM final;**

I only ran this command after I realized that the pattern in factor is the minute cubed. However, this command was not as insightful for the pi variable.


Next, we will look at the factor commands and their outputs only:

**SELECT AVG(factor) FROM final;** 

The averge for the factor column is : 53100.

**SELECT MIN(factor) FROM final;** 1

The minimum for the factor column is: 1.

**SELECT MAX(factor) FROM final;** 205379

The maximum for the factor column is: 205379.

Based on these three statistics, we can see that there is a very large range in the factor column.

**SELECT DISTINCT factor from final;**

This command was essentially useless because factor was the primary key of the table, and hence cannot have any repeats. This command confirmed that there were no repeats in factor.

**SELECT STD(factor) FROM final;** 

**SELECT VARIANCE(factor) FROM final;** 

The standard deviation for factor is 59746.97289403037 and the variance is 3569700770, which are very large numbers. This further supports the idea that the column factor has a very large range.


**SELECT POWER(factor,(1/3)) FROM final;**

If you look closer at the data, it is evident that factor is the cube of the minute in time. Hence, for the first minute (1) the cube root/factor is 1, and for the second minute (2), factor is 8, and so on. I ran this MySQL command to double check my theory. The rounding is not perfect, but we can see that my theory is correct.

<img width="371" alt="Screen Shot 2021-05-04 at 2 54 06 PM" src="https://user-images.githubusercontent.com/50887095/117077778-b8fe1380-ad06-11eb-85af-850cf0efec59.png">


Now, we can look at joint commands and their outputs:

**SELECT factor,pi FROM final ORDER BY pi DESC;**

From this command, we are able to notce a pattern in the pi column. We can see that row each new row/minute pi alternates from being the next biggest/smallest number, until it reaches itself in the middle.

<img width="494" alt="Screen Shot 2021-05-04 at 2 39 25 PM" src="https://user-images.githubusercontent.com/50887095/117077865-db902c80-ad06-11eb-8522-23d376d40324.png">


**SELECT factor/pi FROM final;**

This command was just to see if we could get anymore information, but was not very insightful.

<img width="233" alt="Screen Shot 2021-05-04 at 3 15 21 PM" src="https://user-images.githubusercontent.com/50887095/117077686-8f44ec80-ad06-11eb-89e7-ed1230ed94c4.png">


**SELECT pi/factor FROM final;**

This command was just to see if we could get anymore information, but was not very insightful.

<img width="372" alt="Screen Shot 2021-05-04 at 3 19 10 PM" src="https://user-images.githubusercontent.com/50887095/117077736-a8e63400-ad06-11eb-8523-82441e59a885.png">

**SELECT pi*factor FROM final;**

This command was just to see if we could get anymore information, but was not very insightful.

<img width="318" alt="Screen Shot 2021-05-04 at 3 20 39 PM" src="https://user-images.githubusercontent.com/50887095/117077841-d16e2e00-ad06-11eb-933c-c3a0d64df76b.png">


**SELECT power(factor, (1/pi)) FROM final;**

This command was just to see if we could get anymore information, but was not very insightful.

<img width="293" alt="Screen Shot 2021-05-04 at 3 22 36 PM" src="https://user-images.githubusercontent.com/50887095/117077904-ea76df00-ad06-11eb-965b-9e27b257d370.png">


Finally, I created two graphs of the data in excel: 

In the graph below, we can get an overview of all of the data. We see one outlier, where pi = 4. The rest of the pi values pretty much in a straight line. The factor values are rapidly increasing. 

<img width="391" alt="Screen Shot 2021-05-04 at 4 02 52 PM" src="https://user-images.githubusercontent.com/50887095/117076837-198c5100-ad05-11eb-8561-47761155e409.png">

Here is the same graphed, but zoomed in. We can see that even with a closer view, the pi value all look to be basically in a line, and the factor values are rapidly increasing.

<img width="403" alt="Screen Shot 2021-05-04 at 4 01 35 PM" src="https://user-images.githubusercontent.com/50887095/117076832-18f3ba80-ad05-11eb-8f9d-c416216c9241.png">


