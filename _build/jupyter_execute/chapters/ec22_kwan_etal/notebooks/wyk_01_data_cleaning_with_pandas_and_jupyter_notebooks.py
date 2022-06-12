#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning with Pandas and Jupyter Notebooks

# ## Author(s)
# 
# - Author1 = {"name": "Wai-Yin Kwan", "affiliation": "Whirl-i-Gig", "email": "wyk@whirl-i-gig.com", "orcid": "0000-0001-6113-0210"}
# 

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Data-Cleaning-with-Pandas-and-Jupyter-Notebooks" data-toc-modified-id="Data-Cleaning-with-Pandas-and-Jupyter-Notebooks-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Data Cleaning with Pandas and Jupyter Notebooks</a></span><ul class="toc-item"><li><span><a href="#Author(s)" data-toc-modified-id="Author(s)-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Author(s)</a></span></li><li><span><a href="#Purpose" data-toc-modified-id="Purpose-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Purpose</a></span></li><li><span><a href="#Technical-contributions" data-toc-modified-id="Technical-contributions-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Technical contributions</a></span></li><li><span><a href="#Methodology" data-toc-modified-id="Methodology-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Methodology</a></span></li><li><span><a href="#Results" data-toc-modified-id="Results-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Results</a></span></li><li><span><a href="#Funding" data-toc-modified-id="Funding-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Funding</a></span></li><li><span><a href="#Keywords" data-toc-modified-id="Keywords-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Keywords</a></span></li><li><span><a href="#Citation" data-toc-modified-id="Citation-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Citation</a></span></li><li><span><a href="#Acknowledgements" data-toc-modified-id="Acknowledgements-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Acknowledgements</a></span></li></ul></li><li><span><a href="#Setup" data-toc-modified-id="Setup-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Setup</a></span><ul class="toc-item"><li><span><a href="#Directory-structure" data-toc-modified-id="Directory-structure-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Directory structure</a></span></li><li><span><a href="#Library-import" data-toc-modified-id="Library-import-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Library import</a></span></li><li><span><a href="#Local-library-import" data-toc-modified-id="Local-library-import-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Local library import</a></span></li><li><span><a href="#Set-file-path-variables" data-toc-modified-id="Set-file-path-variables-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Set file path variables</a></span></li></ul></li><li><span><a href="#Best-practices-and-processing-notes" data-toc-modified-id="Best-practices-and-processing-notes-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Best practices and processing notes</a></span><ul class="toc-item"><li><span><a href="#Use-conda-to-manage-dependencies-and-virtual-environments" data-toc-modified-id="Use-conda-to-manage-dependencies-and-virtual-environments-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Use conda to manage dependencies and virtual environments</a></span></li><li><span><a href="#Version-Control-/-Git" data-toc-modified-id="Version-Control-/-Git-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Version Control / Git</a></span></li><li><span><a href="#Unit-testing" data-toc-modified-id="Unit-testing-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Unit testing</a></span></li><li><span><a href="#Changes-to-data-files-are-done-in-code" data-toc-modified-id="Changes-to-data-files-are-done-in-code-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Changes to data files are done in code</a></span></li><li><span><a href="#Read-files" data-toc-modified-id="Read-files-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Read files</a></span><ul class="toc-item"><li><span><a href="#Example" data-toc-modified-id="Example-3.5.1"><span class="toc-item-num">3.5.1&nbsp;&nbsp;</span>Example</a></span></li></ul></li><li><span><a href="#Viewing-the-dataframe" data-toc-modified-id="Viewing-the-dataframe-3.6"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>Viewing the dataframe</a></span></li><li><span><a href="#Basic-cleanup-pattern" data-toc-modified-id="Basic-cleanup-pattern-3.7"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>Basic cleanup pattern</a></span></li><li><span><a href="#View-the-changed-files" data-toc-modified-id="View-the-changed-files-3.8"><span class="toc-item-num">3.8&nbsp;&nbsp;</span>View the changed files</a></span></li></ul></li><li><span><a href="#Data-processing-and-analysis" data-toc-modified-id="Data-processing-and-analysis-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Data processing and analysis</a></span><ul class="toc-item"><li><span><a href="#Basic-file-cleanup" data-toc-modified-id="Basic-file-cleanup-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Basic file cleanup</a></span><ul class="toc-item"><li><span><a href="#Before-cleanup" data-toc-modified-id="Before-cleanup-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Before cleanup</a></span></li><li><span><a href="#After-cleanup" data-toc-modified-id="After-cleanup-4.1.2"><span class="toc-item-num">4.1.2&nbsp;&nbsp;</span>After cleanup</a></span></li><li><span><a href="#Clean-up-all-files-and-save-the-changes" data-toc-modified-id="Clean-up-all-files-and-save-the-changes-4.1.3"><span class="toc-item-num">4.1.3&nbsp;&nbsp;</span>Clean up all files and save the changes</a></span></li></ul></li><li><span><a href="#Remove-leading-and-trailing-white-spaces" data-toc-modified-id="Remove-leading-and-trailing-white-spaces-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Remove leading and trailing white spaces</a></span><ul class="toc-item"><li><span><a href="#Before-cleanup" data-toc-modified-id="Before-cleanup-4.2.1"><span class="toc-item-num">4.2.1&nbsp;&nbsp;</span>Before cleanup</a></span></li><li><span><a href="#After-cleanup" data-toc-modified-id="After-cleanup-4.2.2"><span class="toc-item-num">4.2.2&nbsp;&nbsp;</span>After cleanup</a></span></li><li><span><a href="#Clean-up-all-files-and-save-the-changes" data-toc-modified-id="Clean-up-all-files-and-save-the-changes-4.2.3"><span class="toc-item-num">4.2.3&nbsp;&nbsp;</span>Clean up all files and save the changes</a></span></li></ul></li><li><span><a href="#Normalizing-columns-names" data-toc-modified-id="Normalizing-columns-names-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Normalizing columns names</a></span><ul class="toc-item"><li><span><a href="#Get-all-unique-column-names" data-toc-modified-id="Get-all-unique-column-names-4.3.1"><span class="toc-item-num">4.3.1&nbsp;&nbsp;</span>Get all unique column names</a></span></li><li><span><a href="#Create-taxa-and-non-taxa-files" data-toc-modified-id="Create-taxa-and-non-taxa-files-4.3.2"><span class="toc-item-num">4.3.2&nbsp;&nbsp;</span>Create taxa and non-taxa files</a></span></li><li><span><a href="#Normalize-headers" data-toc-modified-id="Normalize-headers-4.3.3"><span class="toc-item-num">4.3.3&nbsp;&nbsp;</span>Normalize headers</a></span></li><li><span><a href="#Before-changing-headers" data-toc-modified-id="Before-changing-headers-4.3.4"><span class="toc-item-num">4.3.4&nbsp;&nbsp;</span>Before changing headers</a></span></li><li><span><a href="#After-changing-headers" data-toc-modified-id="After-changing-headers-4.3.5"><span class="toc-item-num">4.3.5&nbsp;&nbsp;</span>After changing headers</a></span></li><li><span><a href="#Change-headers-for-all-files-and-save-the-changes" data-toc-modified-id="Change-headers-for-all-files-and-save-the-changes-4.3.6"><span class="toc-item-num">4.3.6&nbsp;&nbsp;</span>Change headers for all files and save the changes</a></span></li></ul></li><li><span><a href="#Turn-one-column-into-multiple-columns" data-toc-modified-id="Turn-one-column-into-multiple-columns-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Turn one column into multiple columns</a></span><ul class="toc-item"><li><span><a href="#Before-cleanup" data-toc-modified-id="Before-cleanup-4.4.1"><span class="toc-item-num">4.4.1&nbsp;&nbsp;</span>Before cleanup</a></span></li><li><span><a href="#After-cleanup" data-toc-modified-id="After-cleanup-4.4.2"><span class="toc-item-num">4.4.2&nbsp;&nbsp;</span>After cleanup</a></span></li><li><span><a href="#Clean-up-all-files-and-save-the-changes" data-toc-modified-id="Clean-up-all-files-and-save-the-changes-4.4.3"><span class="toc-item-num">4.4.3&nbsp;&nbsp;</span>Clean up all files and save the changes</a></span></li></ul></li><li><span><a href="#Clean-up-row-values" data-toc-modified-id="Clean-up-row-values-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Clean up row values</a></span><ul class="toc-item"><li><span><a href="#Before-cleanup" data-toc-modified-id="Before-cleanup-4.5.1"><span class="toc-item-num">4.5.1&nbsp;&nbsp;</span>Before cleanup</a></span></li><li><span><a href="#After-cleanup" data-toc-modified-id="After-cleanup-4.5.2"><span class="toc-item-num">4.5.2&nbsp;&nbsp;</span>After cleanup</a></span></li><li><span><a href="#Clean-up-all-files-and-save-the-changes" data-toc-modified-id="Clean-up-all-files-and-save-the-changes-4.5.3"><span class="toc-item-num">4.5.3&nbsp;&nbsp;</span>Clean up all files and save the changes</a></span></li></ul></li><li><span><a href="#Check-if-required-columns-exists" data-toc-modified-id="Check-if-required-columns-exists-4.6"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>Check if required columns exists</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# ## Purpose
# 
# Since its inception in the 1960s, the International Ocean Discovery Program (IODP) and its predecessors have recovered sediment cores from ocean basins around the world. The cores provide an extensive amount of information about microorganism fossils and lithologies spanning millions of years. Current challenges to using the scientific ocean drilling (SOD) data include: datasets are stored in different databases with different formats, databases have limited search capabilities, and no one database has all the SOD data. 
# 
# The [extending Ocean Drilling Pursuits (eODP)](https://eodp.github.io/) project aims to standardized SOD data from several sources into one standardize database structure. The standardized data is then added to the Paleobiology Database (paleobiodb.org) and Macrostrat (macrostrat.org) to make the data easily accessible to researchers. This notebook demonstrates how the eODP team uses Jupyter notebooks to clean and standardize 50+ years of SOD data.  This notebook is developed for Python 3.8+ and Jupyter Lab.
# 
# ## Technical contributions
# 
# Demonstration of how to create a reproducible data cleaning workflow using Git, unit testing, directory organization, and modular code.
# 
# 
# ## Methodology
# For eODP, we use multiple notebooks to clean and standardize over 10,000 CSVs of ocean core data. For this presentation, we are using one notebook to clean just 10 files.  
# 
# For each data cleaning step we created: separate sections in this notebook, data cleaning functions in `scripts/normalize_data.py`, and unit tests in `test/test_normalize_data.py`
# 
# ## Results
# 
# By making the raw data, processed data, and data cleaning code available, we hope to give ocean core drilling researchers the ability review our data cleaning process and customize the data cleaning steps if so desired. We also hope researchers can apply ideas and tips from our data cleaning process to their own datasets. 
# 
# ## Funding
# 
# - Award1 = {"agency": "US National Science Foundation", "award_code": "1928362", "award_URL": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1928362 "}
#  
#  
# ## Keywords
# Include up to 5 keywords, using the template below.
# 
# keywords=["data cleaning", "reproducibility", "version control", "testing"]
# 
# ## Citation
# 
# Wai-Yin Kwan, 2021. Data Cleaning with Pandas and Jupyter Notebooks. Accessed 5/30/2022 at https://github.com/wykhuh/ec_eodp_demo
# 
# 
# 
# ## Acknowledgements 
# 
# The template is licensed under a <a href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License.</a>

