import json


with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

# Opening the CSV file to write
with open('chacon.csv', 'w') as csvfile:
    for i in range(5):
        selected_line = data[i]
        line = f"{selected_line['name']},{selected_line['html_url']},{selected_line['updated_at']},{selected_line['visibility']}\n"
        csvfile.write(line)

