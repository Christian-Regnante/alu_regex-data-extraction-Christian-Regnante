import re

def main():    # Main Program
    print("\t" * 2, "Welcome To The Text Format Pattern Finder & Checker!\n")

    while True:   # Menu Loop
        print("1. Validate Currency Amount")
        print("2. Validate Phone Number")
        print("3. Validate HTML Tag")
        print("4. Validate URL Address")
        print("5. Validate Email Address")
        print("6. EXIT")
        print()

        try:
            choice = int(input("Please select an option from the above menu(1-6): "))
        except ValueError:
            print("\nInvalid input! Please enter a number between 1 and 6.\n")
            continue
        if choice == 1:     # Validate Currency Amount
                text = input("Enter the currency amount: ")
                pattern = re.compile(r'\$\d{1,3}(,?\d{3})*(.?\d{2})?')
                matches = pattern.findall(text)
                print()
                if matches:
                    print(f"Currency amount: '{text}':  --Valid--\n")
                else:
                    print(f"Currency amount: '{text}':  --Invalid--\n")

        elif choice == 2:   # Validate Phone Number
                text = input("Enter the phone number: ")
                pattern = re.compile(r'\(?\d{3}\)?[ -.]\d{3}[-.]\d{4}')
                matches = pattern.findall(text)
                print()
                if matches:
                    print(f"Phone number: '{text}':  --Valid--\n")
                else:
                    print(f"Phone number: '{text}':  --Invalid--\n")

        elif choice == 3:   # Validate HTML Tag
            text = input("Enter the HTML tag: ")
            pattern = re.compile(r'<[a-z]+(\s[a-z]+="[a-zA-Z. ]+")*>')
            matches = pattern.findall(text)
            print()
            if matches:
                print(f"HTML tag: '{text}':  --Valid--\n")
            else:
                print(f"HTML tag: '{text}':  --Invalid--\n")

        elif choice == 4:   # Validate URL Address
            text = input("Enter the URL address: ")
            pattern = re.compile(r'https?://(www\.)?[a-z.-_]+\.[a-z_-]{2,}+/?')
            matches = pattern.findall(text)
            print()
            if matches:
                print(f"URL address: '{text}':  --Valid--\n")
            else:
                print(f"URL address: '{text}':  --Invalid--\n")

        elif choice == 5:   # Validate Email Address
            text = input("Enter the email address: ")
            pattern = re.compile(r'[a-zA-Z0-9.-_]+@[a-zA-Z0-9.-_]+\.[a-zA-Z.]{2,}+')
            matches = pattern.findall(text)
            print()
            if matches:
                print(f"Email address: '{text}':  --Valid--\n")
            else:
                print(f"Email address: '{text}':  --Invalid--\n")

        elif choice == 6:   # Exit the program
            print("Exitting the program...")
            break

if __name__ == '__main__':
    main()
    