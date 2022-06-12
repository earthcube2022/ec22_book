#!/usr/bin/env python
# coding: utf-8

# # AJ_01_MPIL_Detection_and_Analysis_Tool

# ## Author(s)
# - Author1 = {"name": "Anli Ji", "affiliation": "Department of Computer Science, Georgia State University, Atlanta, GA", "email": "aji1@student.gsu.edu", "orcid": "0000-0002-1551-2370"}
# - Author2 = {"name": "Nigar Khasayeva", "affiliation": "Department of Computer Science, Georgia State University, Atlanta, GA", "email": "nkhasayeva1@student.gsu.edu", "orcid": "0000-0002-4590-7031"}
# - Author3 = {"name": "Xumin Cai", "affiliation": "Department of Computer Science, Georgia State University, Atlanta, GA", "email": "xcai3@student.gsu.edu", "orcid": ""}
# - Author4 = {"name": "Manolis K. Georgoulis", "affiliation": "Research Center for Astronomy and Applied Mathematics, Academy of Athens, Greece", "email": "manolis.georgoulis@academyofathens.gr", "orcid": "0000-0001-6913-1330"}
# - Author5 = {"name": "Petrus C. Martens", "affiliation": "Department of Physics & Astronomy, Georgia State University, Atlanta, GA", "email": "martens@astro.gsu.edu", "orcid": ""}
# - Author6 = {"name": "Rafal A. Angryk", "affiliation": "Department of Computer Science, Georgia State University, Atlanta, GA", "email": "rangryk@cs.gsu.edu", "orcid": "0000-0001-9598-8207"}
# - Author7 = {"name": "Berkay Aydin", "affiliation": "Department of Computer Science, Georgia State University, Atlanta, GA", "email": "baydin2@gsu.edu", "orcid": "0000-0002-9799-9265"}

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item">
#     <li><span><a href="#MPIL_Detection_and_Analysis_Tool" data-toc-modified-id="MPIL_Detection_and_Analysis_Tool"><span class="toc-item-num">1&nbsp;&nbsp;</span>MPIL_Detection_and_Analysis_Tool</a></span><ul class="toc-item">
#         <li><span><a href="#Author(s)" data-toc-modified-id="Author(s)-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Author(s)</a></span></li>
#         <li><span><a href="#Purpose" data-toc-modified-id="Purpose-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Purpose</a></span></li>
#         <li><span><a href="#Technical-contributions" data-toc-modified-id="Technical-contributions-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Technical contributions</a></span></li>
#         <li><span><a href="#Methodology" data-toc-modified-id="Methodology-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Methodology</a></span></li>
#         <li><span><a href="#Results" data-toc-modified-id="Results-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Results</a></span></li>
#         <li><span><a href="#Funding" data-toc-modified-id="Funding-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Funding</a></span></li>
#         <li><span><a href="#Keywords" data-toc-modified-id="Keywords-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Keywords</a></span></li>
#         <li><span><a href="#Citation" data-toc-modified-id="Citation-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Citation</a></span></li>
#         <li><span><a href="#Acknowledgements" data-toc-modified-id="Acknowledgements-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Acknowledgements</a></span></li></ul></li>
#     <li><span><a href="#Setup" data-toc-modified-id="Setup-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Setup</a></span><ul class="toc-item">
#         <li><span><a href="#Library-import" data-toc-modified-id="Library-import-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Library import</a></span></li>
#         <li><span><a href="#Local-library-import" data-toc-modified-id="Local-library-import-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Local library import</a></span></li></ul></li>
#     <li><span><a href="#Parameter-definitions" data-toc-modified-id="Parameter-definitions-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Parameter definitions</a></span></li>
#     <li><span><a href="#Data-import" data-toc-modified-id="Data-import-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Data import</a></span></li>
#     <li><span><a href="#Data-processing-and-analysis" data-toc-modified-id="Detection-process-and-analysis-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Detection process and analysis</a></span><ul class="toc-item">
#         <li><span><a href="#Identify-polarity-regions" data-toc-modified-id="Identify-polarity-regions-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Identify Polarity Region by Strength threshold</a></span></li>
#         <li><span><a href="#Identify-polarity-regions" data-toc-modified-id="Identify-polarity-regions-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Apply Canny Edge Detection</a></span></li>
#         <li><span><a href="#Extend-edge-thickness" data-toc-modified-id="Extend-edge-thickness-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Extend the thickness of edge of Polarity region</a></span></li>
#         <li><span><a href="#Candidate-PIL" data-toc-modified-id="Candidate-PIL-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Candidate PIL</a></span></li>
#         <li><span><a href="#Magnetic-field-strength-filter" data-toc-modified-id="Magnetic-field-strength-filter-5.5"><span class="toc-item-num">5.5&nbsp;&nbsp;</span>Remove part based on magnetic field strength filter (95% threshold)</a></span></li>
#         <li><span><a href="#Morphological-thinning-operations" data-toc-modified-id="Morphological-thinning-operations-5.6"><span class="toc-item-num">5.6&nbsp;&nbsp;</span>Morphological thinning operations</a></span></li>
#         <li><span><a href="#Further-filter-PIL" data-toc-modified-id="Further-filter-PIL-5.7"><span class="toc-item-num">5.7&nbsp;&nbsp;</span>Further Filter PIL based on Length/Size (14 pixel)</a></span></li>
#         <li><span><a href="#Generate-RoPI" data-toc-modified-id="Generate-RoPI-5.8"><span class="toc-item-num">5.8&nbsp;&nbsp;</span>Generate Region of Polarity Inversions (RoPI)</a></span></li>
#         <li><span><a href="#Generate-convex-hull" data-toc-modified-id="Generate-convex-hull-5.9"><span class="toc-item-num">5.9&nbsp;&nbsp;</span>Generate convex hull of PIL</a></span></li></ul>
#     <li><span><a href="#Video-analysis-tool" data-toc-modified-id="Video-analysis-tool-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Video Analysis Tool</a></span></li>
#     <li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# ## Purpose
# Magnetic polarity inversion lines (MPILs) detected from solar active regions with attributes engineered from them are recognized as one of the essential features for predicting the characteristics of explosive and eruptive instabilities such as solar flares and coronal mass ejections (CME). We have built a software framework that can detect MPILs from the line-of-sight (LoS) or the radial component of the magnetic field vector in solar active region magnetogram patches. As part of our efforts, we applied this detection method on magnetogram patches obtained from HMI Active Region Patches (HARP) data product. This tool is customizable and can be used to detect, understand and analyze intrinsic characteristics of MPILs.
# 
# 
# ## Technical contributions
# - We share detection our tool in the notebook and present the inner works of our detection functions as well as visualization for the MPIL detection technique over a set of eruptive active regions from Solar Cycle 24.
# - We also provide a qualitative evaluation of our module and exploratory analyses that highlight the relationships between the time evolution characteristics of MPILs in addition to a video visualization tool for the MPILs and related data products.
# - The tools and code implemented in the notebook have been developed with user defined thresholds that allow easy modification for analysis.
# 
# 
# ## Methodology
# A brief summary of the detection method is as follows: 
# 
# First, we identify the positive and negative polarity regions by applying a magnetic field strength threshold of +/-100 Gauss on active region magnetogram patches. Then, we obtain the boundaries of positive and negative polarity regions by using an edge detection technique and apply intersection and thinning morphological operations along with a magnetic field strength filter to identify coarse MPILs. Lastly, we generate final MPILs by imposing a size filter that removes the relatively small disconnected components/lines and retains more significant ones. 
# 
# In addition to the MPIL detection tool, we provide feature extraction functions to obtain the properties of MPILs (i.e., MPIL size, the area of polarity inversion, the masked unsigned flux of enclosing MPIL, convexity, eigenvalues, fractal dimension, and Hu moments) and MPIL-related binary masks of rasters. These spatiotemporal data components can be extracted from any set of magnetogram patch series, which can be used to build a comprehensive and complementary data source for space weather forecasting efforts.
# 
# 
# ## Results 
# This work provides a detection and visualization analysis tool for identifying MPILs and it can also be parameterized based on users' requirements. We present detection results for a well-known active region, NOAA AR 11158 (HARP 377), consisting of 50 magnetogram patches (CEA series) with 1 hour cadence. Our detection results show that our approach can successfully identify PILs and other relevant metadata elements. Our video visualization tool can also be used to visually analyze the evolution of magnetic polarity inversion lines and their structure.
# 
# 
# ## Funding
# - Award = {"agency": "NSF", "award_code": "2104004", "award_URL": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2104004"}
# 
# 
# ## Keywords
# keywords=["Magnetic Polarity Inversion Lines", "Solar Active Regions", "Feature Extraction"]
# 
# 
# ## Citation 
# A. Ji, N. Khasayeva, X. Cai, M. K. Georgoulis, P. C. Martens, R. A. Angryk, B. Aydin, 2022. MPIL Detection and Analysis Tool. Accessed 4/13/2022 at https://github.com/annieee6446/ec22-MPIL
# 
# 
# ## Acknowledgements 
# The data used in this research is courtesy of NASA/SDO and the HMI science teams.

