import random
clearConsole = lambda: print('\n' * 5)
newgame = lambda: print('NEW GAME\n\n\n')
while True:
    with open("1-1000.txt","r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        word = random.choice(words)
    lives = 13
    wl = list(word)
    print('Number of letters in the word are ',len(word),'And the number of lives are',lives)
    rl = len(word)
    fw = ['_']*(len(word))
    selwor = []
    while (rl!=0):
        execom = 0
        rb = rl
#       word = 'testing'
        pos = 0
#       wl = list(word)
        #fw = ['Unknown']*len(wl)
        fl = input('Enter a letter of your choice')
        #print(selwor)
        for j in selwor:
            if fl == j :
                execom = execom + 1
                print('\nLETTER ALREADY CHOSEN')
        selwor.append(fl)
        if execom==0:
            for l in wl:
                pos = pos + 1
                if fl == l:
                    #print('letter detected',fl)
                    #print('position',count)
                    del fw[pos-1]
                    fw.insert(pos-1,fl)
                    rl = rl - 1
                    #print('\nREMAINING LETTERS',rl)
                    print(fw)
                #elif fl!= l:
                    #print('incorrect')
            if rb == rl:
                lives = lives -1
                print('\nIncorrect, REMAINING LIVES',lives)
            if lives == 0:
                rl=0
        
    if rl == 0 and lives !=0 :
        print('You have guessed the correct word',word)
    if lives==0:
        print('The correct word was :',word)
    clearConsole()
    newgame()
    clearConsole()
