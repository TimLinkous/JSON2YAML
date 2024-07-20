import json
import yaml

def y2j(yaml_filepath: str, json_filepath: str):
    with open(yaml_filepath, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    with open(json_filepath, 'w') as json_file:
        json.dump(yaml_data, json_file, indent=4)


yaml_file_path = 'xmas.yaml'  # Replace with your YAML file
json_file_path = 'xmas.json'  # Replace with your desired JSON file
y2j(yaml_file_path, json_file_path)