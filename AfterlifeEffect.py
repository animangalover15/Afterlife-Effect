import sys
node = None

class Story:
    def __init__(self, name, story, dialouge, next, a, b, c, d):
        self.name = name
        self.story = story
        self.dialouge = dialouge
        self.next = next
        self.choice1 = a
        self.choice2 = b
        self.choice3 = c
        self.choice4 = d
        
    def Choose(self, Choice):
        global node
        node - globals()[getattr(self, Choice)]
    
Intro = Story("Intro", "Long ago, In a land long forgotten, an adventurer destined for the fate they chose came across two strange looking children. What no mortal knew was thet these children had a large secret. A secret that could effect every thing on earth, both living and dead. This adventurer did not know their secret, did not even know who they were but took them in for one reason. You are this adventurer, and your name is 'Player'", None, None, None, None, None, None)
#directions are here 
Direction = Story("Direction", "To choose an option, type a, b, c, or d in lowercase. This game is based on your choices and will effect the ending you get.", None, None, None, None, None, None)
#the story starts
The_forest = Story("The forest", "Its a beautiful day as you walk through the lush forest. Though, it was hard to enjoy a day like ths when your exahuseted from your adventures.", None, None, None, None, None, None)
The_children = Story(None, "You continue to walk, in search for a village. You notice something in the corner of your eye", 'Who\'s there\!\?', None, None, None, None, None)
#first yet small desision
Greeting = Story(None, "Out of the bushes came a small figure lurching at you with a dagger to which you eaisly dodged", None, "Tell your little friend to come out of hiding and nobody gets hurt", "If you just tell your buddy to stop hiding in the bushes, we could talk this out", None, None, None)
Life_appears = Story(None, "A small boy holding a stuffed bear emerges from the bushes", None, None, None, None, None, None)
Children_speak = Story(None, "The girl looks up at you and speaks fist. She has eyes darker then tar and no pupils with hair to match.", "Kamatayon: M-my name is Kamatayon and t-this is my brother, leven. We just needed some food", None, "So you tried to kill me!?", "I suppose i understand", "I'm debating on weather i should kill you or not", None)
Life_speaks = Story(None, "The boy speaks next. His eyes were as white as snow but at least you could tell he had pupils. His hair a whitish bash", "Leven: U-Um, if you let us go... w-we wont try to bother you again, s-so...", None, "...Come with me", "um, i can take you home", None, None)
Kama_speaks = Story(None, "They eye you suspisiously", "Kama: H-how can we trust you?", None, "You dont have to come", "I wont hurt you, I'll help you get home.", "Then stay here, I dont care.", None)
Agreement = Story(None, "They still seem uneasy. Kama grabs Levens arm and puts herself in between you two.", "Kama: F-ine. W-we'll go with you", None, "Then lets go.", None, None, None)
First_small_villiage = Story("Small villiage", "You three enter a small villiage and go to gather supplies.", "Kama: A-are you sure you wanna buy this for us?", None, "Well...Yeah! you look like you need the food!", "Why not, It wasnt too much", "For you?, this is for me", None)
Hotel = Story("Hotel", "You check into a hotel and head to your room. You flop down onto your bed, ready to rest. Leven is the first to fall asleep", "Kama: Um... thanks...for uh, helping us", None, "Of course, I'd never leave children alone in the woods", "'You look away from her' Whatever...", "...", None)
Room = Story(None, "You look around the room as the children sleep. You cant seem to sleep and feel as if your being watched but when you turn around, you see nothing. You look at the clock to see how long you've- ...Strange The clock is broken.", None, None, None, None, None, None)
Waking_up = Story(None, "Waking, you hear an eerie, saddening whisper '...ring...em...ack' You can barely understand the words. Suddenly you hear a voice in the distance", "Kama:...ey...Hey wake up! Youve been tossing in your sleep, now lets get ready, its morning.", None, None, None, None, None)
Getting_up = Story(None, "You Say nothing and get dressed in proper clothing and armor. Going to the dining hall, you have that feeling again. You keep your weapon close to you. Leven speaks in a timid yet hopeful voice", "Leven: U-um... s-so... i-is it ok i-if i get s-some walffles...?", None, "Smile and say yes", "Say no annoyed", None, None)
#This is where the players desisions will start to be seperated
#A small desision that may just effect you later
Say_yes_to_leven = Story(None, "You watch Levens face light up as he excitedly goes to his sister to tell her. You smile.", "Leven: 'Did you hear that Kama!? They said yea!' Kama:'Heh, yea I heard' She smiles at you", None, None, None, None, None)
Say_no_to_leven = Story(None, "You watch Leven's face drop and hug his teddy bear tighter. He looks as if he might cry", "Leven: 'O-oh...o-ok...*sniff*' He goes to Kama as she glares at you and gives him a flower she seems to have found. He looks a bit happier", None, None, None, None, None)
#if yes
Dining_hall_yes = Story(None, "You enter the dining hall and watch as Leven dashes for the waffles. Kama smiles at him", "Kama: Thank you for Telling him yes", None, "'hm...' you grunt", "'Of course' you smile", "...", None)
#if no
Dining_hall_no = Story(None, "You enter the dining hall and watch as Leven sulks to his seat at the table. Kama seems to glare at you.", "Leven: 'I'm gonna go get some water' He gets up. Kama:'OK'She turns to you why did you say no to him?'", None, "We dont have the money to spare", "...", "Who cares, he'll live", None)
#Back to story
The_feeling_again = Story(None, "Kama turns away as leven comes back. You all eat in silence when suddenly, You feel your being watched again", "Kama:'Whats wrong?' You:...Nothing...i'm going to get more water", None, None, None, None, None)
#A save point shows
Girl_shows = Story(None, "You get up and look around as you get your water. You notice a strange looking girl looking at you smiling", "Strange girl:'Yo' You:'Yo?' She laughs, Strange girl:'Whoops, forgot the era...'She mumbles", None, None, None, None, None)
Girl_appearence = Story(None, "The girl is dressed strange. although it wasnt unusual for women to waer garments similar to men, especially with armour, her cloths was different. She had a strange red and black wool Shirt with a strange metal zig zaged line down the middle. She had pants made of a strange dark blue material and shoes with strings tied on them. Her brown hair was held up by a ponytail, though it did little to hold her bangs off her left eye", None, None, None, None, None, None)
Girl_speaks = Story(None, "You stare cnfused for a moment", "Strange girl:'Anyways! The name\'s Brenda, nice to meet ya, i've actually needed to tell you something.'", None, "OK...?", "Walk away", None, None)
Brenda_the_saver = Story(None, None, "Brenda: 'Great! Now, I have this...power that allows you to go back to your last 'Checkpoint'! Here!'She hands you a broken watch, Brenda: Just press that button anytime you need me and I'll show up!", None, None, None, None, None)
Save = Story(None, "To save, press 'S'", "Brenda:'So just call if you need me! Well! GTG- er...Gotta go!' You:'Wait who-' She was already gone.", None, None, None, None, None)
Go_back = Story(None, "You head back to the table", "Kama: 'I thought you were gonna get water?' You:'I changed my mind' Kama eyes you suspisiously but seems to except the answer.", None, None, None, None, None,)
Ask_kids = Story(None, "You look curiously at the children happily eating their food. 'Where are they from?' you wonder.", "Kama: 'Whats wrong? You've been staring for a bit' She asks. You:'oh, i was just wondering where you guys are from.' They stay silent.", None, "Press on", "Keep silent", "Say you understand", None)
#Another choice
Press_on = Story(None, "You press them on", "You:'Come on, tell me' Kama stays silent. Maybe you touched a nerve?", None, None, None, None, None)
Stay_silent = Story(None, "you choose to stay silent There seems to be an akward tension in the air after that", None, None, None, None, None, None)
You_Understand = Story(None, "You nod your head.", "You:'Don't worry, I understand.' Kama smiles slightly.", None, None, None, None, None)
#back to story
Senseing_again = (None, "You sense someone watching you again. You look around, maybe its that girl again? But... she left, right? So, who?", "Kama: \'Whats wrong? You\'ve been really tense?\' You see a shadow move in the corner of your eye. Strange figure... You: \'Are you guys done? I think we should go\'", None, None, None, None, None)



print Intro.story
print('\n')
print Direction.story
print('\n')
print The_children.story
print('\n')
print The_children.story

user = raw_input()