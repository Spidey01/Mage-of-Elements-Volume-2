label part2_be_brash:

    "You deposit the empty stein on the bar and decide to be brash."

    show prick at left
    show vanderpool at right

    "With a swift kick to the jewels, the troublesome prick goes down in one blow."
    "A second swift kick sends him toppling into his drunken buddy, Vanderpol."

    hide prick with vpunch
    hide vanderpool with hpunch

    "You stride out of the inn, flicking another coin over your shoulder for the troubles."

    scene bg stable

    "You head for your horse. Schatten is softly enjoying her feed as you pat her apologetically."
    "She won't have time to finish dinner."

    jump part2_common

label part2_be_patient:

    "Better to avoid causing a scene."

    show prick at left
    show vanderpool at right

    "The prick slides one arm around your waist."
    "You grit your teeth and resist the urge to kick him. He smells of urine and mead."
    "You're not in the mood to be groped but wish to avoid a fight."

    "Male voice" "Hey, leave the lady be!"

    show prick scowl at left
    show vanderpool at offscreenleft with moveinleft
    show kaz at right with dissolve

    "Prick" "Whatz it to ya? Piss off, nerd."

    "Glancing over your shoulder: you notice the speaker."
    "He wears brown robes. Book in one hand, beer stein in the other."
    "He means well but doesn't look like much help in a bar room brawl."
    "This isn't going to go well by any means. So much for being patient."

    "You drop the beer stein on the Prick's foot and leave the inn."
    jump part2_common

label part2_common:

    scene bg stable
    "Prick" "Think ya getting away after that missy?"

    "The prick and his buddy stagger out of the inn."
    show prick scaled armor at center
    show vanderpool hunter armor at right

    "Prick has a jack of scaled armour over his doublet and a mid length dagger in his hand."
    "His buddy holds a rope about two metres long in both hands and wears a hunter's leather armour."
    "Looks like these assholes aren't going to take no for an answer."

    "As you draw your sword, Demonslayer, the two bastards rush at you."
    show prick at left with moveinright
    "Side stepping: you avoid a dagger thrust to the rib cage."
    "Your plate armour offers great protection but it is far from complete coverage."
    "Unfortunately the hunter catches you around the neck with his rope and drags you to your knees."

    hide prick with vpunch

    "Everything starts to become fuzzy as your neck tightens under the rope's pressure."
    "You reach for the rope with your free hand but it is no use."
    "The hunter now stands behind you: choking you with the rope."
    "Before you can swing Demonslayer, the prick in the doublet is upon you again."

    show vanderpool at offscreenright with moveinright
    show prick at left

    "Prick" "Now, now. Why so fiesty, bitch?"

    show cg lighting bolt with vpunch

    "Suddenly a lightening bolt turns everything blindly bright."

    "Prick's hair stands on end and begins to smell of ozone as he turns to track the bolt."

    show kaz at right

    "The robed nerd from before stands at the inn door: book in one hand and the other raised towards your position."

    show vanderpool at center with hpunch
    show prick at left with moveinleft

    "A hunter has you by the neck with a rope, a prick is rushing towards the lightening mage."


    menu:
        "Friend or foe, it is now your only chance to get out of this alive."

        "Kill them all.":
            pass

        "Attach the hunter.":
            pass

        "Attach the prick.":
            pass

    # This ends the game.
    "DEBUG END"
    return
