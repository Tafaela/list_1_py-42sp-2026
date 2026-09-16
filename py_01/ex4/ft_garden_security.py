class Plant:
    def __init__(self, name, height, old):
        self.name = name
        self._height = height
        self._age = old

    def show(self):
        print(f"Plant created {self.name}: {self._height}cm, {self._age} days old")
        if(self._height > 0 & self._age > 0):
            print(f"Height updated: {self._height}cm")
            print(f"Age updated: {self._age} days")
            print()
            print(f"Current state: {self.name}: {self._height}, {self._age} days old")
        elif(self._height <= 0 & self._age <= 0):
            print(f"{self.name}: Error, height can't be negative Height update rejected")
            print(f"{self.name}: Error, age can't be negative Age update rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 120)
    rose.show()
