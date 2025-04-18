from pet import Pet

def main():
    my_pet = Pet("Yali")

#testing the methods
    my_pet.get_status()
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.get_status()

# # Other tests
    my_pet.train("happy jump")
    my_pet.train("obedience training")
    my_pet.show_tricks()


    my_pet.get_status()

if __name__ == "__main__":
    main()