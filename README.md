# STT890_Capstone_Siemens

1. Data Creation: <br>
   Execute the **(1) pymoo.generate.py, (2) NonDominatedSorting.py, and (3) rankgenerater.py** files sequentially.<br>
   This process will yield three CSV files: **ZDT1_10var100gen.csv, only_objectives.csv, and rank_info.csv**.<br>

2. Code: <br>
   **CODE 1: EDA and Preprocessing** <br>
   The file focuses on exploratory data analysis, utilizing ten independent variables (from x1 to x10), two objective functions (f1, f2), and rank information generated in the data creation stage. Before predicting Pareto and non-Pareto sets, this file provides insights into how to best categorize the y data. It examines three methods of dividing y data: (1) a multi-class approach with ten y classes for ranks 0-9, (2) a three-class approach dividing y into lower, middle, and high ranks ranging from 0-62, and (3) a binary class approach with two y classes for lower and high ranks within the 0-62 range.

   **CODE 2: supervised without GAP** <br>
   This file used PCA on three datasets, trained models using datasets with and without PCA, and compared the models' performances. F1 score was chosen to evaluate the models. Because, the datasets were imbalanced, and predicting efficiency in low rank was more meaningful in this problem. (1) According to the principle compoenent analysis, the first two principle components in all three datasets can explain most of the vairiance, therefore, reducing data's dimension to **2** for this kind problem is reasonable. (2) To define the low rank population, the loop worked as model selection to find the best boudary separating the near-pareot set from far-pareto set. 
   (Note, detailed explanation is written in our final report powerpoint.)


   **CODE 3: Merged dataset ML** <br>
   The idea of this file is enlightened by CODE2 file. The reliability of PCA in these kind of data is supported by CODE2 file. PCA can reduce the dimensions of all dataset to two, no matter the original variables number is. Therefore, **training a generalized model is reasonable which can fit in all datasets after reducing dimension**. (1) The result shows that all four models have ideal performance when we set boundary equal to 4. (2) This file also can contribute to the following capstone project in the next semester. The inverse of generalized model can be used to predicted the principle components. And the predicted principle components can be expanded to datasets with different attributes' number.

3. Poster: <br>
   [Click Here](https://github.com/yenything/STT890_Capstone_Siemens/blob/main/Poster.pdf)

4. Slide: <br>
   pending....