# # Setup

# ## Directory structure
# 
# - notebooks: Jupyter notebooks
# - processed_data: processed data files
# - raw_data: raw, unprocessed data files
# - scripts: custom data cleaning scripts 
# - tests: unit tests written in pytest

# ## Library import

# In[1]:


# Data manipulation
import pandas as pd

# handle file system
from pathlib import Path 


# ## Local library import
# 

# In[2]:


# Include local library paths
import sys
sys.path.append(str(Path.cwd().parent))

# Import local libraries
from scripts.normalize_data import (
    normalize_columns, 
    remove_bracket_text,
    remove_whitespace,
    normalize_expedition_section_cols,
    print_df
)


# ## Set file path variables
# 
# We store the file paths as variables so that can access the paths in multiple data cleaning steps.

# In[3]:


normalized_nontaxa_path = Path('..', 'processed_data', 'normalized_nontaxa_list.csv')
normalized_taxa_path = Path('..', 'processed_data',  'normalized_taxa_list.csv')

taxa_list_path = Path('..', 'processed_data', 'drafts', 'taxa_list.csv')
nontaxa_list_path = Path('..', 'processed_data', 'drafts', 'nontaxa_list.csv')


# Use `Path` and `rglob` to get all the CSVs in `clean_data/taxa` directory.
paths = list(Path('..', 'processed_data', 'clean_data', 'taxa').rglob('*.csv'))
len(paths)


