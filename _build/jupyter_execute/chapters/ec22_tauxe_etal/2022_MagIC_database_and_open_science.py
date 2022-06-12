#!/usr/bin/env python
# coding: utf-8

# # Jupyter Notebooks as a bridge to the MagIC Database and Open Science

# ## Author(s)
# - Author1 = {"name": "Lisa Tauxe", "affiliation": "Scripps Institution of Oceanography", "email": "ltauxe@ucsd.edu", "orcid": "0000-0002-4837-8200"}
# - Author2 = {"name": "Rupert Minnett", "affiliation": "Oregon State University", "email": "rminnett@earthref.org", "orcid": "0000-0002-9000-2100"}
# - Author3 = {"name": "Nick Jarboe", "affiliation": "Oregon State University", "email": "njarboe@earthref.org", "orcid": "0000-0003-1465-9394"}
# - Author4 = {"name": "Catherine Constable", "affiliation": "Scripps Institution of Oceanography", "email": "cconstable@ucsd.edu", "orcid": "0000-0003-4534-4977"}
# - Author5 = {"name": "Anthony Koppers", "affiliation": "Oregon State University, "email": "Oregon State University, "orcid": "0000-0002-8136-5372"}
# 
# 

# ## Purpose
# 
# This notebook demonstrates how to access data in the MagIC open-source database at https://earthref.org/MagIC. MagIC is the first of a set of data repositories created by the EarthCube-funded project FIESTA. 
# The MagIC Database (Magnetics Information Consortium) allows magnetic measurement data of rocks and archaeological artifacts to be more Findable, Accessible, Interoperable, and Re-usable.  The MagIC Data Model governs the dataset contributions in the MagIC Database and is fully described here: https://earthref.org/MagIC/data-models/3.0.  PmagPy is a cross-platform and open-source software package  with Python functions written for the analysis of paleomagnetic and rock magnetic data, including tools that facilitate uploading, downloading and (re)interpretion of data in the MagIC Database.  It is intended to make the uploading of paleomagnetic data into MagIC straight-forward as MagIC data tables are created as part of normal data analysis and these can be uploaded to MagIC using the EarthCube-unded FIESTA API https://api.earthref.org within a Jupyter notebook or through the MagIC website itself.  
# 
# ### Overview of the  MagIC database
# Figure 1 shows the basic workflow of a typical paleomagnetic project from sampling in the field to contributing to the MagIC Database. Samples are taken in the field, and prepared into specimens, which then get measured. The measurements can be made on many different measurements and converted into a single, standard (MagIC) format which can then be operated on by an open-source software package, _PmagPy_ to visualize and interpret the data.  The measurement data and interpretations can be compiled into a hierarchy of MagIC data tables and then uploaded into the MagIC database.  
# 
# ![pmag_workflow.png](attachment:pmag_workflow.png)
# 
# Figure 1: Workflow of a typical paleomagnetic project (from Tauxe et al., 2016; doi:10.1002/2016GC006307)
# 
# The MagIC Data Model is built with the hierarchical structure typical of paleomagnetism whereby samples are taken in the field from "sites", which are considered homogeneous with respect to the magnetic property being measured (for example a lava flow or sedimentary horizon).  Sites can be grouped into "locations" which can be stratigraphic sections, drill cores, or regions.   The links between specimens, samples, sites, and locations are specified in the various data tables in the MagIC data format. 
# 
# Each contribution in the database is associated with a publication via the DOI.  There are nine data tables:
# 
# - contribution: metadata of the associated publication.
# - locations: metadata for locations, which are groups of sites (e.g., stratigraphic section, region, etc.)
# - sites: metadata and derived data at the site level (units with a common expectation)
# - samples: metadata and derived data at the sample level.
# - specimens: metadata and derived data at the specimen level.
# - measurements: metadata and measurements made on specimens from which all other data are derived
# - criteria: criteria by which data are deemed acceptable
# - ages: ages and metadata for sites/samples/specimens
# - images: associated images and plots.  
# 
# Only the contribution and location tables are required for a given study, but others can be used if desired.  The most useful datasets include the measurements table and the full hierarchy of data tables.   
# 
# ### Overview of the PmagPy software package
# 
# _PmagPy_ is a software package with over 1000 functions grouped into several modules that provide data analysis tools for visualizing and interpreting many different kinds of data including those in the MagIC format.  It can be accessed through [https://github.com/PmagPy/PmagPy](https://github.com/PmagPy/PmagPy) and downloaded onto a personal computer following instructions in the PmagPy cookbook [https://earthref.org/PmagPy/cookbook/](https://earthref.org/PmagPy/cookbook/).  There are many notebooks in the _PmagPy_ software package which can also be run without installation through the website: [https://jupyterhub.earthref.org](https://jupyterhub.earthref.org) after creating a personal user's space and running a simple Jupyter notebook (PmagPy\_online setup).
# 
# Functions as simple as calculating the expected direction at a given latitude to those as complicated as interpreting paleointensity data are available.  Most functions for making such calculations are grouped into the _pmag_ module.  Functions for making specialized plots are grouped into the _pmagplotlib_ module.  Functions specifically designed for use within Jupyter notebooks are grouped in the _ipmag_ module.  There are also a number of command line programs that allow similar data analysis to be performed as in the notebooks.  Finally, there are several Graphical User Interfaces (GUIs) that, when installed on a personal computer aid in interpretation and data analysis, call the many functions in the _PmagPy_ package.  This notebook focuses on  the use of Jupyter Notebooks for using the _PmagPy_ functions.  
# 
# 
# ### Use of PmagPy from within a Jupyter notebook
# 
# Notebooks such as this one can be used to call _PmagPy_ functions.  They can be used to convert data from laboratory formats into the MagIC format and produce many of the plots and make the calculations required in paleomagnetic projects.  
# 
# Data can be accessed either through a web browser or through the FIESTA API queries, the most direct of which connects a dataset to the DOI of the publication using Python code that is part of the PmagPy software package. Data can therefore be downloaded, unpacked, re-analyzed or imaged and then repackaged and uploaded back into a private workspace of the user. Jupyter notebooks can then be attached to a new publication and serve as important supplemental material for publication, making the data and the analysis thereof transparent and reproducible. We will illustrate the use of Jupyter notebooks in connection with FAIR data practices in the rock and paleomagnetic world.  
# 
# 
# ## Technical contributions
# 
# - Paleomagnetic data published on the MagIC website and linked to a DOI can be downloaded from the database using the FIESTA API. 
# - The PmagPy python software package imported in the notebook can be used to unpack and re-analyze data in the database to reproduce results, demonstrating the benefits of FAIR principles. 
# 
# 
# ## Methodology
# - import useful Python modules
# - import the PmagPy software package
# - download a dataset from MagIC using the FIESTA API through PmagPy
# - re-analyze the data using PmagPy plotting and analysis functions
# 
# 
# ## Results
# This notebook illustrates how open-source databases can be accessed and used to further the goals of open science. 
# 
# 
# ## Funding
# 
# - Award1 = {"agency": "US National Science Foundation", "award_code": "1822336", "award_URL": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1822336"}
# - Award2 = {"agency": "US National Science Foundation", "award_code": "2126298", "award_URL": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2126298"}
# 
# 
# ## Keywords
# keywords=["FAIR", "Open Science", "MagIC database", "PmagPy software package", "paleomagnetism"]
# 
# 
# ## Citation
#  Tauxe et al., 2022, Jupyter Notebooks as a bridge to the MagIC Database and Open Science, 2022 EarthCube Annual Meeting. Accessed XX/XX/XXXX at https://github.com/PmagPy/2022_Tauxe-et-al_MagIC-Database-and-Open-Science
# 
# ## Acknowledgements 
# We thank  members of the MagIC/FIESTA database team Nick Swanson-Hysell and Christeanne Santos for help in maintaining the PmagPy software package.  We also thank EarthCube for providing support for the further development of PmagPy and MagIC under the umbrella of the FIESTA project, meant to expand database design beyond MagIC into other geoscience domains.   
# 
# The template is licensed under a <a href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License.</a>

