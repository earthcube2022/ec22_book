#!/usr/bin/env python
# coding: utf-8

# <img src='https://github.com/LinkedEarth/Logos/raw/master/PYLEOCLIM_logo_HORZ-01.png' width="800">
# 
# # PaleoHack: Putting EarthCube tools in the hands of paleogeoscientists
# 
# ## Authors
# 
# **Deborah Khider<sup>1</sup>, Julien Emile-Geay<sup>2</sup>, Alexander James<sup>2</sup>, Feng Zhu<sup>3</sup>**
# 
# <sup>1</sup> Information Sciences Institute, University of Southern California
# <sup>2</sup> Department of Earth Sciences, University of Southern California
# <sup>3</sup> Nanjing University of Information Science and Technology
# 
# * Author1 = {"name": "Deborah Khider", "affiliation": "Information Sciences Institute, University of Southern California", "email": "khider@usc.edu", "orcid": "0000-0001-7501-8430"}
# * Author2 = {"name": "Julien Emile-Geay", "affiliation": "Department of Earth Sciences, University of Southern California", "email": "julieneg@usc.edu", "orcid": "0000-0001-5920-4751"}
# * Author3 = {"name": "Alexander James", "affiliation": "Department of Earth Sciences, University of Southern California", "email": "akjames@usc.edu", "orcid": "0000-0001-8561-3188"}
# * Author4 = {"name": "Feng Zhu", "affiliation": "Nanjing University of Information Science and Technology", "email": "fzhu@nuist.edu", "orcid": "0000-0002-9969-2953"}

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#PaleoHack:-Putting-EarthCube-tools-in-the-hands-of-paleogeoscientists" data-toc-modified-id="PaleoHack:-Putting-EarthCube-tools-in-the-hands-of-paleogeoscientists-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>PaleoHack: Putting EarthCube tools in the hands of paleogeoscientists</a></span><ul class="toc-item"><li><span><a href="#Authors" data-toc-modified-id="Authors-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Authors</a></span></li><li><span><a href="#Purpose" data-toc-modified-id="Purpose-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Purpose</a></span></li><li><span><a href="#Technical-contributions" data-toc-modified-id="Technical-contributions-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Technical contributions</a></span></li><li><span><a href="#Methodology" data-toc-modified-id="Methodology-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Methodology</a></span></li><li><span><a href="#Results" data-toc-modified-id="Results-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Results</a></span></li><li><span><a href="#Funding" data-toc-modified-id="Funding-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Funding</a></span></li><li><span><a href="#Keywords" data-toc-modified-id="Keywords-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Keywords</a></span></li><li><span><a href="#Citation" data-toc-modified-id="Citation-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Citation</a></span></li><li><span><a href="#Acknowledgements" data-toc-modified-id="Acknowledgements-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Acknowledgements</a></span></li></ul></li><li><span><a href="#Setup" data-toc-modified-id="Setup-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Setup</a></span><ul class="toc-item"><li><span><a href="#Library-import" data-toc-modified-id="Library-import-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Library import</a></span></li></ul></li><li><span><a href="#Data-import" data-toc-modified-id="Data-import-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Data import</a></span></li><li><span><a href="#Data-Processing-and-Analysis" data-toc-modified-id="Data-Processing-and-Analysis-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Data Processing and Analysis</a></span><ul class="toc-item"><li><span><a href="#Tutorial-1:-Forcing-and-response" data-toc-modified-id="Tutorial-1:-Forcing-and-response-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Tutorial 1: Forcing and response</a></span><ul class="toc-item"><li><span><a href="#Constructing-insolation-curves" data-toc-modified-id="Constructing-insolation-curves-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Constructing insolation curves</a></span></li><li><span><a href="#Orbital-Coherence" data-toc-modified-id="Orbital-Coherence-4.1.2"><span class="toc-item-num">4.1.2&nbsp;&nbsp;</span>Orbital Coherence</a></span><ul class="toc-item"><li><span><a href="#Clean-up-tool-#1:-Lowpass-filter." data-toc-modified-id="Clean-up-tool-#1:-Lowpass-filter.-4.1.2.1"><span class="toc-item-num">4.1.2.1&nbsp;&nbsp;</span>Clean-up tool #1: Lowpass filter.</a></span></li><li><span><a href="#Clean-up-tool-#2:-Singular-spectrum-analysis-(SSA)" data-toc-modified-id="Clean-up-tool-#2:-Singular-spectrum-analysis-(SSA)-4.1.2.2"><span class="toc-item-num">4.1.2.2&nbsp;&nbsp;</span>Clean-up tool #2: Singular spectrum analysis (SSA)</a></span></li></ul></li><li><span><a href="#Causality" data-toc-modified-id="Causality-4.1.3"><span class="toc-item-num">4.1.3&nbsp;&nbsp;</span>Causality</a></span></li></ul></li><li><span><a href="#Tutorial-2:-Fishing-for-Correlations-at-Sea" data-toc-modified-id="Tutorial-2:-Fishing-for-Correlations-at-Sea-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Tutorial 2: Fishing for Correlations at Sea</a></span><ul class="toc-item"><li><span><a href="#A-case-study-from-Crystal-Cave" data-toc-modified-id="A-case-study-from-Crystal-Cave-4.2.1"><span class="toc-item-num">4.2.1&nbsp;&nbsp;</span>A case study from Crystal Cave</a></span><ul class="toc-item"><li><span><a href="#The-Crystal-Cave-record" data-toc-modified-id="The-Crystal-Cave-record-4.2.1.1"><span class="toc-item-num">4.2.1.1&nbsp;&nbsp;</span>The Crystal Cave record</a></span></li><li><span><a href="#SST-data" data-toc-modified-id="SST-data-4.2.1.2"><span class="toc-item-num">4.2.1.2&nbsp;&nbsp;</span>SST data</a></span></li></ul></li><li><span><a href="#Pitfall-#1:-Persistence" data-toc-modified-id="Pitfall-#1:-Persistence-4.2.2"><span class="toc-item-num">4.2.2&nbsp;&nbsp;</span>Pitfall #1: Persistence</a></span><ul class="toc-item"><li><span><a href="#Single-location" data-toc-modified-id="Single-location-4.2.2.1"><span class="toc-item-num">4.2.2.1&nbsp;&nbsp;</span>Single location</a></span></li></ul></li><li><span><a href="#Pitfall-#2:-Multiple-testing" data-toc-modified-id="Pitfall-#2:-Multiple-testing-4.2.3"><span class="toc-item-num">4.2.3&nbsp;&nbsp;</span>Pitfall #2: Multiple testing</a></span></li><li><span><a href="#Pitfall-#3:-Age-uncertainties" data-toc-modified-id="Pitfall-#3:-Age-uncertainties-4.2.4"><span class="toc-item-num">4.2.4&nbsp;&nbsp;</span>Pitfall #3: Age uncertainties</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-4.2.5"><span class="toc-item-num">4.2.5&nbsp;&nbsp;</span>Conclusions</a></span></li></ul></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# ## Purpose
# 
# PaleoHack aims to train a new generation of paleogeoscientists to use emerging standards and tools developed through EarthCube, namely the Linked Paleo Data Format (LiPD [1]) and Pyleoclim [2]. Training is accomplished through biannual [hackathons](https://linked.earth/paleoHackathon) open to researchers at various career stages. The activities are organized around eight self-guided Jupyter Notebook-based tutorials deployed on a JupyterHub walking the participants through an introduction to Pyleoclim and its object-oriented programming interface to using the package in advanced scientific paleoclimate workflows [3]. These notebooks were based on several studies published within the LinkedEarth group over the past several years.
# 
# The notebooks are hosted on [GitHub](https://github.com/LinkedEarth/paleoHackathon) and made available through [myBinder](https://mybinder.org/v2/gh/LinkedEarth/paleoHackathon/HEAD) for execution, allowing a growing number of scientists to access these training resources without participating in the hackathons. Notebooks 1 and 2 provide general Python and Pyleoclim tutorials while Notebooks 3 to 8 walk through workflows from published studies in the field using Pyleoclim. The notebooks provide example code that can be executed with the data uploaded to the GitHub repository and exercises to test understanding of specific functionalities. 
# 
# In addition to the Pyleoclim-dedicated notebooks, a basic scientific Python [training website](http://linked.earth/ec_workshops_py/) was deployed for new Python users. This website uses material developed by the EarthCube community, in particular [Project Pythia](https://projectpythia.org). Although it is not meant as a replacement for an *Introduction to Python* course, it provides a basic understanding of data structures and analysis code in Python, which Pyleoclim aims to automate and complement for paleoclimate datasets. 
# 
# The purpose of this notebook is to walk through two of the notebooks and the pedagogy behind its development. In this particular examples, we will be examining (1) the relationship between insolation and a composite of three $\delta^{18}O$ records from Chinese speleothems (Sanbao, Hulu, and Dongge caves, [4]) and (2) the danger of relying too strongly on correlation analysis for the interpretation of paleoclimate data using a speleothem record from Crystal Cave, CA ([5]). The version presented here is the *instructor copy*, which contains the answers to the various exercises and is stored on a private GitHub repository.
# 
# ## Technical contributions
# 
# * Leverage existing functionalities in Pyleoclim to understand the relationship between orbital forcing and cave $\delta^{18}O$ from China and pitfalls resulting from correlation analysis.
# * Teach fundamental statistical concepts and associated pitfalls.
# * Introduce Pyleoclim functionalities that enable the rapid analysis and visualization of paleoclimate data.
# 
# ## Methodology
# 
# This notebook utilizes [Pyleoclim](https://pyleoclim-util.readthedocs.io/en/master/)[2], a Python package for the analysis and visualization of paleoclimate data. Pyleoclim builds upon standard Python libraries, namely numpy, pandas, matplotlib, cartopy, and scikit-learn (among others). The package is designed around object-oriented [Series](https://pyleoclim-util.readthedocs.io/en/master/core/ui.html#series-pyleoclim-series), which can be manipulated for plotting, spectral and wavelet analysis, and other time series appropriate operations. 
# 
# An high-level diagram of Pyleoclim user APIs is shown below.
# 
# <img src='https://pyleoclim-util.readthedocs.io/en/master/_images/Pyleoclim_API.png' width="800">
# 
# This notebook features two tutorials based on paleoclimate records obtained from both non-LiPD (csv and a record generated from the [climlab](https://climlab.readthedocs.io/en/latest/) library [6]) and LiPD-formatted datasets to illustrate how Pyleoclim can be used with various data formats. It walks through basic data visualization and analysis of the records using coherence, correlation, and causality. During hackahtons, participants are asked to answer specific questions in the notebooks, designed to help them learn Pyleoclim as well as critically thinking about their scientific objectives. For the purpose of this presentation, the answers will be provided in cells labeled as `answers`. 
# 
# ## Results
# 
# The primary objective of this notebook is to serve as a learning tool for scientists engaged in paleoclimate research at all career stage. It is also an introduction in the use of the Pyleoclim software package.
# 
# ## Funding
# 
# Award1 = {"agency": "US National Science Foundation", "award_code": "1541029", "award_URL": https://www.nsf.gov/awardsearch/showAward?AWD_ID=1541029&HistoricalAwards=false}
# 
# Award2 = {"agency": "JP Morgan"}
# 
# Award3 = {"agency": "US National Science Foundation", "award_code": "2002556", "award_URL": https://www.nsf.gov/awardsearch/showAward?AWD_ID=2002556&HistoricalAwards=false}
# 
# Award3 = {"agency": "US National Science Foundation", "award_code": "2126510", "award_URL": https://www.nsf.gov/awardsearch/showAward?AWD_ID=2126510&HistoricalAwards=false}
# 
# ## Keywords
# 
# keywords=["Paleoclimate","LiPD","Python","Coherence","Correlation","Causality']
# 
# ## Citation
# 
# Khider D., Emile-Geay, J., James, A., Zhu, F. (2022). PaleoHack: Putting EarthCube tools in the hands of paleogeoscientists. Jupyter Notebook. 
# 
# ## Acknowledgements
# 
# The LinkedEarth team would like to thank the EarthCube Technology and Architecture Committee for their support in developing and deploying an introduction Python tutorial and [2i2c](https://2i2c.org) for providing JupyterHub capabilities during the hackathons.
# 
# # Setup
# 
# ## Library import
# 
# We will import 6 libraries:
# 
# * numpy, to facilitate operations with:
# * [climlab](https://climlab.readthedocs.io/en/latest/), a Python package for process-oriented modeling, which we will use to compute insolation curves for specific orbital timescales.
# * pandas, to read csv
# * xarray to read and analyze gridded data
# * cartopy, seaborn and matplotlib for visualizations
# * Pyleoclim

