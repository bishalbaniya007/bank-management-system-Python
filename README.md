##Bank Management System (Python CLI)
##Overview

The Bank Management System is a command-line interface (CLI) application built in Python.
It allows users to create bank accounts, log in securely, and perform basic banking operations like checking balance, depositing, and withdrawing funds.
Account data is stored persistently in a local file (accounts.txt) to maintain records between sessions.

##Features

- Create Account: Users can create a new bank account with a unique account number, 4-digit PIN, and initial balance.

- Login System: Secure login with 3 attempts for entering the correct PIN.

- Check Balance: Users can view their current account balance.

- Deposit Funds: Add money to your account securely.

- Withdraw Funds: Withdraw money with balance checks to prevent overdraft.

- Data Persistence: All account information is saved in a file for future use.

##Input Validations:

- Account number must be numeric.

- PIN must be exactly 4 digits.

- Balance cannot be negative.

- Withdrawal cannot exceed current balance.

- Login allows 3 attempts for correct PIN entry.

##Limitations

- Does not currently support account-to-account transfers.

- No transaction history is maintained.

Uses a flat file (accounts.txt) for storage, which may not scale for large datasets.
