# JupyStore

<p align="center">
    <img src="readme_image.webp" alt="CodePlayground" width="400"/>
<p>



This project helps you store variables in Jupyter Notebooks and avoid Pylance warnings.
How it Works

## JupyStore consists of two parts:

* `store_variables.py`: This script saves variables from your notebook's current namespace to a file named 
* retrieve_variables.ipynb: This notebook retrieves variables stored in `variables.txt` and makes them available for use in your notebook.

## Using JupyStore

*Store Variables:*

* Open the notebook containing the variables you want to save.

* Run all the cells that define and assign values to your variables.

* In a new cell, execute this command:

    `%run store_variables.py`

* This creates a file named `variables.txt` in your current directory.

*Retrieve Variables:*

* Open a new notebook or switch to the notebook where you want to use the stored variables.

* In the first cell, run this command:

    `%load variables.txt`

* This loads the content of `variables.txt` into the current namespace.

* Optional: The retrieve_variables.ipynb notebook shows another way to achieve the same result. You can copy and run the cells from this notebook.

## Notes

`store_variables.py` uses a list named _variable_types_interest to filter the variables it stores. This list specifies which variable types are saved. You can modify this list to include or exclude specific types.
`variables.txt` is recreated every time you run `store_variables.py`. This ensures the file reflects the latest state of your variables.
