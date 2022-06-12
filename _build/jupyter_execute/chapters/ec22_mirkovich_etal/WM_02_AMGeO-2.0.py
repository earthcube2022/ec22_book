#!/usr/bin/env python
# coding: utf-8

# # AMGeO 2.0: Crafting an API for Geospace Data Scientists
# 
# <img src='./static/AMGeOLogo.svg'/>

# ## Authors

# Author1 = {
#     "name": "Willem Mirkovich",
#     "affiliation": "University of Colorado Boulder, Smead Aerospace Engineering Sciences",
#     "email": "willem.mirkovich@colorado.edu",
#     "orcid": "0000-0003-0955-8281"
# }
# 
# Author2 = {
#     "name": "Tomoko Matsuo",
#     "affiliation": "University of Colorado Boulder, Smead Aerospace Engineering Sciences",
#     "email": "tomoko.matsuo@colorado.edu",
#     "orcid": "0000-0002-2754-1224" 
# }
# 
# Author3 = {
#     "name": "Liam Kilcommons",
#     "affiliation": "University of Colorado Boulder, Smead Aerospace Engineering Sciences",
#     "email": "Liam.Kilcommons@colorado.edu",
#     "orcid": "0000-0002-4980-3045"
# }

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#AMGeO-2.0:-Crafting-an-API-for-Geospace-Data-Scientists" data-toc-modified-id="AMGeO-2.0:-Crafting-an-API-for-Geospace-Data-Scientists-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>AMGeO 2.0: Crafting an API for Geospace Data Scientists</a></span><ul class="toc-item"><li><span><a href="#Authors" data-toc-modified-id="Authors-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Authors</a></span></li><li><span><a href="#Purpose" data-toc-modified-id="Purpose-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Purpose</a></span></li><li><span><a href="#Technical-contributions" data-toc-modified-id="Technical-contributions-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Technical contributions</a></span></li><li><span><a href="#Methodology" data-toc-modified-id="Methodology-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Methodology</a></span></li><li><span><a href="#Funding" data-toc-modified-id="Funding-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Funding</a></span></li><li><span><a href="#Keywords" data-toc-modified-id="Keywords-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Keywords</a></span></li><li><span><a href="#Citation" data-toc-modified-id="Citation-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Citation</a></span></li><li><span><a href="#Work-in-progress" data-toc-modified-id="Work-in-progress-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Work in progress</a></span></li><li><span><a href="#Suggested-next-steps" data-toc-modified-id="Suggested-next-steps-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Suggested next steps</a></span></li><li><span><a href="#Acknowledgements" data-toc-modified-id="Acknowledgements-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Acknowledgements</a></span></li></ul></li><li><span><a href="#Setup" data-toc-modified-id="Setup-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Setup</a></span><ul class="toc-item"><li><span><a href="#Library-imports" data-toc-modified-id="Library-imports-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Library imports</a></span></li></ul></li><li><span><a href="#Parameter-definitions" data-toc-modified-id="Parameter-definitions-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Parameter definitions</a></span></li><li><span><a href="#Data-import" data-toc-modified-id="Data-import-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Data import</a></span></li><li><span><a href="#Data-processing-and-analysis" data-toc-modified-id="Data-processing-and-analysis-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Data processing and analysis</a></span><ul class="toc-item"><li><span><a href="#AMGeO's-new-API" data-toc-modified-id="AMGeO's-new-API-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>AMGeO's new API</a></span><ul class="toc-item"><li><span><a href="#Creating-an-AMGeO-API-instance" data-toc-modified-id="Creating-an-AMGeO-API-instance-5.1.1"><span class="toc-item-num">5.1.1&nbsp;&nbsp;</span>Creating an AMGeO API instance</a></span><ul class="toc-item"><li><span><a href="#Setting-our-output-directory-for-AMGeO-data" data-toc-modified-id="Setting-our-output-directory-for-AMGeO-data-5.1.1.1"><span class="toc-item-num">5.1.1.1&nbsp;&nbsp;</span>Setting our output directory for AMGeO data</a></span></li></ul></li><li><span><a href="#Creating-an-AMGeO-controller" data-toc-modified-id="Creating-an-AMGeO-controller-5.1.2"><span class="toc-item-num">5.1.2&nbsp;&nbsp;</span>Creating an AMGeO controller</a></span></li><li><span><a href="#Generating-AMGeO-maps" data-toc-modified-id="Generating-AMGeO-maps-5.1.3"><span class="toc-item-num">5.1.3&nbsp;&nbsp;</span>Generating AMGeO maps</a></span></li><li><span><a href="#Browsing-AMGeO-maps" data-toc-modified-id="Browsing-AMGeO-maps-5.1.4"><span class="toc-item-num">5.1.4&nbsp;&nbsp;</span>Browsing AMGeO maps</a></span></li><li><span><a href="#Loading-AMGeO-maps" data-toc-modified-id="Loading-AMGeO-maps-5.1.5"><span class="toc-item-num">5.1.5&nbsp;&nbsp;</span>Loading AMGeO maps</a></span></li></ul></li><li><span><a href="#AMGeO's-xarray-datasets" data-toc-modified-id="AMGeO's-xarray-datasets-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>AMGeO's xarray datasets</a></span><ul class="toc-item"><li><span><a href="#Data-variables" data-toc-modified-id="Data-variables-5.2.1"><span class="toc-item-num">5.2.1&nbsp;&nbsp;</span>Data variables</a></span></li><li><span><a href="#Coordinates/Dimensions" data-toc-modified-id="Coordinates/Dimensions-5.2.2"><span class="toc-item-num">5.2.2&nbsp;&nbsp;</span>Coordinates/Dimensions</a></span></li><li><span><a href="#Dataset-metadata" data-toc-modified-id="Dataset-metadata-5.2.3"><span class="toc-item-num">5.2.3&nbsp;&nbsp;</span>Dataset metadata</a></span></li></ul></li><li><span><a href="#Compatability-with-matplotlib" data-toc-modified-id="Compatability-with-matplotlib-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Compatability with matplotlib</a></span></li><li><span><a href="#Compatability-with-numpy" data-toc-modified-id="Compatability-with-numpy-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Compatability with numpy</a></span></li><li><span><a href="#Compatability-with-apexpy" data-toc-modified-id="Compatability-with-apexpy-5.5"><span class="toc-item-num">5.5&nbsp;&nbsp;</span>Compatability with apexpy</a></span><ul class="toc-item"><li><span><a href="#AMGeO-to-geodetic" data-toc-modified-id="AMGeO-to-geodetic-5.5.1"><span class="toc-item-num">5.5.1&nbsp;&nbsp;</span>AMGeO to geodetic</a></span></li></ul></li><li><span><a href="#Compatability-with-cartopy" data-toc-modified-id="Compatability-with-cartopy-5.6"><span class="toc-item-num">5.6&nbsp;&nbsp;</span>Compatability with cartopy</a></span><ul class="toc-item"><li><span><a href="#Plotting-AMGeO-electostatic-potential-on-orthographic-projection" data-toc-modified-id="Plotting-AMGeO-electostatic-potential-on-orthographic-projection-5.6.1"><span class="toc-item-num">5.6.1&nbsp;&nbsp;</span>Plotting AMGeO electostatic potential on orthographic projection</a></span></li></ul></li><li><span><a href="#Pandas-compatability" data-toc-modified-id="Pandas-compatability-5.7"><span class="toc-item-num">5.7&nbsp;&nbsp;</span>Pandas compatability</a></span></li><li><span><a href="#Conclusion" data-toc-modified-id="Conclusion-5.8"><span class="toc-item-num">5.8&nbsp;&nbsp;</span>Conclusion</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# ## Purpose
# 
# The purpose of this notebook is to introduce Geospace scientists to the new AMGeO 2.0 API, as well as demonstrate functionality with other popular python packages.

