import random
import string

def generate_password(length=12):
    """Generate a strong password with given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Strong Password Generator!")
    while True:
        try:
            num_passwords = int(input("How many passwords would you like to generate? "))
            length = int(input("Enter the length of each password: "))
            if num_passwords <= 0 or length <= 0:
                raise ValueError("Please enter positive integers.")
            break
        except ValueError as e:
            print("Invalid input:", e)
    
    print("\nGenerating Passwords:")
    for i in range(num_passwords):
        password = generate_password(length)
        print(f"Password {i+1}: {password}")

if __name__ == "__main__":
    main()
