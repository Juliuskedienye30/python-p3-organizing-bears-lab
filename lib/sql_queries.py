# 1. All female bears: name + age
select_all_female_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE sex = 'F';
"""

# 2. All bears: names in alphabetical order
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name
    FROM bears
    ORDER BY name ASC;
"""

# 3. All alive bears: name + age, youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT name, age
    FROM bears
    WHERE alive = 1
    ORDER BY age ASC;
"""

# 4. Oldest bear: name + age
select_oldest_bear_and_returns_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

# 5. Youngest bear: name + age
select_youngest_bear_and_returns_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age ASC
    LIMIT 1;
"""
