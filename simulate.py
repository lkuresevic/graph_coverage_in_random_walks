import random
import csv
from plot import *

def simulate_heuristic(A, B, S, x_apple, y_apple, x_snake, y_snake):
    move_limit = 35*S
    num_moves = 0
    while (num_moves < move_limit) and not (x_apple == x_snake and y_apple == y_snake):
        steps = random.randint(1, 2)
        if steps == 1:
            x_snake = (x_snake + 1) % B
        else:
            y_snake = (y_snake + 1) % A
        num_moves = num_moves + 1
    return num_moves
  
def simulate_random(A, B, S, x_apple, y_apple, x_snake, y_snake):
    move_limit = 35*S
    num_moves = 0
    while (num_moves < move_limit) and not (x_apple == x_snake and y_apple == y_snake):
        steps = random.randint(1, 4)
        if steps == 1:
            x_snake = (x_snake + 1) % B
        elif steps == 2:
            x_snake = (x_snake - 1) % B
        elif steps == 3:
            y_snake = (y_snake + 1) % A
        else:
            y_snake = (y_snake - 1) % A
        num_moves = num_moves + 1
      
    return num_moves
  
def generate_board(max_height, max_width, n, heuristics_on):
    for h in range(2, max_height+1):
        for w in range(2, max_width+1):
            for i in range(1, n+1):
                s = h*w
            
                x_apple = random.randrange(0, w)
                y_apple = random.randrange(0, h)
                x_snake = random.randrange(0, w)
                y_snake = random.randrange(0, h)
                while(x_snake == x_apple):
                    x_snake = random.randrange(0, w)
                while(y_snake == y_apple):
                    y_snake = random.randrange(0, h)
                
                if(heuristics_on):
                    result_list.append([simulate_heuristic(h, w, s, x_apple, y_apple, x_snake, y_snake), 35*s])
                else:
                    result_list.append([simulate_random(h, w, s, x_apple, y_apple, x_snake, y_snake), 35*s])
                print(str(w) + ", " + str(h) + ": " + str(i))

def generate_max_board(n, heuristics_on):
    for i in range(1, n+1):
        h = random.randint(2, 1000)
        w = 1000000//h
        s = h*w
        
        x_apple = random.randrange(0, w)
        y_apple = random.randrange(0, h)
        x_snake = random.randrange(0, w)
        y_snake = random.randrange(0, h)
        while(x_snake == x_apple):
            x_snake = random.randrange(0, w)
        while(y_snake == y_apple):
            y_snake = random.randrange(0, h)
        
        if(heuristics_on):
            result_list.append([simulate_heuristic(h, w, s, x_apple, y_apple, x_snake, y_snake), 35*s])
        else:
            result_list.append([simulate_random(h, w, s, x_apple, y_apple, x_snake, y_snake), 35*s])
        print(str(i) + ": " + str(w) + ", " + str(h))
            
def save_csv(filename):
    with open('Results/' + filename, mode = 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["moves_used", "move_limit"])
        writer.writerows(result_list)
    
if __name__ == "__main__":
    random.seed(42)
    
    print(stats("heuristic_strategy_experiment.csv"))
    
    print(stats("stats_heuristic.csv"))
    
    print(stats("stats_random.csv"))