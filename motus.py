from colorama import init
init()
from colorama import Fore, Back, Style

def play():
    #programme du jeu

    from random import choice
    words = [word.strip() for word in open("listemotus.txt", encoding="utf-8")]
    message = choice(words)

    messagetentative = ""
    messagetentez = ""

    print ("mot en", len(message), "lettre")

    while messagetentative != message:
        messagetentative = str(input("Tentez un message!"))
        while len(messagetentative) < len(message) or len(messagetentative) > len(message):
            messagetentative = str(input("Le mot est trop cour ou trop long.. quel dommage, réésaye!"))
        for i in range(len(message)):
                if message[i]== messagetentative[i]:
                    messagetentez=messagetentez + Back.RED + message[i]
                elif messagetentative[i] != message[i] and messagetentative[i] in message:
                    messagetentez=messagetentez + Back.YELLOW + messagetentative[i] + Style.RESET_ALL
                elif messagetentative[i]  not in message:
                    messagetentez=messagetentez + Style.RESET_ALL + messagetentative[i]
        print(messagetentez + Style.RESET_ALL)
        if messagetentative != message:
            messagetentez = ""
        
            

    if messagetentative == message:
        print("bien jouer!")

def add():
    #programme d'ajout de mot a la liste, pour pimenter le jeu!
    
    ajout=str(input("quel mot voulez vous ajouter?"))
    f = open('listemotus.txt','a')
    f.write('\n' + ajout)

#début du code

choice = str(input("voulez vous jouer ou ajouter un mot a la liste? veuillez répondre avec ajouter ou jouer!"))

while choice != "jouer" and choice != "ajouter":
    choice = str(input("je n'ai pas compris, veuillez rééssayer. N'oubliez pas de répondre avec " +Fore.RED+ "AJOUTER "+ Style.RESET_ALL + "ou " + Fore.RED + "JOUER " + Style.RESET_ALL + "sinon cela ne fonctionnera pas!"))
    
if choice == "jouer":
    play()
elif choice == "ajouter":
    add()
