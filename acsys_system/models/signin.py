class Signin:
    account_ID = 0
    account_name = ""
    account_height = 0
    account_weight = 0
    account_birthday = ""
    account_level = 0
    account_address = ""
    account_pass = ""

    def __init__(self, account_ID, account_name, account_height, account_weight,
                 account_birthday, account_level, account_address, account_pass):
        self.account_ID = account_ID
        self.account_name = account_name
        self.account_height = account_height
        self.account_weight = account_weight
        self.account_birthday = account_birthday
        self.account_level = account_level
        self.account_address = account_address
        self.account_pass = account_pass

    def __iter__(self):
        yield 'account_ID', self.account_ID
        yield 'account_name', self.account_name
        yield 'account_height', self.account_height
        yield 'account_weight', self.account_weight
        yield 'account_birthday', self.account_birthday
        yield 'account_level', self.account_level
        yield 'account_address', self.account_address
        yield 'account_pass', self.account_pass