# # Setup
# 
# ## Library import
# We will import glob for file operations. We will import sunpy.map and matplotlib.pylot for visualizations. 

# In[1]:


# File operations
import glob as glob
# Visualizations
import sunpy.map
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


# ## Local library import
# We will import the utility functions from our detection framework and video visualization tool. 

# In[2]:


# Include local library paths
import sys
sys.path.append('../utils')

# Import local libraries
from utils.region_detection import pos_neg_detection
from utils.pil_detection import detection
from utils.video_loading import video_loader

# Define HARP AR number as well as input and output path
HARP_AR = 377
input_path = './Sample_Input/'
output_path = './Sample_Output/'

# Create class object by initializing path to samples and the HARP number of the sample input
dt = pos_neg_detection()
pil_dt = detection(input_path,HARP_AR)
loader = video_loader()

# Check whether output path exists
pil_dt.check_outpath(output_path)


# # Parameter definitions
# The tools and code implemented in the notebook have been developed with user defined thresholds that allow easy modification for analysis.
# - STRENGTH_FILTER: Unsigned magnetic field strength threshold for identifying polarity regions.
# - BUFFER_SIZE: Kernel size for spatial buffering of polarity region edges in pixels.
# - PRESERVED_FLUX_RATIO: Flux threshold for filtering insignificant intersection regions based on accumulated flux. The minimum ratio of total unsigned flux to be preserved in polarity inversion regions is between [0, 1]
# - MIN_MPIL_SIZE: Size filter threshold for removing small polarity inversion lines. It represents the minimum number of contiguous CEA pixels contained in each disconnected MPIL. Each pixel size from HARP series roughly covers 131,400 km^2. 

