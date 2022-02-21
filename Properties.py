import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
standard_deviation = statistics.stdev(data)

""""finding one standard deviation start and end values, second standard deviation start and end values, and third as well"""
first_std_deviation_start, first_std_deviation_end = mean - standard_deviation, mean + standard_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*standard_deviation), mean + (2*standard_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*standard_deviation), mean + (3*standard_deviation)

""""ploting the chart, lines of mean, one is standard deviation, two standard deviation, third standard deviation"""
fig = ff.create_distplot([data], ["Result"], show_hist=False)

fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x  = [first_std_deviation_start, first_std_deviation_start], y = [0,0.17], mode = "lines", name = "standard deviation 1"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0,0.17], mode = "lines", name = "standard deviation 1"))

fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0,0.17], mode = "lines", name = "standard deviation 2"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17], mode = "lines", name = "standard deviation 2"))

fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0,0.17], mode = "lines", name = "standard deviation 3"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0,0.17], mode = "lines", name = "standard deviation 3"))

fig.show()

"""printing the findings"""
list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("mean of data is{}".format(mean))
print("median of data is{}".format(median))
print("mode of data is{}".format(mode))
print("standard deviation of data is{}".format(standard_deviation))

print("{}% of data lies within one standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within second standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within third standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))