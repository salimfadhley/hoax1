import base64
import codecs
rot13 = codecs.getencoder( "rot-13" )


CLEARTEXT_MESSAGE:bytes = rot13("Mark Steele is a gullible fuckwit!")[0].encode("utf-8")

with open("message.txt", "w") as f:
    f.write(base64.b64encode(CLEARTEXT_MESSAGE).decode("utf-8"))
