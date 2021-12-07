import pyotp
import time
import base64


def generate_otp(password):
    totp = _get_totp_parameters(password)
    return totp.now()


def verify_otp(password, otp):
    totp = _get_totp_parameters(password)
    return totp.verify(otp)


def _get_totp_parameters(password):
    return pyotp.TOTP(s=str(base64.b32encode(bytearray(password, 'ascii')).decode('utf-8')), digits=6, interval=60)


if __name__ == "__main__":
    password = input("Password: ")
    print(generate_otp(password))
    otp_input = input("Introduce la otp: ")
    print(verify_otp(password, otp_input))
    otp_input = input("Introduce la otp: ")
    print(verify_otp(password, otp_input))

    time.sleep(60)
    otp_input = input("Introduce la otp: ")
    print(verify_otp(password, otp_input))
