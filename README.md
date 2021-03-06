These are [cookiecutter](https://github.com/cookiecutter/cookiecutter) templates for templating simple python projects. Install it with `pip install -U cookiecutter` to use.

- python-cli (`cookiecutter https://github.com/robrua/project-templates.git --directory python-cli`) is for simple python packages that include "main" functionality. It includes a CLI for your project using click. 

- python-docker (`cookiecutter https://github.com/robrua/project-templates.git --directory python-docker`) is the same as python-cli but includes a Dockerfile which builds and image with your project.

- python-library (`cookiecutter https://github.com/robrua/project-templates.git --directory python-library`) is for packages that don't have any "main" functionality and will only be imported into other projects.