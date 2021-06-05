with open('ht.html', 'r') as rf:
    with open('link.txt', 'w') as wf:
        for line in rf.readlines():
            if '<a href=' in line:
                pos = line.find('<a href=')
                first = line.find('\"', pos)
                second = line.find('\"', first+1)
                url = line[first+1:second]
                wf.write(url + '\n')
