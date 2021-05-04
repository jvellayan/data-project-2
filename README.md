# data-project-2
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

The
## Analysis
