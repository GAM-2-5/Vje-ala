
import random
import time

def vješala():

    print('Dobrodošli u vješala! Trebate pogoditi'
           'nasumično odabranu riječ prije nego iskoristite'
           'sve pokušaje. Sretno! ;)')
    time.sleep(1.0)


    pokretanje=True
    
    while pokretanje:
        riječi=['a','b']      
        
        riječ=random.choice(riječi)
        pokušaji=None 
        pogođena_slova=[]
        p_riječ=[]
        for slovo in riječ:
          p_riječ.append('-')
        rije=None

        
        prikaz=['''
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
                elif len(pokušaji)>1:
                    print('Uneseno je više od jednog slova. Pokušajte ponovo.')
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
            print(('\n{} je bila odabrana riječ!').format(riječ))
        else:
                  print(('\nIzgubili ste! Riječ je bila {}.').format(riječ))
                  
        print('\Želite li igrati ponovo?')

        odgovor=input('> ').lower()
        if odgovor not in ('da'):
            pokretanje=False


vješala()


        
                

        
                    
            
                
                
            
        
