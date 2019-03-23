import sys

inputFile = 'input.txt'
outputFile = 'output.txt'
accounts = {}
account = ""
params = list()
counter = 0

# Read file
with open(inputFile, 'r') as f:
    content = f.readlines()

# Store data
for i in content:
    if "[" in i:
        account = i.replace("[", "").replace("]", "").replace("\n", "")
        accounts[account] = {}
        params = list()
    elif i == '\n' and counter != 0:
        params = list()
    elif i != '' and '\n' in i and counter != 0:
        params.append(i)
        accounts[account] = params
    counter += 1

# Set Selected Account as Default
accountArg = str(sys.argv[1])
if accountArg != '' and accounts[accountArg] != '':
    accounts["default"] = accounts[accountArg]

# print Accounts
# print(accounts)

# construct Accounts output text
accountData = ""
for account in accounts:
    accountData += "[" + account + "]\n"
    for data in accounts[account]:
        accountData += data
    accountData += "\n"

# Write Accounts to the file
with open(outputFile, 'w') as the_file:
    the_file.write(accountData)
