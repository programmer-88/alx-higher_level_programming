#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    
    func = dir(hidden_4)
    for f in func:
        if f[0:2] != "__":
            print("{:s}".format(f))