# # Setup
# 
# ## Access of the notebook:
# 
# ### Using Binder
# 
# This notebook can be run by launching Binder from the GitHub repository.  
# 
# - Go to [https://github.com/earthcube2022/ec22_tauxe_etal.git](https://github.com/earthcube2022/ec22_tauxe_etal.git) and click on Binder label at the top of the README.md file.
# 
# - Once the dependencies are installed, JupyterLab loads, and the notebook opens, the cells in the notebook can be executed and edited as needed.
# 
# ### Using jupyterhub
# 
# The Binder version does not allow uploading of user's own data and is therefore useful only for demonstration purposes.  However, this notebook is also included in the PmagPy software package which can be installed on a personal and downloaded onto a personal computer following instructions in the PmagPy cookbook [https://earthref.org/PmagPy/cookbook/](https://earthref.org/PmagPy/cookbook/)or  run without installation through the website: [https://jupyterhub.earthref.org](https://jupyterhub.earthref.org).
# 
# 
# 
# 

# 
# 
# ## Library import
# Import all the required Python libraries.
# 
# 
# 

# In[2]:


# This allows you to make matplotlib plots inside the notebook
get_ipython().run_line_magic('matplotlib', 'inline')
# Import packages
import pandas as pd # and  Pandas for data wrangling
import os # some useful operating system functions
from IPython.display import Image


