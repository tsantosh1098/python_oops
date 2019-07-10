class animal:
    pass

class human(animal):
    pass
        
class fish(human):
    def __init__(self):
        super().move()
    def move(self):
        print("fish")



p2=fish()


