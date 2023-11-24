# PCA_radiomics
The `PCA_radiomics_topfeatures.py` Python script performs Principal Component Analysis (PCA) on a dataset of radiomics features. Here are the steps it follows:

1. Import necessary libraries: The script imports necessary libraries for data manipulation, PCA, and data visualization.

2. Load the dataset: The script loads a CSV file into a pandas DataFrame. The CSV file contains radiomics data.

3. Display the dataset: The script displays the first few rows of the dataset using the `head()` function.

4. Preprocess the data: The script drops the feature names column to work with numerical data only.

5. Standardize the data: The script standardizes the numerical data using Z-score standardization. This is done to give equal importance to all features.

6. Apply PCA: The script applies PCA to the standardized data and fits the data. It reduces the dimensionality of the data to two principal components.

7. Create a DataFrame: The script creates a DataFrame with the first two principal components.

8. Plot the data: The script plots the first two principal components using a scatter plot.

9. Extract PCA loadings: The script extracts the PCA loadings for the first two principal components.

10. Create a DataFrame with PCA loadings: The script creates a DataFrame with the PCA loadings and feature names.

11. Add columns for tumor areas and scan types: The script adds columns for tumor areas and scan types to the DataFrame. This is done based on the feature names.

12. Display the PCA loadings DataFrame: The script displays the first few rows of the PCA loadings DataFrame.

13. Plot the PCA loadings: The script plots the PCA loadings in 2D, colored by tumor area and faceted by scan type.

14. Extract the loadings for PC1 and PC2: The script extracts the loadings for the first two principal components from the PCA loadings DataFrame.

15. Sort the loadings: The script sorts the loadings in descending order of their absolute values.

16. Extract the top 10 features: The script extracts the top 10 features for each component.

17. Print the results: The script prints the top 10 features for PC1 and PC2.
