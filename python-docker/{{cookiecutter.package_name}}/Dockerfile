FROM debian:stable-slim


ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8


# -- Install utilities
RUN apt-get update --fix-missing --no-install-recommends && \
    apt-get install -y wget bzip2 ca-certificates curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# -- Anaconda home setup
ENV CONDA_HOME /opt/conda
ENV PATH $CONDA_HOME/bin:$PATH


# -- Python version
ARG python_version=3.10


# -- Install Miniconda python
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/conda.sh && \
    /bin/bash ~/conda.sh -b -p $CONDA_HOME && \
    rm ~/conda.sh && \
    conda install --yes python=${python_version} && \
    $CONDA_HOME/bin/conda clean --all --yes


# -- Install the project
ADD setup.py /opt/{{cookiecutter.package_name}}/setup.py
ADD MANIFEST.in /opt/{{cookiecutter.package_name}}/MANIFEST.in
ADD pyproject.toml /opt/{{cookiecutter.package_name}}/pyproject.toml
ADD src/ /opt/{{cookiecutter.package_name}}/src/

RUN pip install -e /opt/{{cookiecutter.package_name}}/


# -- Launch project on run
ENTRYPOINT ["{{cookiecutter.cli_command}}"]