`Heaps` are concrete data structures --> They define an implementation
`Priority Queues` -> Abstract Data Structures that determine interface

`Heaps` -> Ensures performance guarantee (relationship between the size of the structure and the time operations take)

## Must know heap functions:

`is_empty` -> Checks if heap is empty
`add_element` adds an element to the queue. `O(log(N))` 
`pop_element` pops the element with the highest priority. `O(log(N))` 


The `heap` implementation of the priority queue guarantees that both pushing (`adding`) and popping (`removing`) elements are `logarithmic` `O(log(N))` time operations. 

In a heap tree, the value in a node is always `smaller` than both of its children


## Heaps as a list
Its `first` child is at `2*k + 1`.
Its `second` child is at `2*k + 2`.
Its `parent` is at `(k - 1) // 2`.

THe following condition is always True in a Heap:

```py
h[k] <= h[2*k + 1] and h[k] <= h[2*k + 2]
```