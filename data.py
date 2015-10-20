



def save(angle, n_nodes, n_levels, speed, value):
    f = open('data.txt', 'a')
    s = str(angle) + ';' + str(n_nodes) + ';' + str(n_levels) + ';' + str(speed) + ':' + str(value) + '\n'
    f.write(s)
    f.close()

def exists(angle, n_nodes, n_levels, speed):
    f = open('data.txt', 'r')
    s = str(angle) + ';' + str(n_nodes) + ';' + str(n_levels) + ';' + str(speed) + ':'
    for line in f:
        if(s in line):
            return True
    return False

def get(angle, n_nodes, n_levels, speed):
    f = open('data.txt', 'r')
    s = str(angle) + ';' + str(n_nodes) + ';' + str(n_levels) + ';' + str(speed) + ':'
    for line in f:
        if(s in line):
            return line[len(s):-1]
    return('')

def clear_file():
    f = open('data.txt', 'w')
    f.write('')
    f.close()


#clear_file()
