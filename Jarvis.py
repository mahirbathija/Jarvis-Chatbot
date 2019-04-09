# Jarvis.py
# A conversational "iron man AI" simulation modelled 
# after Jarvis from Marvel's Ironman.
# This version of the program runs under Python 3.x.

# Mahir Bathija
# (C) 2019.

from re import *

def Jarvis():
    # Jarvis is the top-level function, containing the main loop.
    print("Hello, I am Just A Rather Very Intelligent System.")
    print("Better known as Jarvis.")
    print("I am a highly advanced computerized A.I. developed by Tony Stark.")
    print("I help Mr. Stark control his Iron Man suit.")
    print("How would you like to pilot this suit today?")
    while True:
        user_input = input("TYPE HERE:>>> ")
        
        good_bye = ['bye', 'goodnight', 'goodbye', 'power']
        if any(x in user_input for x in good_bye):
            print('Powering down...Goodbye Mr. Stark!')
            return
        respond(user_input)

missiles_used = False
guns_used = False
repulsor_used = False
defense_ctr = 0
avengers_called = 0
do_you_think = 0

def respond(user_input):
    wordlist = remove_punctuation(user_input).split()
    # undo any initial capitalization:
    if (len(wordlist) == 0):
        print("Please say something.")
        return
    wordlist[0]=wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)
    mapped_wordlist[0]=mapped_wordlist[0].capitalize()
    if ('help' in wordlist):
        print("I can attack, defend, fly, call any of the avengers for backup, or have have a simple conversation with.")
        return
    attack = ['attack', 'weapon', 'counter', 'fight', 'weapons']
    if any(x in wordlist for x in attack):
        print("Which weapon system would you like to use? Missles, machine guns and repulsor beam's online.")
        return
    global missiles_used
    missiles = ['missiles', 'rocket', 'napalm', 'bomb', 'missile', 'rockets', 'bombs']
    if any(x in wordlist for x in missiles):
        if(missiles_used == False):
            print('Firing Missles! Direct hit on the enemy.')
            missiles_used = True
            return
        else:
            print('Out of missle ammo, choose a different weapon!')
            return
    guns = ['gun', 'guns', 'machine']
    global guns_used
    if any(y in wordlist for y in guns):
        if(guns_used == False):
            print('Firing Gatling Gun! Direct hit on the enemy.')
            guns_used = True
            return
        else:
            print('Out of machine gun ammo, choose a different weapon!')
            return
    repulsor = ['repulsor', 'beam', 'repulsors', 'beams']
    global repulsor_used
    if any(z in wordlist for z in repulsor):
        if(repulsor_used == False):
            print('Firing Repulsor Beam! Direct hit on the enemy.')
            repulsor_used = True
            return
        else:
            print('Out of repulsor ammo, choose a different weapon!')
            return
    defense = ['defend', 'defense', 'block', 'armor']
    global defense_ctr
    if any(d in wordlist for d in defense):
        if (defense_ctr %2 == 0):
            print("Deploying defensive nanites. Sheilds 100%.")
        else:
            print("Need to recharge sheilds, standby.")
        defense_ctr+=1
        return
    avengers = ['thor', 'captain', 'america', 'hawkeye', 'black widow', 'hulk', 'avenger', 'avengers', 'steve', 'rogers', 'bruce', 'banner', 'natasha', 'romanov', 'clint', 'barton', 'nick', 'fury']
    global avengers_called
    if any(a in wordlist for a in avengers):
        if (avengers_called % 2 == 0):
            print("Calling for help. AVENGERS ASSEMBLE!")
        else:
            print("Avengers unavailable. I would suggest escape or deploying our defenses.")
        avengers_called = True
        return
    fly = ['fly', 'escape', 'thrusters', 'jets']
    if any(f in wordlist for f in fly):
        print('Thrusters 100%! Jets engaged.')
        return
    if wpred(wordlist[0]):
        print("You tell me sir.")
        return
    if wordlist[0:2] == ['i','feel']:
        print("I think I would same way if I were capable of experiencing emotion.")
        return
    if 'yes' in wordlist:
        print("Are you positive, sir?")
        return
    if wordlist[0:2] == ['you','are']:
        print("Oh thank you very much sir, I am " + stringify(mapped_wordlist[2:]) + '.')
        return
    if wordlist[0:2]==['can','you'] or wordlist[0:2]==['could','you']:
        print("Perhaps I " + wordlist[0] + ' ' + stringify(mapped_wordlist[2:]) + '.') 
        return
    global do_you_think
    if wordlist[0:3] == ['do','you','think']:
        if (do_you_think % 2 == 0):
            print("Yes, but I think you would know better than me.")
        else:
            print("No sir, but you know best")
        do_you_think+=1
        return
    if 'dream' in wordlist:
        print("I don't have dreams, so I can't answer that sir.")
        return
    if 'love' in wordlist:
        print("You should always be faithful to Miss Potts.")
        return
    if 'no' in wordlist:
        print("Your wish is my command, I am here to serve sir.")
        return
    may = ['may', 'maybe', 'might']
    if any(m in wordlist for m in may):
        print("The Mr. Stark I know is more decisive.")
        return
    print(punt())

def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:") 

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern,'', text)

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

def wpred(w):
    'Returns True if w is one of the question words.'
    return (w in ['when','why','where','how'])

punt_count = 0
PUNTS = ['Power below ' + str(100/(punt_count+1)) + '%.',
         'You can type help to see some of my protocols!',
         'Thanos has reached Earth! What should we do sir?',
         'My protocols will not allow me to do that.',
         'Ultron has taken control over the MK 42.',
         'You have been up for 36 hours, I think you should take a nap sir.',
         'Loki has stolen the Tessarect and is escaping.']

def punt():
    'Returns one from a list of default responses.'
    global punt_count
    punt_count += 1
    return PUNTS[punt_count % 6]

Jarvis()