import requests
import ezgmail
import time

dog_image_url = requests.get("https://dog.ceo/api/breeds/image/random").json()["message"]
dog_image_url_response = requests.get(dog_image_url)
dog_image_file = open("dog_image.png","wb")
dog_image_file.write(dog_image_url_response.content)



email_id_list = []
no_of_email_ids = input("Enter number of email ids: ")
no_of_email_ids = int(no_of_email_ids)

print("Please input the e-mail ids one by one: ")
for i in range(0,no_of_email_ids):
    email_id = input()
    email_id_list.append(email_id)

while True:
    print("Enter frequency, 1. just once 2. every hour 3. daily")
    frequency = input()
    if frequency == "1": 
        subject = "Dog Picture"
        text = "This is a dog picture."
        for i in range(0,no_of_email_ids):
            ezgmail.send(email_id_list[i], subject, text, "dog_image.png")
        break
    elif frequency == "2":
        subject = "Dog Picture"
        text = "This is a dog picture."
        while True:
            if time.ctime().split()[3].split(':')[1] == "00" and time.ctime().split()[3].split(':')[2] == "00":
                for i in range(0,no_of_email_ids):
                    ezgmail.send(email_id_list[i], subject, text, "dog_image.png")
    elif frequency == "3":    
        subject = "Dog Picture"
        text = "This is a dog picture."
        while True:
            if time.ctime().split()[3] == "00:00:00":
                for i in range(0,no_of_email_ids):
                    ezgmail.send(email_id_list[i], subject, text, "dog_image.png") 
    else:
        print("Please try again")
        continue
