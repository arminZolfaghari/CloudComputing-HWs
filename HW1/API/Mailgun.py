import requests

EMAIL_ADDRESS = "test@gmail.com"
TEXT = "Your ad (ID) has been accepted!"
SUBJECT = "Cloud Computing HW1"


# get YOUR_DOMAIN_NAME and YOUR_API_KEY from Mailgun dashboard
def send_simple_message(email, subject, text):
    return requests.post(
        f"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", "YOUR_API_KEY"),
        data={"from": "<mailgun@YOUR_DOMAIN_NAME>",
              "to": [email],
              "subject": subject,
              "text": text})


if __name__ == '__main__':
    response = send_simple_message(EMAIL_ADDRESS, SUBJECT, TEXT)
    print(response.json())
