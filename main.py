import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
conn1 = sqlite3.connect('planets.db')

# Select all (provided by framework)
pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1: Return all columns for planets with 0 moons
df_no_moons = pd.read_sql("""
    SELECT * FROM planets 
    WHERE num_of_moons = 0;
""", conn1)

# STEP 2: Name and mass of planets with exactly 7 letters in their name
df_name_seven = pd.read_sql("""
    SELECT name, mass FROM planets 
    WHERE LENGTH(name) = 7;
""", conn1)


##### Part 2: Advanced Filtering #####

# STEP 3: Name and mass where mass is less than or equal to 1.00
df_mass = pd.read_sql("""
    SELECT name, mass FROM planets 
    WHERE mass <= 1.00;
""", conn1)

# STEP 4: All columns for planets with at least one moon and mass < 1.00
df_mass_moon = pd.read_sql("""
    SELECT * FROM planets 
    WHERE num_of_moons >= 1 AND mass < 1.00;
""", conn1)

# STEP 5: Name and color where color contains the string "blue"
df_blue = pd.read_sql("""
    SELECT name, color FROM planets 
    WHERE color LIKE '%blue%';
""", conn1)


##### Part 3: Ordering and Limiting #####

# Create a connection
conn2 = sqlite3.connect('dogs.db')

# Select all (provided by framework)
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6: Hungry dogs (flag 1) sorted from youngest to oldest
df_hungry = pd.read_sql("""
    SELECT name, age, breed FROM dogs 
    WHERE hungry = 1 
    ORDER BY age ASC;
""", conn2)

# STEP 7: Hungry dogs between 2 and 7 years old, sorted alphabetically by