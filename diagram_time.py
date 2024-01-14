import matplotlib.pyplot as plt
import numpy as np

# Results for databases with indexes
databases_with_indexes = {
    "Database_20": {"Query_1": 0.00047059, "Query_2": 0.00042989, "Query_3": 0.00044399},
    "Database_1000": {"Query_1": 0.00045469, "Query_2": 0.00044159, "Query_3": 0.00056249},
    "Database_5000": {"Query_1": 0.00049299, "Query_2": 0.00087729, "Query_3": 0.00162099},
}

# Results for databases without indexes
databases_without_indexes = {
    "Database_20": {"Query_1": 0.00082949, "Query_2": 0.00082000, "Query_3": 0.00061200},
    "Database_1000": {"Query_1": 0.00050129, "Query_2": 0.00108710, "Query_3": 0.00061650},
    "Database_5000": {"Query_1": 0.00086779, "Query_2": 0.00095409, "Query_3": 0.0011033},
}

# Extracting data for plotting
database_names = list(databases_with_indexes.keys())
queries = list(databases_with_indexes["Database_20"].keys())
num_databases = len(database_names)

# Set up subplots for each query
fig, axs = plt.subplots(1, len(queries), figsize=(15, 5), sharey=True)

for i, query in enumerate(queries):
    with_indexes_data = [databases_with_indexes[database][query] for database in database_names]
    without_indexes_data = [databases_without_indexes[database][query] for database in database_names]

    # Plotting the data
    x = np.arange(num_databases)
    width = 0.35
    axs[i].bar(x - width/2, with_indexes_data, width, label='With Indexes')
    axs[i].bar(x + width/2, without_indexes_data, width, label='Without Indexes')

    # Adding labels, title, and legend
    axs[i].set_ylabel('Time (seconds)')
    axs[i].set_title(f'Time Comparison for {query}')
    axs[i].set_xticks(x)
    axs[i].set_xticklabels(database_names)
    axs[i].legend()

# Display the plot
plt.show()
