with open('file.txt', 'r') as rf:
    with open('file2.txt', 'w') as wf:
        lines = rf.readlines()
        for line in lines:
            for i in range(1, len(line)):
                if (line[i] == ','):
                    wf.write(f"{line[0:i]} salary is {line[i+1:len(line)]}")
            # name, salary = line.split(',')
            # wf.write(f"{name}'s salary is {salary}'")
