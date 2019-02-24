max_temp = 102.5

temperature = float(input("Enter the substance's Celsius temperature: "))

while temperature > max_temp:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then the temperature')
    print('again and enter it.')
    temperature = float(input('Enter the new calsius temperature:'))

    print('The temperature is acceptable.')
