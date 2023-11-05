#!/bin/python3

import sys
import yaml

def read_and_modify_yaml_data(infile,outfile, key, value):
   with open(f'{infile}', 'r') as f:
       data = yaml.safe_load(f)
       data['spec'][f'{key}'] = value
       print(data)
   with open(f'{outfile}', 'w') as file:
       yaml.dump(data,file,sort_keys=False)
   print('done!')


def main():
    args = sys.argv[1:]
    read_and_modify_yaml_data(args[0], args[0], key=args[1], value=args[2])

if __name__ == '__main__':
    main()
