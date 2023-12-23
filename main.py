import requests
import ezgmail

dog_image_url = requests.get("https://dog.ceo/api/breeds/image/random").json()["message"]
dog_image_url_response = requests.get(dog_image_url)
dog_image_file = open("dog_image.png","wb")
dog_image_file.write(dog_image_url_response.content)



email_id_list = []
print("Enter number of email ids: ")
no_of_email_ids = input()

for i in range(0,no_of_email_ids):
    email_id = input()
    email_id_list.append(email_id)

subject = "Daily Dog Picture"
text = "This is a dog picture."
for i in range(0,no_of_email_ids):
    ezgmail.send(email_id_list[i], subject, text, dog_image_file)