size = input

student_score = []

i = 1

minimun_index = 0
minimun_value = student_score[0]
maximun_index = 0
maximun_index = student_score[0]

while (i < size) :
    if (student_score[i] < minumum_value):
        minumum_value = student_score[i]
        minumum_index=i
        
    else if (student_score[i] > maximum_value):
        maximum_value = student_score[i]
        maximum_index = i
        
    else i = i + 1

print(maximum_value, maximun_index)
print(minumum_value, minumum_index)