# # Best practices and processing notes

# ## Use conda to manage dependencies and virtual environments

# The package versions are stored environmental.yml so that when other people run the code, they will install the same packages.
# 
# We use virtual environments to avoid dependency conflicts with other projects.

# ## Version Control / Git
# 
# We use git to track changes in the code and data files.
# 
# We found it helpful to make a commit after each data cleaning step in order to make it easier keep track of the data cleaning steps, and undo the certain steps if needed. To undo a data cleaning step that hasn't been committed, use `git restore`. To undo a data cleaning step that has been committed, use `git revert`, `git reset --hard`, or `get rebase`.

# ## Unit testing
# 
# We wrote unit tests for the data cleaning functions in order to reduce the chances that our data cleaning steps would alter the data files in unexpected ways. The tests are in the `./tests` directory. We used pytest for the unit tests.
# 
# Since we use the same data cleaning functions in multiple notebooks, we created a separate tests directory instead of putting the tests inside the notebooks.
# 
# To run the tests, use `pytest` from the command line. All green dots and `[100%]` means all the tests passed.
# 
# ![screenshot pytest results](images/pytest.png)

# ## Changes to data files are done in code
# 
# In order to make the data cleaning process reproducible, all the changes to the processed data files are done in code. We do not manually edit the processed files. 

