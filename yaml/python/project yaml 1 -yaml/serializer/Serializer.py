import yaml

dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

with open(r'E:\devops\yaml\project yaml 1 -yaml\serializer\output.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)