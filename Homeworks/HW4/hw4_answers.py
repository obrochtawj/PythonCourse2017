#Homework 4
#William O'Brochta
import random
import timeit
#These three imports might be redundant, but I couldn't get it to work otherwise.
import plotly.graph_objs as go
import plotly.plotly
from plotly.graph_objs import Scatter, Layout

#Bubble Sort (because it has the coolest name)
def Bubble_Sort(sort_list):
    #Implement the sort to keep the last elements that have
    #already been sorted.
    for item in range(len(sort_list)-1,0,-1):
        for entry in range(0,item):
            #Comparing if the entry is bigger than the adjacent entry.
            if sort_list[entry+1] < sort_list[entry]:
                #Shuffle the entries
                a_number = sort_list[entry]
                sort_list[entry] = sort_list[entry+1]
                sort_list[entry+1] = a_number
    return sort_list

def Merge_Sort(sort_list):
    sorted_list = []
    #Tells the recursive function when to stop.
    if len(sort_list) < 2:
        return sort_list
    #Find the middle and split the list in half.
    middle = int(len(sort_list)/2)
    left_half = sort_list[0:middle]
    right_half = sort_list[middle:]
    #Recursively sort the left and right halves of the list
    #until there are fewer than 2 elements in each list.
    left_sorted = Merge_Sort(left_half)
    right_sorted = Merge_Sort(right_half)
    index1=index2=0
    #Compare the elements in the left and right list.
    #Append the smaller one.
    while index1 < len(left_sorted) and index2 < len(right_sorted):
        if left_sorted[index1] < right_sorted[index2]:
            sorted_list.append(left_sorted[index1])
            index1+=1
        else:
            sorted_list.append(right_sorted[index2])
            index2+=1
    #Remove elements already sorted from the left and right lists.
    sorted_list +=left_sorted[index1:]
    sorted_list +=right_sorted[index2:]
    return sorted_list

def time_trials(n,iterations):
    Bubble_Sort_Time = []
    Merge_Sort_Time = []
    #Repeat for a certain number of iterations.
    for each_iteration in range(0,iterations):
        #Pick a random combination of n elements to sort.
        sort_sample = random.sample(range(n),n)
        #Start a timer.
        time_start = timeit.default_timer()
        Bubble_Sort(sort_sample)
        time_middle = timeit.default_timer()
        Merge_Sort(sort_sample)
        time_end = timeit.default_timer()
        #Get elapsed time for sorts.
        Bubble_Sort_Time.append(time_middle-time_start)
        Merge_Sort_Time.append(time_end-time_middle)
    #Return the mean. I tried max too, but it gives some weird results if
    #a sort randomly takes a long time.
    return sum(Bubble_Sort_Time)/len(Bubble_Sort_Time), sum(Merge_Sort_Time)/len(Merge_Sort_Time)

#Do not run since this takes a very long time (~10-20 minutes)
Bubble_Sort_Time = []
Merge_Sort_Time = []
#Have lists from 2 to 500 elements long.
n = 500
#For each list length repeat the sort 50 times and get the mean sort time.
for index in range(2,n):
    sorting_times = time_trials(index,50)
    Bubble_Sort_Time.append(sorting_times[0])
    Merge_Sort_Time.append(sorting_times[1])

#This is how to plot in plotly. Define both datasets.
trace = go.Scatter(x=range(2,500), y=Bubble_Sort_Time, 
        mode='Bubble Sort', name = 'Bubble Sort')
trace2 = go.Scatter(x=range(2,500), y=Merge_Sort_Time,
        mode='Merge Sort', name='Merge Sort')
data = [trace, trace2]


#Create a plot (that opens in a brower for whatever reason)
#I've included a png of the plot.
plotly.offline.plot({
    "data": data,
    "layout": Layout(title="Bubble and Merge Sort Comparison", xaxis=dict(title='Number of Items'), yaxis=dict(title='Time in Seconds'))
})

