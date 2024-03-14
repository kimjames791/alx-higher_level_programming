#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    def_names = dir(hidden_4)

    for k in range(len(def_names)):
        if def_names[k][:2] != '__':
            print(def_names[k])
