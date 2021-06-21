import csv
import sys
import random

if len(sys.argv) < 4:
    print("ERROR: Not enough arguments")
    sys.exit(-1)

random.seed(51307)
ril = []
nal = []
mgl = []
all = []
sil = []
kl = []
cal = []
bal = []
fel = []

def maptoval(value, val_list):
    ind = 0
    for i, val in enumerate(val_list):
        ind = i
        if val == value:
            return str(i)
    val_list.append(value)
    return str(ind)

filename = sys.argv[1]
trainName = sys.argv[2]
testName = sys.argv[3]
with open(filename, "r") as f:
    with open(trainName, "w") as train:
        with open(testName, "w") as test:
            train.write("% Train database")
            train.write("@RELATION Train")
            test.write("% Test database")
            test.write("@RELATION Test")
            for file in [train, test]:
                file.write("")
                file.write("@ATTRIBUTE ri NUMERIC")
                file.write("@ATTRIBUTE na NUMERIC")
                file.write("@ATTRIBUTE mg NUMERIC")
                file.write("@ATTRIBUTE al NUMERIC")
                file.write("@ATTRIBUTE si NUMERIC")
                file.write("@ATTRIBUTE k NUMERIC")
                file.write("@ATTRIBUTE ca NUMERIC")
                file.write("@ATTRIBUTE ba NUMERIC")
                file.write("@ATTRIBUTE fe NUMERIC")
                file.write("@ATTRIBUTE type NUMERIC")
            CSV_DICT_READER = csv.DictReader(f)
            for row in CSV_DICT_READER:
                line = ""
                line += maptoval(row["RI"], ril)
                line += ","
                line += maptoval(row["Na"], nal)
                line += ","
                line += maptoval(row["Mg"], mgl)
                line += ","
                line += maptoval(row["Al"], all)
                line += ","
                line += maptoval(row["Si"], sil)
                line += ","
                line += maptoval(row["K"], kl)
                line += ","
                line += maptoval(row["Ca"], cal)
                line += ","
                line += maptoval(row["Ba"], bal)
                line += ","
                line += maptoval(row["Fe"], fel)
                line += ","
                line += str(row["Type"])
                if random.choice([True, True, True, False]):
                    train.write(line)
                else:
                    test.write(line)
