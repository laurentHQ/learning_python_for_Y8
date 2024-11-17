# Data Analysis and Visualization with Python
## Year 11 Advanced Programming

### 📚 Overview
In this notebook, you'll learn how to analyze and visualize real-world data using Python. We'll work with a dataset about global temperature changes and create meaningful insights through data analysis.

### 🎯 Learning Objectives
- Work with Pandas DataFrames
- Clean and process data
- Perform statistical analysis
- Create professional visualizations
- Build interactive dashboard elements

### 📋 Prerequisites
First, let's install and import required libraries:

```python
# Install required libraries
!pip install pandas numpy matplotlib seaborn plotly

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
```

### 🌡️ Step 1: Data Loading and Initial Exploration
#### Concepts Covered:
- Reading CSV files with Pandas
- Basic DataFrame operations
- Data inspection methods
- Understanding data structure

```python
# Download sample temperature dataset
!wget https://raw.githubusercontent.com/datasets/global-temp/master/data/annual.csv -O temperature.csv

# Task 1.1: Load the dataset
def load_and_examine_data(filename):
    """
    Load the CSV file and perform initial examination
    Return the DataFrame and basic information
    """
    # Your code here
    # 1. Read the CSV file
    # 2. Display first few rows
    # 3. Get basic information about the dataset
    # 4. Check for missing values
    pass

# Example usage:
df = load_and_examine_data('temperature.csv')
```

#### 💡 Challenge 1:
Create a function that provides a comprehensive summary of the dataset including:
- Number of rows and columns
- Data types of each column
- Basic statistical measures
- Missing value counts

```python
# Your challenge code here
def create_data_summary(df):
    """
    Create a comprehensive data summary
    """
    pass
```

### 📊 Step 2: Data Cleaning and Preprocessing
#### Concepts Covered:
- Handling missing values
- Data type conversion
- Creating new features
- Data filtering

```python
# Task 2.1: Clean and preprocess the data
def clean_temperature_data(df):
    """
    Clean the temperature dataset and prepare it for analysis
    """
    # Your code here
    # 1. Handle any missing values
    # 2. Convert date column to datetime
    # 3. Create decade column
    # 4. Filter out any invalid temperatures
    pass

# Example usage:
clean_df = clean_temperature_data(df)
```

#### 💡 Challenge 2:
Add more sophisticated preprocessing:
- Create seasonal averages
- Handle outliers using IQR method
- Add temperature change from previous year
- Create temperature categories (Cold, Moderate, Hot)

```python
# Your challenge code here
def advanced_preprocessing(df):
    """
    Perform advanced data preprocessing
    """
    pass
```

### 📈 Step 3: Basic Statistical Analysis
#### Concepts Covered:
- Descriptive statistics
- Groupby operations
- Rolling averages
- Correlation analysis

```python
# Task 3.1: Perform statistical analysis
def analyze_temperature_trends(df):
    """
    Analyze temperature trends over time
    """
    # Your code here
    # 1. Calculate yearly averages
    # 2. Compute rolling averages
    # 3. Find temperature extremes by decade
    # 4. Calculate rate of temperature change
    pass

# Example usage:
analysis_results = analyze_temperature_trends(clean_df)
```

#### 💡 Challenge 3:
Extend the analysis with:
- Variance analysis by decade
- Trend detection using linear regression
- Seasonal decomposition
- Statistical hypothesis testing

```python
# Your challenge code here
def advanced_statistical_analysis(df):
    """
    Perform advanced statistical analysis
    """
    pass
```

### 🎨 Step 4: Data Visualization
#### Concepts Covered:
- Different plot types
- Customizing visualizations
- Multiple subplots
- Interactive plotting

```python
# Task 4.1: Create visualization suite
def create_temperature_visualizations(df):
    """
    Create a suite of visualizations for temperature data
    """
    # Your code here
    # 1. Line plot of temperature over time
    # 2. Box plot by decade
    # 3. Heatmap of monthly temperatures
    # 4. Distribution plot of temperatures
    pass

# Example usage:
create_temperature_visualizations(clean_df)
```

#### 💡 Challenge 4:
Create advanced visualizations:
- Animated temperature changes
- Interactive plotly dashboard
- Custom visualization themes
- Multi-variable analysis plots

```python
# Your challenge code here
def create_advanced_visualizations(df):
    """
    Create advanced interactive visualizations
    """
    pass
```

### 📱 Step 5: Building an Interactive Dashboard
#### Concepts Covered:
- Creating interactive elements
- Combining multiple visualizations
- User input handling
- Dynamic updates

```python
# Task 5.1: Create interactive dashboard
def create_temperature_dashboard(df):
    """
    Create an interactive dashboard for temperature analysis
    """
    # Your code here
    # 1. Create year range selector
    # 2. Add temperature trend plot
    # 3. Include statistical summary
    # 4. Add interactive features
    pass

# Example usage:
dashboard = create_temperature_dashboard(clean_df)
```

#### 💡 Challenge 5:
Enhance the dashboard with:
- Multiple view options
- Custom filtering capabilities
- Export functionality
- Predictive features

```python
# Your challenge code here
def create_advanced_dashboard(df):
    """
    Create an advanced interactive dashboard
    """
    pass
```

### 🎓 Final Project
Combine all steps to create a comprehensive climate analysis tool:
1. Load and clean temperature data
2. Perform statistical analysis
3. Create visualizations
4. Build interactive dashboard
5. Generate automated reports

```python
# Main execution
def main():
    # Load data
    df = load_and_examine_data('temperature.csv')
    
    # Clean data
    clean_df = clean_temperature_data(df)
    
    # Analyze trends
    analysis = analyze_temperature_trends(clean_df)
    
    # Create visualizations
    visualizations = create_temperature_visualizations(clean_df)
    
    # Build dashboard
    dashboard = create_temperature_dashboard(clean_df)
    
    return dashboard

# Run the analysis
if __name__ == "__main__":
    main()
```

### 📚 Additional Resources
- Pandas Documentation: https://pandas.pydata.org/docs/
- Plotly Documentation: https://plotly.com/python/
- Seaborn Tutorial: https://seaborn.pydata.org/tutorial.html
- Data Science Concepts: https://www.kaggle.com/learn/data-science

### ✅ Assessment Criteria
Your solution will be evaluated based on:
1. Code Quality
   - [ ] Clear and consistent style
   - [ ] Proper documentation
   - [ ] Efficient implementation
   
2. Analysis Quality
   - [ ] Depth of insights
   - [ ] Statistical rigor
   - [ ] Proper handling of edge cases
   
3. Visualization Quality
   - [ ] Clear and informative plots
   - [ ] Professional appearance
   - [ ] Interactive features
   
4. Documentation
   - [ ] Clear explanations
   - [ ] Usage instructions
   - [ ] Result interpretation