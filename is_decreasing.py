#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 02/12/2023
#This code is designed to take a list of numbers and return true if they are strictly decreasing and false otherwise




def is_decreasing(my_list):
    if len(my_list)<=1:
        return True
    else:
        if my_list[0] > my_list[1]:
            return is_decreasing(my_list[1::])
        else:
            return False
