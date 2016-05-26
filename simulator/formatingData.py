from simulator import app, os
from os import listdir
from os.path import isfile, join

def formatData(scenario, inputList, fdp):
    save_path = os.path.join(app.config['INPUT_DATA'] + '/input')
    str1 = str(scenario) + ', '+ ', '.join(str(r) for v in fdp for r in v)
    str2 = ', '.join(inputList)
    file = open(save_path, "w")
    file.write(str1)
    file.write("\n")
    file.write(str2)
    file.close()


