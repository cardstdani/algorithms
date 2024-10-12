# Bogo Sort

## Description
Bogo Sort or Stupid Sort it's a sorting algorithm that generates a random permutation of the elements and check if it's sorted. If it's not, it generates a new random permutation and checks again, until the list is sorted.

## Efficiency
Temporal complexity
- Best case scenario: 
$$O(n)$$

    To build a randomly shuffled list from the original one the algorithm needs a time proportional to the list's length, which in this case is denoted as n. Therefore, in the best case, the first iteration finds the sorted list, needing only $$O(n)$$ elementary operations for generating the shuffled list.
- Average case: 
$$O(n\cdot n!)$$

    In the average case, the algorithm traverses all the state space of the input list, which has a $$n!$$ cardinal, and then reaches the sorted list. For each generated list, it performs a work proportional to n, so the ultimate complexity bound is $$O(n\cdot n!)$$, which has a constant multiplying it stemming from the probability of the random generator reaching the sorted sequence in a reduced, or augmented quantity of iterations.
- Worst case scenario: 
$$undefined$$

    It could take an infinite amount of time to achieve a sorted list if the random generator used to build the intermediate lists does not reach the specific sorted state, that is, it depends on the probability of the randomly generated sequence reaching such state, which in the worst case might approach infinity.

Memory complexity:
$$O(1)$$ (no extra space is required)

## Pseudocode
```
WHILE LIST NOT SORTED
    SHUFFLE LIST
END
```

## C++ implementation
```c++
bool isSorted(std::vector<type> list)
{
   for (size_t i = 1; i < list.size(); i++)
        if (list[i] < list[i - 1]) return false;
    return true;
}

int main()
{
    std::vector<type> list = {0, 2, 1};
    while (!isSorted(list)) std::random_shuffle(list.begin(), list.end());
    return 0;
}
```

## Comon usage

Just please don't use it, this is intended to be a joke. Not any real usages...

## Extras
