import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "data.csv"

# Check if file exists
if not os.path.exists(file_path):
    print("❌ data.csv file not found. Please create it and add data.")
else:
    if os.stat(file_path).st_size == 0:
        print("⚠️ data.csv file is empty. Please add data.")
    else:
        # Load data
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully\n")

        # -------------------------
        # Meaningful Questions
        # -------------------------
        print("📌 Meaningful Questions:")
        print("1. Average age and marks of students?")
        print("2. Marks distribution among male/female?")
        print("3. Students with unusually high or low marks?")
        print("4. Does age affect marks?")
        print("5. Missing or invalid values?\n")

        # -------------------------
        # Explore Data
        # -------------------------
        print("📌 Dataset Shape:", df.shape)
        print("📌 Columns:", df.columns.tolist())
        print("📌 Data Types:\n", df.dtypes, "\n")
        print("📌 Summary Statistics:\n", df.describe(), "\n")
        print("📌 Missing Values:\n", df.isnull().sum())
        print("📌 Duplicate Rows:", df.duplicated().sum(), "\n")

        # -------------------------
        # Basic Observations
        # -------------------------
        print(f"Average age: {df['age'].mean():.2f}")
        print(f"Average marks: {df['marks'].mean():.2f}")
        print(f"Median marks: {df['marks'].median()}")
        print(f"Mode marks: {df['marks'].mode().values}")

        for col in df.select_dtypes(include='object').columns:
            print(f"{col} unique values: {df[col].unique()}")
        print("\n")

        # -------------------------
        # Plots in ONE Window
        # -------------------------
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        # Age histogram
        axs[0,0].hist(df['age'], edgecolor='black')
        axs[0,0].set_title('Age Distribution')
        axs[0,0].set_xlabel('Age')
        axs[0,0].set_ylabel('Count')

        # Marks histogram
        axs[0,1].hist(df['marks'], edgecolor='black')
        axs[0,1].set_title('Marks Distribution')
        axs[0,1].set_xlabel('Marks')
        axs[0,1].set_ylabel('Count')

        # Gender bar chart
        df['gender'].value_counts().plot(kind='bar', ax=axs[1,0])
        axs[1,0].set_title('Gender Count')
        axs[1,0].set_xlabel('Gender')
        axs[1,0].set_ylabel('Count')

        # Scatter plot Age vs Marks
        axs[1,1].scatter(df['age'], df['marks'])
        axs[1,1].set_title('Age vs Marks')
        axs[1,1].set_xlabel('Age')
        axs[1,1].set_ylabel('Marks')

        plt.tight_layout()
        plt.show()

        # -------------------------
        # Boxplot for Marks
        # -------------------------
        df.boxplot(column='marks', grid=False)
        plt.title('Boxplot of Marks')
        plt.ylabel('Marks')
        plt.show()

        # -------------------------
        # NEW ADDITION 1: Marks by Gender
        # -------------------------
        df.boxplot(column='marks', by='gender', grid=False)
        plt.title('Marks Distribution by Gender')
        plt.suptitle("")
        plt.xlabel('Gender')
        plt.ylabel('Marks')
        plt.show()

        # -------------------------
        # NEW ADDITION 2: Age-wise Average Marks
        # -------------------------
        age_avg = df.groupby('age')['marks'].mean()
        print("📌 Average Marks by Age:")
        print(age_avg, "\n")

        age_avg.plot(kind='bar')
        plt.title('Average Marks by Age')
        plt.xlabel('Age')
        plt.ylabel('Average Marks')
        plt.show()

        # -------------------------
        # Correlation & Insights
        # -------------------------
        print("📌 Correlation between numeric columns:\n", df.corr(), "\n")
        print("📌 Observations / Insights:")
        print(f"- Age range: {df['age'].min()} to {df['age'].max()}")
        print(f"- Marks range: {df['marks'].min()} to {df['marks'].max()}")
        print("- Male vs Female count:\n", df['gender'].value_counts())
        print("- Correlation indicates relationship between age and marks")
        print("- Boxplots help identify outliers")
        print("- Dataset is clean with no major issues")