# ## Local library import
# 
# - import the special PmagPy and mapping modules
# - create a directory for use in this notebook

# In[3]:


# Import PmagPy modules
import pmagpy.pmag as pmag
import pmagpy.pmagplotlib as pmagplotlib
import pmagpy.ipmag as ipmag

dirs=os.listdir() # get a list of directories in this one
if 'MagIC_for_earthcube' not in dirs:
    os.mkdir("MagIC_for_earthcube")


# # Parameter definitions
# 
# - after installation of PmagPy software, set up the directory structure for this notebook
# 
# - Define path, desired DOI for downloading data from MagIC and a placeholder filename. 
# 

# In[4]:


dir_path='MagIC_for_earthcube' # set the path to the working directory
reference_doi='10.1029/2019GC008479' # Behar et al. (2019)
magic_contribution='magic_contribution.txt' # temporary name for contribution prior to unpacking


# 
# # Data import
# Retrieve all the required data for the analysis.
# 
# We will be using the data from this reference: 
# 
# Behar, N., Shaar, R., Tauxe, L., Asefaw, H., Ebert, Y., Heimann, A., Koppers, A.A.P., and Ron, H., Paleomagnetic study of the Plio-Pleistocene Golan Heights volcanic field, Israel: confirmation of the GAD field hypothesis,  Geophys., Geochem. Geosyst., 20,  doi: 10.1029/2019GC008479, 2019. 
# 
# The purpose of that paper was to provide new data relating to the geomagnetic field over the last few million years.  The Plain Language Summary stated: 
# 
# "Since the early days of paleomagnetic research, it has been inferred that the time‐averaged structure of the field is a geocentric axial dipole (GAD)—equivalent to a field generated by a dipole at the center of the Earth aligned with its rotation axis. This so‐called GAD hypothesis is fundamental in paleomagnetism and is the basis for plate tectonic reconstructions. However, recent studies have suggested persistent departures from a GAD structure, manifested as an anomaly in the inclination angle of the field in northern hemispheric low to middle latitudes. To address this problem, we analyzed 91 basaltic lava flows from the Golan Heights volcanic plateau in Israel (32–33°N), spanning the past 5 Myr. As each basaltic flow captured the direction of the ambient magnetic field when it cooled, these flows provide us information about the averaged direction of the ancient geomagnetic field. Our results show that the averaged field in the Golan Heights is in agreement with a GAD structure. We also show that if we reanalyze the global paleomagnetic data from lava flows spanning the past 10 Myr using stricter selection criteria and a different inclination anomaly calculation method, the data do not support a
# global non‐GAD field."
# 
# In this notebook, we will reproduce a few of the key diagrams in the paper. 
# 
# Steps for data import:
# - create a directory to put downloaded data
# - download the data from the database using the reference DOI
# - move the data to the directory
# - unpack the data into MagIC formatted tab-delimited files. 
# 
# For help on all functions use:
# help(ModuleName.FunctionName)
# 
# example:

# In[5]:


help(ipmag.download_magic_from_doi)


# In[6]:


