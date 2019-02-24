start_speed = 60
end_speed = 131
increment = 10
conversion_factor = 0.6214

print ('KPH\tMPH')
print('--------------')

for kph in range(start_speed, end_speed, increment):
    mph = kph * conversion_factor
    print(kph, '\t', format(mph, '.1f'))

