import hmac
import base64
import hashlib
key="123"
secret="wwwww"
string_to_sign="key=123/users/get"
def generate_sign(string_to_sign, secret):
    hmac_sha256 = hmac.new(secret.encode('utf-8'), string_to_sign.encode('utf-8'), hashlib.sha256)
    hmac_bytes = hmac_sha256.digest()
    return base64.b64encode(hmac_bytes).decode('utf-8')
