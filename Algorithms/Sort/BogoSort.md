# Bogo Sort

## Description
Bogo Sort or Stupid Sort it's a sorting algorithm that generates a random permutation of the elements and check if it's sorted. If it's not, it generates a new random permutation and check again, until the list is sorted.

## Eficiency
Temporal complexity
- Best case scennario: 
$$O(n)$$ 
- Mean case scennario: 
$$O((n-1)n!)$$
- Worst case scennario: 
$$undefined$$

Memory complexity
$$O(1)$$

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