# ## Technical contributions
# 
# - Introduces geospace researchers to AMGeO's new API
# - Showcases power of using Xarray to enable research of multidimensional datasets
# - Gives examples of using the API with various other Python packages, including
#     - Numpy
#     - Matplotlib
#     - Apexpy
#     - Cartopy

# ## Methodology
# 
# The Assimilative Mapping of Geospace Observations (AMGeO) is a data science tool for the geospace science community that automates labor-intensive data acquisition and processing, combining observations from various sensors into assimilative maps of the high-latitude ionosphere. While AMGeO offers a highly configurable toolset, it currently requires both domain expertise and familiarity with Python to use it effectively for scientific research. 
# 
# To remove hurdles for novice users and empower all AMGeO users, we have recently introduced a new Application Programming Interface (API) focused on enhanced user-experience, including better compatibility with Jupyter Notebooks, improved data manipulation with Xarray and more flexible data generation. This notebook will demonstrate the functionality offered by the new API and how to use AMGeO in conjunction with other popular Python research tools in order to accelerate geospace data science processes.

# ## Funding
# 
# AMGeO is supported by the NSF EarthCube grants ICER 1928403 to the University of Colorado Boulder, ICER 1928327 to the Virginia Tech, and ICER 1928358 to the Johns Hopkins University Applied Physics Laboratory.

