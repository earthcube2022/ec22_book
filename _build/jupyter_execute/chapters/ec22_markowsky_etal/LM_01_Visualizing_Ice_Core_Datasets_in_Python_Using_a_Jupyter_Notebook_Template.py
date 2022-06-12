#!/usr/bin/env python
# coding: utf-8

# # Visualizing Ice Core Datasets in Python Using a Jupyter Notebook Template

# ## Authors
# 
# - Author1 = {"name": "L. Markowsky", "affiliation": "Kennesaw State University", "email": "lmarkowsky@gmail.com"}
# - Author2 = {"name": "Jessica Scheick", "affiliation": "University of New Hampshire", "email": "jbscheick@gmail.com", "orcid": "0000-0002-3421-4459"}

# <h1>Table of Contents</h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Visualizing-Ice-Core-Datasets-in-Python-Using-a-Jupyter-Notebook-Template" data-toc-modified-id="Visualizing-Ice-Core-Datasets-in-Python-Using-a-Jupyter-Notebook-Template-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Visualizing Ice Core Datasets in Python Using a Jupyter Notebook Template</a></span><ul class="toc-item"><li><span><a href="#Authors" data-toc-modified-id="Authors-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Authors</a></span></li><li><span><a href="#Purpose" data-toc-modified-id="Purpose-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Purpose</a></span></li><li><span><a href="#Technical-contributions" data-toc-modified-id="Technical-contributions-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Technical contributions</a></span></li><li><span><a href="#Methodology" data-toc-modified-id="Methodology-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Methodology</a></span></li><li><span><a href="#Results" data-toc-modified-id="Results-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Results</a></span><ul class="toc-item"><li><span><a href="#Part-1" data-toc-modified-id="Part-1-1.5.1"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Part 1</a></span></li><li><span><a href="#Part-2" data-toc-modified-id="Part-2-1.5.2"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Part 2</a></span></li></ul></li><li><span><a href="#Keywords" data-toc-modified-id="Keywords-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Keywords</a></span></li><li><span><a href="#Citation" data-toc-modified-id="Citation-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Citation</a></span></li><li><span><a href="#Future-work" data-toc-modified-id="Future-work-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Future work</a></span></li><li><span><a href="#Acknowledgements" data-toc-modified-id="Acknowledgements-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Acknowledgements</a></span></li><li><span><a href="#Copyright-and-License" data-toc-modified-id="Copyright-and-License-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Copyright and License</a></span></li></ul></li><li><span><a href="#Setup" data-toc-modified-id="Setup-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Setup</a></span><ul class="toc-item"><li><span><a href="#Library-import" data-toc-modified-id="Library-import-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Library import</a></span></li></ul></li><li><span><a href="#Source-data" data-toc-modified-id="Source-data-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Source data</a></span><ul class="toc-item"><li><span><a href="#NEEM-ion-concentration-data-in-10-yr-resolution" data-toc-modified-id="NEEM-ion-concentration-data-in-10-yr-resolution-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>NEEM ion concentration data in 10 yr resolution</a></span></li><li><span><a href="#Aerosol-source-concentrations-and-atmospheric-lifetime-in-10-yr-resolution" data-toc-modified-id="Aerosol-source-concentrations-and-atmospheric-lifetime-in-10-yr-resolution-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Aerosol source concentrations and atmospheric lifetime in 10 yr resolution</a></span></li></ul></li><li><span><a href="#Data-processing-and-analysis" data-toc-modified-id="Data-processing-and-analysis-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Data processing and analysis</a></span><ul class="toc-item"><li><span><a href="#A-brief-introduction-to-the-Python-data-science-ecosystem" data-toc-modified-id="A-brief-introduction-to-the-Python-data-science-ecosystem-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>A brief introduction to the Python data science ecosystem</a></span><ul class="toc-item"><li><span><a href="#Why-Python?" data-toc-modified-id="Why-Python?-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Why Python?</a></span></li><li><span><a href="#Some-of-Python's-benefits" data-toc-modified-id="Some-of-Python's-benefits-4.1.2"><span class="toc-item-num">4.1.2&nbsp;&nbsp;</span>Some of Python's benefits</a></span></li><li><span><a href="#An-overview-of-the-Python-data-science-stack-(with-links-to-resources)" data-toc-modified-id="An-overview-of-the-Python-data-science-stack-(with-links-to-resources)-4.1.3"><span class="toc-item-num">4.1.3&nbsp;&nbsp;</span>An overview of the Python data science stack (with links to resources)</a></span></li></ul></li><li><span><a href="#A-first-look-at-NumPy,-Pandas,-and-Matplotlib" data-toc-modified-id="A-first-look-at-NumPy,-Pandas,-and-Matplotlib-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>A first look at NumPy, Pandas, and Matplotlib</a></span><ul class="toc-item"><li><span><a href="#Exploring-a-namespace" data-toc-modified-id="Exploring-a-namespace-4.2.1"><span class="toc-item-num">4.2.1&nbsp;&nbsp;</span>Exploring a namespace</a></span></li><li><span><a href="#Accessing-built-in-help" data-toc-modified-id="Accessing-built-in-help-4.2.2"><span class="toc-item-num">4.2.2&nbsp;&nbsp;</span>Accessing built-in help</a></span></li><li><span><a href="#Three-fundamental-NumPy-and-Pandas-data-structures:-ndarray,-Series,-and-DataFrame" data-toc-modified-id="Three-fundamental-NumPy-and-Pandas-data-structures:-ndarray,-Series,-and-DataFrame-4.2.3"><span class="toc-item-num">4.2.3&nbsp;&nbsp;</span>Three fundamental NumPy and Pandas data structures: ndarray, Series, and DataFrame</a></span></li><li><span><a href="#Exploring-an-ice-core-dataset-with-Pandas" data-toc-modified-id="Exploring-an-ice-core-dataset-with-Pandas-4.2.4"><span class="toc-item-num">4.2.4&nbsp;&nbsp;</span>Exploring an ice core dataset with Pandas</a></span></li><li><span><a href="#A-brief-look-at-Seaborn" data-toc-modified-id="A-brief-look-at-Seaborn-4.2.5"><span class="toc-item-num">4.2.5&nbsp;&nbsp;</span>A brief look at Seaborn</a></span></li><li><span><a href="#Getting-started-with-Matplotlib" data-toc-modified-id="Getting-started-with-Matplotlib-4.2.6"><span class="toc-item-num">4.2.6&nbsp;&nbsp;</span>Getting started with Matplotlib</a></span></li></ul></li><li><span><a href="#Part-1:-Recreate-Figure-2,-step-by-step,-with-intermediate-results" data-toc-modified-id="Part-1:-Recreate-Figure-2,-step-by-step,-with-intermediate-results-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Part 1: Recreate Figure 2, step-by-step, with intermediate results</a></span><ul class="toc-item"><li><span><a href="#Step-1:-Prepare-the-data-and-initialize-the-figure-with-four-empty-axes" data-toc-modified-id="Step-1:-Prepare-the-data-and-initialize-the-figure-with-four-empty-axes-4.3.1"><span class="toc-item-num">4.3.1&nbsp;&nbsp;</span>Step 1: Prepare the data and initialize the figure with four empty axes</a></span></li><li><span><a href="#Step-2:-Position-the-y-axis-labels-and-tick-marks" data-toc-modified-id="Step-2:-Position-the-y-axis-labels-and-tick-marks-4.3.2"><span class="toc-item-num">4.3.2&nbsp;&nbsp;</span>Step 2: Position the y-axis labels and tick marks</a></span></li><li><span><a href="#Step-3:-Remove-unnecessary-spines" data-toc-modified-id="Step-3:-Remove-unnecessary-spines-4.3.3"><span class="toc-item-num">4.3.3&nbsp;&nbsp;</span>Step 3: Remove unnecessary spines</a></span></li><li><span><a href="#Step-4:-Configure-the-tick-marks" data-toc-modified-id="Step-4:-Configure-the-tick-marks-4.3.4"><span class="toc-item-num">4.3.4&nbsp;&nbsp;</span>Step 4: Configure the tick marks</a></span></li><li><span><a href="#Step-5:-Plot-data-in-subplots-a-c" data-toc-modified-id="Step-5:-Plot-data-in-subplots-a-c-4.3.5"><span class="toc-item-num">4.3.5&nbsp;&nbsp;</span>Step 5: Plot data in subplots a-c</a></span></li><li><span><a href="#Step-6:-Use-a-log-scale-for-selected-subplots" data-toc-modified-id="Step-6:-Use-a-log-scale-for-selected-subplots-4.3.6"><span class="toc-item-num">4.3.6&nbsp;&nbsp;</span>Step 6: Use a log scale for selected subplots</a></span></li><li><span><a href="#Step-7:-Plot-a-running-average" data-toc-modified-id="Step-7:-Plot-a-running-average-4.3.7"><span class="toc-item-num">4.3.7&nbsp;&nbsp;</span>Step 7: Plot a running average</a></span></li><li><span><a href="#Step-8:-Draw-horizonal-dashed-lines" data-toc-modified-id="Step-8:-Draw-horizonal-dashed-lines-4.3.8"><span class="toc-item-num">4.3.8&nbsp;&nbsp;</span>Step 8: Draw horizonal dashed lines</a></span></li><li><span><a href="#Step-9:-Plot-data-in-subplot-d" data-toc-modified-id="Step-9:-Plot-data-in-subplot-d-4.3.9"><span class="toc-item-num">4.3.9&nbsp;&nbsp;</span>Step 9: Plot data in subplot d</a></span></li><li><span><a href="#Step-10:-Draw-vertical-gridlines" data-toc-modified-id="Step-10:-Draw-vertical-gridlines-4.3.10"><span class="toc-item-num">4.3.10&nbsp;&nbsp;</span>Step 10: Draw vertical gridlines</a></span></li><li><span><a href="#Step-11:-Adjust-axes-to-match-the-published-figure" data-toc-modified-id="Step-11:-Adjust-axes-to-match-the-published-figure-4.3.11"><span class="toc-item-num">4.3.11&nbsp;&nbsp;</span>Step 11: Adjust axes to match the published figure</a></span></li><li><span><a href="#Step-12:-Draw-a-depth-scale-along-top-of-figure" data-toc-modified-id="Step-12:-Draw-a-depth-scale-along-top-of-figure-4.3.12"><span class="toc-item-num">4.3.12&nbsp;&nbsp;</span>Step 12: Draw a depth scale along top of figure</a></span></li><li><span><a href="#Step-13:-Remove-extraneous-spines" data-toc-modified-id="Step-13:-Remove-extraneous-spines-4.3.13"><span class="toc-item-num">4.3.13&nbsp;&nbsp;</span>Step 13: Remove extraneous spines</a></span></li><li><span><a href="#Step-14:-Plot-gray-uncertainty-bands" data-toc-modified-id="Step-14:-Plot-gray-uncertainty-bands-4.3.14"><span class="toc-item-num">4.3.14&nbsp;&nbsp;</span>Step 14: Plot gray uncertainty bands</a></span></li><li><span><a href="#Step-15:-Tweak-the-y-axis-settings" data-toc-modified-id="Step-15:-Tweak-the-y-axis-settings-4.3.15"><span class="toc-item-num">4.3.15&nbsp;&nbsp;</span>Step 15: Tweak the y-axis settings</a></span></li><li><span><a href="#Step-16:-Annotate-the-figure" data-toc-modified-id="Step-16:-Annotate-the-figure-4.3.16"><span class="toc-item-num">4.3.16&nbsp;&nbsp;</span>Step 16: Annotate the figure</a></span></li><li><span><a href="#Step-17.-Adjust-the-figure-size-and-the-font-size-of-the-labels-on-the-x-axes,-y-axes,-and-legend" data-toc-modified-id="Step-17.-Adjust-the-figure-size-and-the-font-size-of-the-labels-on-the-x-axes,-y-axes,-and-legend-4.3.17"><span class="toc-item-num">4.3.17&nbsp;&nbsp;</span>Step 17. Adjust the figure size and the font size of the labels on the x-axes, y-axes, and legend</a></span></li><li><span><a href="#Step-18.-Save-the-figure-to-a-file" data-toc-modified-id="Step-18.-Save-the-figure-to-a-file-4.3.18"><span class="toc-item-num">4.3.18&nbsp;&nbsp;</span>Step 18. Save the figure to a file</a></span></li><li><span><a href="#Final-complete-script-(with-our-final-output)" data-toc-modified-id="Final-complete-script-(with-our-final-output)-4.3.19"><span class="toc-item-num">4.3.19&nbsp;&nbsp;</span>Final complete script (with our final output)</a></span></li><li><span><a href="#Published-figure-(for-comparison)" data-toc-modified-id="Published-figure-(for-comparison)-4.3.20"><span class="toc-item-num">4.3.20&nbsp;&nbsp;</span>Published figure (for comparison)</a></span></li></ul></li><li><span><a href="#Part-2:-Recreate-Figure-1-(subplots-a-e)-using-the-preceding-code-as-a-template" data-toc-modified-id="Part-2:-Recreate-Figure-1-(subplots-a-e)-using-the-preceding-code-as-a-template-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Part 2: Recreate Figure 1 (subplots a-e) using the preceding code as a template</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# ## Purpose
# Chemical constituents measured in ice cores are often visualized in a standard format, with figures produced by proprietary or closed tools. Such tools present an extra step that requires a context switch in the process of analyzing and visualizing results. Python and its many machine learning, numerical computation, and visualization libraries together with Jupyter notebooks offer a unified alternative that permits researchers to analyze and visualize ice core datasets in a single, highly-integrated ecosystem. This Jupyter notebook uses exclusively open-source Python libraries (specifically NumPy, Matplotlib, and Pandas) to create a readily reproducible, publication quality figure. We demonstrate the utility of the notebook as a template for ice core researchers engaging in open science by recreating multiple figures published by Schupbach et al. in Nature Communications, 16 April 2018. This notebook provides a step-by-step guide to systematically recreate two figures using Schupbach's original data.
# 
# ## Technical contributions
# - This notebook presents an annotated, step-by-step template to create publication-quality figures presenting ice
#   core chemistry data using open-source Python libraries.
# - Two figures from an article by [Schupbach et al.](./nature.comm.2018/schupbach-nature-communications-2018.pdf)
#   that appeared in *Nature Communications*, 16 April 2018, are reproduced to demonstrate
#   how to use Python to visualize ice core data.
# - Part 1: First, as closely as possible, we will reproduce [Figure 2](./nature.comm.2018/Fig2.jpg)
#   as published in *Nature* using the datasets provided by the authors.
# - Part 2: Then, we will use Part 1 as a model to reproduce [Figure 1](./nature.comm.2018/Fig1.jpg)
#   (subplots a-e only).
# 
# 
# ## Methodology
# A typical visualization of ice core data is shown, step-by-step, with explanations.
# Briefly, the steps in the process are:
# 1. Prepare the data and initialize a figure with four empty axes.
# 2. Move the y-axis labels and tick marks of every other plot to the right-hand side.
# 3. Remove extraneous spines (lines).
# 4. Draw the tick marks inside the plot area.
# 5. Plot the data in a light shade of each selected color.
# 6. Use a log scale for the y-axis of slected plots.
# 7. Plot a running average of the data using a darker shade of each selected color.
# 8. Add horizontal dashed lines to show the early Holocene average.
# 9. Plot lines in the final subplot, and create a legend to label them.
# 10. Draw vertical gridlines common to all plots in the figure.
# 11. Adjust the axes (remove horizontal space, tweak tick settings) to match the published figure.
# 12. Draw a depth scale along the top of the figure.
# 13. Remove extraneous spines (lines) created by step 12.
# 14. Plot gray bands in subplots a-c.
# 15. Adjust the limits of the y-axes to match the published figure.
# 16. Add annotations to the figure.
# 17. Adjust the figure size and the font size of the labels on the x-axes, y-axes, and legend.
# 18. Save the figure to a file.
# 
# The code used to produce the facimile of Figure 2 (Part 1) is then used as
# a template to produce a facimile of Figure 1 (subplots a-e) (Part 2).
# 
# ## Results
# ### Part 1
# 
# | Figure 2 (as published in Nature Communications [[4]](#4)) | The resulting facimile of Figure 2 | 
# | - | - |
# | ![Fig2.jpg](attachment:Fig2.jpg) | ![OurFig2.png](attachment:OurFig2.png) |
# 
# 
# 
# 
# ### Part 2
# 
# | Figure 1 (as published in Nature Communications [[4]](#4)) | The template deleveloped in Part 1 was adapted to produce the following facimile of Figure 1 (subplots a-e only) |
# | - | - |
# | ![Fig1.jpg](attachment:Fig1.jpg) | ![OurFig1.png](attachment:OurFig1.png) |
# 
# ## Keywords
# keywords=["ice core", "visualization", "climate", "climate change", "reproducible"]
# 
# ## Citation
# Markowsky, L., and Scheick, J. "Visualizing Ice Core Datasets in Python Using a Jupyter Notebook Template," 2022.
# 
# ## Future work
# The authors' future work based on this notebook will be to modularize the code and then to:
# - Create a Jupyter book, with the introductory material (subsections 4.1 and 4.2) expanded and separated into a separate notebook. This Jupyter book will be designed for use by novice Python programmers and especially crafted for use in a classroom setting.
# - Develop and release a Python package, designed for use by ice core scientists wishing to use a more flexible, or simply a Python-based, tool to create this well-known type of visualization of chemical constituents in ice core datasets.
# 
# ## Acknowledgements 
# The authors thank the organizers of the NSF 2019 Arctic Data Workshop, held at the University of Maine, where a preliminary version of this notebook was presented. The authors also thank the reviewers for their helpful remarks.
# 
# ## Copyright and License
# Copyright 2022 L. Markowsky and J. Scheick. This work is is distributed under the terms of the GNU General Public License (GPLv3) [[1]](#1).

