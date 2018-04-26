time-series-sandbox
==============================

A sandbox for testing techniques against the standard AirPassenger dataset

## Getting Started

You will have needed to built the Docker template image prior to running this repo. See the cookiecutter README.md file in the template repo for instructions.

Clone this repo, then execute the following command to build your container environment.  

    $ docker-compose build

Then copy the credentials template, and complete the sections.

    $ cp src/credentials.txt.template src/credentials.txt

**Getting a shell**

You can start a temporary container with a shell in the working directory by typing `make shell`. When you exit out of this shell the container will be destroyed, but any files you create in the working directory will remain as they are a mapped volume to your host _./src_ directory.

**Jupyter Notebook server**

    1. Run `docker-compose build explore` to build the exploratory analysis image
    2. Run `docker-compose up explore` to start the Jupyter server

This will build the image, and start a container running Jupyter notebook, returning the link to access the notebook.

To run a specific Python script inside the running container: `docker-compose exec explore COMMAND [ARGS...]`.  
Alternatively you can just open a shell session up on the running container: `docker-compose exec explore /bin/bash`.  
To run one off command using that service image (in this case a shell): `docker-compose run --rm -w /usr/src explore /bin/bash`. 

## Project Organisation

    ├── README.md                    <- The top-level README for data scientists using this project.
    │
    ├── docker-compose.yml           <- The compose file to configure the containers and set up interactions between each other
    │
    │── Makefile                     <- Makefile with commands like `make data`, `make shell`
    │
    ├── references                   <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── src                          <- Working directory for use in this project.
    │   ├── app                      <- Python app to automate repetitive tasks
    │   │
    │   ├── data
    │   │   ├── external             <- Data from third party sources.
    │   │   ├── interim              <- Intermediate data that has been transformed.
    │   │   ├── processed            <- The final, canonical data sets for modeling.
    │   │   └── raw                  <- The original, immutable data dump.
    │   │
    │   ├── helpers                  <- Helper libraries to navigate the project, query data stores, get credentials etc
    │   │
    │   │── models                   <- Trained and serialized models, model predictions, or model summaries
    │   │
    │   ├── notebooks                <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                               the creator's initials, and a short `-` delimited description, e.g.
    │   │                               `1.0-jqp-initial-data-exploration`.
    │   │
    │   │── queries                  <- Data queries for running against a data store, e.g. .sql, .bq SQL files
    │   │
    │   ├── reports                  <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   │   └── figures              <- Generated graphics and figures to be used in reporting
    │   │
    │   │── workbooks                <- Tableau workbooks. Naming convention similar to notebooks above.
    │   │
    │   ├── config.yaml              <- Holds project configuration
    │   │
    │   ├── credentials.txt          <- Contains your personal credentials for access to data stores
    │   │

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
