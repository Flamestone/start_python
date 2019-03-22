import json

DATAFILE = 'data.json'


def read_json(filename):
    with open(filename, 'r') as stream:
        return json.load(stream)


def write_json(obj, filename):
    with open(filename, 'w') as stream:
        return json.dump(obj, stream)


def print_balances_and_names(list_of_users):
    """
    [
        {
            "balance": "$2,958.03",
            "name": "Karin Kelly"
        }
    ]
    """
    for user in list_of_users:
        print '{username} has {balance}'.format(username=user['name'], balance=user['balance'])


users = read_json(DATAFILE)

print 'Before sort'
print_balances_and_names(users)

print 'After sort'
users.sort(key=lambda user: user['balance'][1:])
print_balances_and_names(users)
