import random
import time
import math
#                                                        #help#
########################################################################################################################
def emf_help():
    print("\n\033[1;35;40mTo use the emf you need to say scan, this will scan for electronic")
    print("disturbances left by the ghost. All ghosts leave some level of")
    print("electronic disturbance but some ghosts will leave an emf level 5.")
    print("If it leaves a level 5 then that counts as evidence. Keep in mind")
    print("you won't know after one scan you may have to try multiple times")
    print("before it leaves a level 5.")

def freezing_temps_help():
    print("\n\033[1;35;40mTo use the freezing temperatures you need to say measure. This")
    print("will measure the temperatures of your location. All ghosts are at")
    print("least a little cold but some are exceedingly cold causing the")
    print("area they're in to reach temperatures below freezing. Keep in mind")
    print("you won't know after one try, you may have to try multiple times")
    print("before it gets below zero.")

def spirit_box_help():
    print("\n\033[1;35;40mTo use the spirit box you need to say certain phrases into it.")
    print("The spirit box allows your voice to cross over into the spirit")
    print("realm allowing ghosts to hear you, certain types of ghosts can")
    print("even respond to you through the spirit box. Keep in mind you")
    print("only certain phrases will give you a response and even then it")
    print("still might not respond the first time.")
    print("\n\033[1;34;40m** If you want to be lame you can say phrase list")
    print("to see a list of all the phrases you can use **")

def phrase_list():
    print("\n\033[1;35;40mwhere are you, are you here, are you near, is anyone there, how old are you,")
    print("what do you want, show yourself, give me a sign, talk to me, can you speak, are there any ghosts")
    print("let us know you are here, is there anyone here, scream, can we speak, do you speak french")
    print("are you happy, do you want us to leave, can you make a sound, do you want to hurt us")

def ultraviolet_help():
    print("\n\033[1;35;40mTo use the ultraviolet light you have to say look. Some")
    print("ghost leave behind a mark of sorts when they touch stuff.")
    print("When an ultraviolet light is shined on a spot touched by ")
    print("one of these ghosts you can see the mark they left behind.")
    print("Keep in mind it may take you more then one try to see it.")

def ghost_writing_help():
    print("\n\033[1;35;40mTo use the ghost writing book you have to say place. Some")
    print("ghosts like to share information with us in the form of writing.")
    print("So if you put down a book some types of ghosts will write in")
    print("it. Keep in mind it may take you more then one try to see it.")

def dots_help():
    print("\n\033[1;35;40mTo use dots you have to say watch, this will scatter small lasers all throughout")
    print("the room. Some ghosts are more prominent in the living realm then others.")
    print("Do to this they will occasionally become visible when they walk through")
    print("the dots. Keep in mind it may take you more then one try to see it.")

def ghost_orbs_help():
    print("\n\033[1;35;40mTo use the ghost orbs camera you have to say film, this will take ")
    print("footage of the room. Some ghosts leave behind a sort of mystical ")
    print("emanation that clumps together into orbs.These clumps of mystical ")
    print("energy are called ghost orbs and can be seen using ghost orb ")
    print("cameras. Keep in mind it may take you more then one try to see it.")

