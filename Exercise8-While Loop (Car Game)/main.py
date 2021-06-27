command = input('Console command: ').upper()
x = 0
y = 0
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
            if command == 'START' and x == 0:
                x = x + 1
                print('The engine started.')
            elif command == 'STOP' and y == 0:
                print('Car Stopped.')
                y = y + 1
            elif command == 'START'and x >= 1:
                print('The engine already started.')
            elif command == 'STOP' and y >= 1:
                print('Car already Stopped.')
            elif command == 'QUIT':
                break
        else:
            print('Command not recognized.')
            command = input('Console command: ').upper()
else:
    print('Program Terminated. Goodbye.')