# In[36]:


# Data manipulation and analysis
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import seaborn as sns

#relevant climlab libraries
from climlab import constants as const
from climlab.solar.orbital import OrbitalTable
from climlab.solar.insolation import daily_insolation

#pyleoclim and set its style to 'web'
import pyleoclim as pyleo
pyleo.set_style('web')


# # Data import
# 
# We will import the following datasets throughout the notebook:
# * Tutorial 1: 
#     * A composite record of Chinese speleothem $\delta^{18}O$ (`Sanbao_composite.csv`) [4]. The data is in tabular format with the first column representing age and the second column the $\delta^{18}O$. 
#     * This record will be compared to a generated insolation curve from the climlab package [5]. 
# * Tutorial 2: 
#     * A $\delta^{18}O$ speleothem record from Crystal Cave, California ([6]), stored in LiPD format
#     * the Met Office Hadley Centre's sea surface temperature dataset (HadSST.4.0.1.0) a monthly global field of SST on a 5° latitude by 5° longitude grid from 1850 to date, stored in NetCDF [7]. 

# # Data Processing and Analysis
# 
# ## Tutorial 1: Forcing and response
# 
# A common task in paleoclimatology is to relate a record (or several of them) to what is thought to be their forcing. A classic example comes $\delta^{18}O$ records from Chinese speleothems, broadly interpreted as reflecting continental-scale monsoon circulations. In this notebook we focus on a composite of three Chinese speleothem records (Sanbao, Hulu, and Dongge caves) [4] and its relationship to insolation.
# 
# The composite isn't available in LiPD form, so we create a `Series` object by hand:

