MIN_SALARY = 30000.0
MIN_YEARS = 2

def main():
   
    salary = float(input('Enter your annual salary: '))

 
    years_on_job = int(input('Enter the number of ' +
                             'years employed: '))

    
    if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You do not qualify for this loan.')


main()
