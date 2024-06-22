started=False
while True:
    option=input('enter your option : ')
    if option=='help':
        print('start - for starting the game ')
        print('stop - for stoping the game')
        print('quit - to exit from the game')
    elif option=='start':
       if started:
           print('the game is already started')
       else:
           print('game started')
           started=True
    elif option=='stop':
       if started:
          print('game stopped')
          started=False
       else:
          print('the game is already stopped')
    elif option=='quit':
        print('thankyou for visiting ')
        break
    else:
        print('incorroct option')
