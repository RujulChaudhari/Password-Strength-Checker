# Password Strength Checker Project! 

## Overview:

This project is a simple password strength checker implemented in Python. It checks various criteria, such as password length, the presence of uppercase and lowercase letters, numbers, and special characters. It gives you a rough estimation on how long it would take a threat actor to brute force and crack the password based on the complexity.

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
- Create a new python script, this will be our main PW checker file. <br>
  ![](https://i.imgur.com/A5DMyG9.png)

## Step 2:
- Open up terminal in VScode.
- run the following command:
  ```bash
  pip install pyinstaller
- What this will do is help us compile our python script into a executable .exe file.

## Step 2:
- Copy the code below into your script.
```python
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to evaluate password strength
def evaluate_password(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for c in password)
    
    strength_points = sum([has_upper, has_lower, has_digit, has_special])

    if length < 6 or strength_points < 2:
        return "Poor", 1
    elif length < 8 or strength_points < 3:
        return "Good", 2
    elif length < 12 or strength_points < 4:
        return "Excellent", 3
    else:
        return "Amazing", 4

# Function to estimate time to crack the password
def time_to_crack(password):
    length = len(password)
    complexity = 26 + 26 + 10 + 32  # Upper + Lower + Digits + Special characters
    time_seconds = (complexity ** length) / 1e9  # Assume 1 billion guesses per second

    intervals = [
        ('years', 60 * 60 * 24 * 365),
        ('months', 60 * 60 * 24 * 30),
        ('weeks', 60 * 60 * 24 * 7),
        ('days', 60 * 60 * 24),
        ('hours', 60 * 60),
        ('minutes', 60),
        ('seconds', 1)
    ]

    for name, count in intervals:
        value = time_seconds // count
        if value >= 1:
            return format_time(value, name)
    
    return "less than a second"

def format_time(value, unit):
    if value >= 1e12:
        return f"{value / 1e12:.1f}T {unit}"
    elif value >= 1e9:
        return f"{value / 1e9:.1f}B {unit}"
    elif value >= 1e6:
        return f"{value / 1e6:.1f}M {unit}"
    elif value >= 1e3:
        return f"{value / 1e3:.1f}K {unit}"
    else:
        return f"{int(value)} {unit}"

# Function to update the GUI based on the password entered
def update_password_strength(event=None):
    password = entry.get()
    strength, level = evaluate_password(password)
    time = time_to_crack(password)

    strength_label.config(text=f"Password Strength: {strength}")
    time_label.config(text=f"Estimated Time to Crack: {time}")

    update_progress_bar(level)

def update_progress_bar(level):
    ax.clear()
    ax.barh(0, level, height=0.1, color=['red', 'orange', 'yellow', 'green'][level-1])
    ax.set_xlim(0, 4)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_frame_on(False)
    canvas.draw()

# Set up the GUI
root = tk.Tk()
root.title("Password Strength Checker")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter Password:").grid(row=0, column=0, padx=5, pady=5)
entry = ttk.Entry(frame, width=30, show="*")
entry.grid(row=0, column=1, padx=5, pady=5)
entry.bind("<KeyRelease>", update_password_strength)

strength_label = ttk.Label(frame, text="Password Strength: ")
strength_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

time_label = ttk.Label(frame, text="Estimated Time to Crack: ")
time_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(4, 0.1))  # Further adjusted height for a slimmer bar
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the GUI
root.mainloop()
```
  
    
  

## Step 3:
- Once you've verified the script works without any errors.
- Run the following command in terminal in your terminal to compile it as a .exe file. <br>
  ```bash
  pyinstaller --onefile your_script_name.py
- This wil create a Build and dist folder where your project is located. The exe file will be under the "dist" folder.
- Go ahead and run the .exe file to make sure it's working. <br>
`NOTE: You might need to add the exe file to your anti-virus as an exception.`

## Done:
- And there you have it, you have successfully created a PW strength checker. You can use this to secure your accounts. Enjoy! :)
![](https://i.imgur.com/O6e5nlN.png)
