import pickle
import time

from generate_dataset import dataset_detail
from util import log_exec_time
from util import profile_memory
from greedy import set_cover
from branch_and_bound import BB


@log_exec_time
def test_greedy(universe, subset, costs):
    cover = set_cover(universe, subset, costs)
    print(f'cost: ${cover[1]}')

@log_exec_time
def test_bb(universe, subset, costs):
    cover = BB(universe, subset, costs)
    print(f'cost: ${cover[0]}')

# separate memory and time benchmark
@profile_memory
def mem_test_greedy(universe, subset, costs):
    set_cover(universe, subset, costs)

@profile_memory
def mem_test_bb(universe, subset, costs):
    BB(universe, subset, costs)
        
if __name__ == '__main__':
    for name, el_count, subset_count in dataset_detail:
        with open(f'dataset_{name}_{subset_count}.pkl', 'rb') as f:
            subset, costs = pickle.load(f)
        
        universe = set(range(1, el_count + 1))

        print(f'Running dataset {name} with {subset_count} subsets...')
        print('Time comparison:')
        test_greedy(universe, subset, costs)
        test_bb(universe, subset, costs)

        print('\nMemory comparison:')
        mem_test_greedy(universe, subset, costs)
        mem_test_bb(universe, subset, costs)
        print('=' * 50)
        print()
