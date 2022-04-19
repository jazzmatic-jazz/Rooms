from room import *

kitchen = Room("kitchen")
kitchen.set_description('A dank and dirty room buzzing with flies')

ballroom = Room('ballroom')
ballroom.set_description('A vast room with a shiny wooden floor; huge candlesticks guard the entrance')


dining = Room('dining')
dining.set_description('A large room with ornate golden decorations on each wall')

kitchen.link_room(dining, 'south')
dining.link_room(kitchen, 'north')
dining.link_room(ballroom, 'west')
ballroom.link_room(dining,'east' )

current = kitchen

while True:
    print('\n')
    current.get_details()
    command = input('> ')
    current = current.move(command)