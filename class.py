class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads


# Create some real monsters
fogthing = Monster("Black", 5)
mournsnake = Monster("Yellow", 4)
tangleface = Monster("Red", 3)

print("I Have " + str(fogthing.heads) + " heads and I'm " + fogthing.color)
print("I also have " + str(mournsnake.heads) + " heads and I'm " + mournsnake.color)
print("I got " + str(tangleface.heads) + " heads and I'm " + tangleface.color)
