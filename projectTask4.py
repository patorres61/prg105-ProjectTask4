# Phyllis Torres
# Task 4 Assignment

# This program will expand the code from Task 1 and Task 2. This task adds code for a returning customer.
# A user will select option 1, indicating they are a returning customer. Then, the user will be asked to enter
# their customer id number. The program will read a file of customers and will select the customer information
# if the customer id matches a customer id in the file. If the customer id does not match an id in the file, an
# error message will be displayed. If the customer id matches a record in the file, the customer information will
# be displayed and the customer will be asked to confirm if this is the correct information. If the customer
# indicates the information is correct, a welcome message is displayed. If the customer indicates the information
# is incorrect, the customer will be prompted to enter the customer id again.

# This program also expands the code from Task 3 in order to allow a new customer to be added to a customer list.
# The program will prompt the user to enter their first name, last name, street address, city, state, zip code, and
# phone number. The program will create a new customer id by determining the sequential number for the next
# record to be added and append it to the last four number of the customer's phone number. The new customer
# information will be concatenated together to form a customer record. The new customer record will be written
# to the file and appended to the end of the customer list.

# Due: 12/9/16

# import the datetime module
from datetime import datetime

# print the assignment information
print 'Task 4'
print 'Phyllis Torres'
print 'Due: 12/9/16\n\n'

# define the input file
fileIn = 'customerList.txt'

# get the current date
today = datetime.today()

# define colors and bold text parameters
class color:
    def __init__(self):
        pass
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# print the title for the display
print color.BOLD + '\n To Bean or Not to Bean...\n\n' + color.END,
print('                              Proprietor: Phyllis Torres\n\n'),
# print the curent day of the week in the following format: day of the week, month, day and year
print ('                           "Brew" day is: ' + today.strftime("%A, %b %d, %Y\n\n"))

selection = 0

# define main menu function
def main_menu():
    print color.BOLD + '<<=====================================================>>' + color.END
    print color.BOLD + '<<===                                               ===>>' + color.END
    print color.BOLD + '\n<<===             1. Returning Customer             ===>>' + color.END
    print color.BOLD + '\n<<===             2. New Customer                   ===>>' + color.END
    print color.BOLD + '\n<<===             3. Guest                          ===>>' + color.END
    print color.BOLD + '\n<<===                                               ===>>' + color.END
    print color.BOLD + '<<=====================================================>>' + color.END

    # display the welcome message
    print color.BOLD + "\n\nWelcome to 'To Bean or Not to Bean!..."
    print "...where the best brews are bubbling in our cauldrons!" + color.END

# define order menu function
def brew_menu():
    print "\nGreat! Let's get to work on your order! "
    print "\n\nHere is our Brew Menu: \n"

    print color.BOLD + '<<=====================================================>>' + color.END
    print color.BOLD + '<<===                                               ===>>' + color.END
    print color.BOLD + '\n<<===             1. Coffee Brews                   ===>>' + color.END
    print color.BOLD + '\n<<===             2. Teas                           ===>>' + color.END
    print color.BOLD + '\n<<===             3. Hot Chocolate                  ===>>' + color.END
    print color.BOLD + '\n<<===                                               ===>>' + color.END
    print color.BOLD + '<<=====================================================>>' + color.END

# define function to accept a user input id to look up a returning guest
def get_customer():
    customer = raw_input('\nPlease enter your Customer ID: ')
    return customer

# define the function open the file, store the customer information in a list and to look up a
# customer by customer id in the input file
def find_customer(customer):
    try:
        with open(fileIn, 'r') as f:
            customer_list = f.readlines()
            for item in customer_list:
                record = item.split(',')
                if customer == record[0]:
                    return record

        return 'none'

    except IOError as a:
        print "I/O error({0}): {1}".format(a.errno, a.strerror) + ': ' + fileIn

    return

# define function to prepare file for new customer
def prep_file():
    # prep file for new customer record
    custfile = open('customerList.txt', 'r+')     # opens the file to allow appending
    custlist = list(custfile)
    flength = len(custlist)     # file index will be used to create customer id
    custfile.close()
    return flength

# define function to confirm customer information is correct
def confirm_info():
    confirm = raw_input('\nIs this information correct? (Y/N): ')
    return confirm.upper()

# define function to confirm customer information is correct
def quit_program():
    leave = raw_input('\nWould you would like to quit the program (Y/N): ')
    return leave.upper()

# define function to confirm customer information is correct
def correct_info():
    correct = raw_input('\nWould you would like to correct your information (Y/N): ')
    return correct.upper()

# define function to ask customer if they wish to re-enter their customer id
def reenter_info():
    reenter = raw_input('\nWould you would like to re-enter your Customer ID (Y/N): ')
    return reenter.upper()

# define function to determine if customer would like to continue to the order menu
def continue_order():
    confirm = raw_input('\nWould you like to continue to the order menu? (Y/N): ')
    return confirm.upper()

# define function to print messages and to leave the program
def leave_program():
    print '\nOk, hope to see you again soon at...'
    print color.BOLD + "\nTo Bean or Not to Bean!..."
    print "...where the best brews are bubbling in our cauldrons!" + color.END
    return

