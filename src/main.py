from bc.client import Client
from bc.transactions import Transactions


if __name__ == '__main__':
    sender = Client(name='Foo', last_name='Bar', amount=3.3, message='Hi from Foo Bar.')
    reciever = Client('Test', 'Test')

    sender.sign_transaction(reciever)

    transaction = Transactions(sender=sender, reciever=reciever)
    print(transaction)
