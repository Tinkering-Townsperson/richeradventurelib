# RicherAdventureLib

[`adventurelib`](https://github.com/lordmauve/adventurelib) provides basic functionality for writing text-based adventure
games, with the aim of making it easy enough for young teenagers to do.

`richeradventurelib` expands upon this by allowing programmers to implement colours and styles into their games using the [`rich` library](https://rich.readthedocs.io/)

Use bbcode-like syntax in your games (`[bold italic orange3 on blue]You are in the bedroom[/]`) and even add emojis (`:fire: You cast fireball :fire:`)!

The foundation of adventurelib is the ability to define functions that are
called in response to commands. For example, you could write a function to
be called when the user types commands like "take hat":

```py
@when('take THING')
def take(thing):
	print(f'You take the {thing}.')
	inventory.append(thing)
```

It also includes the foundations needed to write games involving rooms, items,
characters and more... but users will have to implement these features for
themselves as they explore Python programming concepts.
