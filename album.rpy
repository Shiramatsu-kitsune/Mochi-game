init python:
    gallery = Gallery()

    gallery.button("red")
    gallery.image("jour")
    gallery.unlock("jour")

    gallery.button("blue")
    gallery.image("nuit")

    gallery.button("orange")
    gallery.image("apres_midi")



screen album:
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30

    grid 2 2:
        add gallery.make_button(name="orange", unlocked="image/petit/petit_apres_midi.jpg")
        add gallery.make_button(name="blue", unlocked="image/petit/petit_nuit.jpg")
        add gallery.make_button(name="red", unlocked="image/petit/petit_jour.jpg",locked="GSs/small/locked.jpg")
        spacing 15
    textbutton "Return" action Return()