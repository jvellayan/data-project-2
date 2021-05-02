import requests
import schedule
import datetime


def add_data_to_db():
    #get access to the api
    response = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")

    #get data in json format
    data = response.json()

    print(data)


#get the function to execute every minute
schedule.every().minute.at(":00").do(add_data_to_db)

#keep the program running
while True:
    schedule.run_pending()