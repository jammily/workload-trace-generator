def leer():
    with open('/simulator/simulator/uploads/test') as fp:
        for line in fp:
            print(line)
