import csv
import sys
import random

# Comprovar que el número d'arguments és correcte
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

# Donat un valor i una llista de valors, donar un string amb l'índex d'on està el valor, afegint-lo si no hi és
def maptoval(value, val_list):
    ind = 0
    for i, val in enumerate(val_list):
        ind = i
        if val == value:
            return str(i)
    val_list.append(value)
    return str(ind + 1)

# Passar una llista de llargada  x a un string tipus "0,1,...,x"
def numbers(list_):
    line = ""
    for n in range(len(list_)):
        line += str(n)
        line += ","
    return line[:-1]

filename = sys.argv[1]
trainName = sys.argv[2]
testName = sys.argv[3]
# Obrir els 3 fitxers
with open(filename, "r") as f:
    with open(trainName, "w") as train:
        with open(testName, "w") as test:
            CSV_DICT_READER = csv.DictReader(f)
            rows = []
            # Recórrer totes les dades, poblant les llistes de valors per saber quants valors tindrem
            for row in CSV_DICT_READER:
                rows.append(row)
                line = ""
                line += maptoval(row["RI"], ril)
                line += maptoval(row["Na"], nal)
                line += maptoval(row["Mg"], mgl)
                line += maptoval(row["Al"], all)
                line += maptoval(row["Si"], sil)
                line += maptoval(row["K"], kl)
                line += maptoval(row["Ca"], cal)
                line += maptoval(row["Ba"], bal)
                line += maptoval(row["Fe"], fel)
            # Escriure les capçaleres del fitxer
            train.write("% Train database\n")
            train.write("@RELATION Train\n")
            test.write("% Test database\n")
            test.write("@RELATION Test\n")
            for file in [train, test]:
                file.write("\n")
                file.write("@ATTRIBUTE ri {" + numbers(ril) + "}\n")
                file.write("@ATTRIBUTE na {" + numbers(nal) + "}\n")
                file.write("@ATTRIBUTE mg {" + numbers(mgl) + "}\n")
                file.write("@ATTRIBUTE al {" + numbers(all) + "}\n")
                file.write("@ATTRIBUTE si {" + numbers(sil) + "}\n")
                file.write("@ATTRIBUTE k {" + numbers(kl) + "}\n")
                file.write("@ATTRIBUTE ca {" + numbers(cal) + "}\n")
                file.write("@ATTRIBUTE ba {" + numbers(bal) + "}\n")
                file.write("@ATTRIBUTE fe {" + numbers(fel) + "}\n")
                file.write("@ATTRIBUTE type {" + numbers([1,2,3,4,5,6,7]) + "}\n")
                file.write("@DATA\n")
            # Tornar a recórrer les línies per a escriure-les al fitxer
            for row in rows:
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
                line += str(int(row["Type"]) - 1)
                # Escriure el 75% aprox a train i el 25% a test
                if random.choice([True, True, True, False]):
                    train.write(line + "\n")
                else:
                    test.write(line + "\n")
