# 성적이 낮은 순서로 학생 출력하기 
N = int(input())

students = []

for _ in range(N):
  input_data = input().split()
  students.append([input_data[0], int(input_data[1])])

students = sorted(students, key = lambda student: student[1])

for x in students:
  print(x[0], end = ' ')

