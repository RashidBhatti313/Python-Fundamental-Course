#create text file with python
def createfile(filename):
    with open(filename,'w') as f:
        f.write("lkjfkldjfkljs")

createfile("filling.py")

def read(f):
    with open(f,'r') as file:
        result = file.read()
        return result.split()

print(read("age.py"))



    
f = open('gljkflkjdljgldfjkgljld.txt','w')

def numChar (filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close

    return content
print(numChar('week 05 lec 1,2.py'))

def numWords(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    wordlist = content.split()
    print(wordlist)
    return len(wordlist)
print(numWords("week 05 lec 1,2.py"))

def numlines (filename):
    infile = open(filename)
    linelist = infile.readlines()
    infile.close

    print(linelist)
    return len(linelist)
print(numlines("if_with_in.py"))




