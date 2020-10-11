import base64

CLEARTEXT_MESSAGE = b"Mark Steele is the biggest idiot of all time."

with open("message.txt", "w") as f:
    f.write(base64.b64encode(CLEARTEXT_MESSAGE).decode("utf-8"))
