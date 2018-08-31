label part4_run_for_the_inn:
    scene bg inn

    "You grab the robbed Nerd's hand and book it for the inn. Bursting inside you head for the bar."

    launa "Is there a back exit?"
    show innkeeper surprised
    ik "Yeah, it's in the back!"

    "You leap over the bar, dragging the flabbergasted nerd in your wake."

    scene bg storeroom
    "Slamming the back door open you find yourself in a broom closet."
    "There are boxes piled everywhere and a couple kegs of alcohol stacked."

    launa "Screw it then. Let's hide!"

    "Together you quickly shuffle boxes around but there is no room to squeeze yourself between boxes and walls."
    "Luckily, you find a ladder behind a stack of boxes."
    "You climb up to the roof."

    jump part4_common

label part4_run_for_the_alley:
    scene bg alley

    "You grab the robbed Nerd's hand and book it for the alley. The alleyway is dark and narrow. You run."

    show kaz at left with dissolve

    "Nerd" "Hey, shouldn't I be in front?"
    launa "Not unless you can conjure up plate armour!"

    hide kaz
    "Nerd probably means well but push comes to shove: your steel cuirass will hold off arrows a lot better than his sweaty old robes."

    launa "{i}A magical barrier or whirlwind spell would be damned handy about now.{/i}"

    "Seeing some boxes stacked by a short wall, you let go of the Nerd's hand, climb and jump up."
    "Pulling yourself up to the roof: you stop to help Nerd up."
    "He's probably spent his days in libraries and arcane rituals; you spent your days with a sword as often as you could."
    "You're a far more athletic warrior type but can't use magic like the Nerd."

    jump part4_common

label part4_improvise:

    launa "Hey Archer, hold up!"
    "You shout as loud as you can."
    launa "Let's have the traditional pre-fight mead and settle this with fists!"

    "You gesture towards the inn."

    "{i}Your only answer is a cluster of arrows at your feet{/i}"

    launa "Oh well, that went sour."

    jump part4_run_for_the_alley

label part4_common:

    scene bg inn roof

    "The inn's rooftop offers you a drastic change in position but no safety from what arrows may fly."

    show kaz at right

    "You and the nerd run and leap roof top to roof top."

    show kaz at left with moveinright

    "Fortunately you grew up rambunctious and the roof tops are close enough together that the Nerd manages without falling."

    "Ahead of you appears a short woman with jet black hair."

    show yukari ninja at right with dissolve

    "A small assassin's sized bow in hand, a sword jutting over one of her shoulders and a quiver of arrows over the over."
    "Her red jumpsuit obviously has several weapons. She's clearly armed to the teeth."

    show kaz at left

    "You've got a shiny steel cuirass glinting in the moonlight, your trusty sword demon slayer, and a mage that obviously knows lighting bolt."

    menu:
        "It's time to decide."

        "Charge the ninja!":
            jump part5_charge_the_ninja
        "Run like hell!":
            jump part5_run_like_hell

