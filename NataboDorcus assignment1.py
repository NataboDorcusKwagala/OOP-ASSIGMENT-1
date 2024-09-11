# Class representing different types of animals
class Animals:
    def __init__(self, species, sound):
        # Initializing the species and sound attributes
        self.species = species
        self.sound = sound

    # Method to display the sound the animal makes
    def make_sound(self):
        print(f"This is a {self.species}. It makes a '{self.sound}' sound.")

# Creating an instance of the Animals class for a Dog
dog = Animals("Dog", "Bark")
dog.make_sound()  # Output the sound of the Dog

# Creating an instance of the Animals class for a Cat
cat = Animals("Cat", "Meow")
cat.make_sound()  # Output the sound of the Cat



# Class representing different books
class Books:
    def __init__(self, title, author):
        # Initializing the title and author attributes
        self.title = title
        self.author = author

    # Method to display book information
    def book_info(self):
        print(f"'{self.title}' is written by {self.author}.")

# Creating an instance of the Books class for "Gifted Hands"
gifted_hands = Books("Gifted Hands", "Dr. Benjamin Carson")
gifted_hands.book_info()  # Display information about "Gifted Hands"

# Creating an instance of the Books class for "How to Pray"
how_to_pray = Books("How to Pray", "C.S. Lewis")
how_to_pray.book_info()  # Display information about "How to Pray"



# Class representing different movies
class Movies:
    def __init__(self, title, director):
        # Initializing the title and director attributes
        self.title = title
        self.director = director

    # Method to display movie information
    def movie_info(self):
        print(f"The movie '{self.title}' is directed by {self.director}.")

# Creating an instance of the Movies class for "War Room"
war_room = Movies("War Room", "Alex Kendrick")
war_room.movie_info()  # Display information about "War Room"

# Creating an instance of the Movies class for "Breakthrough"
breakthrough = Movies("Breakthrough", "Roxann Dawson")
breakthrough.movie_info()  # Display information about "Breakthrough"



# Class representing different cars
class Cars:
    def __init__(self, brand, price):
        # Initializing the brand and price attributes
        self.brand = brand
        self.price = price

    # Method to display car information
    def car_info(self):
        print(f"This is a {self.brand}. Its price is {self.price}.")

# Creating an instance of the Cars class for a Benz SUV
benz_suv = Cars("Benz SUV", "70,000 USD")
benz_suv.car_info()  # Display information about the Benz SUV

# Creating an instance of the Cars class for a Honda Fit
honda_fit = Cars("Honda Fit", "18,000 USD")
honda_fit.car_info()  # Display information about the Honda Fit



# Class representing different students and their majors
class Students:
    def __init__(self, name, major):
        # Initializing the name and major attributes
        self.name = name
        self.major = major

    # Method to display student information
    def student_info(self):
        print(f"{self.name} is majoring in {self.major}.")

# Creating an instance of the Students class for Atim Sarah
atim_sarah = Students("Atim Sarah", "Data Science")
atim_sarah.student_info()  # Display information about Atim Sarah

# Creating an instance of the Students class for Magezi Sam
magezi_sam = Students("Magezi Sam", "Computer Science")
magezi_sam.student_info()  # Display information about Magezi Sam
