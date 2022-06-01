password = input()
if len(password) >= 8 and password.isalnum() and not password.isdigit() and not password.isalpha():
    print(True)
else:
    print(False)
