import pyotp


otp = pyotp.OTP(s="blahblahblahblahblah", digits=6)

for input_number in range(100):
    print(otp.generate_otp(input=input_number))
