import hmac

import pyotp
import base64
import qrcode
import time
from PIL import Image
from cryptography.hazmat.primitives import hmac, hashes


def generate_google_authenticator_account(data, user, domain_name):
    key_base32 = str(base64.b32encode(bytearray(data, 'ascii')).decode('utf-8'))
    data_to_generate_qr = pyotp.totp.TOTP(key_base32).provisioning_uri(name=user+"@"+domain_name)
    img = qrcode.make(data_to_generate_qr)
    type(img)
    path = "../" + data + ".png"
    img.save(path)
    og_image = Image.open(path)
    og_image.show()


def generate_otp(data):
    key_base32 = str(base64.b32encode(bytearray(data, 'ascii')).decode('utf-8'))
    totp = pyotp.TOTP(key_base32)

    return totp.now()


def verify_otp(data, otp):
    otp_calculated = generate_otp(data)
    print(otp_calculated)

    if otp == otp_calculated:
        return True
    return False


def code_generator(data):
    key = bytes(data, 'ascii')
    message = int(time.time() / 30)

    hash = hmac.HMAC(key, hashes.SHA1())
    hash.update(message.to_bytes(8, "big"))
    h = hash.finalize()

    offset = int(h.hex()[-1:], 16)

    truncated_hash = h[offset:offset + 4]
    truncated_hash = int.from_bytes(truncated_hash, "big") & 0x7fffffff

    code = truncated_hash % 1000000

    code = str(code).zfill(6)

    return code


if __name__ == "__main__":
    # user = input("user: ")
    # password = getpass.getpass(prompt="password: ", stream=None)
    # domain_name = input("domain name: ")
    # generate_google_authenticator_account(user+password, user, domain_name)
    # otp = input("otp: ")
    # print(verify_otp(user+password, otp))

    print(code_generator("blablablabla"))
