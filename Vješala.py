import random
import time
import unicodedata
def vješala():

    print('Dobrodošli u vješala! Trebate pogoditi'
           ' nasumično odabranu riječ prije nego iskoristite'
           ' sve pokušaje. Sretno! ;)')
    time.sleep(1.0)
    

    
    pokretanje=True
    
    while pokretanje:    
        riječ= "ri.txt"
        r = open(riječ)

        riječi = r.read()
        riječi=riječi.split(',')
        
        r.close()
        
        riječ=random.choice(riječi)
        pokušaji=None 
        pogođena_slova=[] 
        p_riječ=[]
        for slovo in riječ:
          p_riječ.append('-') 
        rije=None 

        
        prikaz=['''
                        ''','''
               
                     ___''','''
                 
                      |
                      |
                      |
                     _|_''','''
                 _____
                      |
                      |
                      |
                     _|_''','''
                 _____
                |     |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
                     _|_''', ''' 
                 _____
                |     |
                O     |
               /|\    |
                |     |
               /     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
               / \   _|_''']
        
        print(prikaz[0])
        pokušaj=len(prikaz)-1

        while (pokušaj !=0 and '-' in p_riječ):
            print(('\nImate {} pokušaja').format(pokušaj))
            rije=''.join(p_riječ)
            print(rije)

            try:
                pokušaji= str(input('\nIzaberite slovo' + '\n'))
            except:
                print('Unos je ne važeći. Pokušajte ponovo.')
                continue
            else:
                if not pokušaji.isalpha():
                    print('Nije unešeno slovo. Pokušajte ponovo.')
                    continue
                elif len(pokušaji)>1  and pokušaji!= 'lj' and pokušaji!= 'nj' and pokušaji!= 'dž':
                    print('Uneseno je više od jednog slova. Pokušajte ponovo.')
                    continue
                elif pokušaji == 'q' or pokušaji == 'x' or pokušaji == 'y' or pokušaji == 'w':
                    print('Uneseno slovo ne pripada hrvatskoj abecedi.')
                    continue
                elif pokušaji in pogođena_slova: 
                    print('Uneseno je ponovljeno slovo. Pokušajte ponovo.')
                    continue
                else:
                    pass
                
            pogođena_slova.append(pokušaji)

            for slovo in range(len(riječ)):
                if pokušaji==riječ[slovo]:
                    p_riječ[slovo]=pokušaji 

            if pokušaji not in riječ:
                pokušaj -=1
                print(prikaz[(len(prikaz)-1)-pokušaj])
        if '-'not in p_riječ:
            print(('\nPOBJEDILI STE!Pogodili ste odabranu riječ tj. {}!').format(riječ))
        else:
                  print(('\nIzgubili ste! Riječ je bila {}.').format(riječ))
                  
        print('Želite li igrati ponovo?')

        odgovor=input('> ').lower()
        if odgovor not in ('da'):
            pokretanje=False


vješala()