# ## Read files

# We used `pandas.read_csv(path, dtype=str)` to read csv and treat all columns as strings. The reason why we used `dtype=str` is because `pandas.read_csv(path)`  will automatically convert the columns to strings, integers, floats, dates. This automatic conversion can change values in unexpected ways such as converting a column with integers and NaN into floats and NaN. 

# ### Example

# In[4]:


path = paths[4]


# We use `dtype=str` so that the column has correct integer values.

# In[5]:


df = pd.read_csv(path, nrows=5 , dtype=str)
df['Pulleniatina coiling (dextral)']


# If we don't include `dtype`, the columns has incorrect float values. pandas automatically converts the integers to floats because of NaNs.

# In[6]:


df = pd.read_csv(path, nrows=5)
df['Pulleniatina coiling (dextral)']


# ## Viewing the dataframe

# One thing that we found helpful when data cleaning is to view the dataframe and the total number of rows and columns to check the changes in the dataframe.
# 
# `print_df` is a custom function that calls `pd.DataFrame.shape` and `pd.DataFrame.head()`

# In[7]:


path = paths[4]
df = pd.read_csv(path, dtype=str)

print_df(df)


# ## Basic cleanup pattern
# 
# For each data cleanup step, we loop over all the files, create a dataframe for each file, execute some code to clean the data, and then save the revised file.

# for path in paths:  
#     
#     df = pd.read_csv(path, dtype=str)
#     
#     # code to change file   
#     
#     df.to_csv(path, index=False)

# ## View the changed files
# 
# After each cleanup step, we use the desktop application [Github Desktop](https://desktop.github.com/) to spot check the changes to the files. 
# 
# If the files look ok, make a commit. If the data cleaning step did not act as expected, undo the changes in the data files using `git restore`, update the data cleaning function and the tests, and rerun the data cleaning step. 
# 
# The screenshot below shows the changes to `Micropal_CSV_1/318_U1355A_Planktic_Forams.csv`

