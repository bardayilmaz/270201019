grades = list()
avGrades=list()
studentCount = int(input("how many students will enter the grades? "))
for i in range(studentCount):
	m_1 = int(input("midterm1: "))
	m_2 = int(input("midterm2: "))
	f = int(input("final: "))

	grades.append([m_1,m_2,f])
	avGrades.append(m_1/3+m_2/3+f/4)
print(grades,"\n",avGrades)		