# ## Keywords

# keywords=["AMGeO", "Xarray", "Python", "API", "Geospace"]

# ## Citation
# 
# Willem Mirkovich, Liam Kilcommons, Tomoko Matsuo, 2022. AMGeO, Xarray, Python, API, Geospace. Accessed 4/15/2022 at https://github.com/willemmirkovich/Earthcube-Meeting-2022
# 

# ## Work in progress
# 
# While this notebook is in a complete state, these are some notable additions that would be nice to add:
# 
# - Apexpy example of converting to base vectors
# - Cartopy example of time-series 
# - Cartopy example of vector plots

# ## Suggested next steps
# 
# Please get started with AMGeO [here](https://amgeo.colorado.edu/), we would love any feedback to continue improving our software.

# ## Acknowledgements
# 
# We would like to thank our data providers:
# 
# - [SuperMAG](https://supermag.jhuapl.edu/)
# - [SuperDARN](http://vt.superdarn.org/tiki-index.php)
# - [AMPERE](http://ampere.jhuapl.edu/)
# - [NASA SPDF](https://spdf.gsfc.nasa.gov/)

# # Setup

# ## Library imports
# 
# Below are the necessary libraries needed to run this notebook: 
# 
# - Python 3.8
# - AMGeO 2.0.2 (comes with Matplotlib, Numpy, Xarray)
# - Apexpy 1.0.1
# - Cartopy 0.20.2
# 
# <div class="alert alert-block alert-info">
#     <b>NOTE:</b> If AMGeO is installed locally, upon import, if you have not configured AMGeO with your API key, SuperMAG username or AMPERE username, this will be asked here (with instructions on how to get each). This notebook bypasses this step.
# </div>

# In[1]:


# Ignore uunecessary warnings from AMGeO dependencies
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# AMGeO's API class
from AMGeO.api import AMGeOApi

# python's datetime module
from datetime import datetime, date

# matplotlib tools
import matplotlib.pyplot as plt
import numpy as np

# cartopy
import cartopy.crs as crs

# apexpy
from apexpy import Apex


# # Parameter definitions
# 
# During the duration of this notebook, there are some commone placeholder variables that will be used.
# 
# `api` will be used to store AMGeO's API instance

# In[3]:


api = AMGeOApi()
api


# `controller` will be used to generate and load assimilative maps using AMGeO. This will be described in more detail in `Creating an AMGeO controller`

# In[4]:


controller = api.get_controller()
controller


