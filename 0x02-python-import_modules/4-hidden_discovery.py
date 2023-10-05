#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4
    func = dir(hidden_4)
    if func[0:2] != "__":
        for f in func:
            print("({:s}".format(func))
