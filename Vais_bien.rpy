label vas_bien:
    e "Je vais bien merci"
    en "J'avais un service a te demander tu peux venir avec moi au temple ?"
    e "Bien sûr je te suis"
    hide enden_joy
    with dissolve
    hide neutre
    with dissolve
    scene temple:
        size(1920, 1080)
    with dissolve
    show neutre
    with dissolve
    e "Nous voila arriver"
    show neutre at left
    with move
    show eden_neutre at center:
        size(720, 1100)
    with dissolve
    en "Oui bon tu m'aider a nettoyer le temple ?"
    e "Bon ok"
    scene black
    n "Shiramatsu et enden nettoie le temple puis rentre chez shira"
    scene maison:
        size(1920, 1080)
    with None
    show eden_neutre at right with moveinright:
        size(720, 1100)
    with dissolve
    en "enfin terminer ! j'ai faim !"
    show eden_neutre at left with move
    en "Shiraaaa j'ai faim !!!"

    show angry_h at right with moveinright
    e "C'est bon ça va !"
    e "Attends moi la je vais te preparé a manger"
    hide angry_h with moveoutright
    en "Merci"
    scene maison02 with wipeleft:
        size(1920, 1080)
    show neutre at right with moveinright
    e "Qu'est ce que je vais lui preparer ?"

menu:
        "Pâte carbo":
            "Tu cherche la recette."
            jump pate_carbo

        "Autre plat (verrouillée)" if not choix_debloque:
            "Cette option est verrouillée pour le moment."

menu:
        "Steak frite ":
            $ choix_debloque = True
            "L'option cachée est maintenant débloquée !"


label cuisine:
menu:
            "Steak frite (débloquée)" if choix_debloque:
                n "Se sera Steak frite"



label pate_carbo:
    e "Bon ça sera des pâte carbonara, allons preparons cela !"
    scene black
    with dissolve
    play sound "Cooking_Succes_Sound_Effect.mp3"
    pause 7
scene maison:
    size(1920, 1080)
with None
show neutre at right with moveinright
e "Enden ! c'est prêt"
en "Euh oui...oui !"


with hpunch
"{size=50}{b}Bruit de fracas...{/b}{/size}"

show eden_naturel at left with moveinleft:
    size(720, 1100)
en "Merci shira !"
e "Je peux savoir ce que tu faissait vers les chambre ?"
en "J'était au wc..."
e "Mmmh bien sûr j'espere que tu t'est lavé les mains."
e "Bref tien..."
show carbonara at center:
    size(720, 1280)
pause 2
hide carbonara
window hide
"{b}Bonne appétit !{/b}"
window show
scene black
with dissolve
window hide
"{b}A suivre{/b}"
window show
return
