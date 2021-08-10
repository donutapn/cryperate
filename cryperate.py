import sys

def ShowUsage():
    print('\npython | python3 cryperate.py [option]\n')
    print('-'*10+'\n| Option |\n'+'-'*10)
    print('--help                 Usage')
    print('[file] [amount]        Seperate character with amount of exception')
    print('[file] --brute         Seperate character with bruteforce of exception')
    print('\n'+'-'*15+'\n| More Option |\n'+'-'*15)
    print('-w    Seperate word instead character')
    print('-s    Ignore space')
    print('\n')

if __name__ == "__main__":
    if len(sys.argv) == 1:
        ShowUsage()
    else:
        if sys.argv[1] == '--help':
            ShowUsage()
        elif len(sys.argv) == 2:
            ShowUsage()
        else:
            File = sys.argv[1]
            Text = open(File,errors = 'ignore').read()
            Option = sys.argv[3:]
            if ('-w' in Option) and ('-s' in Option):
                print('Cannot ignore space and seperate word in same time!')
                exit()
            if '-s' in Option:
                Text = Text.replace(' ','')
            if sys.argv[2] == '--brute':
                if '-w' in Option:
                    CharList = Text.split(' ')
                else:
                    CharList = []
                    for c in Text:
                        CharList.append(c)
                for Amount in range((len(CharList)-2),0,-1):
                    Word = ''
                    for n in range(0,len(CharList),Amount+1):
                        Word += CharList[n]
                        if '-w' in Option:
                            Word += ' '
                    print(Word)
            else:
                try:
                    Amount = int(sys.argv[2])
                    if '-w' in Option:
                        CharList = Text.split(' ')
                    else:
                        CharList = []
                        for c in Text:
                            CharList.append(c)
                    if Amount > (len(CharList)-2):
                        print('The amount is wrong!')
                        exit()
                    Word = ''
                    for n in range(0,len(CharList),Amount+1):
                        Word += CharList[n]
                        if '-w' in Option:
                            Word += ' '
                    print(Word)
                except ValueError as Er:
                    print('The amount must be number!')
        
