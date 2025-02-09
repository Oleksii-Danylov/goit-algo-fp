'''
Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.
Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.
На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
'''
import random
import matplotlib.pyplot as plt
import numpy as np

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_rolls=100000):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        roll_sum = roll_dice()
        sums_count[roll_sum] += 1 
    probabilities = {key: value / num_rolls for key, value in sums_count.items()}
    return probabilities

def theoretical_probabilities():
    outcomes = {i: 0 for i in range(2, 13)}
    for i in range(1, 7):
        for j in range(1, 7):
            outcomes[i + j] += 1
    
    total = sum(outcomes.values())
    return {key: value / total for key, value in outcomes.items()}

def plot_probabilities(monte_carlo_probs, theoretical_probs):
    sums = list(monte_carlo_probs.keys())
    monte_carlo_values = list(monte_carlo_probs.values())
    theoretical_values = list(theoretical_probs.values())
    
    x = np.arange(len(sums))
    width = 0.35
    
    fig, ax = plt.subplots()
    ax.bar(x - width/2, monte_carlo_values, width, label='Монте-Карло')
    ax.bar(x + width/2, theoretical_values, width, label='Теоретичні')
    
    ax.set_xlabel('Сума')
    ax.set_ylabel('Ймовірність')
    ax.set_title('Порівняння ймовірностей сум')
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()
    
    plt.show()

num_rolls = 100000 
monte_carlo_probs = monte_carlo_simulation(num_rolls)
theoretical_probs = theoretical_probabilities()
plot_probabilities(monte_carlo_probs, theoretical_probs)
