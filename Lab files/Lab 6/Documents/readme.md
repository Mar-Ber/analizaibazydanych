# The contents of the replication documentation
The parent folder Lab 2 contains:
- AnalysisData - folder contain copy of original data file (0_DOLNOS╠üLA╠ĘSKIE.csv) and the fully cleaned and processed data files (age_data.csv, days_data.csv, gender_data.csv, name_data.csv and rate_data.csv),
- CommandFiles - the folder contains a script that performs a series of operations to clean, process and visualization data (Lab 6.ipynb),
- Documents - the folder contains document that serves as a codebook for the analysis data files (Data Appendix.md), a document that describes the files included in the replication documentation, and explains how they can be used to replicate the study and reproduce the results (readme.md) and copy of the final report on the project (Final Paper.pdf),
- OriginalData - the folder contains the Metadata folder that provides information about the original data files (Metadata Guide.md) and the original data file serve as a record of the data that started the project (0_DOLNOS╠üLA╠ĘSKIE.csv).

# How to made importable data files
The importable data file does not contain any changes to the original file. In order to restore the importable data file you only have to make a copy of the original file (0_DOLNOS╠üLA╠ĘSKIE.csv).

# Instructions for replicating the study
To replicate the study, run all code sections contained in the file /CommandFiles/Lab 6.ipynb. For this purpose, you must have a documentation structure (all folders) with original and imported files located in the appropriate folders. To run the script, you must have installed Jupyter Notebook (version 4.1.0) and Python (version 3.9) with the following libraries: pandas (version 0.17.1), matplotlib (version 3.3.4) and numpy (version 1.20.1). After the code is executed, new age_data.csv, days_data.csv, gender_data.csv, name_data.csv and rate_data.csv files will appear in the AnalysisData folder (or overwrite the existing ones). The Final Paper.pdf file can be obtained by saving the Lab 6.ipynb script to pdf.
