# vscode-django-notebook

Easily run Django queries and tasks within Jupyter Notebooks in VS Code.

## Overview

`vscode-django-notebook` simplifies the process of initializing Django projects directly in Jupyter Notebook cells. This is particularly useful for quick debugging, querying, and testing in a flexible notebook environment.

---

## Features

- **Convenient Django Initialization**: Avoid repetitive setup steps in Jupyter Notebooks.
- **Interactive Django ORM Access**: Use Django models and utilities interactively.
- **VS Code Compatible**: Tailored for the Jupyter extension in VS Code.

---

## Installation

Install the package via pip:

```bash
pip install vscode-django-notebook
```

---

## **Setup Guide**

### Step 1: Create a Folder for Notebooks

On the same level as `manage.py`, create a folder to organize your Jupyter Notebooks. For example:

```
your_project/
├── manage.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── notebook/
│   ├── __init__.py
│   └── user.ipynb
```

* **Folder Name** : You can name this folder anything you like (e.g., `notebooks`, `playground`, `testing`). In this example, we use `notebook`.
* **Notebook File Name** : The notebook file (e.g., `user.ipynb`) can also have any name, depending on its purpose.

---

### Step 2: Select the Project's Environment in VS Code

1. Open the `user.ipynb` notebook in VS Code.
2. In the top-right corner of the Jupyter Notebook interface, click on the  **kernel selection dropdown** .
3. Choose the Python environment where your Django project dependencies are installed.

---

### Step 3: Install and Initialize `vscode-django-notebook`

1. Install the package:

   ```bash
   pip install vscode-django-notebook
   ```
2. Add the following code at the top of your notebook to initialize Django:

   ```python
   from vscode_django_notebook import init_django

   # Initialize Django by specifying the project name
   init_django(project_name="config")
   ```

   Replace `"config"` with the name of your Django project module (where `settings.py` is located).

---

### Step 4: Write Complex Queries or Debug Utilities

Once initialized, you can interact with Django models, run complex queries, or debug utilities directly in the notebook. Here's an example:

#### Example: Testing a Query

```python
# Import Django models
from myapp.models import User, Order

# Write and test complex queries
users_with_recent_orders = User.objects.filter(
    id__in=Order.objects.filter(date__gte="2024-01-01").values_list("user_id", flat=True)
)

# Inspect the results
print(users_with_recent_orders)
```

#### Example: Writing and Debugging Utilities

```python
# Utility function to calculate total revenue for a user
def calculate_user_revenue(user_id):
    from myapp.models import Order
    return Order.objects.filter(user_id=user_id).aggregate(total_revenue=Sum("amount"))["total_revenue"]

# Test the utility
test_user_id = 1
print(f"Total revenue for user {test_user_id}: {calculate_user_revenue(test_user_id)}")
```

---

### Benefits of This Workflow

* **Interactive Testing** : Test Django ORM queries and helper functions interactively.
* **Debugging Made Easy** : Debug utilities or inspect data before adding them to the project.
* **Reusable Code** : Refine and reuse tested code in the actual project.

---

### Troubleshooting

* **Jupyter Kernel Not Working** : Ensure you’ve selected the correct Python environment in VS Code.
* **Initialization Error** : Verify that the `project_name` in `init_django()` matches the folder containing your `settings.py`.

Now you're ready to streamline your Django development workflow using Jupyter Notebooks! 🚀
