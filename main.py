class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, new_name):
        self.name = new_name
        new_name = "Peter"
        print(f"The Students change his name to {new_name}")

    def change_age(self, new_age):
        self.age = new_age
        new_age = 34 
        print(f"The Student change his age to {new_age}")

    def add_track (self, new_tracks):
        self.tracks = new_tracks
        new_tracks = ("UI/UX")
        print(f"The Student changed his track records to {new_tracks}")

    def get_score(self, new_score):
        self.score = new_score
        new_score = 2.5
        print(f"The student Changed his score to {new_score}")        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(2.5)
#print(f'Student Name:', Bob.change_name,'Bob.change_age', )