command = input('Console command: ').upper()
started = False
while command != 'QUIT':
    if command != 'HELP':
        print('Command not recognized.')
        command = input('Console command: ').upper()
    else:
        print('''
Type "Start" to start the car.
Type "Stop" to stop the car.
Type "Quit" to terminate program.
''')
        while True:
            command = input('Console command: ').upper()
            if command == 'START':
                if started:
                    print('The Car already started.')
                else:
                    started = True
                    print('The engine started.')
            elif command == 'STOP':
                if not started:
                    print('Car is already Stopped.')
                else:
                    started = False
                    print('Car already Stopped.')
            elif command == 'QUIT':
                break
        else:
            print('Command not recognized.')
            command = input('Console command: ').upper()
else:
    print('Program Terminated. Goodbye.')

