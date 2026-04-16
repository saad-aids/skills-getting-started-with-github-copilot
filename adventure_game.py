import time

class AdventureGame:
    def __init__(self):
        self.running = True

    def start(self):
        print("Welcome to the Adventure Game!")
        self.play()

    def play(self):
        while self.running:
            print("\nYou find yourself in a mysterious forest.")
            print("What do you want to do?")
            print("1. Go deeper into the forest")
            print("2. Climb a tree to get a better view")
            choice = input("Enter 1 or 2: ")

            if choice == '1':
                self.forest_path()
            elif choice == '2':
                self.tree_path()
            else:
                print("Invalid choice, please try again.")

    def forest_path(self):
        print("\nYou venture deeper into the forest.")
        print("You come across a river.")
        print("1. Swim across")
        print("2. Follow the river downstream")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            print("\nYou bravely swim across the river but get swept away by a current. Game over!")
        elif choice == '2':
            print("\nYou safely follow the river and find a hidden cave.")
            self.cave_path()
        else:
            print("Invalid choice, please return to the previous step.")
            self.play()

    def tree_path(self):
        print("\nYou climb the tree and spot a clearing in the distance.")
        print("1. Climb down and head towards the clearing")
        print("2. Stay in the tree and look around")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            print("\nYou walk towards the clearing and find a friendly village.")
            print("You have completed your adventure in safety!")
        elif choice == '2':
            print("\nWhile looking around, a bird surprises you and you fall. Game over!")
        else:
            print("Invalid choice, please return to the previous step.")
            self.play()

    def cave_path(self):
        print("\nInside the cave, you find treasures!")
        print("1. Take the treasure and leave the cave")
        print("2. Explore deeper")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            print("\nYou take the treasure but a cave-in occurs. Game over!")
        elif choice == '2':
            print("\nYou discover a hidden passage that leads to a secret treasure! You win!")
        else:
            print("Invalid choice, please return to the previous step.")
            self.play()

if __name__ == '__main__':
    game = AdventureGame()
    game.start()