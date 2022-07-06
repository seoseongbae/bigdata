class Mstack:
    def __init__(self):
        self.stack=[]
        print("Hi Mstack")
    def push(self,int1):
        self.stack.append(int1)
        print(self.stack,type(int1),int1)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)
    def __del__(self):
        print("bye Mstack")

if __name__=='__main__':
    a1=Mstack()
    for x in range(1,6):
        a1.push(x)
    a1.pop()
    print('length :', a1.length())