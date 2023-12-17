# STT890_Capstone_Siemens

1. Data Creation: <br>
   Execute the **(1) pymoo.generate.py, (2) NonDominatedSorting.py, and (3) rankgenerater.py** files sequentially.<br>
   This process will yield three CSV files: **ZDT1_10var100gen.csv, only_objectives.csv, and rank_info.csv**.<br>

2. Code: <br>
   **CODE 1: EDA and Preprocessing** <br>
   The file focuses on exploratory data analysis, utilizing ten independent variables (from x1 to x10), two objective functions (f1, f2), and rank information generated in the data creation stage. Before predicting Pareto and non-Pareto sets, this file provides insights into how to best categorize the y data. It examines three methods of dividing y data: (1) a multi-class approach with ten y classes for ranks 0-9, (2) a three-class approach dividing y into lower, middle, and high ranks ranging from 0-62, and (3) a binary class approach with two y classes for lower and high ranks within the 0-62 range.

   **CODE 2: supervised without GAP** <br>
   This file focuses on training supervised models



   **CODE 3: Merged dataset ML** <br>


3. Poster:
   Simply include the URL for a PDF document on it's own line, or wrapped in the embed tag like [embed]https://drive.google.com/file/d/1w-bqEGv3tCHkD1UgD05NH-9GY0runAwY/view?usp=drive_link[/embed] and the plugin will embed the PDF into the page using the Google Docs Viewer embed code.

The url must end with .pdf
