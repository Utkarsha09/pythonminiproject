import random

otp = random.randrange(100000, 1000000)
print(otp)
user=int(input("Enter OTP:: "))
if user== otp:
    print("Access granted!!!!")
else:
    print("Access Denied!!!!")