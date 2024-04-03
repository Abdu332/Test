# # Lab11 Template

# Write your code for the functions here so that
# they return the correct result

def is_year(year):
    return False


def is_leap_year(year):
    return False


def get_month(month):
    return 'error'


def get_num_days(month, year):
    return -1


def get_month_results(month, year):
    return ''


if __name__ == "__main__":
    # Do not delete or alter this code; run it to test your functions
    
    # call is_year function with input of 2024
    # expected display is True
    print(is_year(2024))

    # call is_year function with input of -2024
    # expected display is False
    print(is_year(-2024))

    # call is_leap_year function with input of 2024
    # expected display is True
    print(is_leap_year(2024))

    # call get_month function with input of 11
    # expected display is 'November'
    print(get_month(11))
    
    # call get_month function with input of -1
    # expected display is 'error'
    print(get_month(-1))
    
    # call get_num_days function with input of 2, 2024
    # expected display is 29
    print(get_num_days(2, 2024)) 

    # call get_num_days function with input of 0, 5
    # expected display is 'error'
    print(get_num_days(0, 5)) 

    # call get_month_results function with input of 2, 2024
    # expected display is 'February has 29 days'
    print(get_month_results(2, 2024))
    
    # call get_month_results function with input of 0, 5
    # expected display is 'error'
    print(get_month_results(0, 5))
    