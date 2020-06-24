# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character(" ")
define mcd = Character("[mcname]")
define unkna = Character("???")
define na = Character("Naomi")
define m = Character("Mom", what_color="#FFFFFF")
define m_shout = Character("Mom", what_color="#FFFFFF", what_size=34)
define n = Character(" ", italic=True, what_layout='subtitle')
define s = Character("Location")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    n "This game touches on sensitive topics."
    n "Are you comfortable with sad, melancholy, and/or depressing material?"

    menu:

        "Yes":
            jump gamestrt

        "No":
            jump perish

label perish:

    n "Alrighty then, I'll go ahead and close the game for you. Have a good day!"

    return

label gamestrt:
    scene city
    show protag at left
    show text "4:00 AM"
    with dissolve
    s "A quiet dorm, 20XX."
    mc "..."
label room:
    scene roomdrk
    with fade
    n "A faint light emanates from a nearby dresser"
    menu:
        "Investigate it":
            jump phone
        "Ignore":
            jump ignore1

label ignore1:
    mc "..."
    n "To your dismay, the phone begins buzzing violently."
label phone:
    scene rotamum
    with dissolve
    show text "7 missed calls"

    n "...from Mom?"
    n "You squint at the screen."

    menu:
        "Call her back":
            jump momcall
        "Wait until morning":
            jump momsleep

label momsleep:
    $ menu_flag = False
    n "You decided it would be best to call her back in the morning."
    jump d1
label momcall:
    $ menu_flag = True
    scene bedcallmom
    with dissolve

    n "You dialed her number."
    n "........"
    show vmom at center
    m "Hey sweetie, how are you?"

    menu:
        "Are you ok?!":
            jump c1
        "It's 4am.":
            jump t1
        "I'm fine, you?":
            jump r1

label c1:
    with vpunch
    m   "Are you?! You haven't called me since you moved,
        and I've been worried sick. Your father told me you'd be fine, but...I can't
        help worrying about my baby!"
jump mcon1
label t1:
    with vpunch
    m "It's never too early to check on family! And I knew you'd be awake, you always
        always stayed up late at home, and-..."
    show vmoms at right
    m "...well, I guess you aren't at home anymore, huh?"
    show vmomh at right
    m "I'm glad you're sleeping before the sun comes up, though. I'll
     try to wait until morning next time, if I can help it. A mother's
     concern is her son's annoyance, as I always say."
    n "You don't seem to recall that quote."
jump mcon1
label r1:
    show vmomr at right
    m "Oh, thank god!"
    m "I was so worried, you haven't called or anything since you moved out there. Remember,
        if you need anything you can call me anytime."
jump mcon1
label mcon1:
    m "By the way, don't you start that job tomorrow?"
    menu:
        "Uh, sure?":
            jump mend1
        "Not in this economy.":
            jump mcon1b
        "I have a job?":
            jump mcon1b
label mcon1b:
    show vmomp at center
    with move
    m "It's part of your work studies, remember? See, I have it on my calender right
        here...oh, uhh...I'll just send it to you."
    n "Received screenshot of Mom's calender!"
    show vmomp at right
    with move
    show calmess at center
    m "See? I don't know what you'd do without me looking after you."
label mend1:
    scene roomdrk
    show vmomh
    m "Once you get there, you'll love it! The sweet smell of strangers, the cold, dusty floors, the ever-ticking clocks!
    They're magical! At least, that's how I felt my first few days."
    m "Your father, on the other hand..."
    show vmoms
    m "He isn't as fond of the workplace as I am."
    show vmomh
    m "Well, anyways, go ahead and get some rest. Good luck, love you!"
    n "....."
    n "She hung up the phone."
label d1:
    show text "Early Morning"
    scene roomday
    with fade
    if menu_flag:
        n "You recall that your first shift is today."
        n "After getting dressed, you head towards the address from Mom's calendar."

    else:
        n "The windows in your room are foggy"
        n "You see a few texts from your mom. Although they're difficult to understand, they say something about work-studies and a job."
        n "School starts soon, so you head there."