# In[2]:


lat_sb = 31.67 # latitude of the composite, defined
df = pd.read_csv('./data/Sanbao_composite.csv')
tsb = pyleo.Series(time=df['age']/1000,time_name='Age',time_unit='ky BP',label='Sanbao/Hulu/Dongge x(-1)',
                  value=-df['d18O'],value_name=r'$\delta^{18}$O',value_unit=u'\u2030')
tsb.plot()


# Note that we multiply the record by `−1`, as the record is conventionally interpreted as "more intense monsoon --> greater isotopic depletion".
# 
# **Exercise 1.1** Use the [`summary_plot`](https://pyleoclim-util.readthedocs.io/en/master/core/ui.html#pyleoclim.core.ui.Series.summary_plot) method to inspect the spectral content of this record. Note that the number of significance test is set to zero by default to save time. For publication-ready plots, you may want to set this to at least 200.

# In[10]:


##your code here##


# **Answer 1.1**

# In[3]:


tsb.summary_plot(n_signif_test=0)


# Sustained power in the ~20ky is evident, suggesting a link to orbital precession. Let us investigate this link in more details:
# 
# ### Constructing insolation curves
# 
# Speleothem records from Asia are often compared to summertime insolation (though the latitude of this field is not always consistently chosen). To compute the insolation, we make use of the excellent package climlab by Brian Rose [6]. 

# In[4]:


kyears = np.linspace(-400, 0, 1001 ) # specify time interval and units
orb = OrbitalTable.interp(kyear=kyears) # subset of orbital parameters for specified time
days = np.linspace(0, const.days_per_year, 365)

Qsb = daily_insolation(lat_sb, days, orb) # generate insolation  at Sanbao latitude
Qsb_jja = np.mean(Qsb[:,151:243], axis=1)  # Julian days 152-243 are JJA


# Note that calendar effects are non-negligible at those scales [8]. To be perfectly rigorous, we should take those into account. But this is a hackathon, so let's proceed.
# 
# ### Orbital Coherence
# 
# Given the scalogram  above, the real question is: what sort of phase lag is there between summertime insolation and the isotopic record? To answer this, let's put the heating into a `Series` object so we can unlock some `Pyleoclim` magic.

# In[5]:


qsb = pyleo.Series(time=-kyears,time_name='Age',time_unit='ky BP',label='JJA insolation',
                   value=Qsb_jja,value_name='Insolation',value_unit=r'$W.m^{-2}$' )
qsb.plot()


# **Exercise 1.2** Plot the two on the same graph. Because of the different units, you might want to standardize first.

# In[14]:


##your code here##


# **Answer 1.2**

# In[6]:


qsb_std=qsb.standardize()
tsb_std=tsb.standardize()

fig,ax = tsb_std.plot()
qsb_std.plot(ax=ax)


# There does seem to be extremely coherent behavior at orbital scales, something that we can confirm using using wavelet coherence:

# In[7]:


coh = qsb.wavelet_coherence(tsb)
coh.plot()


# **Exercise 1.3** Interpret this plot, leaning on the documentation of [`coherence`](https://pyleoclim-util.readthedocs.io/en/master/core/ui.html#pyleoclim.core.ui.Series.wavelet_coherence). What do arrows pointing to the right mean? 
# 
# **Answer 1.3** In the 20kyr band, the records are in phase (the arrows are pointing right).
# 
# We do see fairly incoherent behavior at short time scales. That is to be expected, as the insolation curve is a very smooth, modulated harmonic (or nearly so) coming from theoretical calculations, while the speleothem composite is a real-world dataset with real-world uncertainties. Before spending valuable CPU time to compute significance limits (a non-trivial endeavor), let's break out some possible tools to clean this up. 
# 
# #### Clean-up tool #1: Lowpass filter.
# 
# Given that all the noise appears to be at scales shorter than ~5ky, the simplest thing is to filter them out. Of course, `Pyleoclim` has a button for that.
# 
# **Exercise 1.4** Look up the [`filter`](https://pyleoclim-util.readthedocs.io/en/master/core/ui.html#pyleoclim.core.ui.Series.filter) method for the `Series` class and apply with a cutoff scale of 10 kyr. Then plot it on top of the original, with proper labels.

# In[17]:


##your code here##


# **Answer 1.4**

# In[8]:


tsb_filter = tsb.filter(cutoff_freq=1/10)
tsb_filter.label='Sanbao/Hulu/Dongge - 10kyr filter x(-1)'
fig,ax = tsb.plot()
tsb_filter.plot(ax=ax)