# # Setup
# 
# ## Library import

# In[1]:


# Data manipulation
import numpy as np
import pandas as pd

# Visualizations
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


# # Source data
# All files (paper in PDF format, datasets, figures, and supplementary information)
# were downloaded from [www.nature.com](https://www.nature.com/articles/s41467-018-03924-3)
# on 30 March 2019. [[4]](#4)
# The original datasets were provided in the form of two Excel files, which were then 
# saved as CSV text files using LibreOffice Calc.
# In this notebook, the data are imported and prepared from both the Excel and CSV text files in subsections 4.1.4 (Exploring data with Pandas) and 4.2.1 (Step 1: Prepare the data and initialize the figure with four empty axes).
# 
# Descriptions of the two datasets, reproduced in the following two subsections, are included at the top of Schupbach et al.'s original Excel files.
# 
# References for the two datasets:
# - Schüpbach et al., Greenland records of aerosol source and atmospheric lifetime changes   from the Eemian to the Holocene, Nature Communications, 2018. https://www.nature.com/articles/s41467-018-03924-3#Sec11	
# - Rasmussen et al., A first chronology for the North Greenland Eemian Ice Drilling (NEEM)   ice core. Climate of the Past 9, 2713–2730, doi:10.5194/cp-9-2713-2013 (2013).	

# ## NEEM ion concentration data in 10 yr resolution	
# 	
# | Column | Description of Data |
# | :-: | :- |	
# | A | NEEM depth in m below the surface of top of 10 yr interval |
# | B | NEEM depth in m below the surface of bottom of 10 yr interval |
# | C | NEEM depth in m below the surface of middle of 10 yr interval |
# | D | GICC05 age of the top of the 10 yr interval applied to the NEEM ice core <br> (Rasmussen et al., 2013) in years before present (where present is defined as 1950). |
# | E | GICC05 age of the bottom of the 10 yr interval applied to the NEEM ice core <br> (Rasmussen et al., 2013) in years before present (where present is defined as 1950). |
# | F | GICC05 age of the middle of the 10 yr interval applied to the NEEM ice core <br> (Rasmussen et al., 2013) in years before present (where present is defined as 1950). |
# | G | mean NH4+ ice concentration of each 10 yr interval in ng/g <br> (missing values indicated by NaN) |
# | H | mean NO3- ice concentration of each 10 yr interval in ng/g <br> (missing values indicated by NaN) |
# | I | mean Na+ ice concentration of each 10 yr interval in ng/g <br> (missing values indicated by NaN) |
# | J | mean Ca2+ ice concentration of each 10 yr interval in ng/g <br> (missing values indicated by NaN) |
# | K | meanSO42- ice concentration of each 10 yr interval in ng/g <br> (missing values indicated by NaN) |

