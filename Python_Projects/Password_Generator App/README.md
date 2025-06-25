# **Secure Password Generator**


### ABOUT THE PROJECT
This is a simple but robust desktop app built with Python's Tkinter library, designed to generate strong, customizable, and cryptographically secure passwords. 
It allows users to select various character types (lowercase, uppercase, digits, symbols) and a desired length to create unique passwords instantly. 
For enhanced security, the generated password is not displayed visually on the screen, with the password being accessible only via the "Copy to Clipboard button"


### BUILT WITH

- [Python 3.x](https://www.python.org)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (GUI library)
- [secrets](https://docs.python.org/3/library/secrets.html) (Cryptographically strong pseudo-random number generator)
- [pyperclip](https://pyperclip.readthedocs.io/en/latest/) (Cross-platform clipboard module)

## FEATURES

* Customizable Length: Generate passwords of any desired length.
* Character Set Selection: Include or exclude:
  Lowercase letters (a-z), 
  Uppercase letters (A-Z), 
  Digits (0-9), 
  Symbols (!@#$%, etc.)
* Guaranteed Inclusion: If selected, ensures at least one character of each chosen type is present.
* Cryptographically Secure: Utilizes Python's secrets module for generating random numbers suitable for cryptographic purposes.
* Clipboard Integration: Easily copy the generated password to your system clipboard with a single click.
* Enhanced Security: The actual generated password is never displayed on screen to prevent "shoulder-surfing" or accidental visual exposure.

## GETTING STARTED
To get a local copy up and running, follow this simple steps.

Prerequisites
- Python 3.6 or higher.
- pyperclip library
    (Run in bash: pip install pyperclip)

  
### INSTALLATION 

-  1- Clone the repository
-  2- Navigate to the project directory
-  3- Run the app (Run in bash: python3 passgen.py)

### USAGE
- Set a password length, by default is 10
- Select  characters types want
- Generate the password
- Copy to clipboard

### CONTRIBUTING
Contributions are welcome! If you have suggestions or improvements :)
