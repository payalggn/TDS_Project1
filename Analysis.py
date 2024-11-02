# -*- coding: utf-8 -*-
"""Untitled39.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18a7IX1grkxeImJYxRU6FkMkRxR82vcfm

Analysis of repositories and users dataset
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV files
users_df = pd.read_csv('/content/users.csv')
repos_df = pd.read_csv('/content/repositories.csv')

# Display the first few rows of each dataframe
print("Users DataFrame:")
print(users_df.head())

print("\nRepositories DataFrame:")
print(repos_df.head())

# 1. Distribution of Followers
plt.figure(figsize=(10, 6))
sns.histplot(users_df['followers'], bins=30, kde=True)
plt.title('Distribution of Followers')
plt.xlabel('Number of Followers')
plt.ylabel('Frequency')
plt.show()

# 2. Most Common Programming Languages
top_languages = repos_df['language'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_languages.index, y=top_languages.values)
plt.title('Top 10 Programming Languages')
plt.xlabel('Programming Language')
plt.ylabel('Number of Repositories')
plt.show()

import pandas as pd

# Load data
users_df = pd.read_csv('/content/users.csv')
repos_df = pd.read_csv('/content/repositories.csv')

# Define a threshold for "high follower count"
high_follower_threshold = 100  # Adjust this threshold as needed

# Filter users based on follower count
high_follower_users = users_df[users_df['followers'] >= high_follower_threshold]

# Extract usernames of high and low follower users
high_follower_logins = high_follower_users['login']

# Filter repositories based on high-follower and low-follower users
high_follower_repos = repos_df[repos_df['login'].isin(high_follower_logins)]

# Calculate proportions of repositories with documentation (wiki, license)
high_follower_wiki_proportion = high_follower_repos['has_wiki'].mean() * 100

high_follower_license_proportion = high_follower_repos['license_name'].notna().mean() * 100

# Display the results
print("Documentation Analysis Results:")
print(f"High Follower Wiki Proportion: {high_follower_wiki_proportion:.2f}%")
print(f"High Follower License Proportion: {high_follower_license_proportion:.2f}%")