# ![screenshot of Github Desktop showing the changed data files](images/git_diff.png)
# 

# # Data processing and analysis
# 
# There are many steps needed to clean up the data files. 

# ## Basic file cleanup
# 
# pandas has methods that can be used to do some basic file cleanup.
#   
# - delete dataframe column if all values are NA  
#   dropna(axis='columns', how='all', inplace=True) - [pandas.DataFrame.dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
#   
# 
# - delete dataframe row if all values are NA  
#   dropna(axis='index', how='all', inplace=True) - [pandas.DataFrame.dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
#   
#   
# - remove duplicate rows in dataframe  
#   drop_duplicates(inplace=True) - [pandas.DataFrame.drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)
# 

# ### Before cleanup
# 
# The file has 20 rows and 41 columns.

# In[8]:


path = paths[7]

df = pd.read_csv(path, dtype=str)
print_df(df)


# ### After cleanup 
# 
# The number of rows changed from 20 to 17, and the number of columns changed from 41 to 26.

# In[9]:


df.dropna(axis='columns', how='all', inplace=True)  
df.dropna(axis='index', how='all', inplace=True)
df.drop_duplicates(inplace=True)

print_df(df)


# ### Clean up all files and save the changes
# 
# Do basic file cleanup on all the files.

# In[10]:


for path in paths:
    df = pd.read_csv(path, dtype=str)
    
    df.dropna(axis='columns', how='all', inplace=True)  
    df.dropna(axis='index', how='all', inplace=True)
    df.drop_duplicates(inplace=True)
    
    df.to_csv(path, index=False)


# ## Remove leading and trailing white spaces
# 
# We created a custom function `remove_whitespace` to remove all leading and trailing white spaces from both the headers and row values. 
# 
# Since we wanted to remove white spaces from both the headers and row values, we used `read_csv(header=None)` and `to_csv(header=False)` so that pandas treat the first row like any other row.

# ### Before cleanup

# In[11]:


df = pd.read_csv(paths[0], dtype=str, header=None)

print_df(df)


# ### After cleanup 

# In[12]:


df = pd.read_csv(paths[0], dtype=str, header=None)

remove_whitespace(df)

print_df(df)


# ### Clean up all files and save the changes
# 
# Remove white space from all files.

# In[13]:


for path in paths:
    df = pd.read_csv(path, dtype=str, header=None)
    
    remove_whitespace(df)
    
    df.to_csv(path, index=False, header=False)


# ## Normalizing columns names
# 
# For the ocean core drilling expedition 312 and later, the researchers for each expedition determined the format of their data files. This resulted in a lot of variability in the file columns. We had to standardized the columns names and update data files. For instance, 'Bottom [cm]' and 'Bottom[cm] [cm]' in the raw files are 'Bottom [cm]' in the processed files.
# 
# Another challenge with parsing the files is that we had to standardized the taxa names. Issues include misspelling, taxa names change over time, and inconsistent ways of treating rank modifiers.

# ### Get all unique column names
# 
# In order to normalize the header header names, we needed to get all the headers for all the files. 
# 
# Since we only need the header names, use `nrow=0` with `read_csv`. 

# In[14]:


pd.read_csv(paths[1], dtype=str, nrows=0)


# We used `pandas.DataFrame.columns()` and python `set` to get all the unique columns for all the files.

# In[15]:


all_columns = set()
for path in paths:
    df = pd.read_csv(path, dtype=str, nrows=0)
    
    all_columns.update(df.columns)
    
len(all_columns)


# In[16]:


all_columns


# We then manually separate taxa names from other headers so that we could do some more processing on the taxa.

# In[17]:


