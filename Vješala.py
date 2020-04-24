
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
        riječi=['adresa','aerodrom','akt','alat','aluminij','amper','anđeo','anatomija','argument','arheologija','arhiva','applauz','ateist','atlas','autobiografija','avion','avokado','bajka','bakar','barka','bakterija','balet','banka','bara','bazen','bedro','bejzbol','bicikl','bilježnica','biser','biro','bitka','bivol','bojica','bojler','bol','bombon','bor','briga','bijes','bubanj','car','cesta','cigla','cilj','cjepivo','crkva','crtež','cvijet','duh','dan','daska','dvorac','dijete','dim','disk','dodatak','događaj','dostava','ekologija','eksperiment', 'esej','evolucija',
                'element','ekonomija','elektronika','endem','ekstrakt','evanđelje', 'fjord', 'finale', 'flour', 'fotoaparat', 'funkcija', 'filozofija', 'fakultet', 'fuzija', 'fotografija', 'flora','galeb','gnijezdo','glad','glazba','gledatelj','gorivo','grob','grč','gusar','grozd','haljina','harfa','harmonija','hlad','heroj','hokej','hram','hrast','hlače','hijena','ideja','improvizacija','ime','indigo','industrija','intervju','iskustvo','izreka','izolacija','izvještaj','jabuka','janje','joga','jastuk','jeka','jutro','jug','junak','jezik','jež','kakao','kalcij','kafić','kalorije','kašalj','keks','kemija','kičma','kelj','ključ',
                'ladica','lančić','lak','lopoč','liječnik','luk','lisica','labud','lovor','lubanja','mozak','muha','muzej','misao','metla','milijun','metak','močvara','minus','meteor','naboj','nada','naočale','naselje','novčanik','nacrt','nesvijest','noga','noć','nalipero','ocat','obala','odijelo','odgoj','odsjaj','ogrtač','organizacija','onomatopeja','orhideja','orkestar','pauk','porez','pčela','povijest','princ','profesionalac','proljeće','prorok','prošlost','pisac',
                'radio','radost','rak','rasplet','raspon','ravnina','ravnoteža','razdioba','republika','redatelj','savjest','saturn','sijena','skica','slika','slon','salon','stroj','sljedbenik','savjet','tvornica','talent','tijesto','tamnica','trofej','tlak','trputac','trovanje','tvrtka','tulipan','udica','ucjena','učenik','ugođaj','ulje','upravitelj','uređaj','ušće','utjecaj','utrka','voda','vinograd','vjetar','valjak','vatra','večera','višnja','vojska','vladar','vrata','zmija','zima','zumbul','zatvorenik','zatvor','zvijezda','zraka','zub','zamorac','zavoj']
        riječ=random.choice(riječi)
        pokušaji=None 
        pogođena_slova=[] #lista pogođenih slova
        p_riječ=[]
        for slovo in riječ:
          p_riječ.append('-') #nepogođena slova u riječi će zamijeniti crticom
        rije=None #dodaje riječi u listu p_riječ

        
        prikaz=['''
               
                     _|_''','''
                 
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


        
                

        
                    
            
                
                
            
        
