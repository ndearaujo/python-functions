high_score = 95

test1 = int(input('Enter the score for test 1:' ))
test2 = int(input('Enter the score for test 2:' ))
test3 = int(input('Enter the score for test 3:' ))

average = (test1 + test2 + test3) / 3

print ('the average score is', average)

if average >= high_score:
    print('congratulations!')
    print('this is a great average!')



