import sys

import cookiecutter


# Ensure cookiecutter is recent enough
cookiecutter_min_version = '1.3.0'
if cookiecutter.__version__ < cookiecutter_min_version:
    print("--------------------------------------------------------------")
    print("!! Your cookiecutter is too old, at least %s is required !!" % cookiecutter_min_version)
    print("--------------------------------------------------------------")
    sys.exit(1)


# Ensure the selected repo name is usable
repo_name = '{{ cookiecutter.repo_name }}'
assert_msg = 'Repo name should be valid Python identifier!'

if hasattr(repo_name, 'isidentifier'):
    assert repo_name.isidentifier(), assert_msg
else:
    import re
    identifier_re = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*$")
    assert bool(identifier_re.match(repo_name)), assert_msg


# Ensure selected project_type is valid
valid_project_types = ['standard', 'spa']
if "{{ cookiecutter.project_type }}" not in valid_project_types:
    print("Project type '{{ cookiecutter.project_type }}' is not valid!")
    print("Valid project types are: %s" % ', '.join(valid_project_types))
    sys.exit(1)
