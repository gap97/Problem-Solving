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

print '최댓값:',  maximum_value;
print '최댓값의 index:', maximun_index;

print '최솟값:',  minimum_value;
print '최솟값의 index:', minimun_index;
