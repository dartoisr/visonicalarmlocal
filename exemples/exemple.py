#!/usr/bin/env python3
from visonicalarmlocal import api

url = "http://xxx.xxx.xxx.xxx:8181/remote/json-rpc"
api = api.API(url)

def main():

    while True:
    
        if(api.is_authorized()):
            print("Client registred")
        else:
            print("Client not registred")

        print(f'===========================')
        print(f'=== Alarm Control Panel ===')
        print(f'===========================')
        print()
        print()
        print('  [1] register')
        print('  [2] get_panel_statuses')
        print('  [3] get_panel_state')
        print('  [4] get_devices_config')
        print('  [0] Exit')
        print()
        action = input('  Enter Number: ')
        print()

        if action == '1':
            api.register("user", 1234)    
        elif action == '2':
            print(api.get_panel_statuses())
        elif action == '3':
            print(api.get_panel_state(1))
        elif action == '4':
            print(api.get_devices_config())
        elif action == '0':
            print('On sort')
            break    

if __name__ == "__main__":
    main()

