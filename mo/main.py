import requests
import json
from iterfzf import iterfzf
from cookiecutter.main import cookiecutter

def main():
    resp = requests.get("https://api.github.com/repos/mohankumargupta/cookiecutter-templates/git/trees/main")
    data = json.loads(resp.text)
    options = [entry['path'][len('cookiecutter-'):] for entry in data['tree'] if entry['type'] == 'tree' and entry['path'].startswith('cookiecutter-')]
    #print(options)
    options.reverse()
    selected_item = iterfzf(options, __extra__=["--exact"])
    print(f"Selected item: {selected_item}")
    cookiecutter_template = f"cookiecutter-{selected_item}"
    cookiecutter("gh:mohankumargupta/cookiecutter-templates", directory=cookiecutter_template)