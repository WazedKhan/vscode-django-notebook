import os
import sys

PWD = os.path.dirname(os.getcwd())

PROJ_MISSING_MSG = """Set an environment variable:\n
`DJANGO_PROJECT=your_project_name`\n
or call:\n
`init_django(your_project_name)`
"""


def init_django(project_name=None):
    """
    Initialize Django in a Jupyter notebook environment.

    Args:
        project_name (str): The Django project name. If not provided,
                            the DJANGO_PROJECT environment variable will be used.

    Raises:
        Exception: If no project name is provided or found in the environment variable.
    """
    os.chdir(PWD)
    project_name = project_name or os.environ.get("DJANGO_PROJECT") or None
    if project_name is None:
        raise Exception(PROJ_MISSING_MSG)
    sys.path.insert(0, PWD)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django

    django.setup()
