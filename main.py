import requests
import schedule
import datetime
import mysql.connector

#connect to database
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Abc123",
  database="project2"
)

mycursor = mydb.cursor()



def add_data_to_db():
    # get access to the api
    response = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")

    # get data in json format
    data = response.json()
    # assign variables to different parts of the json
    f = data['factor']
    p = data['pi']
    t = data['time']

    # print to ensure timing is correct
    print(data)

    # create and excute sql statement
    sql = f"INSERT INTO final (factor,pi, time) VALUES ({f}, {p}, '{t}')"
    mycursor.execute(sql)

    #commit statement to database
    mydb.commit()


    # cancel after it has run enough
    # needs to be manually changed to the time you want the execution to stopped
    if data["time"][0:16] == "2021-05-04 18:00":
        schedule.clear()
        quit()
    return data

# get the function to execute every minute
job = schedule.every().minute.at(":00").do(add_data_to_db)


#keep the program running
while True:

    # get the function to execute every minute
    schedule.run_pending()



    