taxa_columns = {
 'Candeina nitida',
 'Dentoglobigerina altispira _T_ _PL5',
 'Dentoglobigerina altispira _T_ _PL5_',
 'Dextral:Sinistral _P. obliquiloculata_',
 'Dextral:Sinistral _P. praecursor_',
 'Dextral:Sinistral _P. primalis_',
 'Fragmentation rank [auto-pop]',
 'Genus/species (upper zone)',
 'Genus/species lower zone)',
 'Globigerina bulloides',
 'Globigerina cf. woodi',
 'Globigerina falconensis',
 'Globigerina umbilicata',
 'Globigerinella aequilateralis',
 'Globigerinella calida',
 'Globigerinella calida _B',
 'Globigerinella calida _B_',
 'Globigerinella obesa',
 'Globigerinita glutinata',
 'Globigerinita parkerae',
 'Globigerinita uvula',
 'Globigerinoides bulloideus',
 'Globigerinoides conglobatus',
 'Globigerinoides extremus _T and B',
 'Globigerinoides extremus _T and B_',
 'Globigerinoides fistulosus',
 'Globigerinoides obliquus _T',
 'Globigerinoides obliquus _T_',
 'Globigerinoides quadrilobatus',
 'Globigerinoides ruber',
 'Globigerinoides ruber (pink)',
 'Globigerinoides ruber (white)',
 'Globigerinoides ruber _pink_ T',
 'Globigerinoides ruber _pink_ _T_',
 'Globigerinoides sacculifer',
 'Globigerinoides sacculifer (without sack)',
 'Globigerinoides tenellus',
 'Globigerinoides trilobus',
 'Globigerinoidesella fistulosa _T and B_ _Pt1a',
 'Globigerinoidesella fistulosa _T and B_ _Pt1a_',
 'Globoconella miozea',
 'Globorotalia (Globoconella) inflata',
 'Globorotalia (Globorotalia) tumida tumida',
 'Globorotalia (Hirsutella) hirsuta',
 'Globorotalia (Hirsutella) scitula',
 'Globorotalia (Truncorotalia) crossaformis',
 'Globorotalia (Truncorotalia) truncatulinoides',
 'Globorotalia anfracta',
 'Globorotalia crassaformis',
 'Globorotalia crassaformis sensu lato',
 'Globorotalia flexuosa',
 'Globorotalia flexuosa _T and B_',
 'Globorotalia hessi',
 'Globorotalia hessi _B_',
 'Globorotalia hirsuta',
 'Globorotalia inflata',
 'Globorotalia limbata _B',
 'Globorotalia limbata _B_',
 'Globorotalia limbata _T_',
 'Globorotalia margaritae _T and B_ _PL3',
 'Globorotalia margaritae _T and B_ _PL3_',
 'Globorotalia menardii',
 'Globorotalia multicamerata _T',
 'Globorotalia multicamerata _T_',
 'Globorotalia plesiotumida _B_ _M13b_',
 'Globorotalia plesiotumida _T',
 'Globorotalia plesiotumida _T_',
 'Globorotalia pseudomiocenica _T_ _PL6',
 'Globorotalia pseudomiocenica _T_ _PL6_',
 'Globorotalia scitula',
 'Globorotalia tosaensis',
 'Globorotalia tosaensis _T and B_ _Pt1b',
 'Globorotalia tosaensis _T and B_ _Pt1b_',
 'Globorotalia truncatulinoides',
 'Globorotalia truncatulinoides _B',
 'Globorotalia truncatulinoides _B_',
 'Globorotalia tumida',
 'Globorotalia tumida _B_ _PL1a_',
 'Globoturborotalita apertura _T and B',
 'Globoturborotalita apertura _T and B_',
 'Globoturborotalita decoraperta _T and B',
 'Globoturborotalita decoraperta _T and B_',
 'Globoturborotalita rubescens',
 'Neogloboquadrina acostaensis',
 'Neogloboquadrina acostaensis (dextral)',
 'Neogloboquadrina cf. pachyderma',
 'Neogloboquadrina dutertrei',
 'Neogloboquadrina humerosa',
 'Neogloboquadrina incompta (dextral)',
 'Neogloboquadrina inglei',
 'Neogloboquadrina kagaensis',
 'Neogloboquadrina nympha',
 'Neogloboquadrina pachyderma (dextral)',
 'Neogloboquadrina pachyderma (sin)',
 'Neogloboquadrina pachyderma (sinistral)',
 'Neogloboquadrina pachyderma B (sinistral, inflated form)',
 'Neogloboquadrina pachyderma(dex)',
 'Orbulina universa',
 'Pulleniatina coiling (dextral)',
 'Pulleniatina coiling (sinistral)',
 'Pulleniatina finalis',
 'Pulleniatina finalis _B',
 'Pulleniatina finalis _B_',
 'Pulleniatina obliquiloculata',
 'Pulleniatina obliquiloculata (D)',
 'Pulleniatina praecursor',
 'Pulleniatina praespectabilis',
 'Pulleniatina primalis  _Tand B',
 'Pulleniatina primalis  _Tand B_',
 'Sphaeroidinella dahiscens sensu lato',
 'Sphaeroidinella dehiscens',
 'Sphaeroidinella dehiscens s.l.',
 'Sphaeroidinella dehiscens sensu lato _B_',
 'Sphaeroidinellopsis kochi _T',
 'Sphaeroidinellopsis kochi _T_',
 'Sphaeroidinellopsis seminulina _T_ _PL4',
 'Sphaeroidinellopsis seminulina _T_ _PL4_',
}