# In[3]:


STRENGTH_FILTER = 100
BUFFER_SIZE = 4
PRESERVED_FLUX_RATIO = 0.95
MIN_MPIL_SIZE = 14


# # Data import
# Our PIL detection framework applies to longitudinal magnetogram patches. Throughout the development lifecycle of our framework, we made use of the HMI Active Region Patches (HARP) data product [1]. However, it can be used with other magnetogram data series. HARPs are essentially tracked active regions and come with both vector and LoS components of magnetic field. The LoS magnetic field product is stored in FITS format and can be accessed from JSOC (http://jsoc.stanford.edu/ajax/lookdata.html). We primarily used the definitive series with 720 seconds cadence which are mapped the Lambert Cylindrical Equal Area (CEA) projection, where each pixel roughly occupies the same physical area on the Sun. For brevity, in the samples shown below, we adopt a one hour cadence instead of the 720 seconds. 

# In[4]:


# Count the number of samples
data = glob.glob('./Sample_Input/377/*.fits')
print('Total number of sample images: ' + str(len(data)))


# ## Plot out an example of imported data

# In[5]:


# Specify the index of desired magnetogram patch
# Our sample includes 50 elements (indices 0 to 49)
data_index = 10


# In[6]:


hmi_magmap = sunpy.map.Map(data[data_index])

fig = plt.figure(figsize=(8,6))
hmi_magmap.plot()
plt.xlabel('Carrington Longitude [deg]',fontsize = 16)
plt.ylabel('Latitude [deg]',fontsize = 16)
plt.show()


# # Detection process and analysis

# ## Identify Polarity Region by Strength threshold
# The detection process starts by identifying the positive and negative polarity regions. We generated and applied two binary masks of the opposite polarity regions onto the original maps with a magnetic field strength thresholds of user defined Gauss values. The predefined thresholds are +/- 100 Gauss.

# In[7]:


# Identify the positive and negative polarity regions
pos_377, neg_377 = dt.identify_pos_neg_region(hmi_magmap, pos_gauss = STRENGTH_FILTER, neg_gauss= -STRENGTH_FILTER)

# Create masks for the identified positive and negative polarity regions 
masked_pos = dt.mask_img(pos_377)
masked_neg = dt.mask_img(neg_377)


# Light blue areas show the positive polarity regions
# 
# Dark red areas show negative polarity regions

# In[8]:


fig = plt.figure(figsize=(8,6))
hmi_magmap.plot()
plt.imshow(masked_pos, 'cool', interpolation='none', alpha=0.2)
plt.imshow(masked_neg, 'autumn', interpolation='none', alpha=0.2)
plt.xlabel('Carrington Longitude [deg]',fontsize = 16)
plt.ylabel('Latitude [deg]',fontsize = 16)
plt.show()


# ## Apply Edge Detection
# In this step, we obtain the boundaries of positive and negative polarity regions separately by using the Canny edge operator [2], which applies a Gaussian filter to smooth the magnetogram images and detects the overall contour of the polarity regions.

