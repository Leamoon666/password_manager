from random import choice, randint, shuffle
from tkinter import messagebox
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_random = [choice(letters) for _ in range(randint(8, 10))]

    symbols_random = [choice(symbols) for _ in range(randint(2, 4))]

    numbers_random = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_random + symbols_random + numbers_random
    shuffle(password_list)

    random_password = "".join(password_list)
    return random_password

def save_data(website, email, password):
    information = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Field empty", message="Field must be filled, try again")
        return None
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(information, data_file, indent=4)
        else:
            data.update(information)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        return True