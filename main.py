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

# STEP 7: Hungry dogs between 2 and 7 years old, sorted alphabetically by name
df_hungry_ages = pd.read_sql("""
    SELECT name, age, hungry FROM dogs 
    WHERE hungry = 1 AND age BETWEEN 2 AND 7 
    ORDER BY name ASC;
""", conn2)

# STEP 8: Name, age, and breed for the 4 oldest dogs, sorted alphabetically by breed.
# Tied breeds are sorted by name descending to position Snowy before Lassie.
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed FROM (
        SELECT name, age, breed FROM dogs 
        ORDER BY age DESC 
        LIMIT 4
    ) 
    ORDER BY breed ASC, name DESC;
""", conn2)


##### Part 4: Aggregation #####

# Create a connection
conn3 = sqlite3.connect('babe_ruth.db')

# Select all (provided by framework)
pd.read_sql("""SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9: Total number of years Babe Ruth played professional baseball
df_ruth_years = pd.read_sql("""
    SELECT COUNT(year) FROM babe_ruth_stats;
""", conn3)

# STEP 10: Total number of home runs hit during his career
df_hr_total = pd.read_sql("""
    SELECT SUM(HR) FROM babe_ruth_stats;
""", conn3)


##### Part 5: Grouping and Aggregation #####

# STEP 11: Team name and the number of years played, aliased as number_years
df_teams_years = pd.read_sql("""
    SELECT team, COUNT(year) AS number_years 
    FROM babe_ruth_stats 
    GROUP BY team;
""", conn3)

# STEP 12: Team name and average number of at-bats, aliased as average_at_bats (> 200)
df_at_bats = pd.read_sql("""
    SELECT team, AVG(at_bats) AS average_at_bats 
    FROM babe_ruth_stats 
    GROUP BY team 
    HAVING AVG(at_bats) > 200;
""", conn3)


# Safely close connections
conn1.close()
conn2.close()
conn3.close()