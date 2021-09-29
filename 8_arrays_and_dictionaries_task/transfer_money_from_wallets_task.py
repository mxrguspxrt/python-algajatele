# PLEASE DO NOT LOOK SOLVED TASK AT transfer_money_from_wallets_task_cheats.py BEFORE YOU HAVE DONE THE TASK ON YOUR OWN
# PALUN ÄRA VAATA transfer_money_from_wallets_task_cheats.py ENNE KUI OLED ISESEISVALT ÜLESANDE LAHENDANUD

wallets = {
    "john": {
        "currency": "EUR",
        "amount": 100.0
    },
    "mary": {
        "currency": "USD",
        "amount": 200.0
    },
    "misha": {
        "currency": "USD",
        "amount": 200.0
    }
}

currency_rate = {
    "from-EUR-to-USD": 1.2,
    "from-USD-to-EUR": 0.8
}

transactions_log = [

]


# TASK 1:
#
# Create a function
# 1. that enables transfering funds from one wallet to other wallet 
# 2. that stores transactions history
# 3. that automatically converts from one currency to another
# 4. bank accounts can not go lower that 0 - error needs to be displayed in that case (it is ok to use print() function)

# ÜLESANNE 1:
#
# Tee funktsioon
# 1. mis võimaldab raha kanda ühest rahakotist teise
# 2. säilitab ülekannete ajaloo
# 3. vajadusel automaatselt konverteerib ühest valuutast teise
# 4. pangakontod ei tohi nullist väiksemaks minna - sellisel juhul tuleb veateadet kuvada (tavaline print() sobib)

def transfer_money(wallet_from_name, wallet_to_name, amount):
    ...

# TASK 2:
#
# Verify that:
# 1. wallets have correct amounts of money
# 2. there is transaction log to verify what transactions were done

transfer_money("misha", "mary", 100)
transfer_money("john", "mary", 100)

print("\n\nWallets are:")
print(wallets)

print("\n\nAll transactions that happened:")
print(transactions_log)



# RELATED LINKS:
#
# 1. https://www.w3schools.com/python/python_dictionaries.asp
# 2. https://www.w3schools.com/python/python_arrays.asp
# 3. https://www.w3schools.com/python/python_conditions.asp