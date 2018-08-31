
label part5_charge_the_ninja:

    "Hopefully your cuirass is up to the challenge and the ninja doesn't aim for your face or knees."
    "You raise Demonslayer to an attack position and charge forward: shouting like a maniac."

    jump part5_common

label part5_run_like_hell:
    scene bg inn roof

    launa "RRRRUUUUNNNNNN!!!!!!"
    "You take off in the opposite direction"

    jump part5_common

label part5_common:
    scene bg inn roof
    hide yukari with fade
    show kaz at offscreenleft with moveinleft

    "Unfortunately the house keeper didn't repair their rooftop very often and your steel plate weighs you down."
    "The roof gives way and you fall."
    show cg launa falling
    "The robbed Nerd grabs your hand and ends up laying prone: holding you by one forearm as your sword arm dangles by your side."

    "Nerd" "Hey Ninja, help me!"

    "You look down and it turns out that it isn't a normal room below."
    "You see a two story drop onto a glass table."
    "Falling isn't looking so good for your health."
    "But why would the Ninja help either of you?"

    scene bg inn roof

    "Ninja" "If she sheathes that blade then I'll help."

    "Before you know it the ninja woman has your other hand and along with the nerd: they haul you back onto the roof top."

    show yukari at center with dissolve
    show kaz at right with dissolve

    launa "Wait, what the heck is happening here?"
    "Nerd" "Yeah? Weren't you trying to kill us?"
    "The Nerd stares curiously."

    "Ninja" "No, I was aiming for the men at the Inn."
    "Ninja" "Well, I did almost shoot Mr. Mage but that was an accident."

    "The three of you decide to introduce yourselves."

    "Ninja" "My name is Anko Yukari. For my people our family name comes first."
    "Nerd" "Zum Kaz. We're backwards from you islanders of the east."
    launa "Launa, just Launa. I'd say nice to meet you all but what the hell is going on?"

    "Zum Kaz, nerd extraordinare and mage speaks up first."

    zum "In my case, I just figured Launa could use a hand at the bar. Those bastards were real pricks."
    launa "And as for me, I just wanted a drink and a nap before moving on."
    launa "Instead I got hit on at the bar and it snowballed."
    yukari "Curious, very curious indeed."

    show yukari crossarmed at center with fade

    "Yukari crosses her arms and continues."

    yukari "I came here on a mission seeking The Island of Divine Wind."
    yukari "A merchant swindled the local ruler the last time the island came overhead."
    yukari "He contracted The Third Order to assassinate the merchant in revenge, and my family was assigned to carry it out."
    yukari "Asking around about the island's current whereabouts: I heard of a blonde sword maiden who also seeks this drifting island."
    launa "{i}Heh. Is that what they're calling me around here?{/i}"
    yukari "By the time that I reached the inn: there were scarcely few women matching any of the descriptions I had been given."

    "Kaz rubs his head in confusion."

    zum "What a coincidence."
    zum "I've been seeking this floating island as well; we simply call it Breeze."
    zum "My order has been researching its movements for years now but I was the first to set out to actually find it."
    zum "Everyone else was too afraid of the fabled Guardians of Breeze."

    "{i}You look from Kaz to Yukari and smile.{/i}"
    "The party is formed and the real quest lay ahead."

    show yukari at left
    show kaz at right

    launa "Well, in my case: I heard there would be fine treasure. Problem is I don't really know where Breeze happens to be right this moment."

    menu:
        "Thus I ..."

        "Ask the Mage.":
            jump part6_ask_mage
        "Ask the Ninja.":
            jump part6_ask_ninja
