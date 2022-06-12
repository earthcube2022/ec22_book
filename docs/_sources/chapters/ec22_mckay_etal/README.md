<!-- badges: start -->
[![Launch Rstudio Binder](http://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/earthcube2022/ec22_mckay_etal/main?urlpath=rstudio)
[![NSF-1929460](https://img.shields.io/badge/NSF-1929460-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1929460)
[![NSF-1347221](https://img.shields.io/badge/NSF-1347221-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1347221)
[![NSF-1540996](https://img.shields.io/badge/NSF-1540996-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1540996)
[![NSF-2126510](https://img.shields.io/badge/NSF-2126510-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=2126510)

(This Binder is slow - please be patient, or check out the [rendered version](https://earthcube2022.github.io/ec22_mckay_etal/).)

# Database interoperability, uncertainty quantification and reproducible workflows in the paleogeosciences

[Rendered version available here](https://earthcube2022.github.io/ec22_mckay_etal/)

## Abstract

The paleogeosciences are becoming more and more interdisciplinary, and studies increasingly rely on large collections of data derived from multiple data repositories. Integrating diverse datasets from multiple sources into complex workflows increases the challenge of creating reproducible and open science, as data formats and tools are often noninteroperable, requiring manual manipulation of data into standardized formats, resulting in a disconnect in data provenance and confounding reproducibility. Here we present a notebook that demonstrates how the Linked PaleoData (LiPD) framework is used as an interchange format to allow data from multiple data sources to be integrated in a complex workflow using emerging packages in R for geochronological uncertainty quantification and abrupt change detection. Specifically, in this notebook, we use the neotoma2 and lipdR packages to access paleoecological data from the Neotoma Database, and paleoclimate data from compilations hosted on Lipdverse. Age uncertainties for datasets from both sources are then quantified using the geoChronR package, and those data, and their associated age uncertainties, are then investigated for abrupt changes using the actR package, with accompanying visualizations. The result is an integrated, reproducible workflow in R that demonstrates how this complex series of multisource data integration, analysis and visualization can be integrated into an efficient, open scientific narrative.

## Contributors

This project is an open project, and contributions are welcome from any individual.  All contributors to this project are bound by a [code of conduct](CODE_OF_CONDUCT.md).  Please review and follow this code of conduct as part of your contribution.

  * [Nicholas McKay](http://nau.edu/mckay) [![orcid](https://img.shields.io/badge/orcid-0000--0003--3598--5113-brightgreen.svg)](https://orcid.org/0000-0003-3598-5113)
  * [Julien Emile-Geay](http://climdyn.usc.edu/) [![orcid](https://img.shields.io/badge/orcid-0000--0001--5920--4751-brightgreen.svg)](https://orcid.org/0000-0001-5920-4751)
  * [Deborah Khider](https://earth.usc.edu/~khider/) [![orcid](https://img.shields.io/badge/orcid-0000--0001--7501--8430-brightgreen.svg)](https://orcid.org/0000-0001-7501-8430)

### Tips for Contributing

Although this notebook is a research product, we'd love to know if something isn't working right, or could be improved, so issues and bug reports are always welcome.  Code clean-up, and feature additions can be done either through pull requests to project forks or branches.

This codebase is under an [MIT License](LICENSE).

## How to use this repository

There are a few ways to use this. 

1. [Check out the rendered notebook](https://nickmckay.github.io/EC22-neotoma-actR). This is the fastest and easiest way to see the code, the narrative and the products. 
2. Clone the repo, and run it all for yourself. Follow the intructions to run the needed libraries. 
3. Run it in [myBinder](https://mybinder.org/v2/gh/earthcube2022/ec22_mckay_etal/main?urlpath=rstudio). Be warned, it can take 10-15 minutes to set up in your browser the first time you run it. 

### Workflow Overview

This project takes data from [neotoma](https://neotomadb.org) and [lipdverse](https://lipdverse.org), and analyzes it using [geoChronR](https://nickmckay.github.io/GeoChronR) and the [abrupt change toolkit in R (actR)](https://linked.earth/actR).

### System Requirements

This project is developed using R, and should run on any platform.

### Data Requirements

This project takes data from [neotoma](https://neotomadb.org) and [lipdverse](https://lipdverse.org).

### Key Outputs

This project generates a notebook. The [rendered notebook is available here](https://earthcube2022.github.io/ec22_mckay_etal/)
