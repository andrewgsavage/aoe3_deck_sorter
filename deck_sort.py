from ahk import AHK
import shutil
import xml.etree.ElementTree as ET
import time


# provide the path to the homecity xml you'd like to change
homecity = r"C:\Users\A\Games\Age of Empires 3 DE\76561198206085488\Savegame\sp_Spanish_homecity.xml"
# change the x, y positions below for your resolution. see https://pypi.org/project/ahk/ to get them
# you must be on the deck builder screen before running this.

ahk = AHK()

shutil.copyfile(homecity, "backup_homecity.xml")

tree = ET.parse('backup_homecity.xml')
root = tree.getroot()
unsorted_decks = [name.text for name in root.findall(".//deck/name")]
sorted_decks = sorted(unsorted_decks)

win = ahk.find_window(title=b'Age of Empires III: Definitive Edition')
win.activate() 

def select_deck(deck_name, unsorted_decks):
    ahk.mouse_move(x= 330, y=330) # first deck in list
    ahk.click()
    ahk.key_press("Home")
    deck_position = unsorted_decks.index(deck_name)
    for i in range(0,deck_position):
        ahk.key_press("Down")

def copy_deck(new_name):
    ahk.mouse_move(x= 620, y=1300) # copy button
    ahk.click()
    ahk.mouse_move(x= 1225, y=1036) # deck name input
    ahk.click()
    ahk.send_input(new_name)
    ahk.mouse_move(x= 1543, y=1174) # yes
    ahk.click()

def delete_deck():
    ahk.mouse_move(x= 330, y=1300) # delete button
    ahk.click()
    ahk.mouse_move(x= 1543, y=1174) # yes
    ahk.click()


for deck_name in sorted_decks:
    select_deck(deck_name, unsorted_decks)
    copy_deck("temp")
    select_deck(deck_name, unsorted_decks)
    delete_deck()
    select_deck(deck_name, unsorted_decks)
    ahk.key_press("End")
    copy_deck(deck_name)
    select_deck(deck_name, unsorted_decks)
    ahk.key_press("End")
    ahk.key_press("Up")
    delete_deck()
    unsorted_decks.pop(unsorted_decks.index(deck_name))
    time.sleep(1) 
    print(deck_name)