# # Data import
# 
# Since this notebook is a technical overview of AMGeO's new API, all Data used will be imported/generated during the course of the `Data Processing` section. 
# To learn more about AMGeO and the data we generate, [please go to our website](https://amgeo.colorado.edu/)

# # Data processing and analysis

# ## AMGeO's new API
# 
# [AMGeO's 2.0 Release](https://amgeo.colorado.edu/) comes with a fleshed out Application Programming Interface (API) for easier
# generation/loading of Assimilative Maps of GeoSpace Observations (AMGeO).
# 
# The development of this API had two main goals in mind:
# 
# 1. Simple *and* functional classes/objects to generate/manipulate/load AMGeO's main data product
# 
# 2. Interopability with various Python scientifict packages, such as 
# Numpy, Xarray, Scipy, as well as popular geospatial packages like
# ApexPy, CartoPy

# ### Creating an AMGeO API instance
# 
# Here, we can create an AMGeO API instance, and get various details as to a default API instance

# In[5]:


api = AMGeOApi()
api


# #### Setting our output directory for AMGeO data
# 
# When running AMGeO, a local file system directory will be selected to store your assimilative maps. By default, AMGeo will use ```~/amgeo_v2_ouptput```

# In[6]:


api.get_output_dir()


# But, if you want to specify another directory, you can set this in the API instance using ```set_output_dir```

# In[7]:


api.set_output_dir('./amgeo_out')


# In[8]:


api.get_output_dir()


# ### Creating an AMGeO controller
# 
# To generate assimilative maps, you will have to load specific settings from AMGeO. Conveniently, AMGeO's new API allows for a simple way to load AMGeO's default settings using a ```controller```.
# 
# To create a ```controller``` instance, you can call ```get_controller``` on an API instance

# In[9]:


controller = api.get_controller()
controller


# As observed, calling ```get_controller``` returns an ```Default AMGeO Controller```, that is able to both create and load assimilative maps using AMGeO's default settings. 

# ### Generating AMGeO maps
# 
# <img src="./static/AMGeOElectricPotentialMap.png" width="500px" height="500px">
# 
# Now that we have a ```controller``` instance, we can create assimilative maps by calling the ```generate``` method on our ```controller```. 
# This method takes both a hemisphere and a date argument. 
# 
# ```controller.generate``` supports multiple different ways of generating maps based on dates/datetimes:
# 
# 1. A single datetime
# 
#     Will generate data for a specific date and time 
#     ```python
#     controller.generate(datetime(YYYY, MM, DD, hh, mm, ss), 'N' | 'S')
#     ```
#     
# 2. A single date
# 
#     Will generate data for 5 min slices over the entire date provided
#     Ex: date(2013, 5, 5) => datetime(2013, 5, 5, 0, 2, 30), datetime(2013, 5, 5, 0, 7, 30), ...
#     ```python
#     controller.generate(date(YYYY, MMMM, DD), 'N' | 'S')
#     ```
# 3. A list of dates/datetimes
# 
#     This will handle each element within the list on a case by case basis, in a bulk job
#     ```python
#     controller.generate([
#         datetime(YYYY, MM, DD, hh, mm, ss),
#         date(YYYY, MM, DD),
#         ...
#     ], 'N' | 'S')
#     ```
# 
# For example, if we wanted to generate maps for dates:
# 
# - January 6th, 2013 16:30:00
# - January 6th, 2013 17:30:00
# - February 6th, 2013 12:30:00
# - February 6th, 2013 13:30:00
# 
# and on the Northern hemisphere, we can call ```generate``` with ...

# In[10]:


dts = [
    datetime(2013, 1, 6, 16, 30, 0), # January 6th, 2013 16:30:00
    datetime(2013, 1, 6, 17, 30, 0), # January 6th, 2013 17:30:00
    datetime(2013, 2, 6, 12, 30, 0), # February 6th, 2013 12:30:00
    datetime(2013, 2, 6, 13, 30, 0) # February 6th, 2013 13:30:00
]
# hemisphere
h = 'N'


