import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load Titanic dataset: This dataset is 
titanic = sns.load_dataset("titanic")

# # Heat map of correlations
# plt.figure(figsize=(10, 6))
# correlation_matrix = titanic.corr(numeric_only=True)
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("Correlation Heatmap")
# plt.show()

# Pair Plot
sns.pairplot(titanic, vars=["age", "fare", "adult_male"], hue="survived", palette="Set2")
plt.title("Pair Plot of Age, Fare, and Survival")
plt.show()

categories = ["Region A", "Region B"]
sales = [500, 700]
random_data = np.random.randn(1000)

# Subplot Example
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Left plot: Bar Plot
axes[0].bar(categories, sales, color=['skyblue', 'salmon'])
axes[0].set_title("Sales by Region")
axes[0].set_xlabel("Region")
axes[0].set_ylabel("Sales ($)")

# Right plot: Histogram
axes[1].hist(random_data, bins=30, color='purple')
axes[1].set_title("Random Data Distribution")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

plt.tight_layout()  # Adjust layout for better spacing
plt.show()

# Using a Custom Color Palette in Seaborn
sns.set_palette("muted")
sns.barplot(x=categories, y=sales)
plt.title("Sales by Region with Custom Palette")
plt.show()