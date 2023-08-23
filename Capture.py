import csv


class Capture:

    fileNameWithExt = None
    species = []
    specie_options = {
        1: 'Tomato',
        2: 'Cabbage',
        3: 'Corn',
        4: 'Carrot',
        5: 'Hat dog',
        6: 'BBQ',
        7: 'Ham',
        8: 'Steak',
        9: 'Salad',
        10: 'Pizza',
    }

    def __init__(self):
        super().__init__()

    def run(self):
        self.print_species()
        self.get_species()
        self.get_winning()

    def get_species(self):
        get_species = input("Enter initial species: ")

        species = get_species.split()
        if len(species) < 9:
            print("Invalid number of species!")
            self.get_species()
        elif len(species) > 9:
            print("Enter maximum of 9 species only!")
            self.print_species()
            self.get_species()
        else:
            self.species = get_species.split()

    def get_winning(self):
        get_winning = input("Enter winning result: ")
        get_heat_specie = input("Enter heat item: ")

        if int(get_winning) > 10 or int(get_heat_specie) > 10:
            self.get_winning()

        self.normalize_species(get_winning, get_heat_specie)
        self.print_current_species()
        self.get_winning()

    def print_species(self):
        print("Species: ", "1 = Tomato, 2 = Cabbage, 3 = Corn, 4 Carrot, "
                           "5 = Hotdog, 6 = BBQ, 7 = Ham, 8 = Meat, 9 = Salad, 10 = Pizza")
        print("Example: 5 6 4 3 2 1 2 3 4; Also translated as: ",
              "Hotdog, BBQ, Carrot, Cabbage, Corn, Cabbage, Tomato, Cabbage, Corn, Carrot")

        print("Note: The 9th specie should be the current Hot item; Hot item frequently moves around.")

    def print_current_species(self):
        data = []
        for idx, i in enumerate(self.species):
            data.append(self.specie_options[int(i)])
        heat = data.copy().pop()
        del data[len(data) - 1]

        print("Running Winning Result: ", data)
        print("Running Heat: ", heat)

        return True

    def normalize_species(self, winning, heat):

        # Normalize previous data
        winning_line = self.species.copy()
        del winning_line[len(winning_line) - 1]
        winning_line.append(heat)
        winning_line.append(winning)
        self.save_result(winning_line)
        # ready for insert

        # normalize new data
        data = self.species.copy()
        del data[len(data) - 1]
        del data[len(data) - 1]
        data.insert(0, winning)
        data.append(heat)
        self.species = data
        self.print_species()

    def save_result(self, data):
        print("Saving...")
        # open the file in the write mode
        f = open(self.fileNameWithExt, 'a+')
        # create the csv wri ter
        writer = csv.writer(f)
        # write a row to the csv file
        # writer.writerow(['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9'])
        writer.writerow(data)
        # close the file
        f.close()


capture = Capture()
capture.fileNameWithExt = 'capture.csv'
capture.run()
