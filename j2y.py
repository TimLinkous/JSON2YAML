import json
import yaml

def j2y(json_filepath: str, yaml_filepath: str):
    #Read JSON data
    with open(json_filepath, 'r') as json_file:
        json_data = json.load(json_file)

    with open(yaml_filepath, 'w') as yaml_file:
        yaml.dump(json_data, yaml_file, default_flow_style=False)



        
json_file_path = 'verify.json'  # Replace with your JSON file
yaml_file_path = 'verify.yaml'  # Replace with your desired YAML file
j2y(json_file_path, yaml_file_path)