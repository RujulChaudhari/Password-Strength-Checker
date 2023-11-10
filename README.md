# Welcome to the Password Strength Checker Project! 

## Overview:

This project is a simple password strength checker implemented in Python. It checks various criteria, such as password length, the presence of uppercase and lowercase letters, numbers, and special characters.

## Key Features:

- **Password Length Check:** Ensures the password is at least 8 characters long.
- **Uppercase Letter Check:** Requires at least one uppercase letter in the password.
- **Lowercase Letter Check:** Requires at least one lowercase letter in the password.
- **Number Check:** Requires at least one number in the password.
- **Special Character Check:** Optionally, you can add a check for at least one special character in the password.

## Getting Started:

- You will need Python and VScode for this project.
- <a href="https://www.python.org/downloads/"> Download Python Here</a>
- <a href="https://code.visualstudio.com/download"> Download VScode Here</a>

## Step 1:
- Open up VScode.
- Create a new python script, this will be our main PW checker file.
- ![](https://i.imgur.com/A5DMyG9.png)

## Step 2:
- Copy the code above into your script.
- Open up terminal in VScode.
- run the following command:
  ```bash
  pip install pyinstaller
- What this will do is help us compile our python script into a executable exe file.

## Step 3:
- Once you've verified the script works without any errors.
- Run the following command in terminal in your terminal to compile it as a .exe file. <br>
  ```bash
  pyinstaller --onefile your_script_name.py
- This wil create a Build and dist folder where your project is located. The exe file will be under the "dist" folder.
- Go ahead and run the .exe file to make sure it's working. <br>
`NOTE: You might need to add the exe file to your anti-virus as an exception.`

  






1. **Clone the Repository:**
   ```bash
   git clone [repository_url]
   cd Password-Strength-Checker
