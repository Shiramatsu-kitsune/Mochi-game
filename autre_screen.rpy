screen route_choice():
    tag menu
    window:
        style "gm_root"
        vbox:
            text "Choisissez votre route :"
            null height 20

            # Option pour choisir la route "École"
            imagebutton idle "gui/school_idle.jpg" hover "gui/school_hover.jpg" action [SetVariable("route", "school"), Start("school_route")]
            # Option pour choisir la route "Maison"

            # Espacement entre les boutons
            null height 20

            # Image bouton pour "Rester à la maison" - Taille 300x75
            imagebutton idle "gui/home_idle.jpg" hover "gui/home_hover.jpg" action [SetVariable("route", "home"), Start("home_route")]

            # Retour au menu principal
            textbutton "Retour au menu principal" action Return()
