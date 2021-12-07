import pyotp

totp = pyotp.TOTP(s="base32secret", digits=6, interval=60)

otp_generated = totp.now()
print(otp_generated)
otp_input = input("Introduce la otp: ")
print(totp.verify(otp_input))
otp_input = input("Introduce la otp: ")
print(totp.verify(otp_input))

time.sleep(60)
