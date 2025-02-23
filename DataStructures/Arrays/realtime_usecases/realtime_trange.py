""""
To answer queries like "How many people visited the site between 10:00 AM and 3:00 PM?" efficiently, we can use a similar approach to the prefix sum technique from the previous example. Here’s a step-by-step guide with a simple input and output scenario.

Step 1: Dataset
Let's assume we are tracking the number of visitors for each hour of a day.

Time	Visitors
9:00 AM	120
10:00 AM	100
11:00 AM	80
12:00 PM	95
1:00 PM	110
2:00 PM	105
3:00 PM	90
4:00 PM	85
We can store the data in a list or a dataframe. For this example, let’s create a simple dataframe.

Step 2: Calculating the Prefix Sum
The prefix sum will help us answer range queries efficiently. We can compute the cumulative sum of visitors for each hour, so that to find the number of visitors between any two hours, we simply subtract the cumulative visitors at the start time from the cumulative visitors at the end time.

Step 3: Example Query
If we want to know how many visitors visited the website between 10:00 AM and 3:00 PM, we can:

Find the cumulative visitors up to 3:00 PM.
Subtract the cumulative visitors up to 9:00 AM (just before 10:00 AM).


"""
import pandas as pd

import pandas as pd

# Step 1: Create a dataset with visitors per hour
data = {
    'time': ['9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM'],
    'visitors': [120, 100, 80, 95, 110, 105, 90, 85]
}

# Create a dataframe
visitor_data = pd.DataFrame(data)

# Step 2: Calculate the prefix sum of visitors
visitor_data['prefix_sum'] = visitor_data['visitors'].cumsum()


# Step 3: Function to get the total visitors between two times
def get_visitors_between(start_time, end_time, df):
    start_idx = df[df['time'] == start_time].index[0]
    end_idx = df[df['time'] == end_time].index[0]

    if start_idx == 0:
        return df.loc[end_idx, 'prefix_sum']
    else:
        return df.loc[end_idx, 'prefix_sum'] - df.loc[start_idx - 1, 'prefix_sum']


# Query: Visitors between 10:00 AM and 3:00 PM
start_time = '10:00 AM'
end_time = '3:00 PM'
total_visitors = get_visitors_between(start_time, end_time, visitor_data)

total_visitors