# In[11]:


controller.generate(dts, h)


# Once complete, we will be able to see generated AMGeO maps for each datetime.

# ### Browsing AMGeO maps
# 
# Once we have generated AMGeO maps, we might be interested in browsing what maps we have available.
# 
# To do this, the ```controller``` has a ```browse``` method that can be used in two ways.

# 1. Browse based on a hemisphere which dates have AMGeO maps already generated.
# 
#     ```python
#     controller.browse('N' | 'S')
#     ```

# In[12]:


controller.browse('N')


# 2. Specify a date and hemisphere for specific times that AMGeO has generated maps for
# 
#     ```python
#     controller.browse(date(YYYY, MM, DD), 'N' | 'S')
#     ```

# In[13]:


controller.browse(date(2013, 2, 6), 'N')


# ### Loading AMGeO maps
# 
# The last and most important piece of AMGeO's new API is the ability to load AMGeO maps into [Xarray datasets](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.html), with no work needed other than calling ```controller.load```
# 
# ```load``` supports the same modularity as ```generate```, to allow for loading various dates/datetimes on a given hemisphere into one dataset.

# 1. A single datetime
# 
#     Will load the specific map from the datetime into a dataset
#     ```python
#     controller.load(datetime(YYYY, MM, DD, hh, mm, ss), 'N' | 'S')
#     ```

# In[14]:


controller.load(datetime(2013, 1, 6, 16, 30, 0), 'N')


# 2. A single date
# 
#     Will load all maps available from a date
#     ```python
#     controller.load(date(YYYY, MM, DD), 'N' | 'S')
#     ```

# In[15]:


controller.load(date(2013, 1, 6), 'N')


# 3. A list of dates/datetimes
# 
#     Will load each date/datetime respectively from the list. NOTE: you can load from multiple dates into one dataset
#     ```python
#     controller.load([
#         datetime(YYYY, MM, DD, hh, mm, ss),
#         date(YYYY, MM, DD),
#         ...
#     ], 'N' | 'S')
#     ```

# In[16]:


controller.load([
    date(2013, 1, 6),
    datetime(2013, 2, 6, 12, 30, 0)
], 'N')


# As you may have noticed, it is really easy to plug dates from the ```browse``` method into the ```load``` method

# In[17]:


hemi = 'N'
dates = controller.browse(hemi)
controller.load(dates, hemi)


# ## AMGeO's xarray datasets
# 
# As stated, AMGeO uses Xarray to load Assimilative Maps into a sensible data structure for 
# data wrangling and processing. 
# 
# This section is to go over some of the neat features that come with interacting with AMGeO maps with Xarray datasets.
# 
# Below is a diagram of the organization of an Xarray dataset with AMGeO maps
# 
# ![AMGeO Xarray dataset](./static/AMGeOXarrayDataset.png)

# Lets load all of our data generated so far into a Dataset for us to experiment with

# In[18]:


ds = controller.load(controller.browse('N'), 'N')
ds


# ### Data variables

# Once you have loaded a dataset, you are able to access various ```data variables``` that an AMGeO map generates. These are just ways to differentiate between different kinds of data you might be interested in. When accessing a ```data variable```, you will get a ```DataArray``` in return.
# 
# We can see all of the data variables that are accessible in an AMGeO Dataset by doing the following: 

# In[19]:


ds.data_vars


# To get a `DataArray` of the data variable in question, simple access it like you would in a normal python `dict` option

# In[20]:


# Get Hall Conductance
ds['cond_hall']


# ### Coordinates/Dimensions
# 
# One of the main advantages to using Xarray for managing scientific data is how it is able to manage multi-dimensional datasets. Traditionally, accessing information regarding the dimensions of your arrays must be made explicit in comments or stored in auxillary data structures. With ```DataArray```, it is all in one place

# In[21]:


