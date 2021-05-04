# data-project-2
## Setting up a Database
I decided to host a MySQL database in Docker. To do this I ran two commands in terminal:

The command simply creates a new directly on your computer. The combination of these two commands allow you to save the changes you made to the database even after you stop running Docker. This means you won't have to repopulation the table every time you load Docker again.

**$mkdir /tmp/datadir**

This command runs a Docker container and sets it up to be mounted with the directory we created in the previous command.

**$docker run -p 4000:3306 -e MYSQL_ROOT_PASSWORD=Abc123  --mount type=bind,src=/tmp/datadir,dst=/var/lib/mysql mysql:5.7**

After these commands finish running, we have a MySql environment set up. We now need to create a database. 

The first step is the open a new tab or window in terminal. Then run a few commands: 

First we run

**docker container ls**
 
## Uploading to the Database
## Analysis
