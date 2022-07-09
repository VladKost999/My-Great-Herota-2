# Определение персонажей игры.

define m = Character('Mорж', color="#6e3296", image="gg")
define t = Character('ТумбаЮмба', color="#ffffff", image="tumba")
define s = Character('Палка Палка Огуречек', color="#ffffff", image="sman")
define k = Character('Кирпич', color="#ffffff", image="brick")

init:
    $ MyLeft = Position(xalign=0.8)
    $ MyRight = Position(xalign=0.2)
    

label start:
    scene ocean
    show gg
    with dissolve

    m "Свинка убита!!!!"

    hide gg
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
    show sman happy at MyLeft with dissolve
    
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

    show sman happy at MyLeft with dissolve
    show brick angry at MyRight with dissolve

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
    scene theend with dissolve
    "Конец"
    return

label bad_end:
    scene theend with dissolve
    "Конец"
    return   