# In[18]:


len(taxa_columns)


# Since both `all_columns` and `taxa_columns` are sets, we can subtract them to get the nontaxa headers.

# In[19]:


nontaxa_columns = all_columns - taxa_columns

nontaxa_columns


# In[20]:


len(nontaxa_columns)


# ### Create taxa and non-taxa files
# 
# We saved the the taxa and nontaxa headers to csv so that we can further process them.

# In[21]:


taxa_df = pd.DataFrame(taxa_columns, columns=['verbatim_name'])
taxa_df.sort_values('verbatim_name', inplace=True)
taxa_df.to_csv(taxa_list_path, index=False)

print_df(taxa_df)


# In[22]:


non_taxa_df = pd.DataFrame(nontaxa_columns, columns=['field'])
non_taxa_df.sort_values('field', inplace=True)
non_taxa_df.to_csv(nontaxa_list_path, index=False)

print_df(non_taxa_df)


# ### Normalize headers

# The software developer first uploads the taxa and nontaxa CSVs to Google Sheets, then project PIs and their students work together to manually normalize the original values. The PIs are currently writing a paper with details about the normalization process [5]. 

# In[23]:


taxa_df = pd.read_csv(normalized_taxa_path, dtype=str)
print_df(taxa_df)


# In[24]:


nontaxa_df = pd.read_csv(normalized_nontaxa_path, dtype=str)
print_df(nontaxa_df)


# After the project PIs manually normalized the columns, we need to update the data files with the normalized columns. We create a dictionary that lists the original field name and normalized field name.

# In[25]:


taxa_mapping = taxa_df.set_index('verbatim_name').to_dict()['normalized_name']
taxa_mapping


# In[26]:


nontaxa_mapping = nontaxa_df.set_index('field').to_dict()['normalized_field']
nontaxa_mapping


# ### Before changing headers

# In[39]:


df = pd.read_csv(paths[8], dtype=str)    
df.columns


# ### After changing headers
# 
# `normalize_columns` replaces the original column names with normalized column names. 
# 
# For the nontaxa mapping, 'Label ID' is changed to 'Sample'. For the taxa mapping, 'Neogloboquadrina pachyderma (sin)' is changed to 'Neogloboquadrina pachyderma (sinistral)',  and 'Neogloboquadrina pachyderma(dex)' to 'Neogloboquadrina pachyderma (dextral)'.

# In[40]:


df = pd.read_csv(paths[8], dtype=str) 
normalize_columns(df, taxa_mapping)
normalize_columns(df, nontaxa_mapping)

df.columns


# ### Change headers for all files and save the changes
# 

# In[41]:


for path in paths:
    df = pd.read_csv(path, dtype=str)    
    
    normalize_columns(df, nontaxa_mapping)
    normalize_columns(df, taxa_mapping)
    
    df.to_csv(path, index=False)