# ## Aerosol source concentrations and atmospheric lifetime in 10 yr resolution	
# 	
# | Column | Description of Data |
# | :-: | :- |	
# | A | NEEM depth in m below the surface of top of 10 yr interval |
# | B | NEEM depth in m below the surface of bottom of 10 yr interval |
# | C | NEEM depth in m below the surface of middle of 10 yr interval |
# | D | GICC05 age of the top of the 10 yr interval applied to the NEEM ice core <br> (Rasmussen et al., 2013) in years before present (where present is defined as 1950). |
# | E | GICC05 age of the bottom of the 10 yr interval applied to the NEEM ice core <br> (Rasmussen et al., 2013) in years before present (where present is defined as 1950). |
# | F | GICC05 age of the middle of the 10 yr interval applied to the NEEM ice core <br> (Rasmussen et al., 2013) in years before present (where present is defined as 1950). |
# | G | mean of NH4+ aerosol concentration at the source for each 10 yr interval in ng/m3 <br> (missing values indicated by NaN) |
# | H | mean + 1 sigma of NH4+ aerosol concentration at the source for each 10 yr interval in ng/m3 <br> (missing values indicated by NaN) |
# | I | mean - 1 sigma of NH4+ aerosol concentration at the source for each 10 yr interval in ng/m3 <br> (missing values indicated by NaN) |
# | J | atmospheric residence time of NH4+ for each 10 yr interval in days | 
# | K | mean of Na+ aerosol concentration at the source for each 10 yr interval in ng/m3 <br> (missing values indicated by NaN) |
# | L | mean + 1 sigma of Na+ aerosol concentration at the source for each 10 yr interval in ng/m3 <br> (missing values indicated by NaN) |
# | M | mean - 1 sigma of Na+ aerosol concentration at the source for each 10 yr interval in ng/m3 <br> (missing values indicated by NaN) |
# | N | atmospheric residence time of Na+ for each 10 yr interval in days | 
# | O | mean of Ca2+ aerosol concentration at the source for each 10 yr interval in ng/m3 <br> (missing values indicated by NaN) |
# | P | mean + 1 sigma of Ca2+ aerosol concentration at the source for each 10 yr interval in ng/m3 <br> (missing values indicated by NaN) |
# | Q | mean - 1 sigma of Ca2+ aerosol concentration at the source for each 10 yr interval in ng/m3 <br> (missing values indicated by NaN) |
# | R | atmospheric residence time of Ca2+ for each 10 yr interval in days |

# # Data Processing and Analysis

# ## A brief introduction to the Python data science ecosystem

# ### Why Python?
# Why spend the time to learn a new language when < *R/Excel/MATLAB* > gets the job done?
# 
# This is a frequently asked question, even among software developers,
# as it is often easier to use a language or tool that you already know well.
# Sometimes, however, a new language or tool can offer benefits not available 
# or not easy to achieve otherwise.

# ### Some of Python's benefits
# The Python ecosystem, and in particular, the Python data science stack, has much to offer:
# 
# - The Python data science stack consists of mature, well-developed and
#   well-documented libraries for analyzing and visualizing data.
# - The Python data science stack is free, open-source, and cross-platform.
# - Although Python, together with its libraries, is an example of a *very high level language,* 
#   well-written programs in the Python ecosystem can have very good performance.
# - Programming in Python yields clean, readable, highly maintainable and reusable source code.
# - Python's large, friendly user community makes it easy to find answers to common problems online.
# - Python has become the most widely used programming language in data science 
#   and machine learning.

# ### An overview of the Python data science stack (with links to resources)
# In addition to *Python* itself, the tools and libraries often used by data scientists include *Jupyter Notebooks, IPython, NumPy, Pandas, Matplotlib, Seaborn, SciPy, Scikit-Learn,* and *Statsmodels.* 
# 
# - ***Python*** is an easy-to-learn, very high level language with 
#   seemingly limitless libraries for every possible purpose. To get 
#   started with Python:
#     - Python Software Foundation. _The Python Tutorial $-$
#       Python 3.10.4 Documentation_, 2001-2022.
#       https://docs.python.org/3/tutorial/index.html
#     - VanderPlas, Jake. _A Whirlwind Tour of Python_, August 2016.
#       https://jakevdp.github.io/WhirlwindTourOfPython/ (book in html)
#       and https://github.com/jakevdp/WhirlwindTourOfPython (full text
#       in Jupyter notebooks)
# 
# 
# - ***Jupyter Notebooks*** and ***IPython*** provide interactive computing and software development environments that encourage an execute-explore workflow as an alternative to the edit-compile-run workflow that long dominated computing. Jupyter notebooks, in particular, are widely used in the data science community to share code, text, and output. _Kernels_ are available to support a variety of languages, including Python, R, C++, Scilab, and MATLAB. The name _Jupyter_ refers to the programming languages Julia, Python and R, and is also a reference to Galileo's notes on his observations of Jupiter and four of its moons. Resources for Jupyter and IPython are abundant, including:
#     - Jupyter/IPython notebook quick start guide:
#       https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html
#     - Jupyter notebook user documentation:
#       https://jupyter-notebook.readthedocs.io/en/stable/notebook.html
#     - VanderPlas, Jake. _Python Data Science Handbook: Essential Tools 
#       for Working with Data, Chapter 1: IPython: Beyond Normal Python_, November 2016.
#       https://jakevdp.github.io/PythonDataScienceHandbook/01.00-ipython-beyond-normal-python.html
#       (in html) and
#       https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/01.00-IPython-Beyond-Normal-Python.ipynb
#       (as a Jupyter notebook)
#     - A curated collection of notable Jupyter/IPython notebooks:
#       https://github.com/jupyter/jupyter/wiki
#     - An example of a paper presented as a notebook:
#       https://nbviewer.jupyter.org/github/cossatot/lanf_earthquake_likelihood/blob/master/notebooks/lanf_manuscript_notebook.ipynb
# 
# 
# - ***NumPy,*** a contraction of _Numerical Python,_ provides an efficient multi-dimensional array object called an ```ndarray```. NumPy features fast, elementwise array operations, functions to read/write array-based datasets from/to disk, linear algebra operations, and an API to allow program access to ndarray objects from C/C++ code. To get started with _NumPy:_
#     - NumPy Developers. _NumPy: the absolute basics for beginners_, 2008-2022.
#       https://numpy.org/doc/stable/user/absolute_beginners.html
#     - VanderPlas, Jake. _Python Data Science Handbook: Essential Tools 
#       for Working with Data, Chapter 2: Introduction to NumPy_, November 2016.
#       https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html (in html)
#       and https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/02.00-Introduction-to-NumPy.ipynb (as a Jupyter notebook)
# 
# 
# - ***Pandas,*** a contraction of _Panel Data_ (an econometrics term for multidimensional datasets), is the heart of much data analysis today. _Pandas_ is centered around two data structures: (1) _DataFrame_:  a tabular, column-oriented data structure; and (2) _Series_: a one-dimensional labeled array object. _Pandas_ provides data preparation and cleaning, data manipulation capabilities similar to SQL, aggregation, subset selection, and sophisticated indexing. To get started with _Pandas:_
#     - Pandas Getting Started Tutorials: https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html
#     - 10 Minutes to Pandas: https://pandas.pydata.org/docs/user_guide/10min.html
#     - Pandas Cookbook: http://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html
#     - VanderPlas, Jake. _Python Data Science Handbook: Essential Tools 
#       for Working with Data, Chapter 3: Data Manipulation with Pandas_, November 2016.
#       https://jakevdp.github.io/PythonDataScienceHandbook/03.00-introduction-to-pandas.html (in html)
#       and https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.00-Introduction-to-Pandas.ipynb (as a Jupyter notebook)
# 
# 
# - ***Matplotlib*** and ***Seaborn*** are two widely-used Python plotting libraries. Both produce publication quality plots. _Seaborn_ is built on _Matplotlib_ and may be easier to use. _Matplotlib,_ however, provides lower-level control and may be preferable when a specific rendering is required. To get started:
#     - Matplotlib Tutorial: https://matplotlib.org/stable/tutorials/index.html
#     - Matplotlib Examples: https://matplotlib.org/stable/gallery/index.html
#     - VanderPlas, Jake. _Python Data Science Handbook: Essential Tools 
#       for Working with Data, Chapter 4: Visualization with Matplotlib_, November 2016.
#       https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html
#       (in html)
#       and https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.00-Introduction-To-Matplotlib.ipynb (as a Jupyter notebook)
#     - Seaborn User Guide and Tutorial: https://seaborn.pydata.org/tutorial.html
#     - Seaborn Example Gallery: https://seaborn.pydata.org/examples/index.html
# 
# 
# - ***SciPy,*** a collection of scientific computing packages, includes _scipy.spatial_ for spatial data structures and algorithms and _scipy.stats_ for statistics. To get started with _SciPy_:
#     - SciPy User Guide: https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide
# 
# 
# - ***Scikit-Learn*** and ***Statsmodels*** are used for machine learning and statistical analysis. _Scikit-Learn,_ a machine learning toolkit, provides functions for classification, regression, clustering, dimensionality reduction, and model selection. The website for _Statsmodels,_ a statistical analysis package, shows numerous examples, including: linear regression models, robust regression, and time series analysis. To get started:
#     - VanderPlas, Jake. _Python Data Science Handbook: Essential Tools 
#       for Working with Data, Chapter 5: Machine Learning_, November 2016.
#       https://jakevdp.github.io/PythonDataScienceHandbook/05.00-machine-learning.html
#       (in html)
#       and https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.00-Machine-Learning.ipynb (as a Jupyter notebook)
#     - Scikit-Learn's home page: https://scikit-learn.org/stable/
#     - Statsmodels: Getting Started: https://www.statsmodels.org/stable/gettingstarted.html
#     - Statsmodels Examples: https://www.statsmodels.org/stable/examples/index.html

# -------
# ## A first look at NumPy, Pandas, and Matplotlib

# ### Exploring a namespace

# We have already imported NumPy and Pandas using standard naming 
# conventions, in part duplicated here for convenience:
# 
# ``` python
# import numpy as np
# import pandas as pd
# ```
# 
# Once a library has been imported, tab completion can be used in a Jupyter 
# notebook code cell to see everything that's included in a particular library. 
# To explore the NumPy namespace, uncomment the line in the next code cell, 
# and then enter a tab at the end of the line to view a dropdown box of all 
# constants and functions available to the user. 
# (The line in the following cell is commented out simply to enable the 
# notebook to run without errors.)
# 
# For example, in the NumPy namespace, enter a *$<$tab$>$* after np. to see the
# dropdown menu. To rapidly look for all names in the namespace beginning with
# the letter 'p', type 'p'. The constant 'pi' can then be selected, and
# as usual, Ctrl-Enter will execute the cell, showing the value of $\pi$, 
# a global constant in the NumPy namespace.

# In[2]:


#np.


# As an example of a function, enter a *$<$tab$>$* after np., type 'cor' 
# to show everything in the namespace beginning with 'cor', select
# 'correlate' from the dropdown menu, and finally Ctrl-Enter to execute 
# the cell to see the value of correlate, a function implemented in NumPy.

# In[3]:


#np.


# ### Accessing built-in help

# Appending ```?``` or ```??``` to a function name returns built-in help:
# - ```?``` shows the Python docstring
# - ```??``` shows the source code (which includes the docstring at the top)
# 
# The docstring includes an explanation of each parameter and the
# return value, if any, and may also examples of the function's use, 
# as seen by executing the cells below.

# In[4]:


get_ipython().run_line_magic('pinfo', 'np.correlate')


# In[5]:


get_ipython().run_line_magic('pinfo2', 'np.correlate')


# ### Three fundamental NumPy and Pandas data structures: ndarray, Series, and DataFrame

# The basic data type in NumPy is the n-dimensional array, or ```ndarray```.
# The values in the array are all of the same type.

# In[6]:


get_ipython().run_line_magic('pinfo', 'np.ndarray')


