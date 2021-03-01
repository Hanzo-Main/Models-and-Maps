# Course: CS 30
# Period: 1
# Date created: 21/01/28
# Date last modified: 21/02/04
# Name: Kira Gray
# Description: RPG nested dictionary for characters, locations, and inventory.

# a nested dictionary of locations in the game
locations = {
  'cargo_left': {
    'size': 'large',
    'apperence': 'many crates are piled high',
    'next_places': """there is more cargo on the right and a latter going up on the left
    """
  },
  'cargo_right': {
    'size': 'large',
    'apperence': """more cargo containers""",
    'next_places': """theres a door to the right and the other side of the cargo hold on the left
    """
  },
  # may not be in the final cut
  'hypdriv_room': {
    'size': 'tiny',
    'apperence': """the hyperdrive, with two pirates""",
    'next_places': 'the only way is to the cargo hold on the left'
  },
  'crew_quarts': {
    'size': 'small',
    'apperence': """there is a table and beds. There are two pirates""",
    'next_places': 'the only way is right to the latter going down',
  },
  'living_area': {
    'size': 'medium',
    'apperence': """typical living arrangements. There are three pirates""",
    'next_places': """the latter going down to the cargo is on the left and
    a latter going up on the right""",
  },
  # may not be in the final cut
  'caps_quarts': {
    'size': 'small',
    'apperence': """normal single bedroom, with a crate against the bed""",
    'next_places': """the only way is to the right to the latter going to the
    living area""",
  },
  'locked_room': {
    'size': 'tiny',
    'apperence': """nothing in it, it's just a room leading to the cockpit""",
    'next_places': """the latter going to the living area is on the left and the
    cockpit is to the right""",
  },
  'cockpit': {
    'size': 'medium',
    'apperence': 'three pirates and the captain, everything else is normal',
    'next_places': 'the only way is to the left back to the small room'
  }
}
# a nested dictionary of characters in the game and information on them.
characters = {
  'player': {
    'descr': 'the character you play as',
    'dmg': '50',
    'health': '100'
  },
# I imagine im going to have to make multiple clones of this guy, but for now
# im sticking with only writing the one. 8 for sure, 10 if i keep the hyperdrive room.
  'pirate': {
    'descr': 'a basic pirate gumby',
    'dmg': '25',
    'health': '50'
  },
  'captain': {
    'descr': 'the pirate captain, the one calling the shots',
    'dmg': '50',
    'health': '150'
  }
}
