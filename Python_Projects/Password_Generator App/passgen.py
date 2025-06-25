import os 
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import string
import secrets
import pyperclip
import tkinter as tk
from tkinter import messagebox


use_lowercase = ""
use_uppercase = ""
use_digits = ""
use_symbols = ""

def generate_custom_password(length,use_lowercase=True,use_uppercase=True,use_digits = True,use_symbols=True):
 if length <= 0:
    raise ValueError("Password length must be positive.")
 
 characters = ""
 if use_lowercase:
    characters += string.ascii_lowercase
 if use_uppercase:
    characters += string.ascii_uppercase
 if use_digits:
    characters += string.digits
 if use_symbols:
    characters += string.punctuation # Or define your own subset of symbols

 if not characters: # Ensure at least one character type is selected 
    raise ValueError("You have to select at least one type of characters for the password.")
 
 password = [secrets.choice(characters) for _ in range(length)]
   # Only if the length is enough
 if length >= (use_lowercase + use_uppercase + use_digits + use_symbols):
   try:
       if use_lowercase and not any(c.islower() for c in password):
                password[secrets.randbelow(length)] = secrets.choice(string.ascii_lowercase)
       if use_uppercase and not any(c.isupper() for c in password):
                password[secrets.randbelow(length)] = secrets.choice(string.ascii_uppercase)
       if use_digits and not any(c.isdigit() for c in password):
                password[secrets.randbelow(length)] = secrets.choice(string.digits)
       if use_symbols and not any(c in string.punctuation for c in password):
                password[secrets.randbelow(length)] = secrets.choice(string.punctuation)
   except ValueError:
      pass
   # Random positions of the characters
 secrets.SystemRandom().shuffle(password)
 return "".join(password)



# -- Class of Tkinter App --
class PasswordGeneratorApp():
   def __init__(self, master):
        self.master = master
        master.title("Secure Password Generator") 
        master.geometry("430x350") # Initial size of the window
        master.resizable(False,False) # Avoid resizable window
      # Variables
        self.password_length_var = tk.StringVar(value="10")
        self.include_lower_var   = tk.BooleanVar(value=True)
        self.include_upper_var   = tk.BooleanVar(value=True)
        self.include_digits_var   = tk.BooleanVar(value=True)
        self.include_symbols_var   = tk.BooleanVar(value=True)
        self.generated_password_var = tk.StringVar()

        # -- GUI Widgets --
      # Entry field for Length 
        tk.Label(master, text="Password Length").pack(pady=5)
        self.length_entry = tk.Entry(master, textvariable=self.password_length_var, width=5)
        self.length_entry.pack(pady=5)
      # Characters confirmation
        tk.Checkbutton(master, text="Lower Case (a-z)", variable=self.include_lower_var).pack(anchor='w', padx=20)
        tk.Checkbutton(master, text="Upper Case (A-Z)", variable=self.include_upper_var).pack(anchor='w', padx=20)
        tk.Checkbutton(master, text="Digits  (0-9)", variable=self.include_digits_var).pack(anchor='w', padx=20)
        tk.Checkbutton(master, text="Symbols (!@#$)", variable=self.include_symbols_var).pack(anchor='w', padx=20)
      # Generate password Button 
        tk.Button(master, text="Generate Password", command=self.generate_and_display_password).pack(pady=15)
        self.password_display_entry = tk.Entry(master, textvariable=self.generated_password_var, width=40, state='readonly')
        self.password_display_entry.pack(pady=5)
      # Copy to clipboard Button
        self.copy_button = tk.Button(master, text="Copy", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)
        self.copy_button.config(state='disabled')
        
   def generate_and_display_password(self):
      try:
            length_str = self.password_length_var.get()
            length = int(length_str) # This line can cause ValueError


            use_lower = self.include_lower_var.get()
            use_upper = self.include_upper_var.get()
            use_digits = self.include_digits_var.get()
            use_symbols = self.include_symbols_var.get()


            # Password Logic Function
            password = generate_custom_password(
                length,
                use_lowercase=use_lower,
                use_uppercase=use_upper,
                use_digits=use_digits,
                use_symbols=use_symbols
            )

            self.password_display_entry.config(state='normal')
            # Show the password on the text field
            self.generated_password_var.set(password)
            self.password_display_entry.config(state='readonly')
            # Enable the copy to clipboard button
            self.copy_button.config(state='normal')
            

      except ValueError as ve:
            messagebox.showerror("Entry Error", str(ve))
            self.generated_password_var.set("")
            self.copy_button.config(state='disabled')
      except Exception as e:
            messagebox.showerror("Unexpected Error", f"{e}")
            self.generated_password_var.set("")
            self.copy_button.config(state='disabled')
       
   def copy_to_clipboard(self):
      password_to_copy = self.generated_password_var.get()
      if password_to_copy:
       try:
         pyperclip.copy(password_to_copy)
       except pyperclip.PyperclipException as e:
         messagebox.showwarning("Copying error", f"Unexpected Error {e}\nPlease copy the password manuall")
      else:
         messagebox.showwarning("Nothing to copy", "First generate a password to copy.")


                                                   # ------ MAIN  ------
if __name__ == '__main__':
   # Create the main window of Tkinter
   root = tk.Tk()
   # Create an instance of the app
   app = PasswordGeneratorApp(root)
   # Initialize the events of Tkinter (window keep open)
   root.mainloop()


   
   
