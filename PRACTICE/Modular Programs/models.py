#Here Lie Definitions 

class Kitten():
    def __init__(self,name,age,weight,hunger,thirst,emotion):
        self.name = name
        self.age = age
        self.weight = weight
        self.hunger = hunger
        self.thirst = thirst
        self.emotion = emotion

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "weight": self.weight,
            "hunger": self.hunger,
            "thirst": self.thirst,
            "emotion": self.emotion
        }  
    
    def stats(self):
        print(f"Name:  {self.name} | Age: {self.age} | Weight: {self.weight} | Thirst: {self.thirst} | Emotion: {self.emotion}")
        print("*" * 50)

    def feed(self):
        self.weight += 20
        self.hunger -= 20
        self.emotion = "Happy"    
        if self.hunger < 0:
            self.hunger = 0
        print("Nom Nom Nom")    

    def play(self):
        if self.hunger > 40:
            print(f"\n {self.name} refuses to play. Too Hungry!")
        else:
            self.hunger += 20
            self.emotion = "Ecstatic"        
