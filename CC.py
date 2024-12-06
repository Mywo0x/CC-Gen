import random
import time
from os import system, name
from pystyle import Anime, Colors, Colorate, System

def clear():
    system("cls" if name == "nt" else "clear")


banner = """


                     ..,**,.                                                    
                  .*(#%%(*,.                                                    
              .,*(#&@&&#/.                                                      
            .*(%&@@@&#/*.                                                       
          .*/#&@@@@&%(,.                                                        
        .,/#&@@@@@@%(*,                                                         
       .*(%&@@@@@@@#/*.                                                         
      .*/%@@@@@@@@@%/*.                                                         
      *(%&@@@@@@@@@#/*.                                                         
    .,/#&@@@@@@@@@@%(*.                                                         
    ,*(%&@@@@@@@@@@&%(,.                                                        
    ,*(%@@@@@@@@@@@@&%(*.                                                       
    ,*(%@@@@@@@@@@@@@&%(,                                                       
    ,*(%@@@@@@@@@@@@@@@&#*,                                           ....      
    .*(%&@@@@@@@@@@@@@@@&#(*,.                                      .,///*.     
     ./#&&@@@@@@@@@@@@@@@@&%#/,.                                 .*(#%%#*..     
      ,/#&@@@@@@@@@@@@@@@@@@@&%(/,.                           .,*(#&@&%(*.      
      .,/#@@@@@@@@@@@@@@@@@@@@@@@&#(/*,..              ...,*/(%&&@@@@%/*.       
        ,/%&@@@@@@@@@@@@@@@@@@@@@@@@@&&%#((//**,,,**//((#%%&@@@@@@@&%(*,        
         ,/#%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%(*.          
          .,/#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#/,.           
             .*(%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#/,.             
               .*/#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#(*,.               
                  .,/(%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&%(/,.                   
                     .,*/(#%&@@@@@@@@@@@@@@@@@@@@@&%%#/*,.                      
                           ..,**//(#########(/**,,..            


"""

Anime.Fade(banner, Colors.purple_to_blue, Colorate.Vertical, interval=0.002, enter=True)


banner1 = """
▄█▄    ▄█▄            ▄   ▄█    ▄▄▄▄▄   ██   
█▀ ▀▄  █▀ ▀▄           █  ██   █     ▀▄ █ █  
█   ▀  █   ▀      █     █ ██ ▄  ▀▀▀▀▄   █▄▄█ 
█▄  ▄▀ █▄  ▄▀      █    █ ▐█  ▀▄▄▄▄▀    █  █ 
▀███▀  ▀███▀        █  █   ▐               █ 
                     █▐                   █  
                     ▐                   ▀   
"""

if name == "nt":
    system("title Checker & mode 160,20")
System.Size(160, 20)


print(Colorate.Vertical(Colors.purple_to_blue, banner1))

print("This generator only generates Visa credit cards.")
mywo = int(input(Colorate.Vertical(Colors.purple_to_blue, "Veuillez saisir le nombre de cartes à générer: ")))
print("Génération de la carte de crédits...")


with open('Codes.txt', "a+") as f:
    for _ in range(mywo):
        exp_date2 = str(random.randint(1, 12)).zfill(2)
        card = (
            f"4540 03{random.randint(10, 99)} {random.randint(1000, 9999)} {random.randint(1000, 9999)} "
            f"| {exp_date2}/{random.randint(21, 26)} | {random.randint(100, 999)}"
        )
        f.write(f"{card}\n")
        print(f"[GENERATED] - {card}")
        time.sleep(0.025)
