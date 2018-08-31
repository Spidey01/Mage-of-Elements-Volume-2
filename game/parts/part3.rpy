label part3_kill_them_all:

    show prick at left with moveinleft
    "You throw Demonsalyer at the prick's back."
    "It pierces the scale armour and juts out of his chest."
    "He drops to his knees in a poll of blood, never to bother another woman again."
    hide prick with vpunch

    "Before you know it: the robed nerd has taken a freak arrow to the knee."
    "Suddenly a burst of arrows follow. Your only ally lays dying with several arrows to the neck and heart."
    "You have no weapons left and there is still a rope around your neck."

    hide kaz with hpunch

    "Everything goes black as the hunter tightens the rope."

    show vanderpool at center with hpunch

    "You begin to lose concisnous and wonder if you will ever again wake to see the sun rise."

    scene bg bad end

    "{b}The End{/b} -- {i}You died at the inn.{/i}"
    return


label part3_attack_the_hunter:

    "Pulling down on the rope with your free hand: you use swing your sword arm upwards and stab the hunter through the eye with Demonslayer."
    "Quickly the rope goes slack and you're on your feet again."
    "It is hard to breath and you feel like you will sound horrible for days but you are alive for the moment."

    "Another lightening bolt lashes out from the robed nerd's hand, catching the prick square in the chest."
    "This bolt was much stronger and he goes down."
    "As you retreive Demonslayer from his buddies face, a mysterious arrow zips past your ear, narrowly missing the nerd's knee as it sticks in the side of the Inn."
    "There is no more time to waste."

    jump part3_common


label part3_attack_the_prick:

    "You toss Demonslayer at the enemy's exposed back."
    "It pierces the scale plate armour and leaves him dropping dead in a pool of blood."
    "But there is still a rope around your neck and your only real weapon is now out of reach."
    "The robed nerd flabbergasted; he should just be glad he's not covered in blood."

    "You feel a trickle of blood down your back as the rope goes slack."
    "The hunter suddenly has an arrow sticking through his neck as he waddles off to die in the darkness."
    "Another burst of arrows and he is down for good. There is no more time to waste."

    jump part3_common


label part3_common:

    menu:
        "You decide to ..."

        "Run for the inn.":
            jump part4_run_for_the_inn
        "Run for the alley.":
            jump part4_run_for_the_alley
        "Improvise on the spot.":
            jump part4_improvise