# #### Clean-up tool #2: Singular spectrum analysis (SSA)
# 
# The previous notebook in the hackathon series (not reproduced here) introduces SSA, which we now apply to this record. However, this turns out to be quite a long series for SSA, and the decomposition takes an impossibly long while. Since our purpose is to isolate long wavelengths (low frequencies), it's just as convenient to first coarse-grain the series prior to analysis. For this, we use `gkernel`, which is quite good at smoothing along the way:

# In[9]:


tsb_coarse = tsb.gkernel(step=2)
fig, ax = tsb.plot(mute=True,label='original')
tsb_coarse.plot(ax=ax,label='gkernel')
pyleo.showfig(fig)


# Let's try SSA reconstruction on this new series:
# 
# **Exercise 1.5**: Experiment with SSA truncation methods to find a tradeoff that best isolates features of interest.

# In[21]:


##your code here##


# **Answer 1.5**

# In[10]:


ssa = tsb_coarse.ssa()
tsb_ssa = tsb_coarse.copy()
tsb_ssa.value = ssa.RCseries
fig, ax = tsb.plot(mute=True,label='original')
tsb_ssa.plot(ax=ax,label='SSA reconstruction')
pyleo.showfig(fig)


# **Exercise 1.6** Compare the two filtering methods, apply a summary plot to them

# In[24]:


##your code here##


# **Answer 1.6**

# In[11]:


fig,ax = tsb_filter.plot()
tsb_ssa.plot(ax=ax,label='SSA')


# In[12]:


tsb_filter.summary_plot()


# In[13]:


tsb_ssa.summary_plot()


# Now we can plot the filtered series next to the insolation curve.
# 
# **Exercise 1.7** Put the two series on a common timescale (hint: use [`common_time()`](https://pyleoclim-util.readthedocs.io/en/master/core/ui.html#pyleoclim.core.ui.MultipleSeries.common_time)), and plot them together.

# In[30]:


##your code here##


# **Answer 1.7**

# In[14]:


ms  = pyleo.MultipleSeries([qsb.standardize(), tsb_filter.standardize()])
msc = ms.common_time()
msc.plot()


# **Exercise 1.8** Recompute wavelet coherence with the coarse-grained, filtered isotopic record. What changes? Was it worth it? How would you summarize the relationship between insolation and the Sanbao/Hulu/Dongge composite?

# In[32]:


##your code here##


# **Answer 1.8**: Cleaned up effectively for frequencies down to 1/10kyr (to be expected from the filter). Record seems to be in-phase with insolation over the orbital band.

# In[15]:


qs = msc.series_list[0]
ts = msc.series_list[1] 
coh = qs.wavelet_coherence(ts)
coh.plot()


# Now, this plot is still messy at high frequencies, and because they don't mean anything here, let's truncate them:

# In[16]:


coh.plot(ylim=[10,200])


# ### Causality
# 
# It's been known for about 300 years that correlation does not imply causation, so several methods have been devised to try to extract the notion of _causality_ from timeseries data.  `Pyleoclim` offers access to two of them:
# - [Granger causality](http://www.scholarpedia.org/article/Granger_causality)
# - [Liang-Kleeman information flow](http://www.ncoads.org/article/show/28.aspx)
# 
# **(optional) Exercise 1.9** Run the two and compare their output. How do you interpret it?

# In[35]:


##your code here##


# **Answer 1.9**

# In[17]:


caus = qs.causality(ts, settings={'nsim': 2000, 'signif_test': 'isopersist'})
print(caus)


# In[18]:


caus_granger = qs.causality(ts, method = 'granger')
print(caus_granger)


# This analysis suggests a causal relationship between insolation and the speleothem $\delta^{18}O$ composite.
# 
# ## Tutorial 2: Fishing for Correlations at Sea
# 
# Correlation analysis, despite its simplicity and many shortcomings, remains a centerpiece of empirical analysis in many fields, particularly the paleosciences. Computing correlations is trivial enough; the difficulty lies in properly assessing their significance. Of particular importance are four considerations:
# 
# 1. **Persistence**, which violates the standard assumption that the data are independent (which underlies the classical test of significance implemented, e.g. in Excel).
# 2. **Time irregularities**, for instance comparing two records with different time axes, possibly unevenly spaced (which standard software cannot deal with out of the box)
# 3. **Age uncertainties**, for example comparing two records, each with an ensemble of plausible chronologies (generated, for instance, by a Bayesian age model)
# 4. **Test multiplicity** aka the "Look Elsewhere effect", which states that repeatedly performing the same test can result in unacceptably high type I error (accepting correlations as significant, when in fact they are not). This arises e.g. when correlating a paleoclimate record with an instrumental field, assessing significance at thousands of grid points at once, or assessing significance within an age ensemble.
# 
# Accordingly, Pyleoclim facilitates an assessment of correlations that deals with all these cases, makes the necessary data transformations transparent to the user, and allows for one-line plot commands to visualize the results.
# 
# ### A case study from Crystal Cave
# 
# In this notebook we reproduce the case of [9], particularly the example of their section 4, which illustrates several of these pitfalls at once. The example illuminates the issue of relying too strongly on correlations between a paleoclimate record and an instrumental field to interpret the record. Before we start, a disclaimer: the studies investigated in this paper are by no means isolated cases. They just happened to be cases that we knew about, and thought deserved a second look in light of more rigorous statistics. The same study could have been written by subsituting any number of other records interpreted, wholly or in part, on the basis of correlations. Accordingly, what follows should not be viewed as an indictment of a particularly study or group of authors, rather, at how easy it is by the best-intentioned scientists to get fooled by spurious correlations, and (thankfully), how easy we've made it not get similarly fooled by carrying out this analysis with pyleoclim.
# 
# #### The Crystal Cave record
# 
# The example uses the speleothem record of [6] from Crystal Cave, California, in the Sequoia National Forest. Of interest to us is the $\delta^{18}O$ record, which the authors interepret as reflecting sea-surface temperatures (SST) in the Kuroshio Extension region of the West Pacific. This is a strong claim, given that no mechanistic link is proposed, and relies entirely on an analysis of correlations between the record and instrumental SST.
# 
# We first load and plot this record. Since this record is available in LiPD format, we can use methods specific to this file format, which rely on the greater availability of metadata.

# In[19]:


d = pyleo.Lipd('./data/Crystal.McCabe-Glynn.2013.lpd')
cc = d.to_LipdSeries(number=2)   


