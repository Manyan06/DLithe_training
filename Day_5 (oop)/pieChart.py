import matplotlib.pyplot as plt
categories = ['Rent', 'Food', 'Transport', 'Entertainment']
expenses = [500, 300, 200, 100]
plt.figure(figsize=(6,6))
plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=90,
        colors=['skyblue','lightgreen','orange','pink'])


# Add white circle in the center to make it look like donut

centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Monthly Expenses Distribution")
plt.show()