# The basic data types in Pandas are ```Series``` and ```DataFrame```.
# The ```Series``` object is like an ```ndarray```, only with an index 
# (which could be names or other identifying information about the array).

# In[7]:


get_ipython().run_line_magic('pinfo', 'pd.Series')


# The ```DataFrame``` holds a table of values, where each column is a 
# ```Series```. While each column has a particular type, different columns 
# may have different types. Like indices, columns can be named to make it easier to reference certain ones.

# In[8]:


get_ipython().run_line_magic('pinfo', 'pd.DataFrame')


# ### Exploring an ice core dataset with Pandas

# Calling the function ```pd.read_csv(<filename>)``` reads a CSV text file 
# into a ```DataFrame```. 
# 
# In the following cell, ```sep=','``` is superfluous (because a comma 
# is the default separator), but the same function can read tab-separated 
# values by specifying ```sep='\t'```.
# 
# The ```skiprows=``` keyword lets Pandas know to not read in the first x rows of the file.
# This is necessary when those first rows contain metadata or other non-tabulated data.
# Here we have manually determined how many rows need to be skipped and entered those values.

# In[9]:


# Read data from two csv files into two DataFrames.
supp_data_1 = pd.read_csv('data/supplementary-data-1.csv', sep=',', skiprows=18)
supp_data_2 = pd.read_csv('data/supplementary-data-2.csv', sep=',', skiprows=27,
                          na_values=['NaN', '#VALUE!'])


# In Python, missing data is often indicated by the ```None```, or in
# the case of missing numerical data, by ```NaN```, which stands for 
# *Not a Number*. In the following (abbreviated) table of values, 
# ```NaN``` is used for the missing data, which appeared as both ```NaN``` 
# and ```#VALUE!``` entries in Schupbach et al.'s original datasets.

# In[10]:


supp_data_1


# The data were initially downloaded as Excel files.
# We could alternatively read the Excel file directly into a Pandas dataframe without first converting the Excel file to an intermediate CSV text file.
# Notice the slightly different keyword inputs required for this function.

# In[11]:


supp_data_1_xlsx = pd.read_excel('data/supplementary-data-1.xlsx',
                                 sheet_name='Blatt1', skiprows=18)
supp_data_1_xlsx


# We can gather information about our data using some of Panda's methods.

# In[12]:


supp_data_1.shape


# In[13]:


supp_data_1.columns


# In[14]:


supp_data_2.shape


# In[15]:


supp_data_2.columns


# Selecting a subset of columns produces a view into the DataFrame.
# This can make large DataFrames easier to work with.
# For efficiency, nothing is copied.

# In[16]:


selectSuppDataCols = supp_data_1[['depth_mid (m)', 'ageGICC05_mid (yr BP)',
                                  'NH4 (ng/g)', 'NO3 (ng/g)', 'Na (ng/g)',
                                  'Ca (ng/g)', 'SO4 (ng/g)']]


# A powerful tool in Pandas is called grouping.
# Grouping allows us to bin data and calculate statistics about each group.
# Here we reduce the number of rows by grouping samples taken in 1 meter segments 
# and then find the ```mean``` of each group.

# In[17]:


groupedSelectSuppData = selectSuppDataCols.round({'depth_mid (m)':0}).groupby('depth_mid (m)').mean()
groupedSelectSuppData


# The ```describe``` method computes some statistics for each DataFrame column.

# In[18]:


groupedSelectSuppData.describe()


# ### A brief look at Seaborn

# Although this notebook uses Matplotlib to create visualizations, for some 
# applications, Matplotlib's low-level control may be more complex than is 
# required. _Seaborn,_ like Matplotlib, produces publication quality plots 
# but is easier to use. 
# 
# We have already imported Seaborn using the standard naming convention, 
# duplicated here for convenience:
# 
# ``` python
# import seaborn as sns
# ```
# 
# As before, to explore the Seaborn namespace, uncomment the line in the next code
# cell, and then enter a tab at the end of the line to view a dropdown box of all 
# constants and functions available to the user. 

# In[19]:


#sns.


# Numerous common visualizations using Seaborn can be constructed in minutes 
# by modifying examples found in the tutorial and gallery. The links below are
# duplicated from subsection 4.1.3 for convenience:
# - Seaborn User Guide and Tutorial: https://seaborn.pydata.org/tutorial.html
# - Seaborn Example Gallery: https://seaborn.pydata.org/examples/index.html
# 
# For example, we can use _Seaborn_ to quickly plot pairwise relationships in 
# the ice core dataset (as selected and grouped in subsection 4.2.4) using the 
# single Python statement:

# In[20]:


sns.pairplot(groupedSelectSuppData[['NH4 (ng/g)', 'NO3 (ng/g)', 'Na (ng/g)',
                                  'Ca (ng/g)', 'SO4 (ng/g)']].dropna())


# ### Getting started with Matplotlib

# In this notebook, we will use Matplotlib to programmatically create a 
# specialized figure with subplots and customized axes. By convention, 
# Matplotlib's ```pyplot``` and ```ticker``` APIs are imported using the 
# statements:
# ``` python
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# ```
# 
# These namespaces can be explored by removing the # and entering a tab 
# at the end of the lines:

# In[21]:


#plt.


# In[22]:


#ticker.


# In Matplotlib, a figure contains subplots arranged in a grid, as shown in 
# this example from Chapter 9 of _Python for Data Analysis: Data Wrangling 
# with Pandas, NumPy, and IPython, Second Edition,_ by Wes McKinney (O'Reilly, 
# September 2018) [[2]](#2).
# Unless otherwise specified, data are plotted on the most recently created 
# subplot, as in the line
# ``` python
# plt.plot(np.random.randn(50).cumsum(), 'k--')
# ``` 
# which plots points on the third subplot, _ax3,_ just created in the preceding 
# line. To select a subplot on which to plot data, use the name of the subplot, 
# as shown in the final two lines:
# ``` python
# ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
# ```

# In[23]:


fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
plt.plot(np.random.randn(50).cumsum(), 'k--')
ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))


# -------
# ## Part 1: Recreate Figure 2, step-by-step, with intermediate results
# In this section, we will create a reasonable facimile of Figure 2, as published in 
# Nature Communications, one step at a time, showing the resulting figure after each
# step.
# 
# 
# | Figure 2 (as published in Nature Communications [[4]](#4)) | The resulting facimile of Figure 2 | 
# | - | - |
# | ![Fig2.jpg](attachment:Fig2.jpg) | ![OurFig2.png](attachment:OurFig2.png) |
# 
# 
# 

# ### Step 1: Prepare the data and initialize the figure with four empty axes
# Figure 2 uses only Supplentary Data 2, which we've already read into a DataFrame
# in subsection 4.2.4.

# In[24]:


supp_data_2


# Listing the column names shows that Supplentary Data 2 lacks a column
# for age in kyr, so first create a new column and add it to the DataFrame.

# In[25]:


supp_data_2.columns


# In[26]:


# Add column for age in kyr to the DataFrame.
supp_data_2['age_kyr'] = supp_data_2['ageGICC05_mid (yr BP)'] / 1000


# Now, listing the columns and viewing the dataset confirm that the
# new column for kyr has been added.

# In[27]:


supp_data_2.columns


# In[28]:


supp_data_2


# Now that the data has been prepared, create a new figure with four subplots.
# Matplotlib supports a subset of latex, so we can use familiar latex format to
# label the y-axes. For more, see the Matplotlib documentation: 
# https://matplotlib.org/stable/tutorials/text/mathtext.html

# In[29]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')


# ### Step 2: Position the y-axis labels and tick marks 
# The 2nd and 4th plots should have y-axis labels and tick marks on the right
# using the Python code:
# ``` python
# for i in [1, 3]:
#     axes[i].yaxis.set_label_position('right')
#     axes[i].tick_params(which='both', left=False, right=True,
#                         labelleft=False, labelright=True)
# ```
# Note that in this and each of the following steps, the newly added code 
# is highlighted by '##########' both above and below.

# In[30]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))

###############################################################################
# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)
###############################################################################

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')


# ### Step 3: Remove unnecessary spines
# Next, we remove lines (spines) that don't appear in Figure 2 as published 
# in Nature by adding:
# ``` python
# for i in [0, 2]:
#     axes[i].spines['right'].set_visible(False)
# for i in [1, 3]:
#     axes[i].spines['left'].set_visible(False)
# for i in [0, 1, 2]:
#     axes[i].spines['bottom'].set_visible(False)
# for i in [1, 2, 3]:
#     axes[i].spines['top'].set_visible(False)
# ```

# In[31]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

###############################################################################    
# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [0, 2]:
    axes[i].spines['right'].set_visible(False)
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)
###############################################################################


# ### Step 4: Configure the tick marks
# To draw the tick marks inside the plot area, we adjust the tick_params
# by setting the direction to 'in':
# ``` python
# for i in range(4):
#     axes[i].tick_params(which='both', direction='in')
# ```

# In[32]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))

###############################################################################
# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')
###############################################################################

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [0, 2]:
    axes[i].spines['right'].set_visible(False)
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')


# ### Step 5: Plot data in subplots a-c
# Plot the data in subplots a-c using a lighter shade (by setting alpha=0.4) 
# of each selected color:
# ``` python
# supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
#                  color='green', alpha=0.4, legend=False)
# supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
#                  color='blue', alpha=0.4, legend=False)
# supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
#                  color='red', alpha=0.4, legend=False)
# ```

# In[33]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')
    
# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [0, 2]:
    axes[i].spines['right'].set_visible(False)
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)

###############################################################################
# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)
###############################################################################

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')


# ### Step 6: Use a log scale for selected subplots
# Next, we use a log scale for the y-axis of subplots a-c, but we don't
# use exponential format for the y-axis labels:
# ``` python
# for i in range(3):
#     axes[i].set_yscale('log')
#     axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())
# ```

# In[34]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')
    
###############################################################################
# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())
###############################################################################

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [0, 2]:
    axes[i].spines['right'].set_visible(False)
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')


# ### Step 7: Plot a running average
# Calculate and plot the smoothed function values using a darker line.
# 
# To do this, first we use min_periods to remove extraneous "mean" values 
# when the actual data is "NaN":
# ``` python
# supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
# supp_data_2_rolling_mean = supp_data_2_smoothed.mean()
# ```
# Then, the smoothed function value is represented by plotting the 21 
# point running means of the 10 year data, as described in the caption for 
# Figure 2, on page 4 of Schupbach et al. [[4]](#4).
# ``` python
# supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
#                               color='green', legend=False)
# supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
#                               color='blue', legend=False)
# supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
#                               color='red', legend=False)
# ```

# In[35]:


supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()
supp_data_2_rolling_mean


# In[36]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [0, 2]:
    axes[i].spines['right'].set_visible(False)
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

###############################################################################
# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)
###############################################################################

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')