# Let's do a quick plot to check that we have what we want:

# In[20]:


fig, ax = cc.plot()


# Notice how the code harvested the correct metadata from the LiPD file. If everything is in its right place, it makes it easy to exploit that information. If you're feeling more frisky, you can even ask for a whole dashboard, including a spectrum:

# In[21]:


cc.dashboard(metadata=False)


# This is a very high resolution record, with near-annual spacing (check it), and a broadly red spectrum that exhibits a number of spectral peaks at interannual and decadal scales.
# 
# #### SST data
# 
# The original paper correlated the above record against the Kaplan SST dataset.  In this notebook we instead use the [HadSST4 dataset](https://www.metoffice.gov.uk/hadobs/hadsst4/index.html) [7],  which is more up to date. During the hackathons, the dataset is downloaded to obtain the most up-to-date version. Here a copy is provided (downloaded April 2022).
# 
# We load via the `xarray` package:

# In[23]:


ds = xr.open_dataset('./data/HadSST.4.0.1.0_median.nc')
print(ds)


# As an example, let's only consider the Northern Hemisphere Pacific Ocean. For practicality, let's first adjust the coordinate system so that longitude is expressed from 0 to 360 degrees instead of 180W to 180E:

# In[24]:


ds_rolled = ds.assign_coords(longitude=(ds.longitude % 360)).roll(longitude=(ds.dims['longitude'] // 2))
ds_rolled


# Now let's select the needed data:

# In[25]:


ds_sel = ds_rolled.sel(longitude=slice(120,280),latitude=slice(0,90))
ds_sel


# ### Pitfall #1: Persistence
# 
# Persistence is the tendency of many geophysical timeseries (particularly paleoclimate ones) to show some kind of memory: consecutive observations tend to resemble each other, resulting in timeseries that have fairly broad trends and low-frequency fluctuations, and comparatively little high-frequency fluctuations. 
# 
# This has an important consequence: the standard assumption of independence, which undergirds much of frequentist statistics, is violated in this case. In a timeseries with $n$ fully independent observations (e.g. white noise), the degrees of freedom for the variance are $DOF = n -1$  But if memory is present, this number can be drastically reduced. 
# 
# #### Single location
# Let us look at a random location and build some intuition. First, we need to compute montly anomalies and annualize them. `xarray` makes that easy (4 lines of code), so let's look at the result:

# In[26]:


st = ds['tos'].sel(latitude=32.5, longitude = 142.5, method='nearest')  # 32.5N 142.5W near Kuroshio Extension
climatology = st.groupby("time.month").mean("time")
anomalies = st.groupby("time.month") - climatology
st_annual = anomalies.groupby("time.year").mean("time")
st_annual.plot(figsize=[12, 6])


# Notice the coverage gaps in the 1860s. This, and the fact that the Crystal Cave chronology is not uniformly spaced, would ordinarily make it challenging to compare the two series, requiring some form of interpolation or binning. Pyleoclim does all this for you under the hood.
# 
# To enjoy these benefits, however, let us turn the temperature data into a `Series` object.

# In[27]:


stts = pyleo.Series(time=st_annual.coords['year'].values,
                    time_unit ='year CE', 
                    value=st_annual.values,
                    value_unit = 'C')


# Now we can compute correlations with the Crystal Cave record.

# In[28]:


corr_res = stts.correlation(cc)
print(corr_res.r)


# Quite a few things happened here. First, `pyleoclim` was smart enough to figure out a common timespan between the two records, and used linear interpolation to align the two timeseries on a common axis. It did all this under the hood without you having to lift a finger, but you could get your head in there and customize this process (e.g. choosing a different way to align the time axes) if you wanted it too.
# 
# Now, about the result: the correlation is $r=0.32$. Is it significant?
# 
# The standard way to assess this uses a t-test using the test statistic: $$T = \frac{r \sqrt{n-2}}{\sqrt{1-r^2}}$$. If we plug in the values of $r$ and $n$, we get: 

# In[29]:


ccs = cc.slice([1854,2020])
n = len(ccs.time)
nu = n-2
r = corr_res.r
T  = r *np.sqrt(nu)/(np.sqrt(1-r**2))
print("The test statistic is "+ str(T))


# Under standard assumptions (the data are independent and identically distributed), $T$ follows Student's $t$ distribution (the first [Guiness-soaked distribution](https://priceonomics.com/the-guinness-brewer-who-revolutionized-statistics/) in history). If we make the same assumption and use the $t$ distribution conveniently programmed for us by SciPy, we can compute the p-value (the probability to observe a test statistic at least as large as this one, under this distribution) thusly:

# In[30]:


from scipy.stats import t
pval = 1-t.cdf(T,nu)
print("The p-value is {:10.2e}".format(pval)) # express in exponential notation


# In other words, using the classic test for the significance of correlations "out of the box", one would conclude that SST at 42N, 164E shares so much similarity with the Crystal Cave record that there are only 3 chances in 10,000 that this could have happened randomly. In other words, it looks _very_ significant. 
# 
# But let's take a step back. That test (which is the one that most computing packages, including Excel, will do for you out of the box), is not appropriate here. Why? Because the assumption of independence tramples over the concept of persistence with gleeful impunity. That is, it assumes that consecutive observations bear no resemblance to each other, which is true neither of the Crystal Cave nor the instrumental target. That is to say: because temperature in one year tends to resemble temperature in the previous or following year (same for $\delta^{18}O$), the data are anything but independent. We will quantify this dependence, and its consequences, in a minute. 
# 
# Going back to the result of the `correlation()` command, let's look at its full output:

# In[31]:


print(corr_res)


# Notice that the p-value has been estimated to be 12% (`'p': 0.12`), and therefore the correlation is not deemed significant (`'signif': False`) at the 5% level (`'alpha': 0.05`).
# 
# How did `pyleoclim` arrive at such a different conclusion? By not applying irrelevant assumptions, of course! To know what method was applied exactly precisely, consult the [documentation](https://pyleoclim-util.readthedocs.io/en/master/utils/correlation/corr_sig.html#pyleoclim.utils.correlation.corr_sig) or the function's docstring. 
# 
# **Exercise 2.1** What method does `correlation` use by default to assess significance and what are its assumptions? (hint: check out "correlation" on [Read The Docs](https://pyleoclim-util.readthedocs.io/en/master/), under "The Pyleoclim user interface"), or type `stts.correlation?` at the prompt.
# 
# **Answer 2.1** The default method is `'isospectral`, which phase-randomizes the original signals, thereby preserving the two spectra but scrambling phase relations between the signals. This is the method proposed by Ebisuzaki (1997).
# 
# **Exercise 2.2** There are in fact 3 ways to make this determination in Pyleoclim. Try the other two in the cells below, and compare their p-values on 2-3 trials. Do they give consistent answers or not?  (Hint: use the `settings` dictionary to pass a `method` parameters, and explore the effect of the parameter `nsim`)
# 
# **Answer 2.2**

# In[32]:


corr_ttest = stts.correlation(cc,settings={'method':'ttest'})
print(corr_ttest)


# In[33]:


corr_isopersist = stts.correlation(cc,settings={'method':'isopersistent'})
print(corr_isopersist)


# In[34]:


corr_isopersist = stts.correlation(cc,settings={'method':'isopersistent','nsim':2000})
print(corr_isopersist)


# **Answer 1.2** The other two methods are the T-test adjusted for the loss of degrees of freedom due to persistence, and the isopersistent test, which compares the observed correlation to the distribution of correlations with (by default) 1000 randomly-generated AR(1) timeseries with the same persistence parameters as the original series. In this particular case, the T-test also judges the correlation to be insignificant, but the isopersistent test is more finicky: sometimes it does, sometimes it doesn't. `nsim` only affects the methods that use Monte Carlo simulations (isopersistent and isospectral).  Upping `nsim` ensures more consistent results: for `nsim >= 2000`, the result is consistently judged insignificant. 
# 
# In this case, the three methods concur that the correlation is insignificant, given a sufficient number of simulations.
# 
# ### Pitfall #2: Multiple testing
# 
# The foregoing shows how to properly assess significance at just one location. How would we go about conducting a similar test for an entire field? Let us first try the naive approach: recursively carry out the same test as above at all grid points.  For this, we need not only to loop over grid points, but also store the p-values for later analysis. To save time, we'll use the `ttest` option for `correlation()`, knowing that it is rather approximate. Also, we need to exclude points that have too few observations.  The loop below achieves that. 

# In[35]:


nlon = len(ds_sel['longitude'])
nlat = len(ds_sel['latitude']) 
pval = np.empty((nlon,nlat)) # declare array to store pvalues
corr = np.empty_like(pval) # declare empty array of identical shape
alpha = 0.05
slon, slat = [], [];
for ji in range(nlon):
    for jj in range(nlat):     # TODO add progress bar 
        st = ds_sel['tos'][:,jj,ji]
        climatology = st.groupby("time.month").mean("time")
        anomalies = st.groupby("time.month") - climatology
        st_annual = anomalies.groupby("time.year").mean("time")
        #  test if at least 100 non-NaNs
        noNaNs = len(np.where(np.isnan(st_annual) == False)[0]) # number of valid years
        sstvar = st_annual.var()
        if noNaNs >= 100 and sstvar >= 0.01:
            print("Computing correlation at " + str(ds_sel.latitude[jj].values) + 'N, ' + str(ds_sel.longitude[ji].values) + 'E')
            sttb = pyleo.Series(time=st_annual.coords['year'].values,
                        time_unit ='year CE', 
                        value=st_annual.values,
                        value_unit = 'C')
            corr_res = sttb.correlation(cc, settings={'method':'ttest'})
            pval[ji,jj] = corr_res.p
            corr[ji,jj] = corr_res.r
            if pval[ji,jj] < alpha:
                slon.append(ds_sel.longitude[ji])
                slat.append(ds_sel.latitude[jj])
        else:  
            pval[ji,jj] = np.nan; corr[ji,jj] = np.nan


# In[37]:


pvals = pval.flatten() # make the p-value array a 1D one
pvec = pvals[pvals<1] # restrict to valid probabilities as there are a few weird values.
nt = len(pvec)
print(nt) # check on the final number


# We found 327 with enough data for a meaningful comparison, and 23 locations that pass the test. Where are they? To gain insight, let us plot the correlations and indicate (by shading) which are deemed significant:

# In[38]:


land_color=sns.xkcd_rgb['light grey']
ocean_color=sns.xkcd_rgb['light grey']

fig = plt.figure(figsize=[12, 8])
ax = plt.subplot(projection=ccrs.PlateCarree(central_longitude=180))

# map
ax.add_feature(cfeature.LAND, facecolor=land_color, edgecolor=land_color)
ax.add_feature(cfeature.OCEAN, facecolor=ocean_color, edgecolor=ocean_color)
ax.coastlines()

transform = ccrs.PlateCarree()
latlon_range = (120, 280, 0, 70)
lon_min, lon_max, lat_min, lat_max = latlon_range
lon_ticks = [60, 120, 180, 240, 300]
lat_ticks = [-90, -45, 0, 45, 90]

ax.set_extent(latlon_range, crs=transform)
lon_formatter = LongitudeFormatter(zero_direction_label=False)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
lon_ticks = np.array(lon_ticks)
lat_ticks = np.array(lat_ticks)
mask_lon = (lon_ticks >= lon_min) & (lon_ticks <= lon_max)
mask_lat = (lat_ticks >= lat_min) & (lat_ticks <= lat_max)
ax.set_xticks(lon_ticks[mask_lon], crs=transform)
ax.set_yticks(lat_ticks[mask_lat], crs=transform)

# contour
clevs = np.linspace(-0.9, 0.9, 19)
#corr_r, lon_r = rotate_lon(corr.T, lon)  # rotate the field to make longitude in increasing order and convert to range (0, 360)
im = ax.contourf(ds_sel.longitude, ds_sel.latitude, corr.T, clevs, transform=transform, cmap='RdBu_r', extend='both')

# significant points
plt.scatter(x=slon, y=slat, color="purple", s=3,
            alpha=1,
            transform=transform) 


# colorbar
cbar_pad = 0.05
cbar_orientation = 'vertical'
cbar_aspect = 10
cbar_fraction = 0.15
cbar_shrink = 0.5
cbar_title = 'R'
cbar = fig.colorbar(im, ax=ax, orientation=cbar_orientation, pad=cbar_pad, aspect=cbar_aspect,
                    fraction=cbar_fraction, shrink=cbar_shrink)
cbar.ax.set_title(cbar_title)


# The purple dots on the map are the locations of the gridpoints where the p-values fall under 5%, and they naturally correspond to the regions of highest correlations, though (and this is suspicious) they are rather randomly scattered across the domain.  
# We might be tempted to declare victory and hail them as "significant", but not so fast! 
# Our correlation test, nifty though it is, isn't infallible. In fact, conducting tests at the 5% level (what most people would call "the 95% confidence level") specifically means that we expect 5% of our tests to return spurious results, just from chance alone (the so-called "type I error"). We just carried out $n_t$ tests, so we expect $0.05*n_t \approx 16 $ of those results to be false positives, right out of the gate.  Which ones can we trust?
# 
# One way to approach this is to rank order the p-values of all 327 tests and plot them as in [9], Fig 2.

# In[39]:


#check i/m vs. p-values
indexm = np.arange(1,nt+1,1)
im = 1.0*indexm / nt
thres = 0.05*im
pvec_s = sorted(pvec)
smaller=[]
small_index=[]
larger=[]
large_index=[]

n=0
for pp in pvec_s:
    if pp <=0.05:
        smaller.append(pp)
        small_index.append(im[n])
    else:
        larger.append(pp)
        large_index.append(im[n])
    n=n+1

f, ax = plt.subplots(figsize=(12,8))
plt.plot(im,thres,label='FDR threshold')
plt.plot(small_index,smaller,'ro',markersize=1.5,label='p-values below threshold')
plt.plot(large_index,larger,'ko',markersize=1.5,label='p-values above threshold',alpha=0.3)
plt.axhline(y=0.05,linestyle='dashed',color='silver',label='5% threshold')
plt.xlabel(r'$i/n_t$',fontsize=14)
plt.ylabel(r'$p_i$',fontsize=14)
plt.title('Correlation p-values',fontsize=14, fontweight='bold')
plt.legend()


# One solution to this is the False Discovery Rate (aka **FDR**), which was devised in a celebrated 1995 paper [10](https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.2517-6161.1995.tb02031.x). The idea is to look not just for the p-values under 5% (red dots in the figure above), but for the fraction of those under the blue line, which guards against the false discoveries one expects out of repeatedly testing the same hypothesis over and over again. Luckily for you, we have this coded up in `pyleoclim` (you knew we would). One way to access it is thus:

# In[40]:


fdr_res = pyleo.utils.correlation.fdr(pvec_s)
print(fdr_res)


# And with this treatment, exactly 0 gridpoints pass the test. 
# 
# **Exercise 1.3** redo this with other correlation methods and see if the results change. A little patience is required for the other two methods, which loop over surrogates. We suggest using a moderate number of simulations (`nsim` < 500) to do so; please check the documentation of `corr_sig` for how to reduce this number, which is 1000 by default.  
# 
# **Answer 1.3**

# In[42]:


pval2 = np.empty((nlon,nlat)) # declare array to store pvalues
corr2 = np.empty_like(pval) # declare empty array of identical shape
slon, slat = [], [];
for ji in range(nlon):
    for jj in range(nlat):  
        st = ds_sel['tos'][:,jj,ji]
        climatology = st.groupby("time.month").mean("time")
        anomalies = st.groupby("time.month") - climatology
        st_annual = anomalies.groupby("time.year").mean("time")
        #  test if at least 100 non-NaNs
        noNaNs = len(np.where(np.isnan(st_annual) == False)[0]) # number of valid years
        sstvar = st_annual.var()
        if noNaNs >= 100 and sstvar >= 0.01:
            print("Computing correlation at " + str(ds_sel.latitude[jj].values) + 'N, ' + str(ds_sel.longitude[ji].values) + 'E')
            sttb = pyleo.Series(time=st_annual.coords['year'].values,
                        time_unit ='year CE', 
                        value=st_annual.values,
                        value_unit = 'C')
            corr_res = sttb.correlation(cc, settings={'method':'isospectral','nsim':1000})
            pval2[ji,jj] = corr_res.p
            corr2[ji,jj] = corr_res.r
            if pval[ji,jj] < alpha:
                slon.append(ds_sel.longitude[ji])
                slat.append(ds_sel.latitude[jj])
        else:  
            pval2[ji,jj] = np.nan; corr2[ji,jj] = np.nan


# In[43]:


fdr_res2 = pyleo.utils.correlation.fdr(pval2.flatten())
print(fdr_res2)


# Only one grid point appears significant now.
# 
# 
# ### Pitfall #3: Age uncertainties
# 
# As if the first two pitfalls weren't enough, there is a third difficulty in this comparison: beautiful though U/Th chronologies may be, they are not perfect (do not believe people who tell you otherwise!). Such chronological uncertainties must be taken into account as well. 
# 
# It turns out that the LiPD file loaded above contains not only the raw U/Th dates (dig for them if you're curious), but also an ensemble of age-depth relationships derived from those dates, via the Bayesian age model [BChron](https://cran.r-project.org/web/packages/Bchron/vignettes/Bchron.html). Let us load those 1000 draws from the posterior distribution of ages and put them in a place where `pyleoclim` will be able to work with them:

# In[46]:


cc_ens = cc.chronEnsembleToPaleo(d)


# There are two ways to plot this ensemble. First, as a series of traces:

# In[47]:


fig, ax = cc_ens.plot_traces(mute=True)
cc.plot(color='black', ax = ax)


# It is quite plain that any of the record's main swings can be swung back and forth by up to decades. Another way to see this is to plot various quantiles as an envelope:

# In[48]:


fig, ax = cc_ens.common_time(method='interp').plot_envelope(ylabel = cc.value_name, mute=True)
cc.plot(color='black', ax = ax, linewidth=1)


# Notice how the quantiles are computed over only part of the interval covered by the original series; that is because some age models end up being more compressed or stretched out than the original, and we need a common interval to compute quantiles. In particular, notice how the base of the record could really be anywhere between 850 and 1100 AD.
# Now, what we'd like to do is repeat the exercise of Part 1, correlating the same SST timeseries from 32.5N 142.5W (near the Kuroshio Extension), not just with the published chronology, but this whole ensemble. Remember how we had computed things:

# In[49]:


corr_res = stts.correlation(cc)
print(corr_res.r)


# Though of course, we could have done just the reverse, as correlation is a symmetric operator:

# In[51]:


corr_res = cc.correlation(stts)
print(corr_res.r)


# Now, consider the task ahead: you must iterate over all ensemble members, taking care of aligning their time axis to that of HadSST4; you must compute the correlation and establish its significance with a sensible test (say, Ebisuzaki's isospectral test, see Pitfall #1), you need watch out for test multiplicity (see Pitfall #2) _and_  you need to visualize the results in an intuitive way. Needless to say, Pyleoclim has the answer.
# 
# To keep computing time manageable, let's reduce the number of isospectral simulations to 500, and correlate the ensemble and the SST series:

# In[52]:


nsim = 1000
corr_Kuroshio = cc_ens.correlation(stts,settings={'nsim':nsim}) 


# Now here's the best part: the `corr_Kuroshio` is an object that contains everything you want: the vector of correlations, the p-values, and a method to plot them all:

# In[53]:


corr_Kuroshio.plot()


# Several things jump out at once:
# 1. the correlation histogram is relatively symmetric, meaning that age uncertainties are able to completely overturn the original correlation of about 0.31 : nearly half of the ensemble exhibits negative correlations with SST).  0.31 (9% of common variance) is not a contender for winning the correlation olympics, but it was at least positive. Age uncertainties can easily reverse even the _sign_ of the correlation, not to mention alter its magnitude.
# 
# 1. As shown in teal, only a few \% of the 500*100 correlations just computed are judged significant (note: this would change somewhat every time you run the calculation, based on the randomness of the phase randomization procedure. If reproducibility is essential, you  may also input a [random seed](https://en.wikipedia.org/wiki/Random_seed) to ensure that the same exact random sequence is used from iteration to iteration. 
# 
# 1. Once we take test multiplicity into account via the False Discovery Rate (orange bar), only a fraction of a \%  is deemed significant.
# 
# **Exercise 1.4** redo this at other locations and see if the results change. you may consider picking a patch of the North Pacific and applying this test recursively at each location. 
# 
# **Answer 1.4**

# In[54]:


st = ds['tos'].sel(latitude=32.5, longitude = 147.5, method='nearest')  # pick a new location
climatology = st.groupby("time.month").mean("time")
anomalies = st.groupby("time.month") - climatology
st_annual = anomalies.groupby("time.year").mean("time")
st_annual.plot(figsize=[12, 6])


# Put into a Series object, compute ensemble correlations, and plot:

# In[55]:


stts2 = pyleo.Series(time=st_annual.coords['year'].values,
                     time_unit ='year CE', 
                     value=st_annual.values,
                     value_unit = 'C')
corr_ens2 = cc_ens.correlation(stts2,settings={'nsim':nsim}) 
corr_ens2.plot()


# ### Conclusions
# 
# 
# **Exercise 2.5**  To bring it all together, summarize everything that can go wrong when fishing for correlations (at sea, or on land). Can you think of other papers where correlations with paleoclimate records might have been used unwisely? (no names needed... Just keep that in mind in your own work and point people to more defensible ways of dealing with this danger, i.e. Pyleoclim!) 
# 
# **Answer 2.5** The moral of the story is that all of these pitfalls matter ; any single one of them can turn a correlation initially reported as "significant" into insignificant ones. That is especially the case with a conjunction of pitfalls, with any 2 out of 3. The conjunction of all 3 pitfalls (persistence, test multiplicity, and age uncertainties) is particularly damaging in this example. Fortunatly, Pyleoclim makes it easy to deal with those pitfalls, so there is no excuse not to. 

# # References
# 
# [1] McKay, N. P., & Emile-Geay, J. (2016). Technical Note: The Linked Paleo Data framework – a common tongue for paleoclimatology. Climate of the Past, 12, 1093-1100.
# 
# [2] Khider, D., F. Zhu, J. E.-G. J. Hu, A. James, M. Kwan, P. Athreya, and D. Garijo.  Pyleoclim: A Pythonpackage for the analysis of paleoclimate data (v0.7.2) (2022).  URL https://doi.org/10.5281/zenodo.4002870
# 
# [3] Deborah Khider, Julien Emile-Geay, Feng Zhu, Alexander James, & Yuvi Panda. (2022). PaleoHackathon. Zenodo. http://doi.org/10.5281/zenodo.4556144. GitHub: https://github.com/LinkedEarth/paleoHackathon.
# 
# [4] Cheng, H., Edwards, R., Sinha, A. et al. The Asian monsoon over the past 640,000 years and ice age terminations. Nature 534, 640–646 (2016). https://doi.org/10.1038/nature18591 
# 
# [5] McCabe-Glynn, S., Johnson, K. R., Strong, C., Berkelhammer, M., Sinha, A., Cheng, H., & Edwards, R. L. (2013). Variable North Pacific influence on drought in southwestern North America since AD 854. Nature geoscience, 6, 617-621. https://doi.org/10.1038/ngeo1862.
# 
# [6] Brian Rose, Andrew Williams, Moritz Kreuzer, Chris Cardinale, krachyon, xoviat, Ryan Abernathey, Filipe, & Paul Gierz. (2021). brian-rose/climlab: Version 0.7.12 (v0.7.12). Zenodo. https://doi.org/10.5281/zenodo.4768597
# 
# [7] Kennedy, J. J., Rayner, N. A., Atkinson, C. P., & Killick, R. E. (2019). An ensemble data set of sea‐surface temperature change from 1850: the Met Office Hadley Centre HadSST.4.0.0.0 data set. Journal of Geophysical Research: Atmospheres, 124. https://doi.org/10.1029/2018JD029867
# 
# [8] Bartlein, P. J., & Shafer, S. L. (2019). Paleo calendar-effect adjustments in time-slice and transient climate-model simulations (PaleoCalAdjust v1.0): impact and strategies for data analysis. Climate of the Past, 12(9), 3889–3913. https://doi.org/10.5194/gmd-12-3889-2019
# 
# [9] Hu, J., Emile-Geay, J., & Partin, J. (2017). Correlation-based interpretations of paleoclimate data - where statistics meet past climates. Earth and Planetary Science Letters, 459, 362-371. https://doi.org/10.1016/j.epsl.2016.11.048
# 
# [10] Benjamin, Y., & Hochberg, Y. (1995). Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing. Journal of the Royal Statistical Society: Series B (Methodological), 57(1), 289-300.  https://doi.org/10.1111/j.2517-6161.1995.tb02031.x
