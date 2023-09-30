class Calc:
    first_line = {
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "purple": 7,
        "gray": 8,
        "white": 9,
    }


    second_line = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "purple": 7,
        "gray": 8,
        "white": 9,
    }

    third_line = {
        "black": 1,
        "brown": 10,
        "red": 100,
        "orange": 1000,
        "yellow": 10000,
        "green": 100000,
        "blue": 1000000,
        "purple": 10000000,
        "gray": 100000000,
        "white": 1000000000,
        "gold": 0.1,
        "silver": 0.01
    }

    forth_plus = {
        "gold": 1.05,
        "silver": 1.1,
        "null": 1.2,
    }

    forth_minus = {
        "gold": 0.95,
        "silver": 0.90,
        "null": 0.80,
    }

    def begin(self):
        mode = input("any text file to input y/n ?:")

        if mode == "n":
            self.one_by_one()
        elif mode == "y":
            self.filed()

    def filed(self):
        temp = open("input.txt", "r")
        f = temp.read().splitlines()

        for x in f:
            work_set = x.split("-")

            one = Calc.first_line[work_set[0]]
            two = Calc.second_line[work_set[1]]
            three = Calc.third_line[work_set[2]]
            four_max = Calc.forth_plus[work_set[3]]
            four_min = Calc.forth_minus[work_set[3]]

            maxi = (((one * 10) + two) * three) * four_max
            mini = (((one * 10) + two) * three) * four_min

            fo = open("output.txt", "a")
            fo.write(
                x + " = \n    max = {0:.3f}\n      min = {0:.3f}\n".format(maxi,
                                                                           mini))

    def one_by_one(self):
        input_str = input(
            "enter colors in order seperated by dash(-) :").lower()
        clr = input_str.split("-")
        print(clr)

        one = Calc.first_line[clr[0]]
        two = Calc.second_line[clr[1]]
        three = Calc.third_line[clr[2]]
        four_max = Calc.forth_plus[clr[3]]
        four_min = Calc.forth_minus[clr[3]]

        maxi = (((one * 10) + two) * three) * four_max
        mini = (((one * 10) + two) * three) * four_min
        print("max = {}, min = {}".format(maxi, mini))


if __name__ == "__main__":
    main = Calc()
    main.begin()
