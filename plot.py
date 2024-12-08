import matplotlib.pyplot as plt
import csv

def plot_results(csv_file):
    percentage_of_moves_used_random, board_size_random = [], []
    percentage_of_moves_used_heuristic, board_size_heuristic = [], []
    
    with open("Results/" + csv_file + "_random.csv", 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            try:
                percentage_of_moves_used_random.append(float(row[0]) / float(row[1]) * 100)
                board_size_random.append(int(row[1]) / 35)
            except ValueError:
                continue

    with open("Results/" + csv_file + "_heuristic.csv", 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            try:
                percentage_of_moves_used_heuristic.append(float(row[0]) / float(row[1]) * 100)
                board_size_heuristic.append(int(row[1]) / 35)
            except ValueError:
                continue

    plt.scatter(board_size_random, percentage_of_moves_used_random, color='blue', label='Random Strategy')
    plt.scatter(board_size_heuristic, percentage_of_moves_used_heuristic, color='red', label='Heuristic Strategy')
    
    plt.ylim(0, 100)
    plt.title('Percentage of Moves Used over Board Size')
    plt.xlabel('Board Size')
    plt.ylabel('Percentage of Moves Used')

    plt.legend(loc='best', fontsize=10, frameon=True, shadow=True, title="Legend")
    plt.grid(True)
    plt.show()