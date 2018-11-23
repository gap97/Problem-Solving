size = input

item = []

i = 1

minimun_index = 0
minimun_value = item[0]
maximun_index = 0
maximun_index = item[0]

while (i < size) :
    if (item[i] < minumum_value):
        minumum_value = item[i]
        minumum_index=i
        
    else if (student_score[i] > maximum_value):
        maximum_value = item[i]
        maximum_index = i
        
    else i = i + 1

print(maximum_value, maximun_index)
print(minumum_value, minumum_index)
