running = True
command = ""
car_running = False
while running:
    command = input('>').lower()
    if command == 'help':
        print("""
start - to start the car
stop - to stop the car')
quit - to exit
        """)
    elif command == 'start':
        if car_running:
            print('car already running')
        else:
            car_running = True
            print('car started')
    elif command == 'stop':
        if car_running:
            car_running = False
            print('car stopped')
        else:
            print('car isnt running')
    elif command == 'quit':
        running = False
    else:
        print(command + ' not understood')