# ### Step 8: Draw horizonal dashed lines
# Next, we plot the dashed lines indicating the early Holocene average,
# using dates selected based on the title of Figure 3, on page 6 of Schupbach 
# et al. [[4]](#4).
# 
# Before modifying the code, we first explore how to find the mean of each 
# column of interest.

# In[37]:


early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_data_2.mean()


# Then, based on the exploration above, we modify the code by adding:
# ``` python
# early_hol_data_2 = (
#     supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
#                [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
# early_hol_mean = early_hol_data_2.mean()
# axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
#                 color='black', linestyle='--')
# axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
#                 color='black', linestyle='--')
# axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
#                 color='black', linestyle='--')
# ```

# In[38]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [0, 2]:
    axes[i].spines['right'].set_visible(False)
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)
###############################################################################
# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')
###############################################################################

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')


# ### Step 9: Plot data in subplot d

# The fourth subplot is a bit different from the first three.
# Rather than a single value plotted with a running average, subplot 
# d will have three values, plotted as colored lines together with a 
# legend to identify them. Although the results of this cell produce 
# a legend that is obscured by the plotted lines, we will fix this 
# soon.
# ``` python
# supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
#                  color='green', label='${NH_4}^+$')
# supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
#                  color='blue', label='$Na^+$')
# supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
#                  color='red', label='$Ca^{2+}$')
# axes[3].legend(loc='upper left', frameon=False)
# ```

# In[39]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [0, 2]:
    axes[i].spines['right'].set_visible(False)
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

###############################################################################
# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')
axes[3].legend(loc='upper left', frameon=False)
###############################################################################

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')


# ### Step 10: Draw vertical gridlines
# 
# The first step in drawing the vertical gridlines consists of two for loops:
# ``` python
# for i in range(4):
#     axes[i].xaxis.grid(which='major')
# for i in [0, 2]:
#     axes[i].spines['right'].set_color('lightgrey')
# ```

# In[40]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [0, 2]:
    axes[i].spines['right'].set_visible(False)
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')
axes[3].legend(loc='upper left', frameon=False)

###############################################################################
# Draw vertical gridlines.
for i in range(4):
    axes[i].xaxis.grid(which='major')
for i in [0, 2]:
    axes[i].spines['right'].set_color('lightgrey')
###############################################################################

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')


# ### Step 11: Adjust axes to match the published figure
# The vertical gridlines produced by the previous cell are disconnected, 
# the gridlines don't show up on the left and right edges,
# and the dark tick marks need to be adjusted to match the figure. To make
# these changes, we will:
# 
# - Remove the space between the subplots:
# ``` python
# fig.subplots_adjust(hspace=0)
# ```
# - By commenting out (and in subsequent cells, removing)
#   the following for loop, show the rightmost gridline in 
#   subplots a and c (axes 0 and 2).
# ``` python
# #for i in [0, 2]:
# #    axes[i].spines['right'].set_visible(False)
# ```
# - Set x-axis ticks (default ticks were drawn every 20 kyr):
# ``` python
# NUM_XTICKS = 14
# axes[3].set_xlim(0, 130)
# axes[3].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
# axes[3].xaxis.set_minor_locator(ticker.LinearLocator(10 * NUM_XTICKS - 1))
# ```
# - Show x-axis tick marks only the bottommost plot:
# ``` python
# for i in range(3):
#     axes[i].tick_params(axis='x', which='both', bottom=False)
# ```

# In[41]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))
###############################################################################
fig.subplots_adjust(hspace=0)
###############################################################################

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
###############################################################################
#for i in [0, 2]:
#    axes[i].spines['right'].set_visible(False)
###############################################################################
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')
axes[3].legend(loc='upper left', frameon=False)

# Draw vertical gridlines.
for i in range(4):
    axes[i].xaxis.grid(which='major')
for i in [0, 2]:
    axes[i].spines['right'].set_color('lightgrey')

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

###########################################################################
# Set x-axis ticks (default ticks were drawn every 20 kyr).
NUM_XTICKS = 14
axes[3].set_xlim(0, 130)
axes[3].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
axes[3].xaxis.set_minor_locator(ticker.LinearLocator(10 * NUM_XTICKS - 1))

# Show x-axis tick marks only on the bottommost plot.
for i in range(3):
    axes[i].tick_params(axis='x', which='both', bottom=False)
###########################################################################


# ### Step 12: Draw a depth scale along top of figure
# Draw an x-axis using an alternate scale (depth) along top of figure.
# First, explore how to plot the depth to correspond to the date axis
# using a lambda function.

# In[42]:


supp_data_2.loc[supp_data_1['depth_mid (m)'] >= 1700, 'ageGICC05_mid (yr BP)']


# In[43]:


supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'ageGICC05_mid (yr BP)'].min()


# In[44]:


supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 2400, 'age_kyr'].min()


# In[45]:


neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2400]
supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'age_kyr'].min()
depth_to_kyr = lambda d: supp_data_2.loc[supp_data_1['depth_mid (m)'] >= d, 'age_kyr'].min()

ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
ax_top_xticks


# In[46]:


kyr_to_depth = lambda y: supp_data_2.loc[supp_data_2['age_kyr'] <= y, 'depth_mid (m)'].max()
print(kyr_to_depth(130))


# Then, using the exploration above (repeated here as it will appear in the code): 
# ``` python
# ax_top = axes[0].twiny()
# ax_top.set_xlabel('NEEM depth (m)')
# ax_top.xaxis.set_label_position('top')
# ax_top.tick_params(top=True)
# neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
#                      2200, 2400]
# supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'age_kyr'].min()
# depth_to_kyr = lambda d: supp_data_2.loc[supp_data_2['depth_mid (m)'] >= d,
#                                          'age_kyr'].min()
# ```
# Draw an x-axis using an alternate scale (depth) along top of figure:
# 
# ``` python
# ax_top.set_xlim(0, 130)
# ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
# ax_top.set_xticks(ax_top_xticks)
# ax_top.set_xticklabels(neem_depth_labels, rotation=90)
# ax_top.tick_params(direction='in')
# ```

# In[47]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))
fig.subplots_adjust(hspace=0)

###########################################################################
# Draw an x-axis using an alternate scale (depth) along top of figure.
ax_top = axes[0].twiny()
ax_top.set_xlabel('NEEM depth (m)')
ax_top.xaxis.set_label_position('top')
ax_top.tick_params(top=True)
neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
                     2200, 2400]
supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'age_kyr'].min()
depth_to_kyr = lambda d: supp_data_2.loc[supp_data_2['depth_mid (m)'] >= d,
                                         'age_kyr'].min()
ax_top.set_xlim(0, 130)
ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
ax_top.set_xticks(ax_top_xticks)
ax_top.set_xticklabels(neem_depth_labels, rotation=90)
ax_top.tick_params(direction='in')
###########################################################################

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')
axes[3].legend(loc='upper left', frameon=False)

# Draw vertical gridlines.
for i in range(4):
    axes[i].xaxis.grid(which='major')
for i in [0, 2]:
    axes[i].spines['right'].set_color('lightgrey')

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

# Set x-axis ticks (default ticks were drawn every 20 kyr).
NUM_XTICKS = 14
axes[3].set_xlim(0, 130)
axes[3].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
axes[3].xaxis.set_minor_locator(ticker.LinearLocator(10 * NUM_XTICKS - 1))

# Show x-axis tick marks only on the bottommost plot.
for i in range(3):
    axes[i].tick_params(axis='x', which='both', bottom=False)


# ### Step 13: Remove extraneous spines
# Remove the right and bottom spines created by the new x-axis by setting their visibility to False:
# ``` python
# ax_top.spines['right'].set_visible(False)
# ax_top.spines['bottom'].set_visible(False)
# ```

# In[48]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))
fig.subplots_adjust(hspace=0)

# Draw an x-axis using an alternate scale (depth) along top of figure.
ax_top = axes[0].twiny()
ax_top.set_xlabel('NEEM depth (m)')
ax_top.xaxis.set_label_position('top')
ax_top.tick_params(top=True)
neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
                     2200, 2400]
supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'age_kyr'].min()
depth_to_kyr = lambda d: supp_data_2.loc[supp_data_2['depth_mid (m)'] >= d,
                                         'age_kyr'].min()
ax_top.set_xlim(0, 130)
ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
ax_top.set_xticks(ax_top_xticks)
ax_top.set_xticklabels(neem_depth_labels, rotation=90)
ax_top.tick_params(direction='in')

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)
###########################################################################
ax_top.spines['right'].set_visible(False)
ax_top.spines['bottom'].set_visible(False)
###########################################################################

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')
axes[3].legend(loc='upper left', frameon=False)

# Draw vertical gridlines.
for i in range(4):
    axes[i].xaxis.grid(which='major')
for i in [0, 2]:
    axes[i].spines['right'].set_color('lightgrey')

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

# Set x-axis ticks (default ticks were drawn every 20 kyr).
NUM_XTICKS = 14
axes[3].set_xlim(0, 130)
axes[3].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
axes[3].xaxis.set_minor_locator(ticker.LinearLocator(10 * NUM_XTICKS - 1))

# Show x-axis tick marks only on the bottommost plot.
for i in range(3):
    axes[i].tick_params(axis='x', which='both', bottom=False)


# ### Step 14: Plot gray uncertainty bands
# In subplots 2a, 2b, and 2c, plot light gray uncertainty bands:
# ``` python
# x = supp_data_2['age_kyr']
# axes[0].fill_between(x, supp_data_2['NH4source+1sigma (ng/m3)'],
#                      supp_data_2['NH4source-1sigma (ng/m3)'],
#                      facecolor='lightgray')
# axes[1].fill_between(x, supp_data_2['Nasource+1sigma (ng/m3)'],
#                      supp_data_2['Nasource-1sigma (ng/m3)'],
#                      facecolor='lightgray')
# axes[2].fill_between(x, supp_data_2['Casource+1sigma (ng/m3)'],
#                      supp_data_2['Casource-1sigma (ng/m3)'],
#                      facecolor='lightgray')
# ```

# In[49]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))
fig.subplots_adjust(hspace=0)

# Draw an x-axis using an alternate scale (depth) along top of figure.
ax_top = axes[0].twiny()
ax_top.set_xlabel('NEEM depth (m)')
ax_top.xaxis.set_label_position('top')
ax_top.tick_params(top=True)
neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
                     2200, 2400]
supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'age_kyr'].min()
depth_to_kyr = lambda d: supp_data_2.loc[supp_data_2['depth_mid (m)'] >= d,
                                         'age_kyr'].min()
ax_top.set_xlim(0, 130)
ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
ax_top.set_xticks(ax_top_xticks)
ax_top.set_xticklabels(neem_depth_labels, rotation=90)
ax_top.tick_params(direction='in')

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)
ax_top.spines['right'].set_visible(False)
ax_top.spines['bottom'].set_visible(False)

