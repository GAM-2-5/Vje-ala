
import random
import time

def vješala():

    print('Dobrodošli u vješala! Trebate pogoditi'
           'nasumično odabranu riječ prije nego iskoristite'
           'sve pokušaje. Sretno! ;)')
    time.sleep(1.0)
    
#uvod u igru
    
    pokretanje=True
    
    while pokretanje:    #pokretanje potlje
        riječi=['adresa','aerodrom','akt','alat','aluminij','amper','anđeo','anatomija','argument','arheologija','arhiva','applauz','ateist','atlas','autobiografija','avion','avokado','bajka','bakar','barka','bakterija','balet','banka','bara','bazen','bedro','bejzbol','bicikl','bilježnica','biser','biro','bitka','bivol','bojica','bojler','bol','bombon','bor','briga','bijes','bubanj','car', ]

            
        riječ=random.choice(riječi)
        pokušaji=None 
        pogođena_slova=[] #lista pogođenih slova
        p_riječ=[]
        for slovo in riječ:
          p_riječ.append('-') #nepogođena slova u riječi će zamijeniti crticom
        rije=None #dodaje riječi u listu p_riječ

        
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
            except:#provjerava unos
                print('Unos je ne važeći. Pokušajte ponovo.')
                continue
            else:
                if not pokušaji.isalpha():#provjerava je li unos slovo
                    print('Nije unešeno slovo. Pokušajte ponovo.')
                    continue
                elif len(pokušaji)>1:#provjerava je li unešeno samo 1 slovo
                    print('Uneseno je više od jednog slova. Pokušajte ponovo.')
                    continue
                elif pokušaji in pogođena_slova:#provjerava je li to slovo već bilo 
                    print('Uneseno je ponovljeno slovo. Pokušajte ponovo.')
                    continue
                else:
                    pass
                
            pogođena_slova.append(pokušaji)

            for slovo in range(len(riječ)):
                if pokušaji==riječ[slovo]:
                    p_riječ[slovo]=pokušaji #zamjenjuje sva točno pogođena slova

            if pokušaji not in riječ:
                pokušaj -=1
                print(prikaz[(len(prikaz)-1)-pokušaj])
        if '-'not in p_riječ:#igrač je pogodio odabranu riječ
            print(('\n{} je bila odabrana riječ!').format(riječ))
        else:#petlja završava jer je igrač potrošio sve pokušaje
                  print(('\nIzgubili ste! Riječ je bila {}.').format(riječ))
                  
        print('\Želite li igrati ponovo?')

        odgovor=input('> ').lower()
        if odgovor not in ('da'):
            pokretanje=False


vješala()


        
                

        
                    
            
                
                
            
        
