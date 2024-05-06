import string, random
lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
digits = string.digits
special = string.punctuation

'''
***Assuming***
Easy - upper case+ lower case
Meduim - Easy + digits
Hard - Meduim + special characters
'''

def generate(s, length, complexity):
    if complexity==3:
        r = random.randint(1,length//2)
        for i in range(r):
            index = random.randint(0,length-1)
            s[index] = random.choice(uppers)
        
        for i in range(length):
            if s[i]=='*':
                s[i] = random.choice(digits)
                break
        
        for i in range(length):
            if s[i]=='*':
                s[i] = random.choice(special)
                break

        for i in range(length):
            if s[i]=='*':
                s[i] = random.choice(lowers)
        password = "".join(s)
        return password
    
    elif complexity==2:
        r = random.randint(1,length//2)
        for i in range(r):
            index = random.randint(0,length-1)
            s[index] = random.choice(uppers)

        for i in range(length):
            if s[i]=='*':
                s[i] = random.choice(digits)
                break

        for i in range(length):
            if s[i]=='*':
                s[i] = random.choice(lowers)
        password = "".join(s)
        return password
    
    elif complexity==1:
        r = random.randint(1,length//2)
        for i in range(r):
            index = random.randint(0,length-1)
            s[index] = random.choice(uppers)

        for i in range(length):
            if s[i]=='*':
                s[i] = random.choice(lowers)
        password = "".join(s)
        return password
    
    else:
        return
    


def main():
    s=[]
    length = int(input("Enter length of password (min 8): "))
    print("Choose complexity of password : ")
    complexity = int(input("1. Easy     2. Medium     3. Hard : "))
    if length<8:
        return
    for i in range(length):
        s.append('*')
    
    print(generate(s, length, complexity))
    
if __name__=='__main__':
    main()