epots = ds['epot']
epots.dims


# As seen above, the first dimension of the 3 dimensional array ```epots``` is ```time```, followed by ```latitude``` and ```longitude``` respectively. 
# 
# `lat` and `lon` have shapes `24` and `37` respecively, to create a 24x37 grid of the N/S hemisphere.
# 
# Another cool part of Xarray is ```coords```, that act as coordinates to your dimensions for specific elements

# In[22]:


epots.coords


# By accessing the ```coords``` property, we can see the types and data stored in the coordinates for a specific DataArray. 
# These are also accessible on a per element basis, with the ability to see a specific coordinate

# In[23]:


# get time coordinate on first element on epot DataArray
epots[0].time


# In[24]:


# dims => [time, lat, lon]
potential = epots[0][12][16]
potential.lat


# ### Dataset metadata
# 
# In addition to robust dimension/coordinate information, you can also attach metadata to your DataArrays. AMGeO does this on multiple properties, and they are accessible by calling the ```attrs``` property

# In[25]:


# get DataSet metadata
ds.attrs


# In[26]:


# get DataVariable metadata
ds['joule_heat'].attrs


# In[27]:


# get latitude attributes
ds['joule_heat'][0].lat.attrs


# ## Compatability with matplotlib
# 
# Xarray DataArrays also make quick plotting much easier, with coordinates and metadata accessible from the same data structure

# In[28]:



def _polar2dial(ax):
    """
    Turns a matplotlib axes polar plot into a dial plot
    """
    #Rotate the plot so that noon is at the top and midnight
    #is at the bottom, and fix the labels so radial direction
    #is latitude and azimuthal direction is local time in hours
    ax.set_theta_zero_location('S')
    theta_label_values = np.array([0.,3.,6.,9.,12.,15.,18.,21.])*180./12
    theta_labels = ['%d' % (int(th/180.*12)) for th in theta_label_values.flatten().tolist()]
    ax.set_thetagrids(theta_label_values,labels=theta_labels)

    r_label_values = 90.-np.array([80.,70.,60.,50.,40.])
    r_labels = [r'$%d^{o}$' % (int(90.-rv)) for rv in r_label_values.flatten().tolist()]
    ax.set_rgrids(r_label_values,labels=r_labels)
    ax.set_rlim([0.,40.])
    
def plot_epot_map(fig, lats, lons, epot):
    ax = fig.add_subplot(111, projection='polar')
    _polar2dial(ax)
    
    # plotting
    r = 90.-lats
    th = np.radians(lons)
    v = 30000
    levels=np.linspace(-v,v,30)
    cb = ax.contourf(th,r,epot,levels=levels,cmap='RdBu_r', vmin=-v, vmax=v,extend='both')
    
    # metadata attributes accessible on a DataArray
    units = epot.attrs['units']
    description = epot.attrs['longname']
    
    fig.colorbar(cb,label=f'{description} [{units}]')
    return ax

fig = plt.figure(figsize=(4, 4))

# grab 24x37 grid of Electo-static potentials
epot = ds['epot'][1]
# grab the time for this grid
t = epot.time.values
# plot epots with correct lat/lon coords
ax = plot_epot_map(fig, epot.lat, epot.lon, epot)
ax.set_title('Electric Potential map for %s' % t, pad=15, size=20)
plt.show()


# ## Compatability with numpy
# 
# Xarray has native support for quite a few Numpy compatable operations
# 
# Look [here](http://xarray.pydata.org/en/stable/user-guide/duckarrays.html) for a full list of support for Numpy
# 
# It is also possible to convert a `DataArray` to a `ndarray` with the `values` property

# In[29]:


# convert from DataArray to Numpy Array
arr = ds['joule_heat'].values
type(arr)


