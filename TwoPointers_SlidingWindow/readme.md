# Two Pointers

Two pointers use **two indices/pointers** to traverse a data structure efficiently.  

### Patterns

#### a) Opposite Directions
- **Pointers:** `i` at start, `j` at end
- **Move:** i forward, j backward based on condition
- **Use Case:** sorted arrays, string comparison

**Example Problems:**
- Two Sum II – Input Array Is Sorted (LeetCode 167)
- Container With Most Water (LeetCode 11)
- Valid Palindrome (LeetCode 125)

**Visualization:**
i → 1 3 5 7 9 ← j


**Template:**
```python
i, j = 0, len(nums)-1
while i < j:
    if condition(nums[i], nums[j]):
        # do something
        i += 1
    else:
        j -= 1
```

#### b) Same Direction
- Pointers: slow and fast moving forward
- Use Case: detecting duplicates, merging, comparing elements
**Example Problems:**
- Remove Duplicates from Sorted Array (26)
- Merge Sorted Array (88)
- Linked List Middle / Cycle (Fast/Slow)

**Template**
```python
slow = 0
for fast in range(len(nums)):
    if condition(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1
```

#### b) Fast & Slow Pointers
- One pointer moves faster (2x) than the other (1x)
- Use Case: detect cycles, find middle, linked list operations
**Example Problems:**
- Linked List Cycle (141)
- Linked List Cycle II (142)
- Middle of Linked List (876)

# Sliding Window

A dynamic subarray/substring technique using two pointers (left and right) to maintain a window of interest.
- Use **two pointers** (`left` and `right`) to represent a window.
- Expand `right` to include elements.
- Shrink `left` to satisfy conditions.
- Often used to compute sums, lengths, or maximum/minimum values in a range.


## 2️⃣ Types of Sliding Window

### a) Fixed-size window
- The window size is constant: `k`.
- Move the window forward one step at a time.
- Common for sums, averages, maximums.

**Example Problems:**
- Maximum Average Subarray I (LeetCode 643)
- Sliding Window Maximum (LeetCode 239)
- Maximum Sum of Subarray of Size K

**Template:**
```python
window_sum = 0
result = float('-inf')

for i in range(len(nums)):
    window_sum += nums[i]             # include new element

    if i >= k - 1:                    # window reached size k
        result = max(result, window_sum)  # update result
        window_sum -= nums[i - k + 1]     # remove leftmost element
```

```
i = index of current element
[nums[i-k+1] ... nums[i]] = current window

```
### b) Variable-size window
- Window size can expand or shrink dynamically.
- Expand right to include elements.
- Shrink left until the condition is satisfied.
- Useful for longest/shortest subarrays, substrings with constraints.

**Example Problems:**
- Longest Substring Without Repeating Characters (LeetCode 3)
- Minimum Size Subarray Sum (LeetCode 209)
- Fruits Into Baskets (LeetCode 904)
- Longest Substring with At Most K Distinct Characters

**Template**
```python
left = 0
window = {}
result = 0

for right in range(len(s)):
    # add element to window
    window[s[right]] = window.get(s[right], 0) + 1

    # shrink window if condition is violated
    while condition_violated(window):
        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]
        left += 1

    # update result (length, sum, etc.)
    result = max(result, right - left + 1)
```
```
left →        |  window  |   ← right

```
### Tips & Tricks
- Sliding window = two pointers + condition
- Always check: do you need fixed-size or variable-size window?
- For strings: use hash map/dictionary to track counts.
- For arrays: simple sums, max, min, or prefix sums can be used.
- Remember to update the result inside the loop after adjusting the window.