ipmag.download_magic_from_doi(reference_doi)
os.rename(magic_contribution, dir_path+'/'+magic_contribution)
ipmag.download_magic(magic_contribution,dir_path=dir_path,print_progress=False)


# # Data processing and analysis
# 
# We will look at three examples of reuse of the data from our study.  The first will make an equal area projection of all the directions found in the study. Paleomagnetists often deal with directional data (Figures 2a,b) and like other Earth Science disciplines (e.g., structural geology) plot directions that are inherently three-dimensional on a 2-D projection (Figure 2c).  Plotted in this way one can assess whether the directions behave as one might expect from secular variation of the field. For example, in our second plot, we will check whether two sets of directions from the two polarities, normal (as in the present field) and reverse (opposite), are antipodal.  
# 
# ![components.png](attachment:components.png)
# Figure 2: a)  Lines of flux of the geomagnetic field of 2005. At point $P$ the horizontal component of the field $B_H$, is directed toward the magnetic north (with a deviation known as declination, $D$). The vertical component $B_V$ is directed down and the field makes an angle $I$ with the horizontal, known as the inclination.   b) Components of the geomagnetic field vector $B$.   c) Construction of an equal area projection for a point $P$ corresponding to a $D$ of 40$^{\circ}$ and an $I$ of 35$^{\circ}$. d) Transformation of a direction measured at location $S$ to a virtual geomagnetic pole (VGP).   Figure  modified from https://earthref.org/MagIC/books/Tauxe/Essentials/ and references therein.  
# 
# 
# In the third plot, we will look at the directional data after transformation to virtual geomagnetic pole positions (Figure 2d).  These we will plot on an orthorhombic projection with the reverse poles (negative latitudes) flipped to their antipodes.    
# 
# For more information on Paleomagnetism, check out the open-source textbook hosted by MagIC at: 
# https://earthref.org/MagIC/books/Tauxe/Essentials/.
# 
# 
# 

# 
# ### MagIC formatted files
# 
# 
# MagIC text files all have the delimiter (tab) and the type of table in the first line and the column headers in the second line.  For details on the column headers in each data table, see the current MagIC database model definitions here: https://earthref.org/MagIC/data-models/3.0
# 
# To read in the site level data into a _Pandas_ DataFrame we specify that the file is tab-delimited with the _sep_ argument and that the header is in the second row (remember that Pandas starts counting at zero).  Then we will look at the first few lines using the _.head()_ function.  To do this, we use the following syntax:
# 
# 

# In[7]:


df=pd.read_csv(dir_path+'/sites.txt',sep='\t',header=1)
df.head()


# ### Equal area projections of directional data.
# First,  will plot the Plio-Pleistocene magnetic field directional data in the Behar et al. (2019) paper in an equal area projection using the PmagPy function ipmag.eqarea_magic().  
# 

# In[7]:


help(ipmag.eqarea_magic)


# ### essential parameters:
# - ipmag.equarea_magic reads in the required directional data from the MagIC formatted txt file '.sites' in the specified directory.
# - dir_path was set previously and all other parameters are the defaults, so we can just run this program. 
# 

# In[8]:


ipmag.eqarea_magic(dir_path=dir_path,save_plots=False)


# Figure 3: Equal area plot of the directions from the downloaded data set.  North is at the top of the diagram and vertical is in the center. Solid (open) symbols are downward (upward) directed.  There are two sets of directions, one pointed north and down and one pointed south and up.  

# ### Saving plots
# - to save the plots, set _save_plots_ to True and your preferred format using the argument, _fmt_. 
# - you can download the resulting png file (or find it in your project directory if running locally).  

# In[10]:


ipmag.eqarea_magic(dir_path=dir_path,save_plots=True,fmt='png')


# ### Are the two sets of directions antipodal? 
# One can see in Figure 3 that there are two sets of directions, one to the north and down (as expected for the latitude of the Golan Heights in Israel and one directed to the south and up (as expected for a reverse field in Israel).  So, are the two sets of directions antipodal?   _PmagPy_ has code to test this hypothesis.  Here we will use the bootstrap reversal test (see opensource textbook Essentials of Paleomagnetism at: https://earthref.org/MagIC/books/Tauxe/Essentials/) to see if the two sets are antipodal.  

# In[11]:


