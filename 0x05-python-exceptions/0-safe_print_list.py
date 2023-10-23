#!usr/bin/python3
# a function that prints x elements of a list

def safe_print_list(my_list=[], x=0):
    c = 0  # keep track of number of elements printed

    try:  # attempt to itterate my_List upto x
        for i in range(x):
            print(my_list[i], end="")
            c += 1

    except IndexError:  # if i goes out of bounds, allow to continue
        pass

    finally:  # prints newline and return total number of elements printed
        print()
        return c
