import re
def main():
    pyscribe_log = open('pyscribe_logs.txt', 'w')
    x = 5
    pyscribe_log.write('From line 3: x is the ' + re.search(r'\'[a-zA-Z]*\'', str(type(x))).group()[1:-1] + ' ' + str(x)+ '\n')
    y = "hello"
    pyscribe_log.write('From line 5: y is the ' + re.search(r'\'[a-zA-Z]*\'', str(type(y))).group()[1:-1] + ' ' + str(y)+ '\n')
    y = "world"

if __name__=="__main__":
    main()
