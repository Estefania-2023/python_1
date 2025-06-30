#
# Adventure Game 
#
# By Estefanía Ortiz
#

print("Starting Story")

print("You are at home, you have nothing to do, so you have three options to continue")
decision=input("STAY at home, WALK to the forest or VISIT a friend: ")

# Level1 A
if decision.upper() == "STAY" :
    print("You stay at home")
    decision = input("IRON the clothes, WATCH a movie or WASH food service: ")

    #Level A.1
    if decision.upper() == "IRON" :
        print("You iron the clothes")
        print("While you iron clothes, one of your childhood friends call you for your phone. What happiness! After a while, you do not communicate")
        decision = input("ANSWER him, IGNORE or CALL him later: ")

        #Level A.1.1
        if decision.upper() == "ANSWER" :
            print("You answer him")
            print("You spend a good time with your friend on the call. Until hours go by and you decide to end the call because you have to go to sleep")
            print("Oh no! You forgot to turn off the iron. You immediately go there and suddenly you hear an explosion")
            print("You die") 

        #Level A.1.2
        elif decision.upper() == "IGNORE" :
            print("You ignore his call") 
            print("Then you finish ironing the clothes")  
            print("You're hungry and go down to dinner")  
            print("Then at the end you go to sleep")              

        #Level A.1.3
        elif decision.upper() == "CALL" :
            print("You call him later that you ironed the clothes") 
            print("At that moment, he answers and tells you that he will go to your house")  
            decision = input("ACCEPT him to come or REJECT him: ")  

            #Level A.1.3.1
            if decision.upper() == "ACCEPT" :
                print("You accept him to come to your house")
                print("After he is knocking on the door of your house, you let him pass, you realize that your friend brought soda to drink")
                decision = input("TAKE the soda or DECLINE: ")

                #Level A.1.3.1.1
                if decision.upper() == "TAKE" :
                    print("You take the soda, later you feel as if you had taken poison")
                    print("You feel very bad after taking it until your heart stopped beating")
                    print("You die")

                #Level A.1.3.1.2
                elif decision.upper() == "DECLINE" :
                    print("You decline it")
                    print("You are not thirsty, but your friend insists, and you keep denying it")
                    print("After having a great conversation, you see that it is very late and you ask your friend to leave because you have to go to sleep")
                    print("But your friend insists on staying")
                    decision = input("You make him LEAVE or LET him stay: ")
                    
                    #Level A.1.3.1.2.1
                    if decision.upper() == "LEAVE" :
                        print("With all your fury and strength, you make him leave")
                        print("Then you go to sleep without any problem")

                    #Level A.1.3.1.2.2
                    elif decision.upper() == "LET" :
                        print("You let him stay")
                        print("Then you tell him the room where he will sleep")
                        print("At bedtime, you feel like you've been stabbed")
                        print("You die")

            #Level A.1.3.2
            elif decision.upper() == "REJECT" :
                print("You reject him by telling him that you have things to do")
                print("He accepts, then you end the call")
                print("Then you go to dinner, then to watch a movie and then to sleep")
                     
    #Level A.2
    elif decision.upper() == "WATCH" :
        print("You watch a movie")
        print("The movie is very long, you watch it until you have to go to sleep.")

    #Level A.3
    elif decision.upper() == "WASH" :
        print("You wash food service")
        print("After that, you think about watching a movie")
        print("At the end of watching a movie, you go downstairs to eat")
        print("At the end of it all, you go to sleep")
        
# Level2 B
elif decision.upper() == "WALK" :
    print("You walk to the forest")
    print("Being there, you get distracted by nature, the song of the birds, the sound of the river, the flowers blooming, and the bees taking advantage of their pollen. ")
    print("However, you do not realize that time passes quickly, and it became night. Everything is dark, but you have something in your pocket. what's there?")
    decision = input("PHONE or FLASHLIGHT: ")

    #Level B.1
    if decision.upper() == "PHONE" :
        print("Your phone is in your pocket")
        print("You turn it on and see the time. It's too late! Until you hear big footsteps, you lean out to see who is coming")
        print("... What is a brown bear doing there?! Will the bear be hungry?. So you have 2 options to do")
        decision = input("RUN or HIDE: ")

        #Level B.1.1
        if decision.upper() == "RUN" :
            print("Your run")
            print("The bear, noticing your escape, decides to chase you")
            print("Along the way, you come across a grand river and the bear is behind you")
            decision = input("JUMP into the river or PLAY dead: ")

            #Level B.1.1.1
            if decision.upper() == "JUMP" :
                print("You jump into the river")
                print("Since you know about swimming, you hold your breath and look for a place to be safe")

            #Level B.1.1.2
            elif decision.upper() == "PLAY" :
                print("You play dead")
                print("The bear approaches you")
                print("You die")
            
        #Level B.1.2
        elif decision.upper() == "HIDE" :
            print("You hide")
            print("But suddenly, the phone rings. One of your friends is calling you")
            print("You try to silent the phone. However, the bear was very close to you, it notices that and approaches you")
            print("You die")
    
    #Level B.2
    elif decision.upper() == "FLASHLIGHT" :
        print("Your flashlight is in your pocket")
        print("You turn on your flashlight, and you see a path. You decide to go there, to find out if it is the exit")
        print("But instantly, you hear big footsteps. It's a brown bear!")
        print("But luckily it's a bit far, so you decide to walk away quietly as you follow the path")
        print("Along the way, you come across a cabin")
        decision = input("ENTER the cabin or CONTINUE on the path: ")

        #Level B.2.1
        if decision.upper() == "ENTER" :
            print("You enter the cabin")
            print("In the cabin, there are all the necessary amenities. A refrigerator, a kitchen, a dining room, a bedroom, and a bathroom")
            print("Since it is already too late to walk alone in the forest, you decide to spend the whole night here")

        elif decision.upper() == "CONTINUE" :
            print("You continue on the path")
            print("Then on the way, you meet the same brown bear")
            print("You are about to run away, but the bear lunges at you")       
            print("You die")
            
