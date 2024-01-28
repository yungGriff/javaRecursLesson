import time
import threading

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.alive = True
        self.lock = threading.Lock()

    def feed(self):
        with self.lock:
            if self.hunger < 90:
                self.hunger += 10
            else:
                print(f"{self.name} is too full!")

    def play(self):
        with self.lock:
            if self.energy > 10:
                self.energy -= 10
                self.hunger -= 5
            else:
                print(f"{self.name} is too tired!")

    def update_status(self):
        with self.lock:
            self.hunger -= 5
            self.energy -= 5
            if self.hunger <= 0 or self.energy <= 0:
                self.alive = False

    def display_status(self):
        with self.lock:
            print(f"{self.name}'s Status:")
            print(f"Hunger: {self.hunger}")
            print(f"Energy: {self.energy}")
            print("")

    def life_cycle(self):
        while self.alive:
            time.sleep(5)  # Adjust the interval as needed
            self.update_status()
            self.display_status()

# Function to interact with the pet
def interact(pet):
    while pet.alive:
        action = input("Choose an action (feed/play/exit): ").lower()
        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "exit":
            pet.alive = False
        else:
            print("Invalid action. Try again.")

if __name__ == "__main__":
    pet_name = input("Enter your virtual pet's name: ")
    my_pet = VirtualPet(pet_name)

    # Start a separate thread for the life cycle of the pet
    pet_thread = threading.Thread(target=my_pet.life_cycle)
    pet_thread.start()

    # Interact with the pet in the main thread
    interact(my_pet)

    # Wait for the pet's life cycle thread to finish before exiting
    pet_thread.join()
    print("Goodbye!")
