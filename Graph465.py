import matplotlib.pyplot as plt

#statistics taken from: https://coronavirus.1point3acres.com/en
plt.style.use('ggplot')

time_stamp = ["3/19", "3/20", "3/21", "3/22", "3/23", "3/24", "3/25", "3/26","3/27", "3/28", "3/29", "3/30",
              "3/31", "4/1", "4/2", "4/3", "4/4", "4/5", "4/6", "4/7", "4/8", "4/9", "4/10", "4/11", "4/12"]
cumulative_cases = [26, 47, 56, 64, 96, 121, 146, 221, 310, 380, 414, 463,
                    553, 603, 734, 802, 945, 1059, 1163, 1235, 1345, 1440, 1506, 1558, 1624]

plt.plot(time_stamp,cumulative_cases, 'r-o', label = "Number of Cumulative Cases ")
#plt.bar(time_stamp,cumulative_cases, color='b' )
plt.xticks(time_stamp, [str(i) for i in time_stamp], rotation=60)
# fig, ax = plt.subplots()
# ax.xaxis_date()
# fig.autofmt_xdate()
plt.title('Cumulative COVID-19 Cases in Erie County PA')
plt.ylabel('Number of Cumulative Cases')
plt.legend()
plt.savefig("tim_graph.png")


