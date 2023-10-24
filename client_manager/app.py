from utils.input_handler import get_user_info
from utils.s3_handler import *
from base import BASE_DATA as bd
from utils.status import STATUS

BASE_URL = "http://localhost:500/api"
user_info = {}


def welcome():
    print("HI!! welcome to brobank")
   # Open a text file for reading (replace 'filename.txt' with your file's path)
    file_path = 'brobank.txt'
    try:
        with open(file_path, 'r') as file:
            # Read the entire file content
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def print_menu():
    print(
        """
        1) Register new Account
        2) Check your request
        3) exit
        """
        )
    
def initiate():
    welcome()

def file_address_generator(raw_address):
    print("user info: ", user_info)
    nat_code = user_info["national_code"]
    return [f"./assets/{raw_address}", f"{nat_code}{raw_address}"]


def register_request():
    global user_info 
    user_info = get_user_info()
    print("this is your info:")
    for i in user_info:
        print(i, " : " ,user_info[i])
    acceptance = input("are you sure?\n1)yes\n2)No\n>")
    if acceptance == '1':
        # endpoint_url= bd["ARVAN_CLOUD_ENDPOINT"]
        # secret_key = bd["SECRET_KEY"]
        # access_key = bd["ACCESS_KEY"]
        # bucket_name = bd["BUCKET_NAME"]
        # file_addresses = list(map(file_address_generator, [user_info["image1_name"], user_info["image2_name"]]))
        
        # # print(file_addresses)
        # for file in file_addresses:
        #     arvan_uploader(endpoint_url, access_key, secret_key, bucket_name, file[0], file[1])
    
     pass
    else:
        print("You rejected the application. redirecting to main page...")

def check_request():
    pass

def user_loop():
    loop_condition = True
    while loop_condition:
        print_menu()
        user_input = input("please pick a choice:\n>")

        if user_input == '1':
            register_request()
        elif user_input == '2':
            check_request()
        else:
            loop_condition = False

if __name__ == '__main__':
    initiate()
    user_loop()