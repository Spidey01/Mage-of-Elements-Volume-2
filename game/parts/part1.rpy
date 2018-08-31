label part1:
    scene bg inn

    "{b}You walk into a busy Inn{/b}"

    "There are clusters of people everywhere."

    show bard

    "Many groups are watching the bard play her lute as two young boys dance about playing flutes."

    #play music "Bard's Song"

    "It is a soft playful tune that you heard once in a country far away."

    "Several staff bustle about serving food and drink to the establishment's many patrons."

    "In the darkest recesses of the inn, there are doubtlessly people lurking; quiet and out of trouble."

    "Most of the inns clientele are dressed in simple robes and tunics and the like; a handful wear any kind of armour."

    scene bg bar
    with dissolve

    "Walking up to the bar, you drop a silver coin on the counter, and look towards the bartender."

    show innkeeper at center
    with fade

    "He catches your look and continues serving. Waiting, you look about and take in your neighbors."

    show shadow at right

    "A dispatch rider wearing a satchel stands a short way off to your right sipping a dark ale at the end of the bar."

    "Off to your left are a five armoured men chatting: some wear jacks of scale and some simple leather armour."

    "Everyone else looks a merchant or farmer. Most of them are armed. A couple of people wear robes, you've no idea what they may conceal."

    hide shadow
    with dissolve

    "{i}Swiftly your coins disappear with a knod. The innkeeper stares at you expectantly.{/i}"

    launa "A mead and a room for the night."

    innkeeper "Private rooms are five septims. Three for a bunk."

    "You plunk down five more silver coins. Soon they are gone and you have your mead."

    hide innkeeper
    with fade

    show bard at right

    "Turning toward the bard's performance, you lean back against the counter and enjoy the mead."
    "One hand resting instinctively on the hilt of your sword, Demonslayer."

    "Mead here is sweet and dingy."
    "It tastes of greyberries and honey. Also like hay."
    "You suspect sans the honey that the mead is probably made from leavings from the barn."
    "At least it hasn't been pissed in."

    "The bard and her apprentices sing a clipped version of an old poem."

    # play music "Old Poem"

    bard "Once upon a ride in the burrow."
    bard "We found ten drunken dwarves."
    bard "Among them were two dozen draugr."
    bard "With not a sword between them."

    launa "{i}I'll never understand this country's poetry{/i}."

    "Regarding you for the first time: one of the men off to your left shifts and says"
    show shadow at left
    with dissolve
    "Prick" "Hey doll, aren't you a bit short for all that plate?"

    hide bard

    "Sipping the last of your mead, you size him up over the edge of the glass."

    hide shadow
    show prick at left

    "He's two heads taller than you. Blond. Deeply set face. Blue eyes and a fairly nasty sneer. He probably has over fourty kilos on you."
    "The prick wears a doublet and hose under a jack of scaled armour."
    "A sword is sheathed at one of his hips and a dagger pommel juts from behind his waist. You wear a light cuirass of fine steel."

    launa "Not at all."

    hide prick

    "You turn away."

    "Prick" "Hey Vanderpol, take a gander at this pretty sword she's got!"
    "He says while clawing at your right arm."

    "Apparently this isn't going to be a fun stay. Your mind snaps to where your horse is stabled."
    "You have more important things to do this night than suffer these pests."

    menu:
        "{b}You decide to ....{/b}"

        "Be rash":
            jump part2_be_brash

        "Be patient":
            jump part2_be_patient

        "Leave quietly":
            jump part2_common

