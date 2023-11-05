#!/bin/python3


import sys
from ruamel.yaml import YAML
yaml=YAML()

def read_and_modify_yaml_data(infile, outfile, deployment_name_to_reset):
    with open(f'{infile}', 'r') as f:
        data = yaml.load(f)

        [data['patchesJson6902'].remove(entry) for entry in data['patchesJson6902'] if 'patchesJson6902' in data if entry['target']['name'] == deployment_name_to_reset ]
        #yaml.dump(data, sys.stdout)
        
    with open(f'{outfile}', 'w') as file:
         yaml.dump(data, file)
    print('done!')


def main():
    args = sys.argv[1:]
    read_and_modify_yaml_data(args[0], args[0], deployment_name_to_reset=args[1])

if __name__ == '__main__':
    main()
