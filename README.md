Hw 6
Varshini Ramanathan, 3 Apr 2024

PURPOSE: Generates demonstrative figure for 20.440 project. Specifically, allows user to compare Hi-C maps from two different T cell differentiation stages. 

STRUCTURE:
code: contains files to run
data: files for this analysis are too large, so data must be downloaded (see below). 
figures: contains output plots from code.

DATA: Data are Hi-C whole-genome contact matrices stored in WashU LongRange format (https://wiki.wubrowse.org/Long-range). Data can be downloaded from the following GSE accession no: GSE79422. [1] Specific filenames are included in exec.py but can be modified; any of the Supplementary files from GSE79422 are valid inputs to exec.py.

FILES:
- exec.py: runs convert_matrices with specifiable input
- convert_matrices.py: converts, processes and displays multiple HiC matrices

USAGE: 
- 1. Run exec.py from an IDE of choice and manually modify filenames. Importantly, convert_matrices must be in the same dir as exec.py so that the functions can be used. 
- 2. Data can be stored in any directory, as long as that directory is specified in exec.py
- 3. Dependencies: pandas, numpy, matplotlib

[1]