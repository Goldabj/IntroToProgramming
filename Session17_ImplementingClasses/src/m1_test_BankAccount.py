"""
Tests the   BankAccount  class
that is defined in the imported   m1_BankAccount   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE

import m1_BankAccount as ba


def main():
    """
    Tests the   BankAccount   class
    defined in the imported   m1_BankAccount   module.

    See   UML_BankAccount.pdf   for BankAccount's UML class diagram.
    """
    # DONE: With your instructor, add code below
    #   (at the appropriate places) to test the   BankAccount   class
    #   that is defined in the imported  m1_BankAccount   module
    #   and whose UML class diagram is shown in   UML_BankAccount.pdf.

    print('--------------------------------------')
    print('Testing __init__:')

    account1 = ba.BankAccount(500)
    account2 = ba.BankAccount()

    print(account1.balance)
    print(account1.transactions)
    print('above should be 500, one initial deposit')

    print(account2.balance)
    print(account2.transactions)
    print('above should be 0, empty initial deposit')


    print('\n--------------------------------------')
    print('Testing __repr__:')

    print(account1)
    print(account2)

    print('\n--------------------------------------')
    print('Testing deposit:')

    account1.deposit(100)
    account2.deposit(10000)

    print(account1)
    print('above should be $600, two deposits')

    print(account2)
    print('above should be $10,000, one deposit')

    print('\n--------------------------------------')
    print('Testing withdraw:')

    account1.withdraw(200)
    account2.withdraw(11000)

    print(account1)
    print('above should be $400, and three transactions')

    print(account2)
    print('above should be $10,000, and a refused withdrawal')

    print('\n--------------------------------------')
    print('Testing number_of_deposits:')

    print(account1.number_of_deposits())
    print('above should have 2 deposits')

    print(account2.number_of_deposits())
    print('above should have 1 deposit')

    print('\n--------------------------------------')
    print('Testing number_of_withdrawals:')

    print(account1.number_of_withdrawals())
    print('above should have 1 withdrawal')

    print(account2.number_of_withdrawals())
    print('above should have 0 withdrawals')

    print('\n--------------------------------------')
    print('Testing number_of_refused_withdrawals:')

    print(account1.number_of_refused_withdrawals())
    print('above should have o refused withdrawals')

    print(account2.number_of_refused_withdrawals())
    print('above should have 1 refused withdraw')

    print('\n--------------------------------------')
    print('Testing transfer_from:')

    account1.transfer_from(account2)
    print(account1)
    print('above should have $10,400, and four transactions')


    print('\n--------------------------------------')
    print('Testing transfer_into:')

    account1.transfer_into(account2)
    print(account2)
    print('above should have $10,400 and 2 transactions')

    print('\n--------------------------------------')
    print('Testing richer:')

    print(account1.richer(account2))
    print('account2 should be richer than account1')

    print('\n--------------------------------------')
    print('Testing transfer_to_new_account:')

    print(account2.transfer_to_new_account())
    print('the new account shoudl have $10,400 and one transaction')

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
