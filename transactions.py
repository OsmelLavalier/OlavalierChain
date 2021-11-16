import keys
import json
import random

class Transactions:
    def __init__(self, sender, reciever, signature, amount):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount

    def get_pair(self):
        pub, priv = keys.key_pair()
        self.sender = pub
        self.reciever = pub

    def json(self):
        t = {
                'sender': self.sender,
                'reciever': self.reciever,
                'amount': random.randrange(0, 50),
                }

        return json.dumps(self.__dict__, sort_keys=True, indent=4)

t = Transactions('0', '0', '0', '0')
t.get_pair()
print(t.json())