###############################################################################
# Subplots 2a, 2b, and 2c.
# Plot gray bands first.
x = supp_data_2['age_kyr']
axes[0].fill_between(x, supp_data_2['NH4source+1sigma (ng/m3)'],
                     supp_data_2['NH4source-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[1].fill_between(x, supp_data_2['Nasource+1sigma (ng/m3)'],
                     supp_data_2['Nasource-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[2].fill_between(x, supp_data_2['Casource+1sigma (ng/m3)'],
                     supp_data_2['Casource-1sigma (ng/m3)'],
                     facecolor='lightgray')
###############################################################################

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')
axes[3].legend(loc='upper left', frameon=False)

# Draw vertical gridlines.
for i in range(4):
    axes[i].xaxis.grid(which='major')
for i in [0, 2]:
    axes[i].spines['right'].set_color('lightgrey')

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

# Set x-axis ticks (default ticks were drawn every 20 kyr).
NUM_XTICKS = 14
axes[3].set_xlim(0, 130)
axes[3].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
axes[3].xaxis.set_minor_locator(ticker.LinearLocator(10 * NUM_XTICKS - 1))

# Show x-axis tick marks only on the bottommost plot.
for i in range(3):
    axes[i].tick_params(axis='x', which='both', bottom=False)


# ### Step 15: Tweak the y-axis settings
# Tweak the y-axis settings to correspond to the published figure:
# ``` python
# axes[0].set_ylim(1, 3000)
# axes[1].set_ylim(10, 1000)
# axes[2].set_ylim(10, 10000)
# axes[3].set_ylim(0, 25)
# ```

# In[50]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))
fig.subplots_adjust(hspace=0)

# Draw an x-axis using an alternate scale (depth) along top of figure.
ax_top = axes[0].twiny()
ax_top.set_xlabel('NEEM depth (m)')
ax_top.xaxis.set_label_position('top')
ax_top.tick_params(top=True)
neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
                     2200, 2400]
supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'age_kyr'].min()
depth_to_kyr = lambda d: supp_data_2.loc[supp_data_2['depth_mid (m)'] >= d,
                                         'age_kyr'].min()
ax_top.set_xlim(0, 130)
ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
ax_top.set_xticks(ax_top_xticks)
ax_top.set_xticklabels(neem_depth_labels, rotation=90)
ax_top.tick_params(direction='in')

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)
ax_top.spines['right'].set_visible(False)
ax_top.spines['bottom'].set_visible(False)

# Subplots 2a, 2b, and 2c.
# Plot gray bands first.
x = supp_data_2['age_kyr']
axes[0].fill_between(x, supp_data_2['NH4source+1sigma (ng/m3)'],
                     supp_data_2['NH4source-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[1].fill_between(x, supp_data_2['Nasource+1sigma (ng/m3)'],
                     supp_data_2['Nasource-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[2].fill_between(x, supp_data_2['Casource+1sigma (ng/m3)'],
                     supp_data_2['Casource-1sigma (ng/m3)'],
                     facecolor='lightgray')

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')
axes[3].legend(loc='upper left', frameon=False)

# Draw vertical gridlines.
for i in range(4):
    axes[i].xaxis.grid(which='major')
for i in [0, 2]:
    axes[i].spines['right'].set_color('lightgrey')

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

# Set x-axis ticks (default ticks were drawn every 20 kyr).
NUM_XTICKS = 14
axes[3].set_xlim(0, 130)
axes[3].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
axes[3].xaxis.set_minor_locator(ticker.LinearLocator(10 * NUM_XTICKS - 1))

# Show x-axis tick marks only on the bottommost plot.
for i in range(3):
    axes[i].tick_params(axis='x', which='both', bottom=False)

###############################################################################    
# Tweak y-axis settings to correspond to published figure.
axes[0].set_ylim(1, 3000)
axes[1].set_ylim(10, 1000)
axes[2].set_ylim(10, 10000)
axes[3].set_ylim(0, 25)
###############################################################################


# ### Step 16: Annotate the figure
# In this step, we annotate the figure. First, add 'a', 'b', 'c', and 'd' to the subplots using the code:
# ``` python
# axes[0].annotate('a', xy=(0.05, 0.85), xycoords='axes fraction',
#                  fontsize=20, fontweight='bold')
# axes[1].annotate('b', xy=(0.95, 0.85), xycoords='axes fraction',
#                  fontsize=20, fontweight='bold')
# axes[2].annotate('c', xy=(0.05, 0.85), xycoords='axes fraction',
#                  fontsize=20, fontweight='bold')
# axes[3].annotate('d', xy=(0.95, 0.85), xycoords='axes fraction',
#                  fontsize=20, fontweight='bold')
# ```
# Then, add the notations 'Hol', 'LGM', 'Warm interstadials', 'Cold interstadials',
# and 'Eem' to subplot c:
# ``` python
# axes[2].annotate('Hol', xy=(5, 80), xycoords='data', fontsize=16)
# axes[2].annotate('LGM', xy=(20, 1000), xycoords='data', fontsize=16)
# axes[2].annotate('Cold stadials', xy=(34, 1000), xycoords='data', fontsize=16)
# axes[2].annotate('Warm interstadials', xy=(29, 12), xycoords='data', fontsize=16)
# axes[2].annotate('Eem', xy=(120, 80), xycoords='data', fontsize=16)
# ```

# In[51]:


# Figure 2
# Create a new figure with four subplots.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(15,10))
fig.subplots_adjust(hspace=0)

# Draw an x-axis using an alternate scale (depth) along top of figure.
ax_top = axes[0].twiny()
ax_top.set_xlabel('NEEM depth (m)')
ax_top.xaxis.set_label_position('top')
ax_top.tick_params(top=True)
neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
                     2200, 2400]
supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'age_kyr'].min()
depth_to_kyr = lambda d: supp_data_2.loc[supp_data_2['depth_mid (m)'] >= d,
                                         'age_kyr'].min()
ax_top.set_xlim(0, 130)
ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
ax_top.set_xticks(ax_top_xticks)
ax_top.set_xticklabels(neem_depth_labels, rotation=90)
ax_top.tick_params(direction='in')

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)
ax_top.spines['right'].set_visible(False)
ax_top.spines['bottom'].set_visible(False)

