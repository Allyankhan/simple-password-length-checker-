import string

class Password:
    def __init__(self):
        self.password = ""

    def user_input(self):
        self.password = input("Enter your password: ")
        strength = self.check_strength()

        if strength == "Weak":
            print("Password is Weak")
        elif strength == "Moderate":
            print("Password is Moderate. Try a stronger one.")
        else:
            print("Password is Strong")

    def check_strength(self):
        has_upper = any(char.isupper() for char in self.password)
        has_lower = any(char.islower() for char in self.password)
        has_digit = any(char.isdigit() for char in self.password)
        has_special = any(char in string.punctuation for char in self.password)

        length = len(self.password)

        # Criteria to determine strength
        if length >= 8 and has_upper and has_lower and has_digit and has_special:
            return "Strong"
        elif length >= 6 and (has_upper or has_lower) and (has_digit or has_special):
            return "Moderate"
        else:
            return "Weak"

    def show_user(self):
        print("Your password is:", self.password)


# Run the password checker
user = Password()
user.user_input()
user.show_user()