# ## Compatability with apexpy
# 
# [ApexPy](https://pypi.org/project/apexpy/) is a fully fleshed out library for geospatial coordinate systems conversions such as Geodetic, Magnetic Local Time, and Apex. 
# 
# AMGeO's latitude and longitude are in `Magnetic Apex Latitude` and `Magnetic Local Time in Degrees`, respectively, which is simple enough to transform to other coordinate systems using this package. 

# In[30]:


# first, create an apex_out instance

# for mlt, need specific date, so lets load up a dataset with a specific date in mine
dates = controller.browse('N')
dates[0]


# In[31]:


d = dates[0]
ds = controller.load(d, 'N')

# from here, we can create an apex_out instance for coordinate conversion
apex_out = Apex(date=d)
apex_out


# ### AMGeO to geodetic
# 
# For plots using the common mercator projection, Geodetic is what we will be looking for

# In[32]:


# need to create 24x37 grid of lat & lons for conversion based on 24x37 lat lon grid

amgeo_lats, amgeo_lons = np.zeros((24, 37)), np.zeros((24, 37))
for i in range(24):
    for j in range(37):
        amgeo_lats[i][j] = ds.lat.values[i]
        amgeo_lons[i][j] = ds.lon.values[j]
amgeo_lats, amgeo_lons = np.array(amgeo_lats), np.array(amgeo_lons)
amgeo_lats.shape, amgeo_lons.shape


# In[33]:


# NOTE: AMGeO lons are mlt in degrees, so simple transform to move to apex mlt
mlt = amgeo_lons / 180 * 12


# In[34]:


# get specific reference date for conversion (needed for mlt conversion)
dt = controller.browse(d, 'N')[0]

# now, can convert to geodetic, AMGeO uses a reference height of 110km (the nominal F layer)
geo_lat, geo_lon = apex_out.convert(amgeo_lats, mlt, 'mlt', 'geo', datetime=dt, height=110)
geo_lat.shape, geo_lon.shape


# ## Compatability with cartopy
# 
# [CartoPy](https://scitools.org.uk/cartopy/docs/latest/index.html) is a popular python package that allows for plotting onto Geographic 
# projections of the world.
# 
# AMGeO's API lends itself well to mapping its data easily to these plotting tools.

# ### Plotting AMGeO electostatic potential on orthographic projection
# 
# Using the convenient `geo_lat` and `geo_lon` values we just generated, we can use Cartopy's `PlatteCarree` transform to map these values onto an `Orthographic` projection. 
# 
# The `Orhtographic` projection will suit nicely for visualzing an AMGeO grid of electostatic potentials on the northern hemisphere, which will spread from the magnetic north pole.

# In[35]:


fig = plt.figure(figsize=[10, 5])

idx = 1

# Northern Hemisphere
ax = fig.add_subplot(1, 2, 1, projection=crs.Orthographic(0, 90))

ax.coastlines(zorder=3)
ax.stock_img()
ax.gridlines()

ax.scatter(geo_lon, geo_lat, c=ds.epot[idx], cmap='coolwarm', transform=crs.PlateCarree())

ax.set_title(f'Epots for {ds.time.values[idx]}')

plt.show()


# ## Pandas compatability
# 
# While not necessarily easier, since AMGeO works with multi-dimensional data, Xarray provides compatability with pandas. A more comprehensive overview can be found [here](http://xarray.pydata.org/en/stable/user-guide/pandas.html)

# In[36]:


# convert AMGeO Xarray DataSet to Pandas DataFrame
df = ds.to_dataframe()
print(type(df))
df


# ## Conclusion
# 
# This notebook showcases the standalone utility of AMGeO's new API, as well as the various ways it can be used in tandem with other popular python packages. 
# 
# Please get started with AMGeO [here](https://amgeo.colorado.edu/), we would love any feedback to continue improving our software.

# # References
# 
# AMGeO Collaboration (2019), A Collaborative Data Science Platform for the Geospace Community: Assimilative Mapping of Geospace Observations (AMGeO) v1.0.0, http://doi.org/10.5281/zenodo.3564914.