# ## Turn one column into multiple columns 
# 
# For some files, `Sample` or `Label ID` column was given, but `Exp, Site, Hole, Core, Type, Section, A/W` columns where not given. All those columns should be in every file.
# 
# `normalize_expedition_section_cols` converts `Sample` or `Label ID` into separate `Exp, Site, Hole, Core, Type, Section, A/W` columns. 
# 
# Sample: 363-U1483A-1H-2-W 75/77-FORAM  
# Exp: 363, Site: U1483, Hole: A, Core: 1, Type: H, Section: 2, A/W: W

# ### Before cleanup
# 
# File has `Sample` column, but is missing `Exp, Site, Hole, Core, Type, Section, A/W` columns.

# In[30]:


df = pd.read_csv(paths[6], dtype=str)  
print_df(df)


# ### After cleanup
# 
# File has `Sample, Exp, Site, Hole, Core, Type, Section, A/W` columns.

# In[31]:


df = pd.read_csv(paths[6], dtype=str) 
df = normalize_expedition_section_cols(df)
print_df(df)


# ### Clean up all files and save the changes
# 
# Normalize `Sample, Exp, Site, Hole, Core, Type, Section, A/W` columns for all files.

# In[32]:


for path in paths:
    df = pd.read_csv(path, dtype=str)   
    
    df = normalize_expedition_section_cols(df)
    
    df.to_csv(path, index=False) 


# ## Clean up row values
# 
# For some of the columns such as taxa, the rows contain abundance data that we want to keep and notes in brackets that we want to remove.  `remove_bracket_text` removes the [note] text.

# ### Before cleanup
# 
# 'Globigerina bulloides' and 'Neogloboquadrina cf. pachyderma' have [318_PF].

# In[33]:


df = pd.read_csv(paths[0], dtype=str)    
print_df(df)


# ### After cleanup
# 
# Remove [318_PF] from 'Globigerina bulloides' and 'Neogloboquadrina cf. pachyderma'.

# In[34]:


df = pd.read_csv(paths[0], dtype=str) 
df = remove_bracket_text(df)
print_df(df)


# ### Clean up all files and save the changes
# 
# Remove bracket text from all files.

# In[35]:


for path in paths:
    df = pd.read_csv(path, dtype=str)
    
    df = remove_bracket_text(df)
    
    df.to_csv(path, index=False)


# ## Check if required columns exists
# 
# After we completed the data cleaning steps, we want to check if certain required columns are present in all the data files.

# In[36]:


required_columns = {
 'A/W',
 'Bottom [cm]',
 'Bottom Depth [m]',
 'Core',
 'Exp',
 'Hole',
 'Sample',
 'Section',
 'Site',
 'Top [cm]',
 'Top Depth [m]',
 'Type'
}


# If a file is missing some required columns, print the file name and the missing columns.

# In[37]:


missing = False

for path in paths:
    df = pd.read_csv(path, dtype=str)    
    cols = set(df.columns)
    diff = required_columns - cols
    
    if(len(diff) > 0):
        missing  = True
        print(path)
        print(required_columns - cols)
    
if not missing:
    print('All files have required columns.')


# # References
# 
# 1. Extending Ocean Drilling Pursuits website https://eodp.github.io
# 2. Github repo for processing eODP data: https://github.com/eODP/data-processing. Folder for eODP raw data files: https://github.com/eODP/data-processing/tree/master/raw_data/
# 3. The normalized nontaxa and taxa csv were provided by Andrew J. Fraass, Leah J. Levay, and Jocelyn A. Sessa.
# 4. LeVay, Leah; Fraass, Andrew; Peters, Shanan; Sessa, Jocelyn; Kaufman, Seth; Kwan, Wai-Yin. Geologic data standardization for database entry: preparing diverse datasets for hosting and accessibility. EarthCube Annual Meeting. Poster.  
# 5. Sessa, Jocelyn; Levay, Leah; Peters, Shanan; Fraass, Andrew. The extending Ocean Drilling Pursuits (eODP) project: synthesizing scientific ocean drilling data.