# define function to handle the selection for a returning customer
def returning_customer():
    my_customer = get_customer()     # call get_customer to accept user input for customer id
    record = find_customer(my_customer)     # call find_customer to look up the customer id in the customer list

    if record == 'none':

        print '\nThere is no record of the customer id you entered, please try again.\n'
        returning_customer()     # call the returning_customer function

    else:

        phone = record[7]      # move phone number from customer list to a variable
        print '\nYour information is as follows: \n'
        print 'Customer ID: ' + record[0]     # display the customer id
        print record[1], record[2]            # display the customer first and last name
        print record[3]                       # display the customer street address
        print record[4] + ', ' + record[5] + '  ' + record[6]     # display the customer city, state, and zip code
        print '(' + phone[0:3] + ') ' + phone[3:6] + '-' + phone[6:10]     # format the phone number in a user friendly display

        response = confirm_info()     # call the confirm_info function

        if response == 'Y':

            order = continue_order()

            if order == 'Y':

                brew_menu()    # call the function to display the brew menu

            else:

                leave = quit_program()

                if leave == 'Y':

                    leave_program()

                else:

                    get_started(selection)

        else:

            reenter = reenter_info()

            if reenter == 'Y':

                returning_customer()     # call returning_customer function to allow user to input another id

            else:

                leave = quit_program()

                if leave == 'Y':

                    leave_program()

                else:

                    get_started(selection)

    return

# define function to handle the selection for a new customer
def new_customer():
    try:
        fileindex = prep_file()

        # get customer information
        print '\nWe need to get some information from you. \n'
        print(24*'=')
        print '\n'

        cust_first = raw_input('Please enter your first name: ')
        cust_first = cust_first.title()
        cust_last = raw_input('Please enter your last name: ')
        cust_last = cust_last.title()
        cust_street = raw_input('Please enter your house number and street name: ')
        cust_street = cust_street.title()
        cust_city = raw_input('Please enter your city: ')
        cust_city = cust_city.title()
        cust_state = raw_input('Please enter your two letter state abbreviation: ')
        cust_state = cust_state.upper()
        cust_zip = raw_input('Please enter your 5 digit zip code: ')
        cust_phone = raw_input('Please enter your phone number with area code: ')

        # create customer id from next sequential record number concatenated to last four digits of phone number
        last_four = cust_phone[6:10]
        str_id = str(fileindex+1)+last_four

        print '\n'
        print(24*'=')
        print '\n'

        # display the customer data for user to verify
        print 'Thank you! Here is what you entered:\n'
        print cust_first + ' ' + cust_last
        print cust_street
        print cust_city + ', ' + cust_state + '  ' + cust_zip

        # format the phone number in a user
        print '(' + cust_phone[0:3] + ') ' + cust_phone[3:6] + '-' + cust_phone[6:10]

        # the following concatenates the customer data to create a record that will be written to the file
        new_cust = str_id+','+cust_first+','+cust_last+','+cust_street+','+cust_city+','+cust_state+','+cust_zip+','+cust_phone+'\n'

        response = confirm_info()     # call the confirm_customer function for customer to verify their info

        if response == 'Y':

            # write record to file
            custfile = open('CustomerList.txt', 'a+')     # opens file to append
            custfile.writelines(new_cust)
            custfile.close()

            print '\nCongratulations, ' + cust_first+'! '
            print 'Your customer id is: ' + str_id
            print 'Please take a moment to jot it down. It will also be displayed on your receipt.'

            order = continue_order()

            if order == 'Y':

                brew_menu()    # call the function to display the brew menu

            else:

                leave = quit_program()

                if leave == 'Y':

                    leave_program()

                else:

                    get_started(selection)

        else:

            correct = correct_info()

            if correct == 'Y':

                new_customer()     # call returning_customer function to allow user to input another id

            else:

                leave = quit_program()

                if leave == 'Y':

                    leave_program()

                else:

                    get_started(selection)

    except IOError as a:
        print "I/O error({0}): {1}".format(a.errno, a.strerror) + ': ' + fileIn
        print 'File not found.'

    return

# define function to handle the selection for a guest
def guest_customer():
    print '\nYou have selected the Guest Customer Option.'
    return

# define function to handle when the selection is not 1, 2, or 3
def wrongnumber():
    print('\nPlease enter the appropriate number for your customer type: 1, 2, or 3. ')
    return

def get_started(selection):
    # prompt the user to enter a selection and validate the data entered before determining which function to call
    while selection >= 0:

        main_menu()       # display the main menu for the customer

        try:
            selection = int(raw_input('\n\nPlease make the appropriate customer selection: '))

            if selection < 1 or selection > 3:
                selection = int(raw_input('Please select your customer type. It must be a number equal to 1, 2, or 3.  '))

            if selection == 1:

                print '\nYou have selected the Returning Customer Option.'
                returning_customer()     # call returning_customer function
                selection = - 1

            elif selection == 2:

                print '\nYou have selected the New Customer Option.'
                new_customer()     # call the new_customer function
                selection = - 1

            elif selection == 3:

                guest_customer()     # call the guest_customer function
                brew_menu()          # call the brew_menu function to allow a guest to begin their order

                selection = - 1

            else:
                wrongnumber()     # call the wrongnumber function if the user entered an invalid number selection

        except ValueError:
            print("\nSorry, I didn't understand that entry. Please enter 1, 2, or 3. \n")     # this will handle if a user just hits enter or spacebar
            continue     # continue through the loop

    return

# program main area to launch the code

get_started(selection)
