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


# -- Conda & Python versions
ARG CONDA_VERSION=latest
ARG PYTHON_VERSION=3.10


# -- Install Miniconda python
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh -O ~/conda.sh && \
    /bin/bash ~/conda.sh -b -p $CONDA_HOME && \
    rm ~/conda.sh && \
    conda install --yes python=${PYTHON_VERSION} && \
    $CONDA_HOME/bin/conda clean --all --yes


# -- Install the project
ARG PROJECT_HOME=/opt/{{cookiecutter.package_name}}

ADD setup.py ${PROJECT_HOME}/setup.py
ADD MANIFEST.in ${PROJECT_HOME}/MANIFEST.in
ADD README.md ${PROJECT_HOME}/README.md
ADD pyproject.toml ${PROJECT_HOME}/pyproject.toml
ADD src/ ${PROJECT_HOME}/src/

RUN pip install -e ${PROJECT_HOME}/


# -- Launch project on run
ENTRYPOINT ["{{cookiecutter.cli_command}}"]