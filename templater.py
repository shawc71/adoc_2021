
import sys

template_vars = {
    'day_number': sys.argv[1],
}

with open("solution.py.template") as f:
    contents = f.read()
    for var_name, val in template_vars.items():
        to_find = "${" + var_name + "}"
        contents = contents.replace(to_find, val)
    print(contents)
