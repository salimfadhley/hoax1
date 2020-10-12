import base64

CLEARTEXT_MESSAGE:bytes = "Mark, how gullible can you be? 5G is not a weapon. Go back to plumbing.".encode("utf-8")

with open("message.txt", "w") as f:
    f.write(base64.b64encode(CLEARTEXT_MESSAGE).decode("utf-8"))
