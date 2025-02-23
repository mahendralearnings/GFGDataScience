

"""
psuedo code

store the temperatures into a list
initialise prefix and prefix 0=temprateur 0
caliculate cumilative sum of temperatures i'e prefix sum of temperature for the temp list

now cali temp range and total_temp for l==0 and l>o
here time is taken as indexes (start_index(l),end_index(r))
total=sum(temp)
avg=total/ len(temp ranges)

Approach: Using Prefix Sum
    -Store the hourly temperature readings in a list.
    -Precompute the prefix sum of the temperatures.
    -For any query range (e.g., 2:00 PM to 6:00 PM), use the prefix sum to calculate the sum of temperatures in constant time.
    -Return the average temperature by dividing the sum by the number of hours in the range.

"""

def prefix_sum_cal(temperatures):
     prefix_sum=[0]*len(temperatures)
     prefix_sum[0]=temperatures[0]

     for i in range(len(temperatures)):
         prefix_sum[i]=temperatures[i] + prefix_sum[i-1]
     return prefix_sum

def avg_temp(start_hour,end_hour,hours,temperatures,prefix_sum):
    start_index=hours.index(start_hour)
    end_index = hours.index(end_hour)

    if start_index ==0:
        total_temp=prefix_sum[end_index]
    else:
        total_temp=prefix_sum[end_index] -prefix_sum[start_index-1]



    num_hours=end_index-start_index+1
    avg_temp=total_temp/num_hours

    return avg_temp



# List of temperature readings from 9:00 AM to 9:00 PM (hourly data)
temperatures = [22, 24, 26, 29, 31, 33, 35, 34, 32, 30, 28, 25, 23]  # Example temperatures
# Corresponding hours (for reference, 9 AM to 9 PM)
hours = ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM",
         "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM",
         "7:00 PM", "8:00 PM", "9:00 PM"]
prefix_sum=prefix_sum_cal(temperatures)


start_hour = "2:00 PM"
end_hour = "6:00 PM"
average_temp = avg_temp(start_hour, end_hour, hours,temperatures, prefix_sum)

print(f"The average temperature between {start_hour} and {end_hour} is {average_temp:.2f}°C")





