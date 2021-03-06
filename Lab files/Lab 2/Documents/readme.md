# The contents of the replication documentation
The parent folder Lab 2 contains:
- AnalysisData - folder contain copy of importable data file (weather_importable.xlsx) and the fully cleaned and processed data files (prcp_data.xlsx and temp_data.xlsx),
- CommandFiles - the folder contains a script that performs a series of operations to clean and process data (Lab 2.ipynb),
- Documents - the folder contains document that serves as a codebook for the analysis data files (Data Appendix.md), a document that describes the files included in the replication documentation, and explains how they can be used to replicate the study and reproduce the results (readme.md) and copy of the final report on the project (Final Paper.pdf),
- OriginalData - the folder contains the Metadata folder that provides information about the original data files (Metadata Guide.md), the original data files serve as a record of the data that started the project (weather.txt) and a modified version of the original data file in a format that can be read by the software (weather_importable.xlsx).

# How to made importable data files
In order to restore the importable file from the original file, the data from original file should be imported into the spreadsheet in such a way that the following rows constitute consecutive observations, and the columns contain separated variables and separators (alternately).

# Instructions for replicating the study
To replicate the study, run all code sections contained in the file /CommandFiles/Lab 2.ipynb. For this purpose, you must have a documentation structure (all folders) with original and imported files located in the appropriate folders. To run the script, you must have installed Jupyter Notebook (version 4.1.0) and Python (version 3.9) with the Pandas library (version 0.17.1). After the code is executed, new prcp_data.xlsx and temp_data.xlsx files will appear in the AnalysisData folder (or overwrite the existing ones).
