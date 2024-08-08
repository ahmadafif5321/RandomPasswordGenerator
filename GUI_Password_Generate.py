import tkinter as tk
import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = [random.choice(characters) for _ in range(length)]
    return ''.join(password_list)

def on_generate():
    length = int(entry.get())
    password = generate_random_password(length)
    result_label.config(text=password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Add GUI elements
tk.Label(root, text="Password Length:").pack()
entry = tk.Entry(root)
entry.pack()

generate_button = tk.Button(root, text="Generate", command=on_generate)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

# Start the GUI event loop
root.mainloop()
