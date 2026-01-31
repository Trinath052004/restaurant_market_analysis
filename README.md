# Food Delivery Data Analysis

This project contains a comprehensive analysis of food delivery data, including dataset merging, exploratory analysis, and answering various business questions based on the data.

## Project Overview

The project involves analyzing food delivery data from three different sources:
- `orders.csv`: Contains order details including order ID, user ID, restaurant ID, order date, and total amount
- `users.json`: Contains user information including user ID, name, city, and membership type
- `restaurants.sql`: Contains restaurant information including restaurant ID, name, cuisine, and rating

## Files in the Repository

- `merge_datasets.py`: Python script to merge the three datasets into a single CSV file
- `hackathon_analysis.ipynb`: Jupyter Notebook containing the complete analysis with answers to multiple choice, numerical, and fill-in-the-blank questions
- `final_food_delivery_dataset.csv`: The merged dataset resulting from `merge_datasets.py`
- `orders.csv`: Raw order data
- `users.json`: Raw user data
- `restaurants.sql`: Raw restaurant data

## Getting Started

### Prerequisites

- Python 3.x
- pandas
- json
- re (regular expressions)
- Jupyter Notebook (for viewing the analysis)

### Installation

1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install pandas
   ```

### Running the Data Merging Script

```bash
python merge_datasets.py
```

This will generate the `final_food_delivery_dataset.csv` file which contains all the merged data.

### Viewing the Analysis

Open `hackathon_analysis.ipynb` using Jupyter Notebook to view the complete analysis.

## Analysis Highlights

The analysis includes:
1. Merging three different datasets using pandas
2. Exploring the merged dataset
3. Answering 10 multiple choice questions about the data
4. Answering 6 numerical questions
5. Answering 9 fill-in-the-blank questions

## Results

Key findings from the analysis include:
- The highest revenue from Gold members comes from Chennai
- Mexican cuisine has the highest average order value
- Over 2000 distinct users have placed orders worth more than ₹1000
- Restaurants with ratings between 4.6-5.0 generate the highest revenue
- Q3 (July-September) has the highest total revenue