#
#! 85. Introduction to Matplotlib

# * Data visualization to gain data-driven decisions

# * we use it as data engineers during wrangling to visualize set of dataframes and set of tables

# * there are two tools for data visualization: matplotlib - c born

# * Matplotlib is not the essential tool to build dashboard for business and management

# * We use for business: Tableau - Power BI

# *==============================================================

#! 86. Plot a Single graph in Matplotlib

# ^ import:
# Import
from matplotlib import pyplot as plt

# ^ import numpy
import numpy as np

plt.plot(x, y)

# ^ add title:
plt.title("single graph")

# ^ add label
plt.xlabel("size m2")
plt.ylabel("price $")
# ^ show the graph
plt.show()

# *==============================================================
#! 87. Plot 2 graphs on the same Chart

# ^ create two plots

# ^ add title
# ^ add labels
# ^ add legend (explicit legend)

# *==============================================================
#! 88. Chart Styling in Matplotlib

# * restart button in file.ipynb restarts the kernel


# * as data engineers we visualize the plot that make you understand the data


# * marker is the data point (x,y), the point on the x-axis list and its corresponding on y-axis


# ^ create plot with color, line style, marker and legend


# ^ show available plotting theme styles

# ^ use one of them

# *==============================================================
#! 89. Real-world Data Visualisation Problem with Matplotlib

# * load the cleaned csv data
# * inspect the data
# * we need to convert string dates into dates data type

# *==============================================================

#! 90. Visualise Top Countries by Shipping Cost

# ^ explore histogram , study more about histogram

# *==============================================================
