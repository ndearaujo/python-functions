mark_up = 2.5
another = 'y'

while another == 'y' or another == 'y':
    wholesale = float(input("Enter the item's "+\
                            "wholesale cost: "))

    retail = wholesale * mark_up

    print('Retail price: $', format(retail, ',.2f'))

    another = input('Do you have another item? '+\
                    '(Enter y for yes): ')

    