#                                                  #is evidence#
########################################################################################################################
def emf(emf_level):
    if emf_level == 1:
        emf_probability = [1, 4, 7, 10, 13, 14]
    elif emf_level == 2:
        emf_probability = [1, 4, 6, 8, 10, 11]
    else:
        emf_probability = [0, 2, 3, 5, 6, 7]

    emf_active = "true"
    while emf_active == "true":
        emf_action = input("\n\033[1;36;40memf on (scan/s): ")
        print(" ")
        if emf_action == "help":
            emf_help()
        elif emf_action == "stop":
            emf_active = "false"
        elif emf_action == "scan" or emf_action == "s":
            emf_random = random.randint(0, emf_probability[5])
            if 0 <= emf_random < emf_probability[0]:
                print("\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif emf_probability[0] <= emf_random < emf_probability[1]:
                print("\033[1;34;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif emf_probability[1] <= emf_random < emf_probability[2]:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif emf_probability[2] <= emf_random < emf_probability[3]:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;32;40mo\033[1;37;40mo\033[1;37;40mo")
            elif emf_probability[3] <= emf_random < emf_probability[4]:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;32;40mo\033[1;33;40mo\033[1;37;40mo")
            elif emf_random == emf_probability[5]:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;32;40mo\033[1;33;40mo\033[1;31;40mo")

def freezing_temps(freezing_temps_level):
    if freezing_temps_level == 1:
        freezing_temps_probability = [13, 15, 0, 3, 16]
    elif freezing_temps_level == 2:
        freezing_temps_probability = [11, 13, 1, 3, 14]
    else:
        freezing_temps_probability = [7, 9, 2, 5, 10]

    freezing_temps_active = "true"
    temp = random.randint(freezing_temps_probability[0], freezing_temps_probability[1])

    while freezing_temps_active == "true":
        freezing_temps_action = input("\n\033[1;36;40mthermometer on (measure/m): \033[1;39;40m")
        print(" ")
        if freezing_temps_action == "help":
            freezing_temps_help()
        elif freezing_temps_action == "stop":
            freezing_temps_active = "false"
        elif freezing_temps_action == "measure" or freezing_temps_action == "m":
            temp_change = random.randint(freezing_temps_probability[2],freezing_temps_probability[3])
            if temp - temp_change < -5:
                temp += temp_change
            elif temp + temp_change > freezing_temps_probability[4]:
                temp -= temp_change
            else:
                temp_negative_positive = random.choice(["negative", "positive"])
                if temp_negative_positive == "negative":
                    temp -= temp_change
                else:
                    temp += temp_change
            if temp == 1 or temp == -1:
                print(temp, "degree celsius")
            else:
                print(temp, "degrees celsius")

def spirit_box(age, spirit_box_level):
    if spirit_box_level == 1:
        spirit_box_probability = 11
    elif spirit_box_level == 2:
        spirit_box_probability = 5
    else:
        spirit_box_probability = 2

    spirit_box_active = "true"
    while spirit_box_active == "true":
        random_spirit_box = random.randint(0, spirit_box_probability)
        spirit_box_action = input("\n\033[1;36;40mspirit box on: \033[1;35;40m")
        print(" ")
        if spirit_box_action == "help":
            spirit_box_help()
        elif spirit_box_action == "stop":
            spirit_box_active = "false"
        elif spirit_box_action == "phrase list":
            phrase_list()

        elif spirit_box_action in ["are you near","is anyone there","can you speak","are there any ghosts","can we speak","are you happy","do you want us to leave","do you want to hurt us"]:
            if random_spirit_box == 0:
                print(random.choice(["Yes", "No"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action == "how old are you":
            if random_spirit_box == 0:
                print("I'm" , age)
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action in ["where are you","are you near","show yourself"]:
            if random_spirit_box == 0:
                print(random.choice(["Behind you","Near","Right here","In front of you","To your right","To your left"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action in ["let us know you are here","is there anyone here","can you make a sound","give me a sign","talk to me"]:
            if random_spirit_box == 0:
                print(random.choice(["I'm here","Hello","I can hear you","Can you hear me","DIE!"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action == "scream":
            if random_spirit_box == 0:
                print(random.choice(["AAAAAAAAAA!","AAA!!!","GRAAAAAAAAAAAAAA!!!!!!","RAAA RAAA RAAAAA!!!","GRA RA GRAAAA RA GRA"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action == "what do you want":
            if random_spirit_box == 0:
                print(random.choice(["To KiLl YoU!!","To be free... save me... please...","To go home","I want to find you","I want to play","Can you play with me!"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action == "do you speak french":
            if random_spirit_box == 0:
                print(random.choice(["yes","no","Oui","Non","Je veux te tuer","Sauve-moi s'il te plaît, je veux être libéré","tue-moi","je te trouverai","joue avec moi"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        else:
           print("** No response **")

def ultraviolet(ultraviolet_level):
    if ultraviolet_level == 1:
        ultraviolet_probability = 13
    elif ultraviolet_level == 2:
        ultraviolet_probability = 10
    else:
        ultraviolet_probability = 6

    ultraviolet_active = "true"
    while ultraviolet_active == "true":
        ultraviolet_action = input("\n\033[1;36;40multraviolet light on (look/l): ")
        print(" ")
        if ultraviolet_action == "help":
            ultraviolet_help()
        elif ultraviolet_action == "stop":
            ultraviolet_active = "false"
        elif ultraviolet_action == "look" or ultraviolet_action == "l":
            random_ultraviolet = random.randint(0, ultraviolet_probability)
            if random_ultraviolet == 0:
                random_true = random.randint(0, 9)
                if random_true == 0:
                    print("\033[1;35;40m                         /\\  __  __")
                    print("\033[1;35;40m                         \\/  \\/  \\/  __")
                    print("\033[1;35;40m                           _______   \\/  __")
                    print("\033[1;35;40m                         /         \\__   \\/")
                    print("\033[1;39;40m      ____________   _   \033[1;35;40m\\             \\     \033[1;39;40m________________")
                    print("\033[1;39;40m  ___/          _/ _ .    \033[1;35;40m\\___         |    \033[1;39;40m_ . \\__           \\_____")
                    print("\033[1;39;40m /           __/ . _           \033[1;35;40m\\______/          \033[1;39;40m.. \\___             \\")
                    print("\033[1;39;40m|           /_  ..                                .   _  \\            |")
                    print("\033[1;39;40m|          | _ .  .                                 . . _ |         _/")
                    print("\033[1;39;40m \\___       \\_ . -                                . .  __/        _/")
                    print("\033[1;39;40m     \\___    \\__ .  .                          .  _ __/      ____/")
                    print("\033[1;39;40m         \\______\\_ . _     \033[1;35;40m______          \033[1;39;40m.   _  ./________/")
                    print("\033[1;35;40m                         /        \\")
                    print("\033[1;35;40m                        |          |")
                    print("\033[1;35;40m                         \\        /")
                    print("\033[1;35;40m                          \\______/")
                elif random_true == 1:
                    print("\033[1;35;40m                              /\\  __  __")
                    print("\033[1;35;40m                              \\/  \\/  \\/  __")
                    print("\033[1;35;40m                               _______   \\/  __")
                    print("\033[1;35;40m                              /         \\__  \\/")
                    print("\033[1;35;40m                              \\             \\")
                    print("\033[1;35;40m                               \\___         |")
                    print("\033[1;35;40m                                    \\______/")
                    print(" ")
                    print(" ")
                    print(" ")
                    print("\033[1;39;40m      ____________                  \033[1;35;40m______    \033[1;39;40m________________")
                    print("\033[1;39;40m  ___/          _/ _              \033[1;35;40m/        \\    \033[1;39;40m\\__           \\_____")
                    print("\033[1;39;40m /           __/ .               \033[1;35;40m|          |    \033[1;39;40m.. \\___             \\")
                    print("\033[1;39;40m|           /_  ..                \033[1;35;40m\\        /      \033[1;39;40m.   _  \\            |")
                    print("\033[1;39;40m|          | _ .  .                \033[1;35;40m\\______/         \033[1;39;40m. . _ |         _/")
                    print("\033[1;39;40m \\___       \\_ . -                                . .  __/        _/")
                    print("\033[1;39;40m     \\___    \\__ .  .     \033[1;35;40m__  __  /\\           \033[1;39;40m.  _ __/      ____/")
                    print("\033[1;39;40m         \\______\\_    \033[1;35;40m__  \\/  \\/  \\/        \033[1;39;40m.  _  ./________/")
                    print("\033[1;35;40m                  __  \\/   _______")
                    print("\033[1;35;40m                  \\/   __/         \\")
                    print("\033[1;35;40m                     /             /")
                    print("\033[1;35;40m                     |         ___/")
                    print("\033[1;35;40m                      \\______/")
                    print(" ")
                    print(" ")
                    print(" ")
                    print("\033[1;35;40m                        ______")
                    print("\033[1;35;40m                      /        \\")
                    print("\033[1;35;40m                     |          |")
                    print("\033[1;35;40m                      \\        /")
                    print("\033[1;35;40m                       \\______/")
                elif random_true == 2:
                    print("\033[1;39;40m __________________")
                    print("\033[1;39;40m|                  |")
                    print("\033[1;39;40m|     ________     |")
                    print("\033[1;39;40m|    |\033[1;35;40m   __   \033[1;39;40m|    |")
                    print("\033[1;39;40m|    |\033[1;35;40m /    \\ \033[1;39;40m|    |")
                    print("\033[1;39;40m|    |\033[1;35;40m |    | \033[1;39;40m|    |")
                    print("\033[1;39;40m|    |_\033[1;35;40m\\____/\033[1;39;40m_|    |")
                    print("\033[1;39;40m|    |  \033[1;35;40m____  \033[1;39;40m|    |")
                    print("\033[1;39;40m|    | \033[1;35;40m/     \\\033[1;39;40m|    |")
                    print("\033[1;39;40m|    |        |    |")
                    print("\033[1;39;40m|    |________|    |")
                    print("\033[1;39;40m|                  |")
                    print("\033[1;39;40m|__________________|")
                elif random_true == 3:
                    print("\033[1;39;40m ___________________")
                    print("\033[1;39;40m|    /    |    \\    |")
                    print("\033[1;39;40m|   |     |     |   |")
                    print("\033[1;39;40m|  /      |      \\  |")
                    print("\033[1;39;40m| |_______|_______| |")
                    print("\033[1;39;40m| |       |       | |")
                    print("\033[1;39;40m|/ \033[1;35;40mlll\033[1;39;40m    |        \\|")
                    print("\033[1;39;40m| \033[1;35;40m-|_|\033[1;39;40m    |         |")
                    print("\033[1;39;40m|_________|_________|")
                elif random_true == 4:
                    print("\033[1;39;40m ____________")
                    print("\033[1;39;40m|   ______   |")
                    print("\033[1;39;40m|   ______   |")
                    print("\033[1;39;40m||           |")
                    print("\033[1;39;40m|     \033[1;35;40mlll\033[1;39;40m    |")
                    print("\033[1;39;40m|    \033[1;35;40m-|_|\033[1;39;40m    |")
                    print("\033[1;39;40m|        |@| |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m||           |")
                    print("\033[1;39;40m|   ______   |")
                    print("\033[1;39;40m|____________|")
                elif random_true == 5:
                    print("\033[1;39;40m __________________")
                    print("\033[1;39;40m|   ____    ____   |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |____|  |____|  |")
                    print("\033[1;39;40m|       \033[1;35;40mlll\033[1;39;40m     @  |")
                    print("\033[1;39;40m|   ____\033[1;35;40m|_|-\033[1;39;40m____   |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |____|  |____|  |")
                    print("\033[1;39;40m|__________________|")
                elif random_true == 6:
                    print("\033[1;39;40m __________________")
                    print("\033[1;39;40m|                  |")
                    print("\033[1;39;40m|     ________     |")
                    print("\033[1;39;40m|    |        |    |")
                    print("\033[1;39;40m|    |        |    |")
                    print("\033[1;39;40m|    |        |    |")
                    print("\033[1;39;40m|    |________|    |")
                    print("\033[1;39;40m|    |\033[1;35;40m  /   \\ \033[1;39;40m|    |")
                    print("\033[1;39;40m|    |\033[1;35;40m |    | \033[1;39;40m|    |")
                    print("\033[1;39;40m|    |_\033[1;35;40m|___/\033[1;39;40m__|    |")
                    print("\033[1;39;40m|     \033[1;35;40m/    |\033[1;39;40m       |")
                    print("\033[1;39;40m|_____\033[1;35;40m|____|\033[1;39;40m_______|")
                elif random_true == 7:
                    print("\033[1;39;40m ___________________")
                    print("\033[1;39;40m|    /    |    \\    |")
                    print("\033[1;39;40m|   |     |     |   |")
                    print("\033[1;39;40m|  /      |      \\  |")
                    print("\033[1;39;40m| |_______|_______| |")
                    print("\033[1;39;40m| |       |  \033[1;35;40mlll\033[1;39;40m  | |")
                    print("\033[1;39;40m|/        |  \033[1;35;40m|_|-\033[1;39;40m  \\|")
                    print("\033[1;39;40m|         |         |")
                    print("\033[1;39;40m|_________|_________|")
                elif random_true == 8:
                    print("\033[1;39;40m __________________")
                    print("\033[1;39;40m|   ____    ____   |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |____|  |____|  |")
                    print("\033[1;39;40m|               @  |")
                    print("\033[1;39;40m|   ____    ____   |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  | \033[1;35;40mlll\033[1;39;40m|  |")
                    print("\033[1;39;40m|  |    |  |\033[1;35;40m-|_|\033[1;39;40m|  |")
                    print("\033[1;39;40m|  |____|  |____|  |")
                    print("\033[1;39;40m|__________________|")
                elif random_true == 9:
                    print("\033[1;39;40m ____________")
                    print("\033[1;39;40m|   ______   |")
                    print("\033[1;39;40m|   ______   |")
                    print("\033[1;39;40m||           |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|        |@| |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|   \033[1;35;40mlll\033[1;39;40m      |")
                    print("\033[1;39;40m|   \033[1;35;40m|_|-\033[1;39;40m     |")
                    print("\033[1;39;40m||           |")
                    print("\033[1;39;40m|   ______   |")
                    print("\033[1;39;40m|____________|")
            else:
                random_false = random.randint(0, 4)
                if random_false == 0:
                    print("\033[1;39;40m __________________")
                    print("\033[1;39;40m|   ____    ____   |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |____|  |____|  |")
                    print("\033[1;39;40m|               @  |")
                    print("\033[1;39;40m|   ____    ____   |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |    |  |    |  |")
                    print("\033[1;39;40m|  |____|  |____|  |")
                    print("\033[1;39;40m|__________________|")
                elif random_false == 1:
                    print("\033[1;39;40m __________________")
                    print("\033[1;39;40m|                  |")
                    print("\033[1;39;40m|     ________     |")
                    print("\033[1;39;40m|    |        |    |")
                    print("\033[1;39;40m|    |        |    |")
                    print("\033[1;39;40m|    |        |    |")
                    print("\033[1;39;40m|    |________|    |")
                    print("\033[1;39;40m|    |        |    |")
                    print("\033[1;39;40m|    |        |    |")
                    print("\033[1;39;40m|    |        |    |")
                    print("\033[1;39;40m|    |________|    |")
                    print("\033[1;39;40m|                  |")
                    print("\033[1;39;40m|__________________|")
                elif random_false == 2:
                    print("\033[1;39;40m ___________________")
                    print("\033[1;39;40m|    /    |    \\    |")
                    print("\033[1;39;40m|   |     |     |   |")
                    print("\033[1;39;40m|  /      |      \\  |")
                    print("\033[1;39;40m| |_______|_______| |")
                    print("\033[1;39;40m| |       |       | |")
                    print("\033[1;39;40m|/        |        \\|")
                    print("\033[1;39;40m|         |         |")
                    print("\033[1;39;40m|_________|_________|")
                elif random_false == 3:
                    print("\033[1;39;40m ____________")
                    print("\033[1;39;40m|   ______   |")
                    print("\033[1;39;40m|   ______   |")
                    print("\033[1;39;40m||           |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|        |@| |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|            |")
                    print("\033[1;39;40m|   ______   |")
                    print("\033[1;39;40m|____________|")
                elif random_false == 4:
                    print("\033[1;39;40m      ____________   _                      .  ________________")
                    print("\033[1;39;40m  ___/          _/ _ .                       _ . \\__           \\_____")
                    print("\033[1;39;40m /           __/ . _                             .. \\___             \\")
                    print("\033[1;39;40m|           /_  ..                                .   _  \\            |")
                    print("\033[1;39;40m|          | _ .  .                                 . . _ |         _/")
                    print("\033[1;39;40m \\___       \\_ . -                                . .  __/        _/")
                    print("\033[1;39;40m     \\___    \\__ .  .                          .  _ __/      ____/")
                    print("\033[1;39;40m         \\______\\_ . _                     .   _  ./________/")

def ghost_writing(ghost_writing_level):
    if ghost_writing_level == 1:
        ghost_writing_probability = 15
    elif ghost_writing_level == 2:
        ghost_writing_probability = 12
    else:
        ghost_writing_probability = 8

    ghost_writing_active = "true"
    while ghost_writing_active == "true":
        ghost_writing_action = input("\n\033[1;36;40mbook in hand (place/p): ")
        print(" ")
        if ghost_writing_action == "help":
            ghost_writing_help()
        elif ghost_writing_action == "stop":
            ghost_writing_active = "false"
        elif ghost_writing_action == "place" or ghost_writing_action == "p":
            ghost_writing_random = random.randint(0,ghost_writing_probability)
            if ghost_writing_random == 0:
                random_true = random.randint(0, 8)
                if random_true == 0:
                    print("\033[1;35;40m _______________/---\\_______________")
                    print("\033[1;39;40m|  . .  _ .   _   |  _   _   _   _  |")
                    print("\033[1;39;40m|  |_| |_ |  |_|  | |_| |_| |_| |_| |")
                    print("\033[1;39;40m|  | | |_ |_ |    | | | | | | | | | |")
                    print("\033[1;39;40m|  .  .   _       |  _   _   _   _  |")
                    print("\033[1;39;40m|  |\\/|  |_       | |_| |_| |_| |_| |")
                    print("\033[1;39;40m|  |  |  |_       | | | | | | | | | |")
                    print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
                elif random_true == 1:
                    print("\033[1;35;40m _______________/---\\_______________")
                    print("\033[1;39;40m|  _   _ . .      | . .  _   . .    |")
                    print("\033[1;39;40m| |_/ |_ |_|      |  V  | |  | |    |")
                    print("\033[1;39;40m| |_\\ |_ | |      |  |  |_|  |_|    |")
                    print("\033[1;39;40m|  ___ .  .  __   |    ___   ___    |")
                    print("\033[1;39;40m|   |  |\\ | |  \\  |   | O | | O |   |")
                    print("\033[1;39;40m|  _|_ | \\| |__/  |    ---   ---    |")
                    print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
                elif random_true == 2:
                    print("\033[1;35;40m _______________/---\\_______________")
                    print("\033[1;39;40m|  \\ /|\\ /|\\ /    |   \\ /  |  / \\   |")
                    print("\033[1;39;40m|  /_\\|/_\\|/_\\    |  _/_\\__|__\\_/_  |")
                    print("\033[1;39;40m|     |/ \\|       |        |        |")
                    print("\033[1;39;40m|  ___|\\_/|___    |   |||| | ||     |")
                    print("\033[1;39;40m|  / \\|\\ /|/ \\    |        |        |")
                    print("\033[1;39;40m|  \\ /|/ \\|\\ /    |        |        |")
                    print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
                elif random_true == 3:
                    print("\033[1;35;40m _______________/---\\_______________")
                    print("\033[1;39;40m|      __|__      |                 |")
                    print("\033[1;39;40m|     /  |  \\     | |   _           |")
                    print("\033[1;39;40m|  --|---+---|--  | | _/ \\_         |")
                    print("\033[1;39;40m|     \\__|__/     | |/_____\\_______/|")
                    print("\033[1;39;40m|        |        | |       \\_   _/ |")
                    print("\033[1;39;40m|                 | |         \\_/   |")
                    print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
                elif random_true == 4:
                    print("\033[1;35;40m _______________/---\\_______________")
                    print("\033[1;39;40m|    ___          | |  |  _         |")
                    print("\033[1;39;40m| |/  |  |  |     | |/\\| |_| ___    |")
                    print("\033[1;39;40m| |\\ _|_ |_ |_    |      | |  | ___ |")
                    print("\033[1;39;40m| .  .  _         | |\\ |  _  _|_ |  |")
                    print("\033[1;39;40m| |\\/| |_         | | \\| | |     |  |")
                    print("\033[1;39;40m| |  | |_ o o o   |      |_|        |")
                    print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
                elif random_true == 5:
                    print("\033[1;35;40m _______________/---\\_______________")
                    print("\033[1;39;40m|       ___       |    ___ .   .    |")
                    print("\033[1;39;40m|        |        | |/  |  |   |    |")
                    print("\033[1;39;40m|       _|_       | |\\ _|_ |__ |__  |")
                    print("\033[1;39;40m| . . . .  _  ___ |  .  .  _        |")
                    print("\033[1;39;40m| |_| | | |_|  |  |  |\\/| |_        |")
                    print("\033[1;39;40m| | | |_| |\\   |  |  |  | |_        |")
                    print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
                elif random_true == 6:
                    print("\033[1;35;40m _______________/---\\_______________")
                    print("\033[1;39;40m|                 |                 |")
                    print("\033[1;39;40m| _|_|_|_|        |   _|_|_         |")
                    print("\033[1;39;40m| _|_|_|_|_|_     | _|_|_|_|_|_     |")
                    print("\033[1;39;40m| _|_|_|_|_|_|_   | _|_|_|_|_|_|_   |")
                    print("\033[1;39;40m|  | |_|_|_| |    | _|_|_|_| | |    |")
                    print("\033[1;39;40m|    | | | |      |  | | | |        |")
                    print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
                elif random_true == 7:
                    print("\033[1;35;40m _______________/---\\_______________")
                    print("\033[1;39;40m|  ___            |                 |")
                    print("\033[1;39;40m| /0 0\\           | 0      0        |")
                    print("\033[1;39;40m| \\___/           | T      T        |")
                    print("\033[1;39;40m| __|__           | ^      ^        |")
                    print("\033[1;39;40m|   |             |                 |")
                    print("\033[1;39;40m|  /\\             |                 |")
                    print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
                elif random_true == 8:
                    print("\033[1;35;40m _______________/---\\_______________")
                    print("\033[1;39;40m|        /   ___  |                 |")
                    print("\033[1;39;40m|   __-_|   /     |   __      _-__  |")
                    print("\033[1;39;40m|  |    /\\  \\  __ |     \\  \\ /  _ \\ |")
                    print("\033[1;39;40m|   \\__/  |   |/  |    _/   |    \\| |")
                    print("\033[1;39;40m|    \\    \\__/\\   |   /     /  __/| |")
                    print("\033[1;39;40m|    /       |    |   \\____/     /  |")
                    print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
            else:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")

def dots(room, dots_level):
    if dots_level == 1:
        dots_probability = 17
    elif dots_level == 2:
        dots_probability = 13
    else:
        dots_probability = 9

    dots_active = "true"
    while dots_active == "true":
        dots_action = input("\n\033[1;36;40mdots on (watch/w): ")
        print(" ")
        if dots_action == "help":
            dots_help()
        elif dots_action == "stop":
            dots_active = "false"
        elif dots_action == "watch" or dots_action == "w":
            dots_random = random.randint(0,dots_probability)
            if room == 0:
                if dots_random == 0:
                    random_true = random.randint(0, 3)
                    if random_true == 0:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .O .  . \033[1;37;40m|____    |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  ooo.  .  .  .\033[1;37;40m|   |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  . o o o  .  \033[1;37;40m___ |   |")
                        print("\033[1;37;40m| _____________  \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.   o .  .\033[1;37;40m__|_|_|   |")
                        print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  ___|\033[1;32;40m.  o o.  .\033[1;37;40m|         |")
                        print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  |  |\033[1;32;40m.  o o.  .\033[1;37;40m|         |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 1:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  O  .  .  .  .  .  .  . \033[1;37;40m|____    |")
                        print("\033[1;37;40m| \033[1;32;40m.  . ooo .  .  .  .  .  .  .  .  .\033[1;37;40m|   |")
                        print("\033[1;37;40m| \033[1;32;40m.  .o o o.  .  .  .  .  .  .  \033[1;37;40m___ |   |")
                        print("\033[1;37;40m| ______\033[1;32;40mo\033[1;37;40m______  \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m__|_|_|   \033[1;37;40m|")
                        print("\033[1;37;40m|  | \033[1;32;40m. o o . \033[1;37;40m|  ___|\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                        print("\033[1;37;40m|  | \033[1;32;40m. o o . \033[1;37;40m|  |  |\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 2:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|____    |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .\033[1;37;40m|   |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  \033[1;37;40m___ |   |")
                        print("\033[1;37;40m| _____________  \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m__|_|_|   |")
                        print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  ___|\033[1;32;40m.  oooo.O \033[1;37;40m|         |")
                        print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  |  | \033[1;32;40mooO  O   \033[1;37;40m|         |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 3:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .O .  .  .  . \033[1;37;40m|____    |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  ooo.  .  .  .  .  .\033[1;37;40m|   |")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .   o o  o  .  .  .  \033[1;37;40m___ |   |")
                        print("\033[1;37;40m| _____________  \033[1;32;40mo \033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m__|_|_|   |")
                        print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m| \033[1;32;40mo\033[1;37;40m_\033[1;32;40mo\033[1;37;40m_|\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                        print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m| \033[1;32;40mo\033[1;37;40m| \033[1;32;40mo\033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                        print("\033[1;37;40m|---------------------------------------|")
                else:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|____    |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .\033[1;37;40m|   |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  \033[1;37;40m___ |   |")
                    print("\033[1;37;40m| _____________  \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m__|_|_|   |")
                    print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  ___|\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                    print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  |  |\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                    print("\033[1;37;40m|---------------------------------------|")
            elif room == 1:
                if dots_random == 0:
                    random_true = random.randint(0, 3)
                    if random_true == 0:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m_________ \033[1;32;40m.  O  .  .  .  \033[1;37;40m|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m. ooo .  .  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.o o o.\033[1;37;40m________|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  o  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m. o o .\033[1;37;40m|_______|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m. o o .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 1:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m_________ \033[1;32;40m.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m. O. \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .  .  .  \033[1;37;40m|___\033[1;32;40mooo\033[1;37;40m_|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m________|  \033[1;32;40mo o o\033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|____\033[1;32;40mo\033[1;37;40m__|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m|_______|  \033[1;32;40m.o o \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|___\033[1;32;40mo\033[1;37;40m_\033[1;32;40mo\033[1;37;40m_|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 2:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m_________ \033[1;32;40m.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .  .  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m________|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.O.oooo\033[1;37;40m|_______|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  O  O\033[1;37;40m|\033[1;32;40mo.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 3:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m___\033[1;32;40mO\033[1;37;40m_____ \033[1;32;40m.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.ooo  .\033[1;37;40m| \033[1;32;40m.  .  .  .  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_\033[1;32;40mo\033[1;37;40m_\033[1;32;40mo\033[1;37;40m_\033[1;32;40mo\033[1;37;40m_| \033[1;32;40m.  .  .\033[1;37;40m________|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  o  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|__\033[1;32;40mo\033[1;37;40m_\033[1;32;40mo\033[1;37;40m__| \033[1;32;40m.  .  .\033[1;37;40m|_______|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.o  o .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m|---------------------------------------|")
                else:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m_________ \033[1;32;40m.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .  .  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m________|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m|_______|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m|---------------------------------------|")
            elif room == 2:
                if dots_random == 0:
                    random_true = random.randint(0, 3)
                    if random_true == 0:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .O .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| __ \033[1;32;40m.  .  ooo.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| || \033[1;32;40m.  . o o o  . \033[1;37;40m__  \033[1;32;40m.  .  \033[1;37;40m| __===|_| |")
                        print("\033[1;37;40m| ||________\033[1;32;40mo\033[1;37;40m______||  .  .  \033[1;37;40m|_|      | |")
                        print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m| |______| |")
                        print("\033[1;37;40m| || \033[1;32;40m.  .  o o.  . \033[1;37;40m||  \033[1;32;40m.  .  \033[1;37;40m| |  |   | |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 1:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| __ \033[1;32;40m.  .  .  .  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m__  \033[1;32;40m.  .  \033[1;37;40m| __===|_| |")
                        print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m|_|      | |")
                        print("\033[1;37;40m| ||_______\033[1;32;40mO.oooo\033[1;37;40m__||  \033[1;32;40m.  .  \033[1;37;40m| |______| |")
                        print("\033[1;37;40m| || \033[1;32;40m.  .  . O. Ooo\033[1;37;40m||  \033[1;32;40m.  .  \033[1;37;40m| |  |   | |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 2:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  . O.  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| __ \033[1;32;40m.  .  .  .  .  .ooo  .  \033[1;37;40m|  \033[1;32;40m.  .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m_\033[1;32;40mo o o .  \033[1;37;40m| __===|_| |")
                        print("\033[1;37;40m| ||_______________|| \033[1;32;40mo.  .  \033[1;37;40m|_|      | |")
                        print("\033[1;37;40m| ||_______________||\033[1;32;40mo o  .  \033[1;37;40m| |______| |")
                        print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m||\033[1;32;40mo o  .  \033[1;37;40m| |  |   | |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 3:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  O  .  . \033[1;37;40m|")
                        print("\033[1;37;40m| __ \033[1;32;40m.  .  .  .  .  .  .  .  \033[1;37;40m| \033[1;32;40mooo .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                        print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m__  \033[1;32;40m.  .  \033[1;37;40m|o__===|_| |")
                        print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m|_|      | |")
                        print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m| |______| |")
                        print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m||  \033[1;32;40m.  .  \033[1;37;40m| |  |   | |")
                        print("\033[1;37;40m|---------------------------------------|")
                else:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| __ \033[1;32;40m.  .  .  .  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m__  \033[1;32;40m.  .  \033[1;37;40m| __===|_| |")
                    print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m|_|      | |")
                    print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m| |______| |")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m||  \033[1;32;40m.  .  \033[1;37;40m| |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")

def ghost_orbs(room, ghost_orbs_level):
    if ghost_orbs_level == 1:
        ghost_orbs_probability = 9
    elif ghost_orbs_level == 2:
        ghost_orbs_probability = 7
    else:
        ghost_orbs_probability = 4

    ghost_orbs_active = "true"
    while ghost_orbs_active == "true":
        ghost_orbs_action = input("\n\033[1;36;40morbs camera on (film/f): ")
        print(" ")
        if ghost_orbs_action == "help":
            ghost_orbs_help()
        elif ghost_orbs_action == "stop":
            ghost_orbs_active = "false"
        elif ghost_orbs_action == "film" or ghost_orbs_action == "f":
            ghost_orbs_random = random.randint(0,ghost_orbs_probability)
            if room == 0:
                if ghost_orbs_random == 0:
                    random_true = random.randint(0, 3)
                    if random_true == 0:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|                           \033[1;38;40mo  \033[1;37;40m|        |")
                        print("\033[1;37;40m|          \033[1;38;40m.                   \033[1;37;40m|        |")
                        print("\033[1;37;40m|                              |____    |")
                        print("\033[1;37;40m|   \033[1;38;40mo                               \033[1;37;40m|   |")
                        print("\033[1;37;40m|                     \033[1;38;40m.         \033[1;37;40m___ |   |")
                        print("\033[1;37;40m| _____________    |          __|_|_|   |")
                        print("\033[1;37;40m|  |         |  ___|          |         |")
                        print("\033[1;37;40m|  |         |  |  |          |         |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 1:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|                      \033[1;38;40mo       \033[1;37;40m|        |")
                        print("\033[1;37;40m|      \033[1;38;40m.                       \033[1;37;40m|        |")
                        print("\033[1;37;40m|                    \033[1;38;40m.         |\033[1;37;40m____    |")
                        print("\033[1;37;40m|            \033[1;38;40mo                      \033[1;37;40m|   |")
                        print("\033[1;37;40m|                               ___ |   |")
                        print("\033[1;37;40m| _____________    |          __|_|_|   |")
                        print("\033[1;37;40m|  |         |  ___|          |         |")
                        print("\033[1;37;40m|  |         |  |  |          |         |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 2:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|                              |        |")
                        print("\033[1;37;40m|                  \033[1;38;40m.       o   \033[1;37;40m|        |")
                        print("\033[1;37;40m|        \033[1;38;40mo                     \033[1;37;40m|____    |")
                        print("\033[1;37;40m|                                   |   |")
                        print("\033[1;37;40m|                         \033[1;38;40m.     \033[1;37;40m___ |   |")
                        print("\033[1;37;40m| _____________    |          __|_|_|   |")
                        print("\033[1;37;40m|  |         |  ___|          |         |")
                        print("\033[1;37;40m|  |         |  |  |          |         |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 3:
                        print("\033[1;37;40m|         \033[1;38;40mo                    \033[1;37;40m|        |")
                        print("\033[1;37;40m|                \033[1;38;40m.             \033[1;37;40m|        |")
                        print("\033[1;37;40m|                         \033[1;38;40mo    \033[1;37;40m|____    |")
                        print("\033[1;37;40m|   \033[1;38;40m.                               \033[1;37;40m|   |")
                        print("\033[1;37;40m|                               ___ |   |")
                        print("\033[1;37;40m| _____________    |          __|_|_|   |")
                        print("\033[1;37;40m|  |         |  ___|          |         |")
                        print("\033[1;37;40m|  |         |  |  |          |         |")
                        print("\033[1;37;40m|---------------------------------------|")
                else:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                              |        |")
                    print("\033[1;37;40m|                              |        |")
                    print("\033[1;37;40m|                              |____    |")
                    print("\033[1;37;40m|                                   |   |")
                    print("\033[1;37;40m|                               ___ |   |")
                    print("\033[1;37;40m| _____________    |          __|_|_|   |")
                    print("\033[1;37;40m|  |         |  ___|          |         |")
                    print("\033[1;37;40m|  |         |  |  |          |         |")
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|---------------------------------------|")
            elif room == 1:
                if ghost_orbs_random == 0:
                    random_true = random.randint(0, 3)
                    if random_true == 0:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|      \033[1;38;40mo                          .     \033[1;37;40m|")
                        print("\033[1;37;40m|                       \033[1;38;40mo    \033[1;37;40m_________  |")
                        print("\033[1;37;40m|   _________                |       |  |")
                        print("\033[1;37;40m|   |    \033[1;38;40m.  \033[1;37;40m|                |_______|  |")
                        print("\033[1;37;40m|   |_______|        ________|       |  |")
                        print("\033[1;37;40m|   |       |        |       |_______|  |")
                        print("\033[1;37;40m|   |_______|        |_______|       |  |")
                        print("\033[1;37;40m|   |       |        |       |_______|  |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 1:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|    \033[1;38;40m.                   o              \033[1;37;40m|")
                        print("\033[1;37;40m|                            _________  |")
                        print("\033[1;37;40m|   _________           \033[1;38;40m.    \033[1;37;40m|       |  |")
                        print("\033[1;37;40m|   |       |   \033[1;38;40mo            \033[1;37;40m|_______|  |")
                        print("\033[1;37;40m|   |_______|        ________|       |  |")
                        print("\033[1;37;40m|   |       |        |       |_______|  |")
                        print("\033[1;37;40m|   |_______|        |_______|       |  |")
                        print("\033[1;37;40m|   |       |        |       |_______|  |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 2:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|       \033[1;38;40mo                      .        \033[1;37;40m|")
                        print("\033[1;37;40m|                            _________  |")
                        print("\033[1;37;40m|   |       |    \033[1;38;40m.           \033[1;37;40m|_______|  |")
                        print("\033[1;37;40m|   |_______|        ________|   \033[1;38;40mo   \033[1;37;40m|  |")
                        print("\033[1;37;40m|   |       |        |       |_______|  |")
                        print("\033[1;37;40m|   |_______|        |_______|       |  |")
                        print("\033[1;37;40m|   |       |        |       |_______|  |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 3:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|                               \033[1;38;40m.       \033[1;37;40m|")
                        print("\033[1;37;40m|    \033[1;38;40mo                      \033[1;37;40m _________  |")
                        print("\033[1;37;40m|   |       |        \033[1;38;40mo       \033[1;37;40m|_______|  |")
                        print("\033[1;37;40m|   |_______|        ________|       |  |")
                        print("\033[1;37;40m|   |       | \033[1;38;40m.      \033[1;37;40m|       |_______|  |")
                        print("\033[1;37;40m|   |_______|        |_______|       |  |")
                        print("\033[1;37;40m|   |       |        |       |_______|  |")
                        print("\033[1;37;40m|---------------------------------------|")
                else:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                                       |")
                    print("\033[1;37;40m|                            _________  |")
                    print("\033[1;37;40m|   |       |                |_______|  |")
                    print("\033[1;37;40m|   |_______|        ________|       |  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|   |_______|        |_______|       |  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|---------------------------------------|")
            elif room == 2:
                if ghost_orbs_random == 0:
                    random_true = random.randint(0, 3)
                    if random_true == 0:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|                                       |")
                        print("\033[1;37;40m|  \033[1;38;40m.                              o     \033[1;37;40m|")
                        print("\033[1;37;40m|            \033[1;38;40mo                          \033[1;37;40m|")
                        print("\033[1;37;40m| __                         |      |   |")
                        print("\033[1;37;40m| ||               __   \033[1;38;40m.    \033[1;37;40m| __===|_| |")
                        print("\033[1;37;40m| ||_______________||        |_|      | |")
                        print("\033[1;37;40m| ||_______________||        | |______| |")
                        print("\033[1;37;40m| ||               ||        | |  |   | |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 1:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|    \033[1;38;40m.                          o       \033[1;37;40m|")
                        print("\033[1;37;40m|                      \033[1;38;40m.                \033[1;37;40m|")
                        print("\033[1;37;40m|                                       |")
                        print("\033[1;37;40m| __      \033[1;38;40mo                  \033[1;37;40m|      |   |")
                        print("\033[1;37;40m| ||               __        | __===|_| |")
                        print("\033[1;37;40m| ||_______________||        |_|      | |")
                        print("\033[1;37;40m| ||_______________||        | |______| |")
                        print("\033[1;37;40m| ||               ||        | |  |   | |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 2:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|                                  \033[1;38;40mo    \033[1;37;40m|")
                        print("\033[1;37;40m|                \033[1;38;40mo                      \033[1;37;40m|")
                        print("\033[1;37;40m|                         \033[1;38;40m.             \033[1;37;40m|")
                        print("\033[1;37;40m| __     \033[1;38;40m.                   \033[1;37;40m|      |   |")
                        print("\033[1;37;40m| ||               __        | __===|_| |")
                        print("\033[1;37;40m| ||_______________||        |_|      | |")
                        print("\033[1;37;40m| ||_______________||        | |______| |")
                        print("\033[1;37;40m| ||               ||        | |  |   | |")
                        print("\033[1;37;40m|---------------------------------------|")
                    elif random_true == 3:
                        print("\033[1;37;40m|---------------------------------------|")
                        print("\033[1;37;40m|        \033[1;38;40mo                              \033[1;37;40m|")
                        print("\033[1;37;40m|                                  \033[1;38;40mo    \033[1;37;40m|")
                        print("\033[1;37;40m|                     \033[1;38;40m.                 \033[1;37;40m|")
                        print("\033[1;37;40m| __   \033[1;38;40m.                     \033[1;37;40m|      |   |")
                        print("\033[1;37;40m| ||               __        | __===|_| |")
                        print("\033[1;37;40m| ||_______________||        |_|      | |")
                        print("\033[1;37;40m| ||_______________||        | |______| |")
                        print("\033[1;37;40m| ||               ||        | |  |   | |")
                        print("\033[1;37;40m|---------------------------------------|")
                else:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                                       |")
                    print("\033[1;37;40m|                                       |")
                    print("\033[1;37;40m|                                       |")
                    print("\033[1;37;40m| __                         |      |   |")
                    print("\033[1;37;40m| ||               __        | __===|_| |")
                    print("\033[1;37;40m| ||_______________||        |_|      | |")
                    print("\033[1;37;40m| ||_______________||        | |______| |")
                    print("\033[1;37;40m| ||               ||        | |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")

#                                                   #NOT#
########################################################################################################################

def not_emf(emf_level):
    if emf_level == 1:
        emf_probability = [1, 4, 7, 10, 13]
    elif emf_level == 2:
        emf_probability = [1, 4, 6, 8, 10]
    else:
        emf_probability = [0, 2, 3, 5, 6]

    emf_active = "true"
    while emf_active == "true":
        emf_action = input("\n\033[1;36;40memf on (scan/s): ")
        print(" ")
        if emf_action == "help":
            emf_help()
        elif emf_action == "stop":
            emf_active = "false"
        elif emf_action == "scan" or emf_action == "s":
            emf_random = random.randint(0, emf_probability[4])
            if 0 <= emf_random < emf_probability[0]:
                print("\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif emf_probability[0] <= emf_random < emf_probability[1]:
                print("\033[1;34;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif emf_probability[1] <= emf_random < emf_probability[2]:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif emf_probability[2] <= emf_random < emf_probability[3]:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;32;40mo\033[1;37;40mo\033[1;37;40mo")
            elif emf_probability[3] <= emf_random < emf_probability[4]:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;32;40mo\033[1;33;40mo\033[1;37;40mo")

def not_freezing_temps(freezing_temps_level):
    if freezing_temps_level == 1:
        freezing_temps_probability = [13, 15, 0, 3, 16]
    elif freezing_temps_level == 2:
        freezing_temps_probability = [11, 13, 1, 3, 14]
    else:
        freezing_temps_probability = [7, 9, 2, 5, 10]

    freezing_temps_active = "true"
    temp = random.randint(freezing_temps_probability[0], freezing_temps_probability[1])

    while freezing_temps_active == "true":
        freezing_temps_action = input("\n\033[1;36;40mthermometer on (measure/m): \033[1;39;40m")
        print(" ")
        if freezing_temps_action == "help":
            freezing_temps_help()
        elif freezing_temps_action == "stop":
            freezing_temps_active = "false"
        elif freezing_temps_action == "measure" or freezing_temps_action == "m":
            temp_change = random.randint(freezing_temps_probability[2], freezing_temps_probability[3])
            if temp - temp_change < 1:
                temp += temp_change
            elif temp + temp_change > freezing_temps_probability[4]:
                temp -= temp_change
            else:
                temp_negative_positive = random.choice(["negative", "positive"])
                if temp_negative_positive == "negative":
                    temp -= temp_change
                else:
                    temp += temp_change
            if temp == 1 or temp == -1:
                print(temp, "degree celsius")
            else:
                print(temp, "degrees celsius")

def not_spirit_box():
    spirit_box_active = "true"
    while spirit_box_active == "true":
        spirit_box_action = input("\n\033[1;36;40mspirit box on: \033[1;35;40m")
        print(" ")
        if spirit_box_action == "help":
            spirit_box_help()
        elif spirit_box_action == "stop":
            spirit_box_active = "false"
        elif spirit_box_action == "phrase list":
            phrase_list()
        else:
            print("** No response **")

def not_ultraviolet(random_ghost):
    ultraviolet_active = "true"
    while ultraviolet_active == "true":
        ultraviolet_action = input("\n\033[1;36;40multraviolet light on (look/l): ")
        print(" ")
        if ultraviolet_action == "help":
            ultraviolet_help()
        elif ultraviolet_action == "stop":
            ultraviolet_active = "false"
        elif ultraviolet_action == "look" or ultraviolet_action == "l":
            if random_ghost == "wraith":
                random_ultraviolet = random.randint(0, 3)
            else:
                random_ultraviolet = random.randint(0, 4)
            if random_ultraviolet == 0:
                print("\033[1;39;40m __________________")
                print("\033[1;39;40m|   ____    ____   |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |____|  |____|  |")
                print("\033[1;39;40m|               @  |")
                print("\033[1;39;40m|   ____    ____   |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |____|  |____|  |")
                print("\033[1;39;40m|__________________|")
            elif random_ultraviolet == 1:
                print("\033[1;39;40m __________________")
                print("\033[1;39;40m|                  |")
                print("\033[1;39;40m|     ________     |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |________|    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |________|    |")
                print("\033[1;39;40m|                  |")
                print("\033[1;39;40m|__________________|")
            elif random_ultraviolet == 2:
                print("\033[1;39;40m ___________________")
                print("\033[1;39;40m|    /    |    \\    |")
                print("\033[1;39;40m|   |     |     |   |")
                print("\033[1;39;40m|  /      |      \\  |")
                print("\033[1;39;40m| |_______|_______| |")
                print("\033[1;39;40m| |       |       | |")
                print("\033[1;39;40m|/        |        \\|")
                print("\033[1;39;40m|         |         |")
                print("\033[1;39;40m|_________|_________|")
            elif random_ultraviolet == 3:
                print("\033[1;39;40m ____________")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m||           |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|        |@| |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m|____________|")
            elif random_ultraviolet == 4:
                print("\033[1;39;40m      ____________   _                      .  ________________")
                print("\033[1;39;40m  ___/          _/ _ .                       _ . \\__           \\_____")
                print("\033[1;39;40m /           __/ . _                             .. \\___             \\")
                print("\033[1;39;40m|           /_  ..                                .   _  \\            |")
                print("\033[1;39;40m|          | _ .  .                                 . . _ |         _/")
                print("\033[1;39;40m \\___       \\_ . -                                . .  __/        _/")
                print("\033[1;39;40m     \\___    \\__ .  .                          .  _ __/      ____/")
                print("\033[1;39;40m         \\______\\_ . _                     .   _  ./________/")

def not_ghost_writing():
    ghost_writing_active = "true"
    while ghost_writing_active == "true":
        ghost_writing_action = input("\n\033[1;36;40mbook in hand (place/p): ")
        print(" ")
        if ghost_writing_action == "help":
            ghost_writing_help()
        elif ghost_writing_action == "stop":
            ghost_writing_active = "false"
        elif ghost_writing_action == "place" or ghost_writing_action == "p":
            print("\033[1;35;40m _______________/---\\_______________")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")

def not_dots(room):
    dots_active = "true"
    while dots_active == "true":
        dots_action = input("\n\033[1;36;40mdots on (watch/w): ")
        print(" ")
        if dots_action == "help":
            dots_help()
        elif dots_action == "stop":
            dots_active = "false"
        elif dots_action == "watch" or dots_action == "w":
            if room == 0:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|____    |")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .\033[1;37;40m|   |")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  \033[1;37;40m___ |   |")
                print("\033[1;37;40m| _____________  \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m__|_|_|   |")
                print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  ___|\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  |  |\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                print("\033[1;37;40m|---------------------------------------|")
            elif room == 1:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m_________ \033[1;32;40m.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .  .  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m________|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m|_______|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m|---------------------------------------|")
            elif room == 2:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                print("\033[1;37;40m| __ \033[1;32;40m.  .  .  .  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m__  \033[1;32;40m.  .  \033[1;37;40m| __===|_| |")
                print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m|_|      | |")
                print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m| |______| |")
                print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m||  \033[1;32;40m.  .  \033[1;37;40m| |  |   | |")
                print("\033[1;37;40m|---------------------------------------|")

def not_ghost_orbs(room):
    ghost_orbs_active = "true"
    while ghost_orbs_active == "true":
        ghost_orbs_action = input("\n\033[1;36;40morbs camera on (film/f): ")
        print(" ")
        if ghost_orbs_action == "help":
            ghost_orbs_help()
        elif ghost_orbs_action == "stop":
            ghost_orbs_active = "false"
        elif ghost_orbs_action == "film" or ghost_orbs_action == "f":
            if room == 0:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m|                              |        |")
                print("\033[1;37;40m|                              |        |")
                print("\033[1;37;40m|                              |____    |")
                print("\033[1;37;40m|                                   |   |")
                print("\033[1;37;40m|                               ___ |   |")
                print("\033[1;37;40m| _____________    |          __|_|_|   |")
                print("\033[1;37;40m|  |         |  ___|          |         |")
                print("\033[1;37;40m|  |         |  |  |          |         |")
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m|---------------------------------------|")
            elif room == 1:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m|                                       |")
                print("\033[1;37;40m|                            _________  |")
                print("\033[1;37;40m|   |       |                |_______|  |")
                print("\033[1;37;40m|   |_______|        ________|       |  |")
                print("\033[1;37;40m|   |       |        |       |_______|  |")
                print("\033[1;37;40m|   |_______|        |_______|       |  |")
                print("\033[1;37;40m|   |       |        |       |_______|  |")
                print("\033[1;37;40m|---------------------------------------|")
            elif room == 2:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m|                                       |")
                print("\033[1;37;40m|                                       |")
                print("\033[1;37;40m|                                       |")
                print("\033[1;37;40m| __                         |      |   |")
                print("\033[1;37;40m| ||               __        | __===|_| |")
                print("\033[1;37;40m| ||_______________||        |_|      | |")
                print("\033[1;37;40m| ||_______________||        | |______| |")
                print("\033[1;37;40m| ||               ||        | |  |   | |")
                print("\033[1;37;40m|---------------------------------------|")

#                                                  #OTHER#
########################################################################################################################

def save_code_verifier(testing_save_code):
    if "-" not in testing_save_code:
        return "That is an invalid save code."
    dash_location = None
    for index in range(len(testing_save_code)):
        if testing_save_code[index] == "-":
            dash_location = index
    for index in range(7):
        if testing_save_code[index] not in ["1", "2", "3"]:
            return "That is an invalid save code."
    try:
        int(testing_save_code[7:dash_location])
        int(testing_save_code[dash_location + 1:len(testing_save_code)])
    except ValueError:
        return "That is an invalid save code."
    return "yes"

def ghost_randomizer():
    ghost_types_list = ["spirit", "wraith", "phantom", "poltergeist", "banshee", "jinn", "mare", "revenant", "shade", "demon", "yurei", "oni", "hantu", "yokai", "goryo", "myling", "onryo", "twins", "raiju", "obake", "mimic", "moroi", "deogen", "thaye"]
    random_ghost = random.choice(ghost_types_list)
    return random_ghost

def intro():
    print(" ")
    print(" ")
    print("\033[1;35;40mWelcome to Phasmophobia Python Edition! \n")
    print("\033[1;36;40m** Tip: Grab a pen and paper so you can write down what evidence you've gotten **")
    print("\033[1;36;40m** This game is case sensitive, everything will be lowercase ** ")
    print("\033[1;36;40m** If you have any typos it will just ask you the same question again ** \n")
    print("\033[1;34;40mIn this game you're supposed to figure out what ghost is haunting your house.")
    print("You will be asked what you want to do and you have 10 options")
    print("To find evidence you can say \033[1;35;40memf, freezing temps, ultraviolet, spirit box, ghost writing, dots, or ghosts orbs.")
    print("\033[1;34;40mWhen trying to find evidence you can say \033[1;35;40mhelp \033[1;34;40mto get an explanation on how to use the tool; \033[1;35;40mstop \033[1;34;40mto stop using")
    print("the tool and go back; or whatever the given action keyword for the tool you're using is")
    print("\033[1;34;40mYou can also say \033[1;35;40mguess \033[1;34;40mto guess the ghost; \033[1;35;40mghosts \033[1;34;40mto see what the ghosts are and what evidence each one has again;")
    print("or \033[1;35;40msave code \033[1;34;40mto get your progress saved up to that point. This doesn't save your current round, it will just save")
    print("your equipment levels, money and the amount of rounds you've won up to this round.")
    print("Your save code will also automatically be given to you at the end of each round.\033[1;38;40m \n")

def ghost_list():
    print("\033[1;35;40mspirit:        \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mspirit box     \033[1;35;40m|   \033[1;34;40mghost writing")
    print("\033[1;35;40mwraith:        \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mspirit box     \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mphantom:       \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mpoltergeist:   \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mghost writing")
    print("\033[1;35;40mbanshee:       \033[1;34;40multraviolet  \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mjinn:          \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mmare:          \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mghost writing")
    print("\033[1;35;40mrevenant:      \033[1;34;40mghost orbs   \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mshade:         \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mdemon:         \033[1;34;40multraviolet  \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40myurei:         \033[1;34;40mghost orbs   \033[1;35;40m|   \033[1;34;40mdots           \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40moni:           \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mdots           \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mhantu:         \033[1;34;40multraviolet  \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40myokai:         \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mgoryo:         \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mmyling:        \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mghost writing")
    print("\033[1;35;40monryo:         \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mtwins:         \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mspirit box     \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mraiju:         \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mobake:         \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mghost orbs")
    print("\033[1;35;40mmoroi:         \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mdeogen:        \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mthaye:         \033[1;34;40mghost orbs   \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mmimic:         \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mfreezing temps")

def guess(random_ghost):
    guessing = "true"
    while guessing == "true":
        guessed_ghost = input("\033[1;35;36mWhat is your guess? ")
        if guessed_ghost == random_ghost:
            print("\033[1;33;40mYou did it!!!")
            return "true"
        elif guessed_ghost in ["spirit","wraith","phantom","banshee","jinn","mare","revenant","shade","demon","yurei","oni","hantu","yokai","goryo","myling","onryo","twins","raiju","obake","mimic","moroi","deogen","thaye"]:
            print("\033[1;31;40mYOU DIE")
            print("The correct ghost was " + random_ghost)
            return "false"
        elif guessed_ghost == "stop":
            return "stop"

def end_game(times_won):
    game_over = "false"
    asking_end_game = "true"
    while asking_end_game == "true":
        play_again = input("\n\n\033[1;35;40mWould you like to play again? (yes or no) ")
        if play_again == "no":
            game_over = "true"
            asking_end_game = "false"
            if times_won == 1:
                print("\033[1;33;40mYou've now won", times_won, "time!")
            else:
                print("\033[1;33;40mYou've now won", times_won, "times!")
            print("Have a great day!")
        elif play_again == "yes":
            if times_won == 1:
                print("\033[1;33;40mYou've now won", times_won, "time!")
            else:
                print("\033[1;33;40mYou've now won", times_won , "times!")
        return game_over

#                                                    #MAIN#
########################################################################################################################

def main():
    game_over = "false"
    round_ghost = ghost_randomizer()
    random_room = random.randint(0,2)
    ghost_age = random.randint(3,110)

    if "yes" == input("Do you have a save code: "):
        save_code = None
        checking = "true"
        while checking == "true":
            save_code = input("\nsave code: ")
            save_code_verified = save_code_verifier(save_code)
            if save_code_verified == "yes":
                checking = "false"
                save_code_verified = "verified"
            print(save_code_verified)
    else:
        save_code = "11111110-0"

    dash_location = None
    for index in range(len(save_code)):
        if save_code[index] == "-":
            dash_location = index

    emf_level = int(save_code[0])
    freezing_temps_level = int(save_code[1])
    spirit_box_level = int(save_code[2])
    ultraviolet_level = int(save_code[3])
    ghost_writing_level = int(save_code[4])
    dots_level = int(save_code[5])
    ghost_orbs_level = int(save_code[6])
    money = int(save_code[7:dash_location])
    times_won = int(save_code[dash_location+1:len(save_code)])

    intro()
    ghost_list()
    print(round_ghost) # this is just for testing remove when done -----------------------------------------------------
    start_time = time.time()

    while game_over == "false":
        action = input("\n\033[1;35;40mWhat would you like to do? \033[1;38;40m")

        if action == "emf":
            if round_ghost in ["spirit","wraith","jinn","shade","oni","goryo","myling","twins","raiju","obake"]:
                emf(emf_level)
            else:
                not_emf(emf_level)

        elif action == "freezing temps":
            if round_ghost in ["jinn","revenant","shade","demon","yurei","oni","hantu","onryo","twins","moroi","deogen"]:
                freezing_temps(freezing_temps_level)
            else:
                not_freezing_temps(freezing_temps_level)

        elif action == "spirit box":
            if round_ghost in ["spirit","wraith","phantom","poltergeist","mare","yokai","onryo","twins","mimic","moroi","deogen"]:
                spirit_box(ghost_age, spirit_box_level)
            else:
                not_spirit_box()

        elif action == "ultraviolet":
            if round_ghost in ["phantom","poltergeist","banshee","jinn","demon","hantu","goryo","myling","obake","mimic"]:
                ultraviolet(ultraviolet_level)
            else:
                not_ultraviolet(round_ghost)

        elif action == "ghost writing":
            if round_ghost in ["spirit","poltergeist","mare","revenant","shade","demon","myling","moroi","deogen","thaye"]:
                ghost_writing(ghost_writing_level)
            else:
                not_ghost_writing()

        elif action == "dots":
            if round_ghost in ["wraith","phantom","banshee","yurei","oni","yokai","goryo","raiju","deogen","thaye"]:
                dots(random_room, dots_level)
            else:
                not_dots(random_room)

        elif action == "ghost orbs":
            if round_ghost in ["banshee","mare","revenant","yurei","hantu","yokai","onryo","raiju","obake","mimic","thaye"]:
                ghost_orbs(random_room, ghost_orbs_level)
            else:
                not_ghost_orbs(random_room)

        elif action == "ghosts":
            ghost_list()

        elif action == "guess":
            player_guess = guess(round_ghost)
            stop_time = time.time()
            total_time = stop_time-start_time
            time_string = str(int(total_time//60)) + ":" + str(int(total_time%60)).zfill(2)
            if player_guess == "true":
                print("It took you", time_string)
                times_won += 1
                money += int(4731.5 * math.exp(-0.01 * total_time) + 268.5)
                print("You made $" + str(int(4731.5 * math.exp(-0.01 * total_time) + 268.5)))
            elif player_guess == "false":
                print("It took you", time_string)
                money_penalty = int((-4731.5 * math.exp(-0.01 * total_time) + 5000)/7)
                print("You lost $" + str(money_penalty))
                if money >= money_penalty:
                    money -= money_penalty
                else:
                    money = 0

            if player_guess == "stop":
                pass
            else:
                if input("\n\033[1;34;40mWould you like to upgrade your gear? ") == "yes":

                    if emf_level == 1:
                        emf_upgrade_cost = 2500
                    else:
                        emf_upgrade_cost = 3500

                    if freezing_temps_level == 1:
                        freezing_temps_upgrade_cost = 2000
                    else:
                        freezing_temps_upgrade_cost = 3500

                    if spirit_box_level == 1:
                        spirit_box_upgrade_cost = 2000
                    else:
                        spirit_box_upgrade_cost = 3000

                    if ultraviolet_level == 1:
                        ultraviolet_upgrade_cost = 3000
                    else:
                        ultraviolet_upgrade_cost = 4000

                    if ghost_writing_level == 1:
                        ghost_writing_upgrade_cost = 3500
                    else:
                        ghost_writing_upgrade_cost = 4500

                    if dots_level == 1:
                        dots_upgrade_cost = 3500
                    else:
                        dots_upgrade_cost = 5000

                    if ghost_orbs_level == 1:
                        ghost_orbs_upgrade_cost = 3000
                    else:
                        ghost_orbs_upgrade_cost = 4000

                    print("\n\033[1;36;40mOk! You have $"+ str(money), "how would you like to spend it?")
                    print("\n\033[1;35;40mYour Emf is currently level:", emf_level)
                    print("\033[1;34;40mIt will cost $" + str(emf_upgrade_cost) + " to upgrade it.")
                    print("\n\033[1;35;40mYour Thermometer (Freezing Temps) is currently level:", freezing_temps_level)
                    print("\033[1;34;40mIt will cost $" + str(freezing_temps_upgrade_cost) + " to upgrade it.")
                    print("\n\033[1;35;40mYour Spirit Box is currently level:", spirit_box_level)
                    print("\033[1;34;40mIt will cost $" + str(spirit_box_upgrade_cost) + " to upgrade it.")
                    print("\n\033[1;35;40mYour Ultraviolet Light is currently level", ultraviolet_level)
                    print("\033[1;34;40mIt will cost $" + str(ultraviolet_upgrade_cost) + " to upgrade it.")
                    print("\n\033[1;35;40mYour Ghost Writing Book is currently level:", ghost_writing_level)
                    print("\033[1;34;40mIt will cost $" + str(ghost_writing_upgrade_cost) + " to upgrade it.")
                    print("\n\033[1;35;40mYour Dots Projector is currently level:", dots_level)
                    print("\033[1;34;40mIt will cost $" + str(dots_upgrade_cost) + " to upgrade it.")
                    print("\n\033[1;35;40mYour Video Camera (Orbs) is currently level:", ghost_orbs_level)
                    print("\033[1;34;40mIt will cost $" + str(ghost_orbs_upgrade_cost) + " to upgrade it.")

                    upgrading = "true"
                    while upgrading == "true":
                        upgrade = input("\n\033[1;36;40mSo what would you like to upgrade? To leave just say 'done' \n** Levels cannot exceed 3 ** ")
                        if upgrade == "done":
                            upgrading = "false"

                        elif upgrade == "emf":
                            if emf_level < 3:
                                if money >= emf_upgrade_cost:
                                    if input("That will cost $" + str(emf_upgrade_cost) + " are you sure you'd like to upgrade this?" ) == "yes":
                                        money -= emf_upgrade_cost
                                        emf_level += 1
                                else:
                                    print("Sorry that's to expensive.")
                            else:
                                print("Sorry you can only upgrade to level 3.")

                        elif upgrade in ["thermometer", "freezing temps", "temps", "freezing"]:
                            if freezing_temps_level < 3:
                                if money >= freezing_temps_upgrade_cost:
                                    if input("That will cost $" + str(freezing_temps_upgrade_cost) + " are you sure you'd like to upgrade this? ") == "yes":
                                        money -= freezing_temps_upgrade_cost
                                        freezing_temps_level += 1
                                else:
                                    print("Sorry that's to expensive.")
                            else:
                                print("Sorry you can only upgrade to level 3.")

                        elif upgrade == "spirit box":
                            if spirit_box_level < 3:
                                if money >= spirit_box_upgrade_cost:
                                    if input("That will cost $" + str(spirit_box_upgrade_cost) + " are you sure you'd like to upgrade this? ") == "yes":
                                        money -= spirit_box_upgrade_cost
                                        spirit_box_level += 1
                                else:
                                    print("Sorry that's to expensive.")
                            else:
                                print("Sorry you can only upgrade to level 3.")

                        elif upgrade in ["ultraviolet light", "uv", "ultraviolet"]:
                            if ultraviolet_level < 3:
                                if money >= ultraviolet_upgrade_cost:
                                    if input("That will cost $" + str(ultraviolet_upgrade_cost) + " are you sure you'd like to upgrade this? ") == "yes":
                                        money -= ultraviolet_upgrade_cost
                                        ultraviolet_level += 1
                                else:
                                    print("Sorry that's to expensive.")
                            else:
                                print("Sorry you can only upgrade to level 3.")

                        elif upgrade in ["book", "ghost writing", "ghost writing book"] :
                            if ghost_writing_level < 3:
                                if money >= ghost_writing_upgrade_cost:
                                    if input("That will cost $" + str(ghost_writing_upgrade_cost) + " are you sure you'd like to upgrade this? ") == "yes":
                                        money -= ghost_writing_upgrade_cost
                                        ghost_writing_level += 1
                                else:
                                    print("Sorry that's to expensive.")
                            else:
                                print("Sorry you can only upgrade to level 3.")

                        elif upgrade in ["dots", "dots projector", 'projector']:
                            if dots_level < 3:
                                if money >= dots_upgrade_cost:
                                    if input("That will cost $" + str(dots_upgrade_cost) + " are you sure you'd like to upgrade this? ") == "yes":
                                        money -= dots_upgrade_cost
                                        dots_level += 1
                                else:
                                    print("Sorry that's to expensive.")
                            else:
                                print("Sorry you can only upgrade to level 3.")

                        elif upgrade in ["orbs","ghost orbs","camera", "video camera"]:
                            if ghost_orbs_level < 3:
                                if money >= ghost_orbs_upgrade_cost:
                                    if input("That will cost $" + str(ghost_orbs_upgrade_cost) +  " are you sure you'd like to upgrade this") == "yes":
                                        money -= ghost_orbs_upgrade_cost
                                        ghost_orbs_level += 1
                                else:
                                    print("Sorry that's to expensive.")
                            else:
                                print("Sorry you can only upgrade to level 3.")

            if player_guess == "stop":
                pass
            else:
                ending_game = end_game(times_won)
                if ending_game == "true":
                    game_over = "true"
                elif ending_game == "false":
                    game_over = "false"
                    round_ghost = ghost_randomizer()
                    start_time = time.time()
                print("\033[1;38;40mYour save code is:", str(emf_level) + str(freezing_temps_level) + str(spirit_box_level) + str(ultraviolet_level) + str(ghost_writing_level) + str(dots_level) + str(ghost_orbs_level) + str(money) + "-" + str(times_won))

        elif action == "save code":
            print("Your save code is:", str(emf_level) + str(freezing_temps_level) + str(spirit_box_level) + str(ultraviolet_level) + str(ghost_writing_level) + str(dots_level) + str(ghost_orbs_level) + str(money) + "-" + str(times_won))


if __name__ == "__main__":
    main()