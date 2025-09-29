# Repeat Offenders

## Search

Practiced on
- 09/15/2025 20 mins
- 09/25/2025 16.5 mins
    - The while condition in iterative search should be `while l <= r` since if there's one ele, l and r will be the same and mid will be the same as l and r and we will return the correct index. `while l < r` will make us stop before we check for the target value.

## Graphs

Practiced on
- 09/15/2025 45 mins
    - Mark visited when adding to the queue. Marking at popping leads to the same node enqueued multiple times.
- 09/25/2025 40 mins
    - This needs more practice as each question is still taking time and I am forgetting stuff. I need to make sure we use consistent patterns across all questions so it's easier to remember.

## Linked List

Practiced on
- 09/15/2025 25 mins
    - use dummy node (If you’re manipulating (inserting/removing) the head, or building a new list → Use a dummy. If you’re only traversing/reading/modifying existing nodes without touching head → Don’t bother.)
        - when the head itself can change, e.g., remove nth node from end, remove duplicates, etc.
        - when inserting nodes at the head is possible (no special casing), e.g., merge two lists
        - when simplifying uniform operations, i.e., remove special casing
- 09/28/2025 20 mins

## Two Pointer

Practiced on
- 09/20/2025 75 mins
    - pay attention to the stopping conditions. try to understand sort colors even better.

## Sliding Window

Practiced on
- 09/21/2025 40 mins
    - pay attention to array indices and loop conditions. `nums[l:r]` should be used `r <= len(nums)`, not `<` size.

## Recursion

Practiced on
- 09/24/2025 35 mins
    - in binary search recursive, right would be len(arr) - 1
    - word break all needs more practice

## Backtracking

Practiced on
- 09/24/2025 55 mins
    - in combination sum, backtrack recursively on the loop index to avoid begining from start and adding duplicates
    - sudoku needs more practice

## Trees

Practiced on
- 09/24/2024 35 mins
    - distance_k needs more practice and deeper understanding
