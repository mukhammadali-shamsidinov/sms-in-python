import vonage


client = vonage.Client(key="505d4adc", secret="UnLrCd53sMSkN30p")
sms = vonage.Sms(client)


responseData = sms.send_message(
    {
        "from": "Muhammadali",
        "to": "998919226296",
        "text": "Hello My name is Muhammadali",
    }
)

print(responseData["messages"])

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
