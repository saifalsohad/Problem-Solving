if __name__ == '__main__':
 N=int(input())
 student_marks = {}
 for _ in range(N):
  #student_marks = {}
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name]=scores

n=input()
s=sum(student_marks[n])
avg=s/len(student_marks[n])

print('{0:.2f}'.format(avg))

#print(avg)
#print(student_marks[n])
