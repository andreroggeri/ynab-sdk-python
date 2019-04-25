import os

from ynab_sdk_python import YNAB

if __name__ == '__main__':
    ynab = YNAB(os.environ.get('YNAB_KEY'))

    response = ynab.budgets.get_budgets()
    #
    # print(user)
    for budget in response.data.budgets:
        detail = ynab.budgets.get_budget(budget.id)
        print(detail.data.budget.accounts)

        # Accounts
        response = ynab.accounts.get_accounts(budget.id)

        for account in response.data.accounts:
            print(account)
            detail = ynab.accounts.get_account(budget.id, account.id)
            print(detail)
        # Categories
        response = ynab.categories.get_categories(budget.id)
        for category_group in response.data.category_groups:
            print(category_group)
            for category in category_group.categories[:2]:
                detail = ynab.categories.get_category(budget.id, category.id)
                print(detail)

        # Payees
        response = ynab.payees.get_payees(budget.id)
        for payee in response.data.payees[:5]:
            print(payee)
            detail = ynab.payees.get_payee(budget.id, payee.id)
            print(detail)

        # Transactions
        response = ynab.transactions.get_transcations(budget.id)
        for transaction in response.data.transactions:
            print(transaction)
