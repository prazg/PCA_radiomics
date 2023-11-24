from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Loading the provided CSV file
file_path = r"Path.csv"
radiomics_data = pd.read_csv(file_path)

# Displaying the first few rows of the dataset
radiomics_data.head()

# Dropping the feature names column to work with numerical data
numerical_data = radiomics_data.drop(columns=['Unnamed: 0'])

# Standardizing (scaling) the data using Z-score
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numerical_data.transpose())

# Applying PCA and fitting the numerical data
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)

# Creating a DataFrame with the first two principal components
pca_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Component 2'])

# Plotting the first two principal components
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Principal Component 1', y='Principal Component 2', data=pca_df)
plt.title('Visualization of the First Two Principal Components')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

# Extracting the PCA loadings for the first two principal components
pca_loadings = pca.components_.T

# Creating a DataFrame with the PCA loadings and feature names
pca_loadings_df = pd.DataFrame(pca_loadings, columns=['PC1', 'PC2'], index=radiomics_data['Unnamed: 0'])

# Adding columns for tumor areas and scan types (if radiomics features are from FLAIR, T1, T2, or T1C scans)
pca_loadings_df['Tumor_Area'] = ['Necrotic Core' if '_1' in feature else 'Enhancing Tumor' if '_2' in feature else 'Edema' for feature in pca_loadings_df.index]
pca_loadings_df['Scan_Type'] = ['FLAIR' if 'flair' in feature else 'T1' if '_t1_' in feature else 'T2' if '_t2_' in feature else 'T1C' if '_t1c_' in feature else 'Other' for feature in pca_loadings_df.index]

# Displaying the first few rows of the PCA loadings DataFrame
pca_loadings_df.head()

# Plotting the PCA loadings in 2D, colored by tumor area and faceted by scan type
g = sns.FacetGrid(pca_loadings_df, col="Scan_Type", col_wrap=2, height=5, aspect=1.2, hue="Tumor_Area", palette="tab10")
g.map(sns.scatterplot, "PC1", "PC2", alpha=0.7, edgecolor=None)
g.add_legend(title="Tumor Area")
g.set_axis_labels("Principal Component 1", "Principal Component 2")
g.set_titles("Scan Type: {col_name}")
plt.suptitle("2D Plot of PCA Loadings by Tumor Area and Scan Type", y=1.02, fontsize=16)
plt.show()

# 1. Extract the loadings for PC1 and PC2 from the pca_loadings_df DataFrame
loadings_pc1 = pca_loadings_df['PC1']
loadings_pc2 = pca_loadings_df['PC2']

# 2. Sort the loadings in descending order of their absolute values
sorted_pc1 = loadings_pc1.abs().sort_values(ascending=False)
sorted_pc2 = loadings_pc2.abs().sort_values(ascending=False)

# 3. Extract the top 10 features for each component
top_10_pc1 = sorted_pc1.head(10)
top_10_pc2 = sorted_pc2.head(10)

# 4. Print or display the results
print("Top 10 features for PC1:")
print(top_10_pc1)

print("\nTop 10 features for PC2:")
print(top_10_pc2)


