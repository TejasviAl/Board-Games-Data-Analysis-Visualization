# Board-Games-Data-Analysis-Visualization
This project performs exploratory data analysis (EDA) and visualizations on a board games dataset (games.csv) using pandas, Seaborn, and Matplotlib. The dataset includes attributes like playingtime, average_rating, minage, total_comments, and type.
________________________________________
📁 Dataset
•	Filename: games.csv
•	Sample Fields: id, name, yearpublished, playingtime, minage, average_rating, total_comments, type
________________________________________
🔍 Features
1. 📊 Data Analysis with Pandas
•	Display the first few rows and dataset info.
•	Compute:
o	Mean playingtime
o	Maximum total_comments
o	Total number of unique game IDs
•	Filter:
o	Game(s) with id == 1500
o	Games with max/min total comments
•	Group and summarize:
o	Mean minage by type
o	Frequency of each type
•	Correlation between playingtime and total_comments
•	Game(s) with:
o	Highest price
o	Lowest price
o	Price equal to a specific value (e.g., 7099)
o	Price > 40000
o	body_style == sedan and price < 7000
________________________________________
2. 📈 Data Visualization with Seaborn
✅ Univariate Plots
•	Distribution of average_rating (using distplot)
✅ Bivariate Plots
•	jointplot: Relationship between minage and average_rating
•	regplot: Regression line between playingtime and average_rating (limited to playingtime < 500)
✅ Multivariate Analysis
•	pairplot: Relationships between playingtime, minage, and average_rating
✅ Categorical vs Continuous
•	stripplot: playingtime by type (with jitter for clarity)
________________________________________
🛠 Requirements
Install required packages with:
bash

pip install pandas seaborn matplotlib

