import random

Greetings = ["Greetings!", "Hi!", "Hi there!", "Hello!", "Hello there!", "Hey there!"]
we = " We "
Saw = ["saw", "viewed", "liked", "appreciated"]
your = " your "
Brilliant = ["brilliant", "awesome", "fantastic"]
postAbout = " post about "
Frieze = ["Frieze.", "the Frieze fair.", "the Frieze art fair."]
artCan = " Art can make our lives better, but have you ever "
Wondered = ["wondered ", "pondered ", "questioned "]
Why = ["why an ", "the reason an "]
Artwork = ["Artwork", "Artpiece"]
is500 = " is £500/£5000/£50,000? Would "
Love = ["love to hear", "be great to hear"]
yourViews = " your views!"
# 6 * 4 * 3 * 3 * 3 * 2 * 2 * 2 = 5184 combinations

Num = 50000
Messages = []
for x in range(Num):
    greetingsIndex = random.randint(0, len(Greetings)-1)
    greetings = Greetings[greetingsIndex]

    sawIndex = random.randint(0, len(Saw)-1)
    saw = Saw[sawIndex]

    brilliantIndex = random.randint(0, len(Brilliant)-1)
    brilliant = Brilliant[brilliantIndex]

    friezeIndex = random.randint(0, len(Frieze)-1)
    frieze = Frieze[friezeIndex]

    wonderedIndex = random.randint(0, len(Wondered)-1)
    wondered = Wondered[wonderedIndex]

    whyIndex = random.randint(0, len(Why)-1)
    why = Why[whyIndex]

    artworkIndex = random.randint(0, len(Artwork)-1)
    artwork = Artwork[artworkIndex]

    loveIndex = random.randint(0, len(Love)-1)
    love = Love[loveIndex]

    Message = greetings + we + saw + your + brilliant + postAbout + frieze + artCan + wondered + why + artwork + is500 + love + yourViews
    Messages.append(Message)
    print(Message)

Duplicates = 0
for i in range(1, len(Messages)-1):
    for j in range(1, len(Messages)-1):
        if(i != j):
            if (Messages[i] == Messages[j]):
                Duplicates = Duplicates + 1
                print(Duplicates)
            else:
                continue

UniqueMessages = []
for message in Messages:
    if message not in UniqueMessages:
        UniqueMessages.append(message)

print(len(UniqueMessages))
print(int(Duplicates))
