import re

while True:
    # Password must be at least 8 characters long
    password = input("Enter Your Password:")

    if len(password) < 8:
        print("Password must be at least 8 characters long")
    elif not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
    elif not re.search(r"[a-z]", password):
        print("Password must contain at least one lowercase letter.")
    elif not re.search(r"[0-9]", password):
        print("Password must contain at least one number.")
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Password must contain at least one special character.")
    else:
        print("Password is Strong!")
        break  # Break out of the loop when a strong password is provided

# Add this part to make the program wait for user input
input("Press Enter to exit...")
