'''
@filename: /readYaml
@time: 2023/10/7 16:01
'''
import yaml

def load_yaml(file_path):
    with open(file_path) as f:
        return yaml.safe_load(f)