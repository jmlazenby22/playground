from datetime import datetime

def greet():
    name = input("What is your name? ")
    today = datetime.now().strftime("%A, %B %d, %Y")
    print(f"Hello, {name}! Today is {today}.")

if __name__ == "__main__":
    greet()
