
def create_account():
    print("\n-----CREATE ACCOUNT-----")
    username= input("Create a User ID:")
    password = input("Create a Password:")

    print("\nAccount Created Successfully !\n")
    return username, password

def login(stored_user,stored_pass):
    print("-----LOGIN-----")

    attempts = 3
    while attempts > 0:
        user_id = input("Enter User ID:")
        password = input("Enter Password:")

        if user_id == stored_user and password == stored_pass:
            print("Login Successful! \n")
            return True
        else:
            attempts -= 1
            print(f"Invalid credentials! Attempts left: {attempts}")

    print("Too many failed attempts.Exiting...") 
    return False   