# Subplots 2a, 2b, and 2c.
# Plot gray bands first.
x = supp_data_2['age_kyr']
axes[0].fill_between(x, supp_data_2['NH4source+1sigma (ng/m3)'],
                     supp_data_2['NH4source-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[1].fill_between(x, supp_data_2['Nasource+1sigma (ng/m3)'],
                     supp_data_2['Nasource-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[2].fill_between(x, supp_data_2['Casource+1sigma (ng/m3)'],
                     supp_data_2['Casource-1sigma (ng/m3)'],
                     facecolor='lightgray')

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')
axes[3].legend(loc='upper left', frameon=False)

# Draw vertical gridlines.
for i in range(4):
    axes[i].xaxis.grid(which='major')
for i in [0, 2]:
    axes[i].spines['right'].set_color('lightgrey')

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

# Set x-axis ticks (default ticks were drawn every 20 kyr).
NUM_XTICKS = 14
axes[3].set_xlim(0, 130)
axes[3].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
axes[3].xaxis.set_minor_locator(ticker.LinearLocator(10 * NUM_XTICKS - 1))

# Show x-axis tick marks only on the bottommost plot.
for i in range(3):
    axes[i].tick_params(axis='x', which='both', bottom=False)

# Tweak y-axis settings to correspond to published figure.
axes[0].set_ylim(1, 3000)
axes[1].set_ylim(10, 1000)
axes[2].set_ylim(10, 10000)
axes[3].set_ylim(0, 25)

###############################################################################
# Annotate the figure.
axes[0].annotate('a', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[1].annotate('b', xy=(0.95, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[2].annotate('c', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[3].annotate('d', xy=(0.95, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')

axes[2].annotate('Hol', xy=(5, 80), xycoords='data', fontsize=16)
axes[2].annotate('LGM', xy=(20, 1000), xycoords='data', fontsize=16)
axes[2].annotate('Cold stadials', xy=(34, 1000), xycoords='data', fontsize=16)
axes[2].annotate('Warm interstadials', xy=(29, 12), xycoords='data', fontsize=16)
axes[2].annotate('Eem', xy=(120, 80), xycoords='data', fontsize=16)
###############################################################################


# ### Step 17. Adjust the figure size and the font size of the labels on the x-axes, y-axes, and legend
# The figure size and the default font size, including all labels of all of the axes 
# and in the legend, can be adjusted by the two lines:
# ``` python
# fig, axes = plt.subplots(4, 1, sharex=True, figsize=(16,14))
# plt.rcParams['font.size'] = 18
# ```
# Note that when adjusting the font size, Matplotlib may alter the number of tick 
# marks displayed. For example, in the preceding line, setting the default font size 
# to 20 (instead of 18) causes many of the desired tick marks on the y-axes to disappear.
# 
# The default label size can be overridden. Here, the labels in the legend are
# adjusted in order to create a better fit in the upper left corner of subplot d:
# ``` python
# axes[3].legend(loc='upper left', frameon=False, fontsize=14)
# ```

# In[52]:


# Figure 2

# Create a new figure with four subplots.
###############################################################################
# Adjust the figure size and the default font size for the figure, which 
# includes the labels on all of the x-axes, y-axes, and the legend.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(16,14))
plt.rcParams['font.size'] = 18
###############################################################################
fig.subplots_adjust(hspace=0)

# Draw an x-axis using an alternate scale (depth) along top of figure.
ax_top = axes[0].twiny()
ax_top.set_xlabel('NEEM depth (m)')
ax_top.xaxis.set_label_position('top')
ax_top.tick_params(top=True)
neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
                     2200, 2400]
supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'age_kyr'].min()
depth_to_kyr = lambda d: supp_data_2.loc[supp_data_2['depth_mid (m)'] >= d,
                                         'age_kyr'].min()
ax_top.set_xlim(0, 130)
ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
ax_top.set_xticks(ax_top_xticks)
ax_top.set_xticklabels(neem_depth_labels, rotation=90)
ax_top.tick_params(direction='in')

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)
ax_top.spines['right'].set_visible(False)
ax_top.spines['bottom'].set_visible(False)

# Subplots 2a, 2b, and 2c.
# Plot gray bands first.
x = supp_data_2['age_kyr']
axes[0].fill_between(x, supp_data_2['NH4source+1sigma (ng/m3)'],
                     supp_data_2['NH4source-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[1].fill_between(x, supp_data_2['Nasource+1sigma (ng/m3)'],
                     supp_data_2['Nasource-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[2].fill_between(x, supp_data_2['Casource+1sigma (ng/m3)'],
                     supp_data_2['Casource-1sigma (ng/m3)'],
                     facecolor='lightgray')

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')

###############################################################################
# Subplot 2d legend. The default label size is overridden in order to create 
# a better fit in the upper left corner of subplot d.
axes[3].legend(loc='upper left', frameon=False, fontsize=14)
###############################################################################

# Draw vertical gridlines.
for i in range(4):
    axes[i].xaxis.grid(which='major')
for i in [0, 2]:
    axes[i].spines['right'].set_color('lightgrey')

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

# Set x-axis ticks (default ticks were drawn every 20 kyr).
NUM_XTICKS = 14
axes[3].set_xlim(0, 130)
axes[3].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
axes[3].xaxis.set_minor_locator(ticker.LinearLocator(10 * NUM_XTICKS - 1))

# Show x-axis tick marks only on the bottommost plot.
for i in range(3):
    axes[i].tick_params(axis='x', which='both', bottom=False)

# Tweak y-axis settings to correspond to published figure.
axes[0].set_ylim(1, 3000)
axes[1].set_ylim(10, 1000)
axes[2].set_ylim(10, 10000)
axes[3].set_ylim(0, 25)

# Annotate the figure.
axes[0].annotate('a', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[1].annotate('b', xy=(0.95, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[2].annotate('c', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[3].annotate('d', xy=(0.95, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')

axes[2].annotate('Hol', xy=(5, 80), xycoords='data', fontsize=16)
axes[2].annotate('LGM', xy=(20, 1000), xycoords='data', fontsize=16)
axes[2].annotate('Cold stadials', xy=(34, 1000), xycoords='data', fontsize=16)
axes[2].annotate('Warm interstadials', xy=(29, 12), xycoords='data', fontsize=16)
axes[2].annotate('Eem', xy=(120, 80), xycoords='data', fontsize=16)


# ### Step 18. Save the figure to a file
# And finally, we save the resulting figure to a file. The file formats
# available are backend-dependent. On one of the author's systems, the 
# available file formats were:
# ``` python
# {'ps':   'Postscript',
#  'eps':  'Encapsulated Postscript',
#  'pdf':  'Portable Document Format',
#  'pgf':  'PGF code for LaTeX',
#  'png':  'Portable Network Graphics',
#  'raw':  'Raw RGBA bitmap',
#  'rgba': 'Raw RGBA bitmap',
#  'svg':  'Scalable Vector Graphics',
#  'svgz': 'Scalable Vector Graphics'}
# ```
# To see a list of the file formats available on your system, execute 
# the following cell. 

# In[53]:


plt.gcf().canvas.get_supported_filetypes()


# The file format to be used is specified by the extension on the filename
# given as the fname parameter to ```savefig```. Here, we request png format and 
# also trim the blank space from the margins:
# ``` python
# fig.savefig(fname='OurFig2.png', bbox_inches='tight', pad_inches=0)
# ```
# Numerous options for ```savefig``` are available, including one to set the desired 
# resolution in dots per inch (dpi). For a full list of available options, see 
# the Matplotlib documentation: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

# In[54]:


# Figure 2

# Create a new figure with four subplots.
# Adjust the figure size and the default font size for the figure, which 
# includes the labels on all of the x-axes, y-axes, and the legend.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(16,14))
plt.rcParams['font.size'] = 18
fig.subplots_adjust(hspace=0)

# Draw an x-axis using an alternate scale (depth) along top of figure.
ax_top = axes[0].twiny()
ax_top.set_xlabel('NEEM depth (m)')
ax_top.xaxis.set_label_position('top')
ax_top.tick_params(top=True)
neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
                     2200, 2400]
supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'age_kyr'].min()
depth_to_kyr = lambda d: supp_data_2.loc[supp_data_2['depth_mid (m)'] >= d,
                                         'age_kyr'].min()
ax_top.set_xlim(0, 130)
ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
ax_top.set_xticks(ax_top_xticks)
ax_top.set_xticklabels(neem_depth_labels, rotation=90)
ax_top.tick_params(direction='in')

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)
ax_top.spines['right'].set_visible(False)
ax_top.spines['bottom'].set_visible(False)

# Subplots 2a, 2b, and 2c.
# Plot gray bands first.
x = supp_data_2['age_kyr']
axes[0].fill_between(x, supp_data_2['NH4source+1sigma (ng/m3)'],
                     supp_data_2['NH4source-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[1].fill_between(x, supp_data_2['Nasource+1sigma (ng/m3)'],
                     supp_data_2['Nasource-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[2].fill_between(x, supp_data_2['Casource+1sigma (ng/m3)'],
                     supp_data_2['Casource-1sigma (ng/m3)'],
                     facecolor='lightgray')

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')

# Subplot 2d legend. The default label size is overridden in order to create 
# a better fit in the upper left corner of subplot d.
axes[3].legend(loc='upper left', frameon=False, fontsize=14)

# Draw vertical gridlines.
for i in range(4):
    axes[i].xaxis.grid(which='major')
for i in [0, 2]:
    axes[i].spines['right'].set_color('lightgrey')

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

# Set x-axis ticks (default ticks were drawn every 20 kyr).
NUM_XTICKS = 14
axes[3].set_xlim(0, 130)
axes[3].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
axes[3].xaxis.set_minor_locator(ticker.LinearLocator(10 * NUM_XTICKS - 1))

# Show x-axis tick marks only on the bottommost plot.
for i in range(3):
    axes[i].tick_params(axis='x', which='both', bottom=False)

# Tweak y-axis settings to correspond to published figure.
axes[0].set_ylim(1, 3000)
axes[1].set_ylim(10, 1000)
axes[2].set_ylim(10, 10000)
axes[3].set_ylim(0, 25)

# Annotate the figure.
axes[0].annotate('a', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[1].annotate('b', xy=(0.95, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[2].annotate('c', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[3].annotate('d', xy=(0.95, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')

axes[2].annotate('Hol', xy=(5, 80), xycoords='data', fontsize=16)
axes[2].annotate('LGM', xy=(20, 1000), xycoords='data', fontsize=16)
axes[2].annotate('Cold stadials', xy=(34, 1000), xycoords='data', fontsize=16)
axes[2].annotate('Warm interstadials', xy=(29, 12), xycoords='data', fontsize=16)
axes[2].annotate('Eem', xy=(120, 80), xycoords='data', fontsize=16)

###############################################################################
# Save the final result to a file.
fig.savefig(fname='OurFig2.png', bbox_inches='tight', pad_inches=0)
###############################################################################


# ### Final complete script (with our final output)
# For completeness, reading the data from the csv file and adding a column
# for the age in kyr have been added to the top of the code. 

# In[55]:


# Figure 2

# Read data from a csv file into a DataFrame.
supp_data_2 = pd.read_csv('data/supplementary-data-2.csv', sep=',',
                          skiprows=27, na_values=['NaN', '#VALUE!'])

# Add column for age in kyr to the DataFrame.
supp_data_2['age_kyr'] = supp_data_2['ageGICC05_mid (yr BP)'] / 1000

# Create a new figure with four subplots.
# Adjust the figure size and the default font size for the figure, which 
# includes the labels on all of the x-axes, y-axes, and the legend.
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(16,14))
plt.rcParams['font.size'] = 18
fig.subplots_adjust(hspace=0)

# Draw an x-axis using an alternate scale (depth) along top of figure.
ax_top = axes[0].twiny()
ax_top.set_xlabel('NEEM depth (m)')
ax_top.xaxis.set_label_position('top')
ax_top.tick_params(top=True)
neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
                     2200, 2400]
supp_data_2.loc[supp_data_2['depth_mid (m)'] >= 1700, 'age_kyr'].min()
depth_to_kyr = lambda d: supp_data_2.loc[supp_data_2['depth_mid (m)'] >= d,
                                         'age_kyr'].min()
ax_top.set_xlim(0, 130)
ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
ax_top.set_xticks(ax_top_xticks)
ax_top.set_xticklabels(neem_depth_labels, rotation=90)
ax_top.tick_params(direction='in')

# Draw all tick marks inside the plot area.
for i in range(4):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-c, but don't use exponential format
# for y-axis labels.
for i in range(3):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 2 as published in Nature.
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in [0, 1, 2]:
    axes[i].spines['bottom'].set_visible(False)
for i in [1, 2, 3]:
    axes[i].spines['top'].set_visible(False)
ax_top.spines['right'].set_visible(False)
ax_top.spines['bottom'].set_visible(False)

# Subplots 2a, 2b, and 2c.
# Plot gray bands first.
x = supp_data_2['age_kyr']
axes[0].fill_between(x, supp_data_2['NH4source+1sigma (ng/m3)'],
                     supp_data_2['NH4source-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[1].fill_between(x, supp_data_2['Nasource+1sigma (ng/m3)'],
                     supp_data_2['Nasource-1sigma (ng/m3)'],
                     facecolor='lightgray')
axes[2].fill_between(x, supp_data_2['Casource+1sigma (ng/m3)'],
                     supp_data_2['Casource-1sigma (ng/m3)'],
                     facecolor='lightgray')

# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_2.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                 color='green', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                 color='blue', alpha=0.4, legend=False)
supp_data_2.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                 color='red', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_2_smoothed = supp_data_2.rolling(21, min_periods=21, center=True)
supp_data_2_rolling_mean = supp_data_2_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_2_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4source (ng/m3)',
                              color='green', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[1], x='age_kyr', y='Nasource (ng/m3)',
                              color='blue', legend=False)
supp_data_2_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Casource (ng/m3)',
                              color='red', legend=False)

# Plot the dashed lines indicating the early Holocene average.
# Dates selected based on the title of Figure 3.
early_hol_data_2 = (
    supp_data_2[(supp_data_2.age_kyr >= 7.6) & (supp_data_2.age_kyr <= 9.8)]
               [['NH4source (ng/m3)', 'Nasource (ng/m3)', 'Casource (ng/m3)']])
early_hol_mean = early_hol_data_2.mean()
axes[0].axhline(y=early_hol_mean['NH4source (ng/m3)'],
                color='black', linestyle='--')
axes[1].axhline(y=early_hol_mean['Nasource (ng/m3)'],
                color='black', linestyle='--')
axes[2].axhline(y=early_hol_mean['Casource (ng/m3)'],
                color='black', linestyle='--')

# Subplot 2d.
supp_data_2.plot(ax=axes[3], x='age_kyr', y='NH4 atm. residence time (days)',
                 color='green', label='${NH_4}^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Na atm. residence time (days)',
                 color='blue', label='$Na^+$')
supp_data_2.plot(ax=axes[3], x='age_kyr', y='Ca atm. residence time (days)',
                 color='red', label='$Ca^{2+}$')

# Subplot 2d legend. The default label size is overridden in order to create 
# a better fit in the upper left corner of subplot d.
axes[3].legend(loc='upper left', frameon=False, fontsize=14)

# Draw vertical gridlines.
for i in range(4):
    axes[i].xaxis.grid(which='major')
for i in [0, 2]:
    axes[i].spines['right'].set_color('lightgrey')

# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $m^{-3}$)')
axes[1].set_ylabel(r'$Na^+$ (ng $m^{-3}$)', )
axes[2].set_ylabel(r'$Ca^{2+}$ (ng $m^{-3}$)')
axes[3].set_ylabel('atm. res. time (days)')

axes[3].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

# Set x-axis ticks (default ticks were drawn every 20 kyr).
NUM_XTICKS = 14
axes[3].set_xlim(0, 130)
axes[3].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
axes[3].xaxis.set_minor_locator(ticker.LinearLocator(10 * NUM_XTICKS - 1))

# Show x-axis tick marks only on the bottommost plot.
for i in range(3):
    axes[i].tick_params(axis='x', which='both', bottom=False)

# Tweak y-axis settings to correspond to published figure.
axes[0].set_ylim(1, 3000)
axes[1].set_ylim(10, 1000)
axes[2].set_ylim(10, 10000)
axes[3].set_ylim(0, 25)

# Annotate the figure.
axes[0].annotate('a', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[1].annotate('b', xy=(0.95, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[2].annotate('c', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[3].annotate('d', xy=(0.95, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')

axes[2].annotate('Hol', xy=(5, 80), xycoords='data', fontsize=16)
axes[2].annotate('LGM', xy=(20, 1000), xycoords='data', fontsize=16)
axes[2].annotate('Cold stadials', xy=(34, 1000), xycoords='data', fontsize=16)
axes[2].annotate('Warm interstadials', xy=(29, 12), xycoords='data', fontsize=16)
axes[2].annotate('Eem', xy=(120, 80), xycoords='data', fontsize=16)

# Save the final result to a file.
fig.savefig(fname='OurFig2.png', bbox_inches='tight', pad_inches=0)


# ### Published figure (for comparison)
# Compare our result above with the published figure below:
# ![Fig2.jpg](attachment:Fig2.jpg)

# -------
# ## Part 2: Recreate Figure 1 (subplots a-e) using the preceding code as a template
# Using the previous code as a template, we can quickly produce a figure similar 
# to Figure 1. Because subplots f and g use data from another source, the facimile 
# only contains subplots a-e. The data used to produce these visualizations are 
# found in Supplementary Data 1.
# 
# The original Figure 1, and then our Python code and its output:
# 
# ![Fig1.jpg](attachment:Fig1.jpg)

# In[56]:


# Figure 1 (subplots a-e)

# Read data from a csv file into a DataFrame.
supp_data_1 = pd.read_csv('data/supplementary-data-1.csv', sep=',',
                          skiprows=18)

# Add column for age in kyr to the DataFrame.
supp_data_1['age_kyr'] = supp_data_1['ageGICC05_mid (yr BP)'] / 1000

# Create a new figure with five subplots.
# Adjust the figure size and the default font size for the figure, which 
# includes the labels on all of the x-axes and y-axes.
fig, axes = plt.subplots(5, 1, sharex=True, figsize=(15,15))
plt.rcParams['font.size'] = 16
fig.subplots_adjust(hspace=0)

# Draw an x-axis using an alternate scale (depth) along top of figure.
ax_top = axes[0].twiny()
ax_top.set_xlabel('NEEM depth (m)')
ax_top.xaxis.set_label_position('top')
ax_top.tick_params(top=True)
neem_depth_labels = [1000, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
                     2200, 2400]
supp_data_1.loc[supp_data_1['depth_mid (m)'] >= 1700, 'age_kyr'].min()
depth_to_kyr = lambda d: supp_data_1.loc[supp_data_1['depth_mid (m)'] >= d,
                                         'age_kyr'].min()
ax_top.set_xlim(0, 130)
ax_top_xticks = [depth_to_kyr(d) for d in neem_depth_labels]
ax_top.set_xticks(ax_top_xticks)
ax_top.set_xticklabels(neem_depth_labels, rotation=90)
ax_top.tick_params(direction='in')

# Draw all tick marks inside the plot area.
for i in range(5):
    axes[i].tick_params(which='both', direction='in')

# Use log scale for y-axis in subplots a-e, but don't use exponential format
# for y-axis labels.
for i in range(5):
    axes[i].set_yscale('log')
    axes[i].yaxis.set_major_formatter(ticker.ScalarFormatter())

# The 2nd and 4th plots have y-axis labels and tick marks on the right.
for i in [1, 3]:
    axes[i].yaxis.set_label_position('right')
    axes[i].tick_params(which='both', left=False, right=True,
                        labelleft=False, labelright=True)

# Remove lines that don't appear in Figure 1 as published in Nature.
for i in [1, 3]:
    axes[i].spines['left'].set_visible(False)
for i in range(4):
    axes[i].spines['bottom'].set_visible(False)
for i in range(1, 5):
    axes[i].spines['top'].set_visible(False)
ax_top.spines['right'].set_visible(False)
ax_top.spines['bottom'].set_visible(False)

# Subplots 1a-e.
# Plot data using a lighter shade (by setting alpha=0.4).
supp_data_1.plot(ax=axes[0], x='age_kyr', y='NH4 (ng/g)',
                 color='green', alpha=0.4, legend=False)
supp_data_1.plot(ax=axes[1], x='age_kyr', y='NO3 (ng/g)',
                 color='orange', alpha=0.4, legend=False)
supp_data_1.plot(ax=axes[2], x='age_kyr', y='Na (ng/g)',
                 color='blue', alpha=0.4, legend=False)
supp_data_1.plot(ax=axes[3], x='age_kyr', y='Ca (ng/g)',
                 color='red', alpha=0.4, legend=False)
supp_data_1.plot(ax=axes[4], x='age_kyr', y='SO4 (ng/g)',
                 color='purple', alpha=0.4, legend=False)

# Calculate and plot the smoothed function values using a darker line.
# Use min_periods to remove extraneous "mean" values when the actual data
# is "NaN".
supp_data_1_smoothed = supp_data_1.rolling(21, min_periods=21, center=True)
supp_data_1_rolling_mean = supp_data_1_smoothed.mean()

# Plot the 21 point running means of the 10 year data.
supp_data_1_rolling_mean.plot(ax=axes[0], x='age_kyr', y='NH4 (ng/g)',
                              color='green', legend=False)
supp_data_1_rolling_mean.plot(ax=axes[1], x='age_kyr', y='NO3 (ng/g)',
                              color='brown', legend=False)
supp_data_1_rolling_mean.plot(ax=axes[2], x='age_kyr', y='Na (ng/g)',
                              color='blue', legend=False)
supp_data_1_rolling_mean.plot(ax=axes[3], x='age_kyr', y='Ca (ng/g)',
                              color='red', legend=False)
supp_data_1_rolling_mean.plot(ax=axes[4], x='age_kyr', y='SO4 (ng/g)',
                              color='purple', legend=False)

# Draw vertical gridlines.
for i in range(5):
    axes[i].xaxis.grid(which='major')
for i in [0, 2, 4]:
    axes[i].spines['right'].set_color('lightgrey')
    
# Set labels directly on the axes objects. Matplotlib supports a subset of latex.
# See https://matplotlib.org/stable/tutorials/text/mathtext.html for documentation.
axes[0].set_ylabel(r'$NH_4^+$ (ng $g^{-1}$)')
axes[1].set_ylabel(r'$NO_3^-$ (ng $g^{-1}$)')
axes[2].set_ylabel(r'$Na^+$ (ng $g^{-1}$)')
axes[3].set_ylabel(r'$Ca^{2+}$ (ng $g^{-1}$)')
axes[4].set_ylabel(r'$SO_4^{2-}$ (ng $g^{-1}$)')

axes[4].set_xlabel('Age (kyr BP GICC05modelext-NEEM-1)')

# Set x-axis ticks (default ticks were drawn every 20 kyr).
NUM_XTICKS = 14
axes[4].set_xlim(0, 130)
axes[4].xaxis.set_major_locator(ticker.LinearLocator(NUM_XTICKS))
axes[4].xaxis.set_minor_locator(ticker.LinearLocator(2 * NUM_XTICKS - 1))

# Show x-axis tick marks only on the bottommost plot.
for i in range(4):
    axes[i].tick_params(axis='x', which='both', bottom=False)
    
# Tweak y-axis limits to correspond to published figure.
axes[0].set_ylim(0.1, 100.0)
axes[1].set_ylim(40, 400)
axes[2].set_ylim(1, 1000)
axes[3].set_ylim(1, 1000)
axes[4].set_ylim(10, 10000)

# Tweak y-axis settings for subplot b.
axes[1].set_yticks([50, 100, 200])
axes[1].get_yaxis().set_major_formatter(ticker.ScalarFormatter())
axes[1].get_yaxis().set_minor_formatter(ticker.NullFormatter())
    
# Annotate the figure.
axes[0].annotate('a', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[1].annotate('b', xy=(0.95, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[2].annotate('c', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[3].annotate('d', xy=(0.95, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')
axes[4].annotate('e', xy=(0.05, 0.85), xycoords='axes fraction',
                 fontsize=20, fontweight='bold')

axes[3].annotate('Hol', xy=(5, 2), xycoords='data', fontsize=16)
axes[3].annotate('LGM', xy=(20, 1000), xycoords='data', fontsize=16)
axes[3].annotate('Cold stadials', xy=(34, 1000), xycoords='data', fontsize=16)
axes[3].annotate('Warm interstadials', xy=(29, 8), xycoords='data', fontsize=16)
axes[3].annotate('Eem', xy=(120, 2), xycoords='data', fontsize=16)

# Save the final result to a file.
fig.savefig(fname='OurFig1.png', bbox_inches='tight', pad_inches=0)


# # References
# 
# <a name="1"></a>
# 1. Free Software Foundation. _The GNU General Public License v3.0_, accessed 4 April 2022.
# https://www.gnu.org/licenses/gpl-3.0.en.html
# 
# <a name="2"></a>
# 2. McKinney, Wes. _Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython, Second Edition_, O'Reilly Media, September 2018. https://wesmckinney.com/pages/book.html (author's page) and https://github.com/wesm/pydata-book (datasets and Jupyter notebooks)
# 
# <a name="3"></a>
# 3. Python Software Foundation. _Python 3.10.4 Documentation_, 2001-2022. https://docs.python.org/3/
# 
# <a name="4"></a>
# 4. Schüpbach, S., et al. "Greenland records of aerosol source and atmospheric lifetime changes from the Eemian to the Holocene," *Nature Communications*, volume 9, Article number: 1476 (2018), last accessed 15 April 2022. https://www.nature.com/articles/s41467-018-03924-3
# 
# <a name="5"></a>
# 5. VanderPlas, Jake. _Python Data Science Handbook: Essential Tools for Working with Data_, November 2016. https://jakevdp.github.io/PythonDataScienceHandbook/ (book in html) and https://github.com/jakevdp/PythonDataScienceHandbook (full text in Jupyter notebooks)
# 
# <a name="6"></a>
# 6. VanderPlas, Jake. _A Whirlwind Tour of Python_, August 2016. https://jakevdp.github.io/WhirlwindTourOfPython/ (free Jupyter notebooks and pdf)
