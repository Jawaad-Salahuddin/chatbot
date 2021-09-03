import config

from wit import Wit

client = Wit(config.token)

while 0 < 1:
    command = input("Say a command: ")
    if (command == 'Exit'):
        break
    else:
        resp = client.message(command)
        print(str(resp))