# In[9]:


# Detect edges of the positive and negative polarity regions
pos_edge_377 = dt.edge_detection(pos_377)
neg_edge_377 = dt.edge_detection(neg_377)

# Create masks for the detected edges of positive and negative polarity regions
masked_pos_edge = dt.mask_img(pos_edge_377)
masked_neg_edge = dt.mask_img(neg_edge_377)


# Light blue areas show the edges of positive polarity regions
# 
# Dark red areas show the edges of negative polarity regions

# In[10]:


fig = plt.figure(figsize=(8,6))
hmi_magmap.plot()
plt.imshow(masked_pos_edge, 'cool', interpolation='none', alpha=1)
plt.imshow(masked_neg_edge, 'autumn', interpolation='none', alpha=1)
plt.xlabel('Carrington Longitude [deg]',fontsize = 16)
plt.ylabel('Latitude [deg]',fontsize = 16)
plt.show()


# ## Apply spatial buffering on the edges of polarity regions
# Region of Polarity Inversions (RoPIs) are the regions where negative and positive polarity regions are sufficiently close. These regions are determined using a topological intersection operation between spatially buffered edges of polarity regions. The intersection areas can then be considered as raw RoPIs. In this step, we spatially buffer the edges of negative and positive polarity regions in binary masks with a user defined buffer kernel size to represent the expanded areas of a given polarity inversion line. This buffer size parameter practically enforces how close polarity regions are expected to be located to be considered as adjacent regions.

# In[11]:


# Spatially buffer edges of negative/positive polarity regions
pos_dil_edge_377 = dt.buff_edge(pos_edge_377, size = BUFFER_SIZE)
neg_dil_edge_377 = dt.buff_edge(neg_edge_377, size = BUFFER_SIZE)

# Create masks for the buffered edges
masked_pos_dil_edge = dt.mask_img(pos_dil_edge_377)
masked_neg_dil_edge = dt.mask_img(neg_dil_edge_377)


# Light blue areas show the buffered edges of positive polarity regions
# 
# Dark red areas show the buffered edges of negative polarity regions

# In[12]:


fig = plt.figure(figsize=(8,6))
hmi_magmap.plot()
plt.xlabel('Carrington Longitude [deg]',fontsize = 16)
plt.ylabel('Latitude [deg]',fontsize = 16)
plt.imshow(masked_pos_dil_edge, 'cool', interpolation='none', alpha=0.5)
plt.imshow(masked_neg_dil_edge, 'autumn', interpolation='none', alpha=0.5)
plt.show()


# ## Candidate RoPIs
# The candidate RoPIs are generated based on the intersection areas of spatially buffered opposite polarity regions.
# 
# In this step, we also include a quality index of SPEI (Severe Projection Effect Index) for checking magnetograms that can be potentially impacted by severe projection effect (greater than 70 degrees East-West).

# In[13]:


pil_orig, label_orig = pil_dt.PIL_detect(pos_gauss = STRENGTH_FILTER, neg_gauss= -STRENGTH_FILTER, size_kernel = BUFFER_SIZE)


# In[14]:


# Generate index for matching the detected MPIL with the current sample
data_num = pil_dt.check_header(hmi_magmap)


# In[15]:


# Create mask for detected MPIL
masked_pil = dt.mask_pil(label_orig[data_num])


# In[16]:


fig = plt.figure(figsize=(8,6))
hmi_magmap.plot()
plt.imshow(masked_pil, 'spring', interpolation='none', alpha=1) # 'spring' represents the bright pink color
plt.xlabel('Carrington Longitude [deg]',fontsize = 16)
plt.ylabel('Latitude [deg]',fontsize = 16)
plt.show()


# ## Candidate MPILs
# ### Refine based on preserved flux ratio
# To generate the candidate PILs, we utilize an unsigned magnetic flux filter on the areas covered by disconnected RoPIs, which ensures that the selected candidate PILs represent within the user defined percentage (denoted by PRESERVED_FLUX_RATIO) of unsigned magnetic flux contained in RoPIs and removes the candidate RoPIs with relatively low flux build up around them.

# In[17]:


strength_label = pil_dt.filter_by_strength(threshold = PRESERVED_FLUX_RATIO)


# In[18]:


masked_filter_RoPIs = dt.mask_pil(strength_label[data_num])


# Magenda lines are the candidate MPILs
# 
# Light yellow parts are removed based on the filter threshold

# In[19]:


