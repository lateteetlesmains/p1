def on_forever():
    basic.show_string("" + str((input.temperature())))
    music.play_melody("- - - - - - - - ", 410)
basic.forever(on_forever)
