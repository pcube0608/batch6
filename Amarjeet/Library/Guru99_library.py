import base64


class Customer_library:

    def decode_passcode(self, encodepassword):
        return base64.b64decode(encodepassword).decode("utf-8")
