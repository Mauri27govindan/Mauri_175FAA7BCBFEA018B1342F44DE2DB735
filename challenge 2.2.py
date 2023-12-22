# Define the base class Player
class Player:
    def play(self):
        print("The player is playing cricket.")

# Derive the Batsman class from Player
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Derive the Bowler class from Player
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of both Batsman and Bowler classes and call their play() methods
if __name__ == "__main__":
    batsman = Batsman()
    bowler = Bowler()

    batsman.play()  # Output: The batsman is batting.
    bowler.play()   # Output: The bowler is bowling.