fig = plt.figure(figsize=(8,6))
hmi_magmap.plot()
plt.imshow(masked_pil, 'Wistia', interpolation='none', alpha=1) # 'Wistia' represents the light yellow color
plt.imshow(masked_filter_RoPIs, 'spring', interpolation='none', alpha=0.8) # 'spring' represents the bright pink color
plt.xlabel('Carrington Longitude [deg]',fontsize = 16)
plt.ylabel('Latitude [deg]',fontsize = 16)
plt.show()


# ## Morphological thinning operations
# The flux filter is followed by applying a morphological thinning operation [3] to the candidate RoPIs. By doing this we eliminate majority of the foreground pixels and preserve the principal topology of the primary shapes for MPILs.

# In[20]:


thin_df, thin_binary = pil_dt.thin_strength_label(strength_label)


# In[21]:


masked_thinned_MPIL = dt.mask_pil(thin_binary[data_num])


# In[22]:


fig = plt.figure(figsize=(8,6))
hmi_magmap.plot()
plt.imshow(masked_thinned_MPIL, 'spring', interpolation='none', alpha=1) # 'spring' represents the bright pink color
plt.xlabel('Carrington Longitude [deg]',fontsize = 12)
plt.ylabel('Latitude [deg]',fontsize = 12)
plt.show()


# ## Further refinement using size filter
# Lastly, we apply a user-defined size filter in CEA pixels. For HARP data series, each pixel roughly covers approximately 131,400 km^2. This operation removes relatively small MPILs and retain a cleaner set of significant MPILs. The predefined size is 14 pixels in this example.

# In[23]:


filter_image = pil_dt.filter_by_size(thin_df, thin_binary, size_threshold = MIN_MPIL_SIZE)


# In[24]:


masked_size_filter = dt.mask_pil(filter_image[data_num])


# Magenda lines are the candidate MPILs
# 
# Light yellow parts are removed based on the filter threshold

# In[25]:


fig = plt.figure(figsize=(8,6))
hmi_magmap.plot()
plt.imshow(masked_thinned_MPIL, 'Wistia', interpolation='none', alpha=1) # 'Wistia' represents the light yellow color
plt.imshow(masked_size_filter, 'spring', interpolation='none', alpha=1) # 'spring' represents the bright pink color
plt.xlabel('Carrington Longitude [deg]',fontsize = 16)
plt.ylabel('Latitude [deg]',fontsize = 16)
plt.show()


# ## Getting Regions of Polarity Inversion (RoPI)
# We fetch the refined RoPIs as part of our additional metadata raster.

# In[26]:


ropi = pil_dt.RoPI(thin_df)


# In[27]:


masked_ropi = dt.mask_pil(ropi[data_num])


# In[28]:


fig = plt.figure(figsize=(8,6))
hmi_magmap.plot()
plt.imshow(masked_ropi, 'summer', interpolation='none', alpha=1) # 'summer' represents the green color
plt.xlabel('Carrington Longitude [deg]',fontsize = 16)
plt.ylabel('Latitude [deg]',fontsize = 16)
plt.show()


# ## Getting convex hull of PIL
# To generate the convex hull, we determine the convex closure of the set in detected MPIL.

# In[29]:


convex_pil = pil_dt.convex_pil(filter_image)


# In[30]:


masked_convex = dt.mask_pil(convex_pil[data_num])


# In[31]:


fig = plt.figure(figsize=(8,6))
hmi_magmap.plot()
plt.imshow(masked_convex, 'autumn', interpolation='none', alpha=0.2)
plt.xlabel('Carrington Longitude [deg]',fontsize = 16)
plt.ylabel('Latitude [deg]',fontsize = 16)
plt.show()


# # Video Analysis Tool
# Generates the magnetogram images of Active Regions with applied on them Polarity Inversion Line, Region of Polarity Inversion, and Convex Hull masks. 

# In[32]:


loader.build_images(input_path + str(HARP_AR), output_path + str(HARP_AR))


# Displays the video slide of previously created magnetogram images.

# In[33]:


video = loader.display_video(output_path + str(HARP_AR))
video


# # Reference
# [1] M. G. Bobra, X. Sun, J. T. Hoeksema, M. Turmon, Y. Liu, K. Hayashi, G. Barnes, and K. D. Leka, “The helioseismic and magnetic imager (hmi) vector magnetic field pipeline: Sharps – space-weather hmi active region patches,” Solar Physics, vol. 289, no. 9, pp. 3549–3578, Sep 2014. Available: https://doi.org/10.1007/s11207-014-0529-3
# 
# [2] J. Canny, “A computational approach to edge detection,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. PAMI-8, no. 6, pp. 679–698, 1986.
# 
# [3] Jean Serra. 1983. Image Analysis and Mathematical Morphology. Academic Press, Inc., USA.
