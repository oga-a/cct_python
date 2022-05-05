:github_url: https://{{ cookiecutter.github_fqdn }}/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

{{ cookiecutter.project_name }}
==========

{{ cookiecutter.project_name }} is a package I use personally.

|

Install:

.. code-block:: none

    pip install "git+ssh://git@{{ cookiecutter.github_fqdn }}/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git"


Minimal Example:

.. code-block:: python

    import {{ cookiecutter.python_package }}
    print({{ cookiecutter.python_package }}.__version__)

|

.. toctree::
    :maxdepth: 1
    :caption: API

    {{ cookiecutter.python_package }}
    {{ cookiecutter.python_package }}.utils

|

.. toctree::
   :caption: Examples
   :hidden:
   :glob:

   Example Codes <https://{{ cookiecutter.github_fqdn }}/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/tree/master/examples>

.. toctree::
    :caption: Development
    :hidden:

    GitHub <https://{{ cookiecutter.github_fqdn }}/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}>
