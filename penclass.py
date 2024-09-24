class Pen:
    colour = "blue"
    cap = True
    ink = True
    grip = "good"
    
    def write(self):
        print("this pen writes well")

bic = Pen()
stabilo = Pen()
abc = Pen()

bic.write()
stabilo.write()
abc.write()

print(bic.grip)
print(stabilo.ink)
print(abc.colour)