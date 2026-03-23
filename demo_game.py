import richeradventurelib as adv

adv.Room.items = adv.Bag()

current_room = starting_room = adv.Room("""
You are in a [bold white on black]dark[/] room.
""")

valley = starting_room.north = adv.Room("""
You are in a beautiful valley.
""")

magic_forest = valley.north = adv.Room("""
You are in a enchanted forest where magic grows wildly.
""")

mallet = adv.Item('rusty mallet', 'mallet')
valley.items = adv.Bag({mallet, })

inventory = adv.Bag()


@adv.when('north', direction='north')
@adv.when('south', direction='south')
@adv.when('east', direction='east')
@adv.when('west', direction='west')
def go(direction):
	global current_room
	room = current_room.exit(direction)
	if room:
		current_room = room
		adv.say('You go [italic]%s[/].' % direction)
		look()
		if room == magic_forest:
			adv.set_context('magic_aura')
		else:
			adv.set_context('default')


@adv.when('take ITEM')
def take(item):
	obj = current_room.items.take(item)
	if obj:
		adv.say('You pick up the [bold]%s[/].' % obj)
		inventory.add(obj)
	else:
		adv.say('There is no [bold]%s[/] here.' % item)


@adv.when('drop THING')
def drop(thing):
	obj = inventory.take(thing)
	if not obj:
		adv.say('You do not have a [bold]%s[/].' % thing)
	else:
		adv.say('You drop the [bold]%s[/].' % obj)
		current_room.items.add(obj)


@adv.when('look')
def look():
	adv.say(current_room)
	if current_room.items:
		for i in current_room.items:
			adv.say('A [bold]%s[/] is here.' % i)


@adv.when('inventory')
def show_inventory():
	adv.say('You have:')
	for thing in inventory:
		adv.say('A [bold]%s[/] is here.' % thing)


@adv.when('cast', context='magic_aura', magic=None)
@adv.when('cast MAGIC', context='magic_aura')
def cast(magic):
	if magic is None:
		adv.say("Which magic you would like to spell?")
	elif magic == 'fireball':
		adv.say("A :fire:[bold orange3]flaming Fireball[/]:fire: shoots from your hands!")


look()
adv.start()
