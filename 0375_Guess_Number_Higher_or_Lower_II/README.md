Question: https://leetcode.com/problems/guess-number-higher-or-lower-ii/

---

try_1.py:
* Runtime: 688 ms, faster than 59.72% of Python3 online submissions for Guess Number Higher or Lower II.
* Memory Usage: 32.5 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.

> dp + recursive

---

try_2.py:
* Runtime: 296 ms, faster than 90.00% of Python3 online submissions for Guess Number Higher or Lower II.
* Memory Usage: 32.4 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.

> optimize try_1.py
> 	* if find out left_max > right_max, then break the loop
> 	* because loop �q�����k��A�����䪺�ȷ|�������j��k��A�]���A���᪺loop�]�|�@������j��k��A���N�S���Aloop�����n�F�A�]���i�Hbreak

---

try_3.py:
* Runtime: 96 ms, faster than 96.20% of Python3 online submissions for Guess Number Higher or Lower II.
* Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.

> optimize try_2.py
> 	* using dictionary instead of array

---

try_4.py: O(n) O(n)

* Runtime: 1176 ms, faster than 87.19% of Python3 online submissions for Guess Number Higher or Lower II.
* Memory Usage: 19.9 MB, less than 42.79% of Python3 online submissions for Guess Number Higher or Lower II.

> divide-and-conquer + dp