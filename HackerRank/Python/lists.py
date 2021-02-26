if __name__ == '__main__':
 N = int(input())
arr=[]
for i in range(N) :
    v=input().split()
    for i in range(1,len(v)):
      v[i]=int(v[i])
    if v[0]== "append":
       arr.append(v[1])
    elif v[0]== "insert":
       arr.insert(v[1],v[2])
    elif v[0]== "remove":
       arr.remove(v[1])
    elif v[0]== "pop": 
       arr.pop()
    elif v[0]== "sort": 
       arr.sort()    
    elif v[0]== "reverse":  
        arr.reverse()
    elif v[0]== "print":  
        print(arr)
    





      
 

