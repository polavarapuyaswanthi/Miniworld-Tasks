import nexmo

# Replace with your Nexmo API credentials
API_KEY = "7695ca78"
API_SECRET = "oXkj4SbwmjDB5Pki"

def send_sms(phone_number, message):
    client = nexmo.Client(key=API_KEY, secret=API_SECRET)
    response = client.send_message({
        "from": "YourCompany",
        "to": phone_number,
        "text": message
    })

    if response["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response['messages'][0]['error-text']}")

def main():
    phone_number = input("Enter your phone number: ")
    message = input("Enter the message you want to send: ")

    send_sms(phone_number, message)

if __name__ == "__main__":
    main()
