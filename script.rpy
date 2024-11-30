
define e = Character('Shiramatsu', color="#cc34eb")
define en = Character('Enden', color="#cc34eb")
define n = Character('', color="#cc34eb")

default choix_debloque = False
label start:


    play music "audio/chillbreeze.ogg" volume 0.5

    scene maison:
        size(1920, 1080)
    show neutre at center:
        size(720, 1280)
    e "Salut mochi"
    e "Alors il voici des exemple de choix tu pourras implanté dans ton jeu "
    n "Toc toc"
    e "Entré c'est ouvert."
    show neutre at left
    with move
    show enden_joy at center:
        size(720, 1100)
    with dissolve
    en "Bonjour shira."
    en "Comment vas tu ?"
    e "Oh euh eh bien je vais..."

menu:

    "oui je vais bien":
        jump vas_bien

    "non je ne vais pas bien":
        jump vas_pas_bien


    "tu fait quoi ici ?":
        jump fait_quoi_ici





return

















label fait_quoi_ici:

return
