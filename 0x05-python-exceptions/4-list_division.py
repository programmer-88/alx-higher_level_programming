#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError

            if type(my_list_1[i]) not in [int, float]:
                raise TypeError

            if type(my_list_2[i]) not in [int, float]:
                raise TypeError

            if my_list_2[i] == 0:
                raise ZeroDivisionError

            result.append(my_list_1[i] / my_list_2[i])

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

        except TypeError:
            print("wrong type")

        except IndexError:
            print("out of range")

    return result
