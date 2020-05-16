from tkinter import *
from tkinter import ttk
import random
import json
from game import Game

root = Tk()
root.geometry("800x400")
root.title("Hangman_Tkinter by Mecke")
root.resizable(0, 0)

g = Game()


def get_setting(option):

    with open("settings.json", "r") as s:
        settings = json.load(s)

        language = settings["Settings"]["Language"]
        tries = settings["Settings"]["Tries"]
        ui = settings["UI"][language]
        langs = settings["Languages"]

    s.close()

    options =   {
                    "language"  : language,
                    "tries"     : tries,
                    "ui"        : ui,
                    "langs"     : langs
                }

    return options[option]


def set_settings(options):

    with open("settings.json", "a") as s:
        settings = json.load(s)

        lang = settings["Settings"]["Language"]
        ui = settings["UI"][lang]

        root.title(ui["Main"]["Title"])

    s.close()


def settings_menu():

    setting = Tk()
    setting.geometry("300x200")
    setting.title("Settings")

    langs = get_setting("langs")

    l = []
    for key in langs.keys():
        l.append(key)
    
    lang_list = ttk.Combobox(setting, values=l).pack(anchor="nw")


btn_settings = Button(root, text="Settings", command=settings_menu).pack(anchor="nw")


root.mainloop()