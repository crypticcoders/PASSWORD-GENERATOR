import secrets
import string
import sys

stored_passwords = {}
while True:
    purpose = input("Enter your purpose: ").strip()
    if purpose in stored_passwords:
        print("Username already exists. Try another.")
        continue
    try:
        length = int(input("Enter the length of the password you want: "))
        if length <= 0:
            print("Password length must be positive.")
            continue
    except ValueError:
        print("Please enter a valid number for length.")
        continue

    while True:
        choice = input("Enter 1 for Moderate or 2 for Hard: ").strip()
        if choice == '1':
            char_set = string.digits
            break
        elif choice == '2':
            include_letters = input("Include letters? (y/n): ").lower() == 'y'
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            include_symbols = input("Include punctuation symbols? (y/n): ").lower() == 'y'

            char_set = ""
            if include_letters:
                char_set += string.ascii_letters
            if include_numbers:
                char_set += string.digits
            if include_symbols:
                char_set += string.punctuation

            if not char_set:  # Fallback if nothing selected
                print("No character types selected, using letters + numbers by default.")
                char_set = string.ascii_letters + string.digits
            break
        else:
            print("Invalid choice. Try again.")

    
    char_set = char_set.replace(" ", "")

    while True:
        password = ''.join(secrets.choice(char_set) for i in range(length))
        if password not in stored_passwords.values():
            break

stored_passwords[purpose] = password

    print(f"\n Your password for {purpose} is: {password}")
    print(f"{purpose} - {password}")
    print("!!! Please save this password. It will not be shown again!\n")

    another = input("Do you want to create another password? (y/n): ").lower()
    if another != 'y':
        print("\nAll stored passwords (for this session only):")
        for user, pwd in stored_passwords.items():
            print(f"{user} - {pwd}")
            print("Thank you for using our site, feel free to visit again")
        sys.exit()
        
        




