import csv
def print_options():
    print("Options: 1 = Tomato, 2 = Cabbage, 3 = Corn, 4 = Carrot, 5 = Hotdog, 6 = BBQ, 7 = Ham, 8 = Meat, 9 = Salad, 10 = Pizza")

def write_csv(row):
    # open the file in the write mode
    f = open('result.csv', 'a+')
    # create the csv wri ter
    writer = csv.writer(f)
    # write a row to the csv file
    writer.writerow(row)
    # close the file
    f.close()

def formatted_data(data, selected, heat):
    result = data.copy()
    result.append(heat)
    result.append(selected)
    return result

def func_options():
    options = {
        1: "Tomato",
        2: "Cabbage",
        3: "Corn",
        4: "Carrot",
        5: "Hotdog",
        6: "BBQ",
        7: "Ham",
        8: "Meat",
        9: "Salad",
        10: "Pizza"
    }

    return options

if __name__ == '__main__':
    results = []
    forWrite = []
    rounds = 0
    hot = 0
    x = None

    while True:
        print_options()
        select = input("Enter winning bet: ")

        if select == "":
            continue

        x = formatted_data(results, select, hot)
        results.insert(0, select)

        if len(results) > 8:
            # hot = input("Enter current heat: ")
            results.pop(len(results) - 1)
            write_csv(x)
            rounds = rounds + 1

        print("Round Count: ", rounds)
        # print(results)
        print(x)
        print("Last result: ", func_options().get(int(select)))
