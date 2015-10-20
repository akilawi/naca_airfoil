DATA_FILE = 'data.txt'

# Saves the value of (angle, n_nodes, n_levels, speed, value)
def save(angle, n_nodes, n_levels, speed, value):
    f = open(DATA_FILE, 'a')
    s = 'a' + str(angle) + 'n' + str(n_nodes) + 'l' + str(n_levels) + 's' + str(speed) + ':' + str(value) + '\n'
    f.write(s)
    f.close()

# Returns true if a value exists for (angle, n_nodes, n_levels, speed)
def exists(angle, n_nodes, n_levels, speed):
    f = open(DATA_FILE, 'r')
    s = 'a' + str(angle) + 'n' + str(n_nodes) + 'l' + str(n_levels) + 's' + str(speed) + ':'
    for line in f:
        if(s in line):
            return True
    return False

# Returns the value of (angle, n_nodes, n_levels, speed)
def get(angle, n_nodes, n_levels, speed):
    f = open(DATA_FILE, 'r')
    s = 'a' + str(angle) + 'n' + str(n_nodes) + 'l' + str(n_levels) + 's' + str(speed) + ':'
    for line in f:
        if(s in line):
            return float(line[len(s):-1])
    return('')

# Clears all data in data.txt
def clear_file():
    f = open(DATA_FILE, 'w')
    f.write('')
    f.close()

# Return all data in an unsorted list of tuples (angle, n_nodes, n_levels, speed, value)
def get_all():
    result = list()
    f = open(DATA_FILE, 'r')
    for line in f:
        a = int(line[line.index('a')+1:line.index('n')])
        n = int(line[line.index('n')+1:line.index('l')])
        l = int(line[line.index('l')+1:line.index('s')])
        s = float(line[line.index('s')+1:line.index(':')])
        v = float(line[line.index(':')+1:-1])
        #i = line.index(':')
        #result.append(line[i+1:-1])
        #result.append(line[:-1])
        result.append((a, n, l, s, v))
    return result

# Sorts data
# data : a list of 5-tuples
def sort(data):
    data.sort(key=lambda x:x[3])
    data.sort(key=lambda x:x[2])
    data.sort(key=lambda x:x[1])
    data.sort(key=lambda x:x[0])

# Return all data in a sorted list of tuples (angle, n_nodes, n_levels, speed, value)
def get_all_sorted():
    result = get_all()
    sort(result)
    return result
