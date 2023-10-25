import json
import os
import requests
from utils.input_handler import get_user_info
from utils.base import BASE_DATA as bd
from utils.status import STATUS
from dotenv import load_dotenv

load_dotenv()


user_info = {}
BASE_URL = os.getenv('API_BASE_URL')

def welcome():
    print("HI!! welcome to brobank")
   # Open a text file for reading (replace 'filename.txt' with your file's path)
    file_path = './brobank.txt'
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
        print('Wait! this might take a moment...')
        img1 = user_info["image1_name"]
        img2 = user_info["image2_name"]

        img1_file = open(f'assets/{img1}', 'rb')
        img2_file = open(f'assets/{img2}', 'rb')

        response = requests.post(
            BASE_URL+'/api/register',
            data={'json_data': json.dumps(user_info)},
            files={
                'img1': ('img1.png', img1_file, 'image/png'),
                'img2': ('img2.png', img2_file, 'image/png') 
                }
        )

        if response.status_code == 200:
            print('congrats ',response.json()["message"])
        elif response.status_code == 401:
            print('sorry ', response.json()["message"])
        else:
            print('Something went wrong please try again')
        
    
    else:
        print("You rejected the application. redirecting to main page...")

def check_request():
    national_id = input('please enter your national ID that you registered with...\n>')

    response = requests.get(
        BASE_URL+ f'/api/check/{national_id}'
    )

    if response.status_code == 200:
        state = response.json()["state"]
        print(f'Your registeration status is at {state}')
    else:
        message = response.json()["message"]
        if response.status_code == 404:
            print(message)
        elif response.status_code == 400:
            print('we occured an error system responded with:\n', message)

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