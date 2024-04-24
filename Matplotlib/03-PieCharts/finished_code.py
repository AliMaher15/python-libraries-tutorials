from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# how much we want to emphasize a slice
# fraction represents how much it is far, 0.1 = 10% radius
explode = [0, 0, 0, 0.1, 0] 

plt.pie(slices, labels=labels, explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})

# autopct (autopercent): shows the percentages and their format

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.savefig('plot_pie_chart.png')
plt.show()
