# Earthcube-Meeting-2022


![AMGeO Logo](./static/AMGeOLogo.svg)

Notebook for Earthcube Meeting 2022

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/willemmirkovich/Earthcube-Meeting-2022/HEAD)

## Abstract

The Assimilative Mapping of Geospace Observations (AMGeO) is a data science tool for the geospace science community that automates labor-intensive data acquisition and processing, combining observations from various sensors into assimilative maps of the high-latitude ionosphere. While AMGeO offers a highly configurable toolset, it currently requires both domain expertise and familiarity with Python to use it effectively for scientific research. 

To remove hurdles for novice users and empower all AMGeO users, we have recently introduced a new Application Programming Interface (API) focused on enhanced user-experience, including better compatibility with Jupyter Notebooks, improved data manipulation with Xarray and more flexible data generation. This notebook will demonstrate the functionality offered by the new API and how to use AMGeO in conjunction with other popular Python research tools in order to accelerate geospace data science processes.

## Binder

To open this notebook in binder, use the following url:

https://mybinder.org/v2/gh/willemmirkovich/Earthcube-Meeting-2022/HEAD

And open `WM_02_AMGeO-2.0.ipynb`

## Docker

To build this docker container locally to run the notebook, 
execute the following commands:

```sh
docker build -t amgeo-earthcube-2022 .
docker run -it --rm -p 8888:8888 amgeo-earthcube-2022 jupyter notebook --ip=0.0.0.0 --port=8888
```

And open `WM_02_AMGeO-2.0.ipynb`