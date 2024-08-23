# Airbnb Analysis Project

## Table of Contents
- [Project Overview](#project-overview)
- [Skills Takeaway](#skills-takeaway)
- [Domain](#domain)
- [Problem Statement](#problem-statement)
- [Data](#data)
- [Project Approach](#project-approach)
- [Learning Outcomes](#learning-outcomes)
- [Project Evaluation Metrics](#project-evaluation-metrics)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Results](#results)
- [License](#license)
- [Contact](#contact)

## Project Overview
This project focuses on analyzing Airbnb data to gain insights into pricing variations, availability patterns, and location-based trends. The data is retrieved from MongoDB Atlas, cleaned, and visualized through interactive geospatial maps and dynamic plots using Streamlit. Additionally, a comprehensive dashboard is created using Tableau or Power BI.

## Skills Takeaway
- Python scripting
- Data Preprocessing
- Visualization
- EDA
- Streamlit
- MongoDB
- PowerBI or Tableau

## Domain
- Travel Industry
- Property Management
- Tourism

## Problem Statement
The objective is to analyze Airbnb data by:
- Establishing a MongoDB connection and retrieving the dataset.
- Cleaning and preparing the dataset for analysis.
- Developing a Streamlit web application with interactive maps.
- Conducting price analysis and visualization based on location, property type, and season.
- Analyzing availability patterns across seasons.
- Investigating location-based insights.
- Creating a comprehensive dashboard using Tableau or Power BI.

## Data
Airbnb data is imported into MongoDB Atlas, containing collections for listings, reviews, and users. The data includes various fields like listing title, description, host details, location coordinates, price, availability, amenities, and ratings.

## Project Approach
1. **MongoDB Connection and Data Retrieval**: Connect to MongoDB Atlas and retrieve the dataset.
2. **Data Cleaning and Preparation**: Handle missing values, remove duplicates, and transform data types.
3. **Geospatial Visualization**: Use Streamlit to create interactive maps showing Airbnb listings distribution.
4. **Price Analysis and Visualization**: Analyze how prices vary based on location, property type, and season.
5. **Availability Analysis by Season**: Visualize occupancy rates and demand fluctuations throughout the year.
6. **Location-Based Insights**: Investigate how prices vary across different locations using MongoDB queries.
7. **Interactive Visualizations**: Develop dynamic visualizations allowing users to explore specific regions and time periods.
8. **Dashboard Creation**: Create a comprehensive dashboard in Tableau or Power BI combining various visualizations.

## Learning Outcomes
1. **MongoDB Atlas**: Proficiency in data management with NoSQL databases.
2. **Streamlit Web Application**: Skills in web app development for interactive data exploration.
3. **Python Data Analysis**: Expertise in Python libraries like Pandas and NumPy.
4. **Geospatial Analysis**: Knowledge of geospatial data processing and visualization.
5. **Tableau or Power BI**: Skills in creating interactive dashboards.
6. **Data Cleaning and Preparation**: Handling missing values, duplicates, and data types.
7. **Data Visualization Techniques**: Creating visually appealing and informative charts, maps, and plots.
8. **Problem-Solving Skills**: Analyzing pricing dynamics and availability patterns.
9. **Data-Driven Decision Making**: Making informed choices based on data insights.
10. **Collaboration and Project Management**: Strengthening collaboration and task planning skills.

## Project Evaluation Metrics
- **Code Modularity**: Code written in functional blocks.
- **Maintainability**: The code can be maintained as the codebase grows.
- **Portability**: Code works the same in every environment.
- **GitHub Repository**: The code is maintained in a public GitHub repo with a proper README file.
- **Coding Standards**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
- **Demo Video**: Create a demo video and post it on LinkedIn.

## Project Structure
```plaintext
Airbnb_Analysis/
│
├── data/
│   └── airbnb_sample_data.json
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_and_visualizations.ipynb
│   └── 03_geospatial_analysis.ipynb
│
├── src/
│   ├── data_retrieval.py
│   ├── data_cleaning.py
│   ├── visualizations.py
│   └── app.py
│
├── dashboard/
│   └── airbnb_dashboard.pbix
│
├── README.md
└── requirements.txt