label school:
    scene sd
    show text "Morning"
    mc "Is this...?"
    s "Amity University"
    n "You see a girl staring at the gate."
    unkna "I see..."
    show Naomishocked
    unkna "..!"
    show Naomir
    unkna "...oh, hi. Do you know where the library is?"
    unkna "I, uh, have work-studies there."
    mc "(So this must be what mom was talking about...)"
    menu:
        "You too?":
            jump na_meet
        "We're working at a library?":
            jump na_meet
label na_meet:
    show Naomi
    na "Oh, so you're taking work-studies too? I hadn't expected to meet a coworker so soon.
        Well then, uh, m-my name's Naomi."
    $ amicuslvl_na = 0
    na "..."
    na "..."
    na "And yours is..?"
python:
    mcname = renpy.input("Oh, my name is...")
    mcname = mcname.strip()

    if not mcname:
        mcname = "Geno"

show Naomip
na "[mcname]? Have we..?"
mcname "?"
show Naomir
na "Nevermind."
if menu_flag:
    show Naomistudy
    na "So anyways...why are you wearing those formal clothes? We don't start work until tomorrow."
    na "Is this your style? Or did you come here with the intent to start today?"
    n "It seems like mom wrote down the wrong date."
    n "You inspect the calendar."
    show calmess
    na "What the hell is that?"
    na "Are your clothes compensation for your unkemptness..?!"
    show Naomiblush
    na "S-sorry, I shouldn't be looking over your shoulder. But if you're struggling this
    much with organization, take this. I don't want you to sleep in and get fired."
    show Naomih
    na "..and I don't want to cover your shifts."
    n "She motions you to hand over your phone."
    n "Received Naomi's phone number!"
    $ amicuslvl_na += 1
    n "You have forged a bond with the Hermit!"
    jump search1

else:
    na "Have you been here before? This is my first time in Amity, so I've been looking for a guide."
    na "Are you new here too?"
    menu:
        "No":
            jump lie1
        "Yes":
            jump truth1

label lie1:
    show Naomistudy
    na "Oh..? {size=-10}You didn't even know where the library was.."
    na "I hope you aren't lying to impress me...I'm not stupid."
    na "If you don't know something, just be honest. No one has all the answers, yknow?"
    jump search1

label truth1:
    show Naomi
    na "Well...in that case, give me your phone."
    mcname "?!"
    show Naomiblush
    na "O-oh, sorry! I just want to put my number in, that's all."
    n "Received Naomi's phone number!"
    $ amicuslvl_na += 1
    n "You have forged a bond with the Hermit!"
    jump search1

label search1:
    na "So, uhm, do you...want to look around with me?"
    na "I'm new here, and you are too, right? So it'd be in our best interests to find our way around together.
        Especially if we need to go pick stuff up for the library or whatever."
    if amicuslvl_na is 0:
        na "Just...be honest with me from here on out, please. I wanna trust my coworkers, at least."
        n "You nod sheepishly."
        show Naomih
        na "Thanks. I don't have a very good history with liars, so...I'm sorry if I went overboard.
            As long as you keep your promise, I forgive you."
        $ debeo = 1
        n "On account of your own free will, you have become indebted to Naomi. If
              you wish to resolve your dues, heed thy debtor's whims."
        na "I'm not good at navigation, so I'll leave that to you, [mcname]. I-if that's alright with you..."
        n "It doesn't seem like you have an option.."
        jump searchstrt1

    else:
        na "I'm not good at navigation, so I'll leave that to you, [mcname]. I-if that's alright with you..."
        n "Out of the kindness of your heart, you take the lead."
        jump searchstrt1

label searchstrt1:
    show Naomih
    na "So..which direction should we go?"
    menu:
        "North":
            na "Alright, l-let's go then."
        "South":
            na "That can't be it, we entered that way."
        "East":
            na "Alright, l-let's go then."
        "West":
            na "Alright, l-let's go then."
return
    # This ends the game.
