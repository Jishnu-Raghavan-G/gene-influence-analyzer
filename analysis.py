import pandas as pd

# Load data
df = pd.read_csv("sample_data.csv")

# Separate healthy and disease
healthy = df[df["condition"] == "healthy"]
disease = df[df["condition"] == "disease"]

# Calculate mean expression per gene
healthy_mean = healthy.groupby("gene")["expression"].mean()
disease_mean = disease.groupby("gene")["expression"].mean()

# Combine into one table
comparison = pd.DataFrame({
    "Healthy": healthy_mean,
    "Disease": disease_mean
}).fillna(0)

# Calculate difference
comparison["Difference"] = comparison["Disease"] - comparison["Healthy"]

# Classify influence
def classify(diff):
    if diff > 1:
        return "Strong Disease Association"
    elif diff > 0:
        return "Moderate Disease Association"
    elif diff < -1:
        return "Strong Healthy Association"
    else:
        return "Neutral"

comparison["Interpretation"] = comparison["Difference"].apply(classify)

# Print results
print("\nGene Influence Analysis:\n")
print(comparison)

# Explain results
print("\nDetailed Explanation:\n")
for gene, row in comparison.iterrows():
    print(f"{gene}: {row['Interpretation']} (Difference = {row['Difference']:.2f})")
