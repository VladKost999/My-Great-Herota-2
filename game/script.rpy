# Определение персонажей игры.

define m = Character('Mорж', color="#6e3296", image="gg")
define t = Character('ТумбаЮмба', color="#cc5353", image="tumba")
define s = Character('Палка Палка Огуречек', color="#a48df5", image="sman")
define k = Character('Кирпич', color="#ffffff", image="brick")
define z = Character('Зонт', color="#ffffff", image="zont")

define pu_zont = False

init:
    $ MyRight = Position(xalign=0.8)
    $ MyLeft = Position(xalign=0.2)
    

label start:
    with dissolve

    "Конец"

    scene black
    with dissolve

    "И новое начало..."

    scene room and bed

    "Жил был Палка Палка Огуречек, как то утром он решил проснуться."

    scene wake

    "Он медленно встал..."

    scene window

    "Подошел к окну и решил поговорить с тумбочкой"

    scene room with dissolve
    show sman happy at MyRight with dissolve
    
    show tumba:
        xalign 0.0 yalign 0.9
    with dissolve
    t "Здравствуй, хозяен"
    s happy "Здравтвуй, Тумьочка"

    s angry "Так, а почему на тебе так много пыли????"

    show tumba:
        xalign 0.0 yalign 0.9
    t pot "Видит бог, я этого не хотель"
    
    hide tumba with moveoutleft
    scene roomwithouttumba with dissolve
    show sman sad

    "Не выдержав позора, тумба скрылась"
    show zont:
        xalign 0.0
    with dissolve
    menu:
        "Но уходя, она выронила зонтик, подобрать?"

        "Да, конечно!":
            $ pu_zont = True
        "Нет, не нужен.":
            pass
    hide zont


    s "Эх{w}.{w}.{w}.{w}."
    show sman happy
    extend " Ладно"

    menu:
        "Но чем же заняться теперь?"
        "Пойти поспать":
            jump GoSleep
        "Пойти прогуляться":
            jump GoOutside
    hide sman
    return

label GoOutside:
    scene roomwin with fade

    "Так как у ППО не было двери, он вышел через окно."

    scene les_and_tuman with dissolve
    show sman happy with dissolve

    "Идет идет себе по туманному лесу, весь счастливый"
    "И вдруг, откуда не возьмись ..."

    show sman happy at MyRight with dissolve
    show brick angry at MyLeft with dissolve

    k angry "Здарова, поц, сигары не найдется?"

    menu:
        "Что же теперь делать? ППО в беде!"
        "В АТАКУУУ!!!!":
            jump attack_brick
        "БЕЖАТБ!!!!!":
            jump run
    hide sman
    hide brick
    return

label GoSleep:
    scene sleeeeeeeep with dissolve
    "Наш главный герой ушел спать, забыл о нужде в еде и умер."
    jump bad_end

label run:
    scene brick_death with fade
    "ППО был быстр, но Кирпич оказался быстрее"
    jump bad_end

label attack_brick:
    hide brick with dissolve
    show sman kill brick at center
    "Быстро подумав ППО ломает Кирпича и продолжает свою путь дорогу!"
    hide sman
    jump end_line

label bad_end:
    scene theend with dissolve
    "Конец"
    return

label end_line:
    scene rain
    "И внезапно начался раиоактивный дождь."
    menu:
        "И что же ППО делать?"

        "Смириться с этим и принять мучительную смерть.":
            hide sman
            scene sman_die
            "ППО прожил хорошую жизнь, как ему казалось. И вот его жизь была прервана отравлением и другими прелестями радиоактивного дождя."
            jump bad_end
        "Попытаться добежать до дома.":
            hide sman
            scene rain_die1
            "Бежит{w}.{w}.{w}."
            scene rain_die2
            "Бежит{w}.{w}.{w}."
            scene die_with_rain
            "Но к превеликому сожалению, ППО не успел добежать до лекарств и умир."
            jump bad_end
        "Достать зонтик и пойти домой." if pu_zont:
            hide sman
            jump final

label final:
    scene rain_zont
    "Шел шел, как ни в чем не бывало, да дошел до дома своего!"
    scene room and bed
    "И вот, нарадовавшись благополучной прогулкой, ППО лег спать после такого трудного дня!"
    menu:
        "Просыпаться на следующий день?"
        "Да!":
            jump start
        "Нет":
            jump thank_you

label thank_you:
    scene tu
    "Спасибо за играние!"
