import socket

def get_user_info():
    user_info = {}
    email = input("please Enter your email address:\n>")
    last_name = input("please Enter your last name:\n>")
    national_code = input("please Enter your national code:\n>")
    IP = socket.gethostbyname(socket.gethostname()) 
    image1 = input("Please enter your first image name:\n>")
    image2 = input("Please enter your second image name:\n>")

    user_info = {
        "email": email,
        "last_name": last_name,
        "national_code": national_code,
        "ip_address": IP,
        "image1_name": image1,
        "image2_name": image2
    }

    return user_info
