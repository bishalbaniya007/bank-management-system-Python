# Bank Management System (Python CLI)
print("\n----- Banking Management System -----")
print("\n----- Welcome to Nabil Bank -----")

def update_dictionary():
  accounts_dict = {}
  try:
    with open("accounts.txt", "r") as f:
      lines = f.readlines()   #reading each lines and storing as list

      for line in lines:
        # Stripping of white-space left and right
        info = line.strip()

        # skipping the empty lines
        if not info:
          continue

        # if file becomes corrupted, skipping malformed lines
        info = info.split("|")
        if len(info) != 4:
          continue

        name, account_number, pin, balance = info

        accounts_dict[account_number] = {
          "name": name,
          "pin": pin,
          "balance": float(balance)
        }

    return accounts_dict

  except FileNotFoundError:
    return {}

# Takes accounts_dict as a parameter and updates in the file
def save_accounts(accounts_dict):
    # writing inside the file

    with open("accounts.txt", "w") as f:

      for account in accounts_dict:

        account_number = account
        name = accounts_dict[account]["name"]
        pin = accounts_dict[account]["pin"]
        balance = str(accounts_dict[account]["balance"])

        f.write(name + "|" + account_number + "|" + pin + "|" + balance + "\n")

def basic_menu():
  print("\n----- Menu -----")
  print("1. Create an account")
  print("2. Log in")
  print("3. Exit")

def create_account(accounts_dict):
  # validating the name
  while True:
    name = input("\nEnter the account holder's name: ").strip()
    if not name:
      print("----- You have to fill in your name -----")
      continue
    else:
      break

  # validating the account number
  while True:
    account_number = input("\nEnter the account number: ")
    if not account_number.isdigit():
      print("---- Account number must be numeric ----")
      continue

    else:
      break

  # checking if the account already exists in the dictionary
  if account_number not in accounts_dict:

    #validation for pin
    while True:
      pin = input("\nSet the 4 digits login pin: ")
      # validating pin
      if not pin.isdecimal():
        print("----- PIN must be a number -----")
        continue
      elif len(pin) != 4:
        print("----- Length of PIN must be 4 digits ----")
        continue
      else:
        break


    # validation for balance
    while True:
      try:
        balance = float(input("\nEnter the initial balance of the account: "))
        if balance < 0:
          print("----- Balance can not be negative -----")
          continue

        accounts_dict[account_number] = {
            "name": name,
            "pin": pin,
            "balance": balance
          }
        # calling save_accounts() to store the newly created dictionary in file
        save_accounts(accounts_dict)
        print("\n----- Account created successfully -----")
        break

      except ValueError:
        print("---- Enter a valid number -----")
        continue

  else:
    print("----- Account already exist. Log in? -----")

def login(accounts_dict):
  account_number = input("\nEnter your account number: ")

  # checking if the account-number-exists or not
  if account_number not in accounts_dict:
    print("----- Account does not exist. Please create an account first -----")

  else:
    attempts = 3
    while True:
      pin = input("Enter you login pin: ")

      if pin == accounts_dict[account_number]["pin"]:
        print("----- Logged in successfully -----")
        login_menu(accounts_dict, account_number)
        break

      else:
        attempts -= 1
        if attempts == 0:
          print("\nToo many incorrect attempts. Returning to main menu.")
          break

        print("----- Incorrect pin! Please try again -----")
        print(f"----- Attempts left: {attempts} -----\n")
        continue
    
def login_menu(accounts_dict, account_number):
  print(f"\n----- Welcome {accounts_dict[account_number]["name"]}! -----")

  while True:
    print("\n----- Menu -----")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Logout")

    try: 
      choice = int(input("\nEnter your choice: "))
    except ValueError:
      print("\nInvalid input!!! Please choose a valid option 1-4: ")
      continue

    if choice == 1:
      print("\n----- Checking balance -----")
      check_balance(accounts_dict, account_number)

    elif choice == 2:
      print("\n------ Deposit -----")
      transaction(accounts_dict, account_number, "deposit")


    elif choice == 3:
      print("\n----- Withdraw -----")
      transaction(accounts_dict, account_number, "withdraw")

    elif choice == 4:
      print("----- Logged out successfully -----")
      break

    else:
      print("Please choose a valid option 1-4. ")

def check_balance(accounts_dict, account_number):
  print(f"Your current balance: ${accounts_dict[account_number]["balance"]:,.2f}")

def transaction(accounts_dict, account_number, action):
  while True:
    try:
      amount = float(input(f"\nEnter the amount you want to {action}: "))
    except ValueError:
      print("Please enter a valid amount.")
      continue

    if amount <= 0:
      print("----- Amount can not be negative or zero. -----")
      continue

    elif action == "deposit":
      accounts_dict[account_number]["balance"] += amount

      # calling save accounts to update the amount in dictionary to file
      save_accounts(accounts_dict)

      print("------ Amount deposited successfully to the account -----")
      break

    elif action == "withdraw":
      if amount <= accounts_dict[account_number]["balance"]:
        accounts_dict[account_number]["balance"] -= amount

        # calling save accounts to update the amount in dictionary to file
        save_accounts(accounts_dict)

        print(f"----- You have withdrawn ${amount:,} successfully -----")
        break

      else:
        print("----- Insufficient balance! -----")

    else:
      print("----- Invalid action -----")
      break
  
def main():
  accounts_dict = update_dictionary()

  while True:
    basic_menu()
    try:
      choice = int(input("\nEnter your choice: "))
    except ValueError:
      print("\nInvalid input!!! Please choose a number between 1-3: ")
      continue

    if choice == 1:
      print("\n----- Creating an account..... -----")
      create_account(accounts_dict)

    elif choice == 2:
      print("\n----- Logging in..... -----")
      login(accounts_dict)

    elif choice == 3:
      print("\n----- Thank You! Visit Again -----")
      break
    else:
      print("Please choose a valid option: 1-3 ")

if __name__ == "__main__":
  main()