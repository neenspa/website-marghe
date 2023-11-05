#!/bin/python3


import sys
from ruamel.yaml import YAML
yaml=YAML()

def read_and_modify_yaml_data(infile, outfile, deployment_name, target_value):
    with open(f'{infile}', 'r') as f:
        data = yaml.load(f)

        new_entry = yaml.load(f"""target:
    version: v1
    kind: Deployment
    name: {deployment_name}
patch: |-
    - op: replace
      path: /spec/replicas
      value: {target_value}
    """)
        
        data['patchesJson6902'].append(new_entry)
        #yaml.dump(data, sys.stdout)
        
    with open(f'{outfile}', 'w') as file:
        yaml.dump(data, file)
    print('done!')


def main():
    args = sys.argv[1:]
    read_and_modify_yaml_data(args[0], args[0], deployment_name=args[1], target_value=args[2])

if __name__ == '__main__':
    main()
