# Docstrings are basically a way for us to create little bits of documentation as we are coding along in our functions or in our other blocks of code

# eg

"""
This is a docstring. Basically a piece of documentation

Can also be used as a multi line comment
"""


def format_name(f_name, l_name):
    """
    Take a first and last name and format it to return the title case version of the name
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_string = format_name('ABDUL', 'rEhMaN')
print(formatted_string)



