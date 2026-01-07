def get_total_balance(transaction_list):
    total = 0
    for transaction in transaction_list:
        total += transaction
    return total

def get_deposit_count(transaction_list):
    deposit = 0
    for transaction in transaction_list:
        if transaction > 0:
            deposit += 1
    return deposit

def get_withdrawal_count(transaction_list):
    withdrawal = 0
    for transaction in transaction_list:
        if transaction < 0:
            withdrawal += 1
    return withdrawal

def get_account_status(balance):
    if balance > 0:
        return "Active"
    elif balance == 0:
        return "Zero balance"
    else:
        return "Overdrawn"

def get_risk_status(transaction_list):
    if not transaction_list:
        return "No activity"
    for transaction in transaction_list:
        if transaction < -5000:
            return "High risk"
    return "Normal"

def transaction_analyzer(transactions):
    result = {}
    for name, transaction in transactions.items():
        balance = get_total_balance(transaction)
        deposits = get_deposit_count(transaction)
        withdrawal = get_withdrawal_count(transaction)
        account_status = get_account_status(balance)
        risk_status = get_risk_status(transaction)
        result[name] = {"Balance" : balance, "Deposits" : deposits, "Withdrawals" : withdrawal, "Account_status" : account_status, "Risk_status" : risk_status}
    return result
transactions = {
    "Akash": [5000, -1200, 3000, -500, 0],
    "Ravi": [-2000, -1500, 0],
    "Neha": [10000, 5000, -2000, -3000],
    "Aman": []
}
print(transaction_analyzer(transactions))