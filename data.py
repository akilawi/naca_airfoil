


# Save the value calculated for angle, n_nodes, n_levels and speed
def save(angle, n_nodes, n_levels, speed, value):
    f = open('data.txt', 'a')
    s = str(angle) + ';' + str(n_nodes) + ';' + str(n_levels) + ';' + str(speed) + ':' + str(value) + '\n'
    f.write(s)
    f.close()

# Returns true if a value for (angle, n_nodes, n_levels, speed) exists
def exists(angle, n_nodes, n_levels, speed):
    f = open('data.txt', 'r')
    s = str(angle) + ';' + str(n_nodes) + ';' + str(n_levels) + ';' + str(speed) + ':'
    for line in f:
        if(s in line):
            return True
    return False

# Returns the value of (angle, n_nodes, n_levels, speed)
def get(angle, n_nodes, n_levels, speed):
    f = open('data.txt', 'r')
    s = str(angle) + ';' + str(n_nodes) + ';' + str(n_levels) + ';' + str(speed) + ':'
    for line in f:
        if(s in line):
            return line[len(s):-1]
    return('')

# Delete the content of data.txt
def clear_file():
    f = open('data.txt', 'w')
    f.write('')
    f.close()

# Returns an unordered list of all values in data.txt
def get_all():
    result = list()
    f = open('data.txt', 'r')
    for line in f:
        i = line.index(':')
        result.append(line[i+1:-1])
    return result

# Returns an unordered dict of all values in data.txt with the key angle;n_nodes;n_levels;speed
def get_dict():
    result = dict();
    f = open('data.txt', 'r')
    for line in f:
        key = line[0: line.index(':')]
        value = line[line.index(':')+1: -1]
        result[key] = value
    return result