# Level3 C
elif decision.upper() == "VISIT" :
    print("You visit a friend")
    print("When your friend sees you, he invites you to enter to his house. You talk together and have a good time")
    print("Until the friend thought of bringing 4 bottles of beer and invites you to drink")
    decision = input("ACCEPT, REJECT or better SMOKE: ")

    #Level C.1
    if decision.upper() == "ACCEPT" :
        print("You accept")
        print("Your friend begins to fill the glasses with beer. You start drinking together with your friend")
        print("... But then, you start to feel dizzy. And you just remembered that you're sensitive to beer. You try to ask for help, but you faint")
        print("Later, you wake up to find yourself inside the bathtub in an unfamiliar bathroom. At that moment you are very confused and scared. Until you stumbled upon the very scary surprise")
        print("You take off your shirt and see that you have scars on your stomach. As if someone had recently sewn it")
        print("Suddenly, someone approaches the door")
        decision = input("HIDE, ATTACK with an object or ASK that person: ")

        #Level C.1.1
        if decision.upper() == "HIDE" :
            print("You hide")
            print("Before hiding, you get out of the bathtub and close the bathtub curtain, and hide behind the door quietly")
            print("The person when entering sees the bathtub with the curtain closed, thinking that you were there")
            print("Taking advantage of it, you run out of the bathroom. Oh no! Three people who were on the side realize that and chase you")
            print("You try to run faster, but something prevents you from running too much")
            print("Why do you feel so empty? Why don't you have too much strength?... At that moment, one of they grabs your arm")
            decision = input("ASK or HIT: ")

            #Level C.1.1.1
            if decision.upper() == "ASK" :
                print("You ask them, why they do all that?")
                print("They tell you that someone ordered them to do it. But who will be that person who wanted to make you in such a severe situation?")
                print("You try to walk away. Suddenly, a well-known voice asks them to let you go. It was your friend who was in a corner. Now you feel very confused")
                print("They confused, saying that your friend is the one who ordered them to remove your organs")
                print("When you hear this, you are shocked and disappointed at the same time. What kind of friend is he?!")
                print("But at that time that friend. He starts hitting them with a wooden stick until they are unconscious. He try to pulls you to escape from the place")
                decision = input("ACCEPT to go with your friend, STAY AWAY from him or HIT him: ")

                #Level C.1.1.1.1
                if decision.upper() == "ACCEPT" :
                    print("You accept to go with your friend")
                    print("Despite all the mistake made. Or you know that he is not as bad as you thought")
                    print("As you leave the place, you tell your friend that you going to report it")
                    print("Since you believe almost nothing in the words of a stranger and you believe that your friend is innocent")
                    print("He accepts it, though seconds later, he decided to stab you from behind, and he thanks you for trusting")
                    print("You die")

                #Level C.1.1.1.2
                elif decision.upper() == "STAY AWAY" :
                    print("You stay away from him completely")
                    print("You ask him why he did all this, but he doesn't answer you and insists that you go with him")
                    print("So you deny it and decide to run towards the exit to go to a nearby police station")
                    print("But he pulls out a gun and points it at you")
                    print("You die")

                #Level C.1.1.1.3
                elif decision.upper() == "HIT" :
                    print("You hit him with all your furious")
                    print("But he resists that and tries to get away from you")
                    print("However, you notice the wooden stick lying around. So you quickly grab it")
                    print("You hit him in the head with all your possible strength and he becomes unconscious")
                    print("In the end, you run out of the place and the neighborhood and ask for help, since your body can't take it anymore")
                    print("Luckily, a person in the car, if he caught sight of you, took you to the hospital and at the same time, called the police to arrest the criminals")

            #Level C.1.1.2
            elif decision.upper() == "HIT" :
                print("You hit this one. And you try to escape")
                print("But the others grab you very tight and start beating you. You beg them to stop since you can't take too many hits")
                print("But they don't listen to you and they keep playing to hurt you. Until one decides to shoot you")
                print("You die")

        #Level C.1.2
        elif decision.upper() == "ATTACK" :
            print("You grab a broom that was next to the bathtub, and you attack with this")
            print("The person upon entering receives a blow from you with the broom and falls. You just run away with the broom in hand")
            print("After that, you meet 3 more people, they try to catch you. But you stop them by hitting them on the head with the broom, leaving them unconscious")
            print("You decide to run even faster to find the exit. But someone stopped you from doing it...")
            print("You meet your friend, being in front of you he stops you telling you not to run too much since you are not in good condition")
            decision = input("HIT him, ASK or LISTEN to him: ")

            #Level C.1.2.1
            if decision.upper() == "HIT" :
                print("You hit him on the head with the broom")
                print("You were very suspicious of him since you heard him say that you are not in a good condition")
                print("Did he know that they removed your organs until you were empty and then sewed without you saying a word?")
                print("Luckily you had enough strength to finish off the criminals and run to ask for help")
                print("You run out of the neighborhood and find a police station, you go to sue the criminals")

            #Level C.1.2.2
            elif decision.upper() == "ASK" :
                print("You ask him")
                print("You ask him what he is doing there and if they did him any harm")
                print("He tells you that after you fainted, they knocked on the door of his house, he had just been threatened by the criminals warning him that they were going to kidnap him and you")
                print("But with the condition that if he wanted to leave without any damage or change, well he had to offer your organs and he apologizes to you for that")
                decision = input("HIT him, FORGIVE him or GET AWAY from him: ")

                #Level C.1.2.2.1
                if decision.upper() == "HIT" :
                    print("You hit him with all your furious")
                    print("You hit him hard on the head with the broom leaving him unconscious")
                    print("You think that was it and you decide to run towards the exit...")
                    print("However, there was someone who was not unconscious and with the gun in his hand, he shot you")
                    print("You die")

                #Level C.1.2.2.2
                elif decision.upper() == "FORGIVE" :
                    print("You forgive him because you assume he wasn't at fault and you believe his words")
                    print("Then you go with him to the exit. And you're happy because you know you have someone to trust right now")
                    print("But suddenly, you feel a knife through your back. You have been betrayed")
                    print("You die")                

                #Level C.1.2.2.3
                elif decision.upper() == "GET AWAY" :
                    print("You get away from him because you do not trust his words")
                    print("Although he urges you to trust him, however, you run further away")
                    print("But you feel a shot in the leg, you fall and scream in pain")
                    print("You realize that he had a gun, he approaches you and says that he was always envious of you. And you get his last shot in the head")
                    print("You die")

            #Level C.1.2.3
            elif decision.upper() == "LISTEN" :
                print("You listen him")
                print("Since he is a brother to you and you think he is innocent")
                print("You still walk fast together though")
                print("However, the friend did not turn out to be someone you imagined. You just got stabbed")
                print("You die")
            
        #Level C.1.3
        elif decision.upper() == "ASK" :
            print("You ask that person who had just entered")
            print("But he doesn't say a word to you and roughly hits you several times")
            print("You can't stand it because you feel empty and weak and you beg him to stop")
            print("But he doesn't listen to you. In the end, he pulls out a gun and shoots you in the head")
            print("You die")

    #Level C.2
    elif decision.upper() == "REJECT" :
        print("You reject")
        print("He insists you so much to accept it, but you deny it")
        print("Like a good friend, he stopped insisting so he offers you an orange juice")
        decision = input("ACCEPT or REJECT: ")

        #Level C.2.1
        if decision.upper() == "ACCEPT" :
            print("You accept")
            print("So your friend pours you the juice in a glass, even though you see the juice in a weird way")
            print("He tells you that he brought it from a new store and it tastes better")
            decision = input("DRINK the juice or REFUSE: ")

            #Level C.2.1.1
            if decision.upper() == "DRINK" :
                print("You drink the juice")
                print("But when you take it you feel dizzy and you faint")
                print("Hours later, you wake up and find yourself on a stretcher. Next to you, you see a scalpel and various medical objects on the table")
                print("Then you take off the T-shirt, and you see that they have drawn circles with the marker all over your abdomen")
                print("Until you hear someone walk in")
                decision = input("ATTACK or ASK: ")

                #Level C.2.1.1.1
                if decision.upper() == "ATTACK" :
                    print("You attack him with the scalpel")
                    print("It receives your attack, begins to bleed, and screams for help, while you cut its neck with the scalpel")
                    print("But another appears and prevents you from doing it with a shot of him in your head")
                    print("You die")

                #Level C.2.1.1.2
                elif decision.upper() == "ASK" :
                    print("You ask him why and what are you here for")
                    print("He doesn't answer you and asks you to get on the stretcher. Which you deny, so he pulls out a gun and forces you to do it")
                    decision = input("GET ON the stretcher or POUNCE on him: ")

                    #Level C.2.1.1.2.1
                    if decision.upper() == "GET ON" :
                        print("You get on the stretcher for fear of being killed")
                        print("Then this person gives you too much anesthesia, to such an extent that it makes you sleepy and you fall asleep")
                        print("But you didn't expect that he would remove all your organs up to your heart")
                        print("You die")

                    #Level C.2.1.1.2.2
                    elif decision.upper() == "POUNCE" :
                        print("You pounce on him to such an extent that you try to take his gun away")
                        print("A shot was heard, you shot him and he screams in pain for help. You put the gun aside and run away")
                        print("But another helped him, shooting from not so far in your head")
                        print("You die")

            #Level C.2.1.2
            elif decision.upper() == "REFUSE" :
                print("You refuse")
                print("You don't want to drink the juice simply because you're not thirsty")
                print("Even if the friend insists, he knows that you would not accept it. So a little moody but with a smile, he invites you to go somewhere")
                print("So you agree to go with him since you are his friend and you don't want to make him feel bad")
                print("Until an unknown place arrives and you ask him what is spectacular about this place")
                print("He tells you that an old friend lives there and invites you to spend time at his friend's house")
                decision = input("BE at his home or DENY it: ")

                #Level C.2.1.2.1
                if decision.upper() == "BE" :
                    print("You accept and going to be in his house. A person receives you at the door and invites you in")
                    print("Then you meet 3 more people in that house who were sitting eating snacks, drinking and enjoying the music, they tell you that they are having a party")
                    print("You sit for a long time until you decide to go to the bathroom. Minutes later you leave the bathroom you see a messy room.")
                    decision = input("ENTER that room or IGNORE: ")

                    #Level C.2.1.2.1.1
                    if decision.upper() == "ENTER" :
                        print("You enter the room that is full of disorder")
                        print("Then, on a table you see a notebook that looks used. Out of curiosity you decide to open it, and you find something terrifying")
                        print("In the notebook, you see many photos of bloody bodies, some with the organs removed, and on the side of each image are written the names of the victims")
                        print("Quickly, you leave the room and try to tell your friend that these people are serial criminals. But he doesn't listen to you, because the volume of the music is very high")
                        print("So, you decide to go out on your own, but your friend stops you, begging you to stay longer")
                        print("You deny it until about 2 people get behind you and decide to beat you to death because they realized what you just saw. And the friend enjoys watching you suffer")
                        print("You die")

                    #Level C.2.1.2.1.2
                    elif decision.upper() == "IGNORE" :
                        print("You ignore the room and go back to the party")
                        print("They invite you a soda, and you accept it since you are thirsty")
                        print("You take it, but after a while you feel bad until it affected your health a lot and you couldn't wake up anymore")
                        print("You die")
                    
                #Level C.2.1.2.1
                elif decision.upper() == "DENY" :
                    print("You deny it")
                    print("Your friend, tired of you denying everything, asks if you're okay")
                    print("You simply tell him that you don't know this place and besides, you suspect that it is a dangerous neighborhood")
                    print("Then you turn around, and later you will realize that the danger was with you all the time. You have been shot")
                    print("You die")

        #Level C.2.2
        elif decision.upper() == "REJECT" :
            print("You reject")
            print("Since you are not thirsty, you decide not to drink any soft drink")
            print("Although the friend is a bit furious, he decides to continue the conversation")
            print("Until the dream caught you and unconsciously you fell asleep. But the next day you didn't wake up again, you were murdered.")
            print("You die")
        
    #Level C.3
    elif decision.upper() == "SMOKE" :
        print("You say it's better to smoke")
        print("Your friend thought that was a great idea, and he's bringing cigars. While he was smoking, his friend came up with the idea of smoking with too many chemicals")
        decision = input("ACCEPT or REJECT the idea")

        #Level C.3.1
        if decision.upper() == "ACCEPT" :
            print("You accept the idea")
            print("You keep smoking with too many chemicals, until you feel bad, and you cough very hard")
            print("You feel as if you have taken poison. There was a moment when you stopped breathing")
            print("You die")
        
        #Level C.3.2
        elif decision.upper() == "REJECT" :
            print("You reject the idea")
            print("Although the friend insists,but you do not want to get worse")
            print("So the friend unable to control his emotions at this time. He hits you very hard to the point of killing you")
            print("You die")

        

