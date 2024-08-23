import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap
from wordcloud import WordCloud

# Load your cleaned DataFrame
df = pd.read_csv('cleaned_data.csv')

st.title('Airbnb Data Analysis')
st.sidebar.header('Filter Options')



# Filter by price range
price_range = st.slider('Select price range for map:', int(df['price'].min()), int(df['price'].max()), (50, 500))

filtered_data = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]

st.write(f"Showing map for price range: {price_range[0]} - {price_range[1]}")

# Create a map centered around the average latitude and longitude
map_center = [filtered_data['Latitude'].mean(), filtered_data['Longitude'].mean()]
price_map = folium.Map(location=map_center, zoom_start=12)

for index, row in filtered_data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color='blue',
        fill=True,
        fill_color='blue',
        popup=f"Price: {row['price']}"
    ).add_to(price_map)

# Display the map
folium_static(price_map)

st.header('Price Distribution')

# Filter by price range
price_range = st.slider('Select price range:', int(df['price'].min()), int(df['price'].max()), (50, 500))

filtered_data = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]

st.write(f"Showing results for price range: {price_range[0]} - {price_range[1]}")

# Plot the distribution
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['price'], kde=True, bins=30)
plt.title('Price Distribution of Airbnb Listings')
plt.xlabel('Price')
plt.ylabel('Frequency')
st.pyplot(plt)


# Room type filter
room_type = st.multiselect('Select room type(s):', df['room_type'].unique(), default=df['room_type'].unique())

filtered_data = df[df['room_type'].isin(room_type)]

st.write("Showing average price for selected room types.")

# Plot the average price by room type
plt.figure(figsize=(10, 6))
sns.barplot(x='room_type', y='price', data=filtered_data, estimator=np.mean)
plt.title('Average Price by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Average Price')
st.pyplot(plt)



# 1. Interactive Price Distribution by Room Type
st.header('Price Distribution by Room Type')
price_limit = st.slider('Select maximum price:', 100, 1000, 500)
filtered_df = df[df['price'] < price_limit]

plt.figure(figsize=(10, 6))
sns.boxplot(x='room_type', y='price', data=filtered_df)
plt.title('Price Distribution by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Price ($)')
st.pyplot(plt)

# 2. Interactive Number of Reviews vs. Price
st.header('Number of Reviews vs. Price')
review_limit = st.slider('Select maximum number of reviews:', 10, 500, 100)
price_limit = st.slider('Select maximum price:', 100, 10000, 5000)
filtered_df = df[(df['price'] < price_limit) & (df['number_of_reviews'] < review_limit)]

plt.figure(figsize=(10, 6))
sns.scatterplot(x='number_of_reviews', y='price', data=filtered_df)
plt.title('Number of Reviews vs. Price')
plt.xlabel('Number of Reviews')
plt.ylabel('Price ($)')
st.pyplot(plt)

# Filter by number of accommodates
accommodates = st.slider('Select number of accommodates:', int(df['accommodates'].min()), int(df['accommodates'].max()), (1, 4))

filtered_data = df[(df['accommodates'] >= accommodates[0]) & (df['accommodates'] <= accommodates[1])]

st.write(f"Showing results for accommodates range: {accommodates[0]} - {accommodates[1]}")

# Plot Price vs. Accommodates
plt.figure(figsize=(10, 6))
sns.scatterplot(x='accommodates', y='price', data=filtered_data)
plt.title('Price vs. Number of Accommodates')
plt.xlabel('Number of Accommodates')
plt.ylabel('Price')
st.pyplot(plt)


# 3. Interactive Word Cloud of Amenities
st.header('Common Amenities Word Cloud')
st.write('The word cloud below shows the most common amenities in the listings.')

all_amenities = ' '.join(df['amenities'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_amenities)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Common Amenities Word Cloud')
st.pyplot(plt)


# 4. Interactive Top Hosts by Number of Listings
st.header('Top 10 Hosts by Number of Listings')
top_n = st.slider('Select number of top hosts:', 5, 20, 10)
top_hosts = df.groupby('host_name')['host_listings_count'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_hosts.values, y=top_hosts.index)
plt.title('Top Hosts by Number of Listings')
plt.xlabel('Number of Listings')
plt.ylabel('Host Name')
st.pyplot(plt)


# 5. Interactive Superhosts vs. Non-Superhosts
st.header('Superhosts vs. Non-Superhosts')
superhost_counts = df['host_is_superhost'].value_counts()

plt.figure(figsize=(6, 4))
sns.barplot(x=superhost_counts.index, y=superhost_counts.values)
plt.title('Superhosts vs. Non-Superhosts')
plt.xlabel('Is Superhost')
plt.ylabel('Count')
st.pyplot(plt)


# 6. Interactive Distribution of Host Response Rates
st.header('Distribution of Host Response Rates')
response_rate_limit = st.slider('Select maximum response rate:', 50, 100, 100)
filtered_df = df[df['host_response_rate'].dropna() <= response_rate_limit]

plt.figure(figsize=(10, 6))
sns.histplot(filtered_df['host_response_rate'], bins=20, kde=True)
plt.title('Distribution of Host Response Rates')
plt.xlabel('Response Rate (%)')
plt.ylabel('Frequency')
st.pyplot(plt)


# 7. Interactive Distribution of Host Response Time
st.header('Distribution of Host Response Time')
response_time_options = st.multiselect('Select response times to display:', df['host_response_time'].unique(), df['host_response_time'].unique())

filtered_df = df[df['host_response_time'].isin(response_time_options)]

plt.figure(figsize=(10, 6))
sns.histplot(filtered_df['host_response_time'].dropna())
plt.title('Distribution of Host Response Time')
plt.xlabel('Response Time')
plt.ylabel('Frequency')
st.pyplot(plt)