class MapElement:
    pass
class Leaf(MapElement):
    pass

class Wall(MapElement):
    pass

class Door(MapElement):
    def __init__(self, room1=None, room2=None):
        self.room1 = room1
        self.room2 = room2

class Container(MapElement):
    def __init__(self):
        self.Children = []
    
    def addChild(self, child):
        self.Children.append(child)
        
    def removeChild(self, child):
        self.Children.remove(child)



class Room(Container):
    def __init__(self):
        self.north = Wall()
        self.east = Wall()
        self.south = Wall()
        self.west = Wall()

class Maze(Container):
    def __init__(self):
        super().__init__()
        
    def addRoom(self, room):
        self.addChild(room)


maze = Maze()
room1 = Room()
room2 = Room()

maze.addRoom(room1)
maze.addRoom(room2)

door = Door(room1, room2)