help(ipmag.reversal_test_bootstrap)


# We already read in the directional data into a Pandas DataFrame _df_, so lets pick out the lists of declinations and inclinations and feed them into _ipmag.reversal_test_bootstrap_. This program first converts one of the sets of directions to their antipodes (by adding 180$^{\circ}$ to the declinations and taking the opposition of the inclinations.  It then calculates the mean directions from 1000 "pseudosamples" of the two data sets and plots the resulting means (converted to their cartesian coordinates) as cumulative distributions. 
# If there is overlap in all three components, then the data sets are likely antipodal.  
# 
# Consulting the MagIC data model page for the sites data table, we see that the desired column headers are 'dir_dec' and 'dir_inc' for declination and inclination. So we can make arrays (or lists) of those and feed them into our reversals test as follows: 

# In[12]:


decs=df['dir_dec'].values
incs=df['dir_inc'].values
ipmag.reversal_test_bootstrap(dec=decs,inc=incs)


# Here we see that the X and Z components are NOT antipodal as the 95\% confidence limits (vertical lines) of the bootstrapped  means do not overlap.  So this data set fails the reversals test.  

# ### Map of equivalent VGPs 
# We can explore the data set further by converting the directions to their equivalent   virtual geomagnetic poles (VGPs).  The transformation and the plot is done for is by the _PmagPy_ function _ipmag.vgpmap_magic()_.  
# 
# 

# In[13]:


help(ipmag.vgpmap_magic)


# In[14]:


ipmag.vgpmap_magic(dir_path=dir_path,size=50,flip=True,save_plots=False,lat_0=60,rsym='b^',rsize=50,fmt='png')


# Figure 4: Orthographic projection of virtual geomagnetic poles calculated from directional data of Behar et al. (2019).  Red dots are for the normal poles and blue squares are the antipodes of the reverse poles.  

# By setting the argument _flip_ to True, we can plot the normal (red dots) and the reverse (blue triangles) poles on the same projection.  Behar et al. (2019) attributed  the difference in mean directions to a tectonic tilting event that offset the two sets.   

# # Next steps:
# - Try out other Jupyter notebooks within the _PmagPy_ software distribution to learn the full functionality of the package either by installing _PmagPy_ on a personal computer (see [https://earthref.org/PmagPy/cookbook/](https://earthref.org/PmagPy/cookbook/)) or  run PmagPy notebooks without installation through the website: [https://jupyterhub.earthref.org](https://jupyterhub.earthref.org). You will have to create a username using an ORCID which will allow you to upload your own data, or download data from the MagIC website, create plots and save them and preserve your work in your own permanent space.  Using the FIESTA API, datasets can be uploaded to a Private Workspace in the MagIC database and published when your manuscript gets accepted.  
# - Become a PmagPy developer! 

# # References
# 
# 1. Behar, N., Shaar, R., Tauxe, L., Asefaw, H., Ebert, Y., Heimann, A., Koppers, A.A.P., and Ron, H. (2019), Paleomagnetic study of the Plio-Pleistocene Golan Heights volcanic field, Israel: confirmation of the GAD field hypothesis,  Geophys., Geochem. Geosyst., 20, https://dx.doi.org/10.1029/2019GC008479. 
# 
# 2. MagIC website: https://earthref.org/MagIC
# 
# 3. EarthRef FIESTA API: https://api.earthref.org
# 
# 4. Textbook for paleomagnetism: https://earthref.org/MagIC/books/Tauxe/Essentials/
# 
# 5. PmagPy installation instructions: https://earthref.org/PmagPy/cookbook/
# 
# 6. Course in Python for Earth Science Students: https://github.com/ltauxe/Python-for-Earth-Science-Students
# 
# 7. PmagPy citation:  Tauxe, L., R. Shaar, L. Jonestrask, N. L. Swanson-Hysell, R. Minnett, A. A. P. Koppers, C. G. Constable, N. Jarboe, K. Gaastra, and L. Fairchild (2016), PmagPy: Software package for paleomagnetic data analysis and a bridge to the Magnetics Information Consortium (MagIC) Database, Geochem. Geophys. Geosyst., 17, https://doi.org/10.1002/2016GC006307.
# 
# 
# 

# In[ ]:




