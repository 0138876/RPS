antwoord= ['rock', 'paper', 'scissors']
rounds = 0
maxrounds = 0
score = 0
spelers = []
players = int(input("How many players are there 2 or 3? \n"))



# kijkt naar of aantal spelers gelijk is aan 2 of 3 zo niet dan wordt er om een correcte input gevraagd
# is de input correct wordt er per speler de naam van elke speler, score en een lege string voor antwoorden toegewezen in de list spelers.


def input_player():
    global players
    if (players == 3 or players == 2):
        playername = input("What is your name \n").lower()
        print("\n")
        spelers.append([playername, score, ""])
    else:
        print("\nChoose one of the possible options")
        players = int(input("How many players are there 2 or 3? \n"))
        print("\n")
        input_player()

# zet het maximaal aantal rondes in wat voor 2 players of 3 players geldt maar omdat ik geen drie player heb is dit niet nodig

def check_players(players):
    global maxrounds
    for i in range(players):
        input_player()
        if(players == 2):
            maxrounds = 3
        else:
            maxrounds = 4

# kijkt wie de winnaar is van de 2 spelers

def who_winner():
    global spelers
    global rounds
    answer1 = spelers[0][2]
    answer2 = spelers[1][2]
    if (answer1==answer2):
        print("it's a tie")
        return
    if(answer1=="rock"):
        if(answer2=="scissors"):
            print(spelers[0][0] +  " wins\n")
            spelers[0][1]= spelers[0][1]+1
        else:
            print(spelers[1][0] + " wins\n")
            spelers[1][1]= spelers[1][1]+1
    elif(answer1=="scissors"):
        if(answer2=="paper"):
            print(spelers[0][0] +  " wins\n")
            spelers[0][1]= spelers[0][1]+1
        else:
            print(spelers[1][0] + " wins\n")
            spelers[1][1]= spelers[1][1]+1
    elif(answer1=="paper"):
        if(answer2=="rock"):
            print(spelers[0][0] +  " wins\n")
            spelers[0][1]= spelers[0][1]+1
        else:
            print(spelers[1][0] + " wins\n")
            spelers[1][1]= spelers[1][1]+1
    print(spelers )
    rounds+=1
    print(" aantal gespeelde rondes: " + str(rounds))
    print("\n")


# kijkt of er iemand een score van 2 heeft of niet zo ja dan wordt de winnaar bekend gemaakt

def check_endgame():
    if spelers[0][1] == 2:
        print("\n"+ spelers[0][0] + " wins with a score of: " + str(spelers[0][1]))
        return True
    elif spelers [1][1] == 2:
        print("\n" + spelers[1][0] + " wins with a score of: " + str(spelers[1][1]))
        return True
    return False



# zorgt ervoor dat de code draait zolang er niemand 2 punten gescoord heeft en vraagt om input van elke player
# kijkt of de input in de antwoorden zit zo ja dan gaat hij verder anders vrijgt hij hetzelfde persoon om input

def play_game():
    correct = False
    while(check_endgame() == False):
        for index, player in enumerate(spelers):
            correct = False
            while(correct == False):
                answer = input("hey " + player[0] + " enter rock, paper or scissors \n").lower()
                print("\n")
                if(answer in antwoord):
                    correct = True  
                spelers[index][2]=answer.lower()
        who_winner()


# zorgt ervoor dat alle functies geroepen worden en uitgevoerd worden die erin staan

def run_game():
    check_players(players)
    play_game()

run_game()


# vraagt of je opnieuw wilt spelen en zorgt dat alles gereset wordt.

def rerun_game():
    restart = input("Do you wanna play again yes or no\n").lower()
    if restart == "yes":
        print("\n")
        global score
        global rounds
        global maxrounds
        global players
        rounds = 0 
        maxrounds = 0
        score = 0
        spelers.clear()
        players = int(input("How many players are there 2 or 3? \n"))
        run_game()
        rerun_game()
    else:
        print("\n")
        exit()

rerun_game()