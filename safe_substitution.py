# safe_substitution.py
import string

template_string = "Your name is ${firstname} ${lastname}"
t = string.Template(template_string)
result = t.safe_substitute(firstname="Florian")
print(result)
