from IPython import get_ipython
import os, sys
import io

try:
    limitation = sys.argv[1]
    if limitation is not list:
        limitation = [limitation]

    limitation_str = " ".join(limitation)

except IndexError:
    limitation = None
    limitation_str = ""

# get variables from current namespace
ipython = get_ipython()
variables = ipython.run_line_magic("who_ls","")

# store variables with magic command store
for var in variables:
    print(f"{var} {type(var)} {isinstance(var, io.TextIOWrapper)}")

    ipython.run_line_magic(f"store", f"{var}")

# generate a file defining list of variables
# this is used to load variables in the next notebook
# so that Pylance doesn't start whining :)
with open("variables.txt", "w") as f:
    for var in variables:
        f.write(f"{var} = globals()['{var}']\n")
        
f.close()

