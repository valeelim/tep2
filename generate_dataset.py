import random
import pickle

dataset_detail = [  # a tuple of (dataset_name, element_count, subset_count)
    ('small', 20, 20),
    ('small', 20, 30),
    ('small', 20, 40),
    ('medium', 200, 20),
    ('medium', 200, 30),
    ('medium', 200, 40),
    ('large', 2000, 20),
    ('large', 2000, 30),
    ('large', 2000, 40),
]

for (name, el_count, subset_count) in dataset_detail:
    universe = set(range(1, el_count + 1))

    subset = []
    temp_set = set()
    while temp_set != universe:
        subset = []
        temp_set = set()
        for i in range(subset_count):
            x = set([random.randint(1, el_count) for _ in range(random.randint(1, el_count))])
            subset.append(x)
            temp_set |= x
    
    costs = [random.randint(1, 1000) for _ in range(subset_count)]
    with open(f'dataset_{name}_{subset_count}.pkl', 'wb+') as f:
        pickle.dump((subset, costs), f)
