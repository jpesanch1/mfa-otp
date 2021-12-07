import time
import hashlib


def generate(user):
    generate_time = str(int(time.time()))

    return _calculate(generate_time, user)


def verify(user, otp_to_verify):
    generate_time = int(time.time())

    for i in range(63):
        otp = _calculate(str(generate_time - i), user)
        if otp == otp_to_verify:
            return True

    return False


def _calculate(generate_time, user):
    text_to_hash = user + generate_time
    hash = hashlib.sha1(bytes(text_to_hash, "ascii")).hexdigest()

    return str(int(hash, 16))[0:6]


if __name__ == "__main__":
    user = "jorge"
    otp = generate(user)
    print(otp)

    time.sleep(25)
    print("antes"+str(int(time.time())))
    print(verify(user, otp))
    print("despues" + str(int(time.time())))

    time.sleep(45)
    print(verify(user, otp))
