Question: https://leetcode.com/problems/reverse-linked-list/

---

try_1.py: O(n)

* Runtime: 28 ms, faster than 97.07% of Python3 online submissions for Reverse Linked List.
* `Memory Usage: 20.4 MB, less than 5.07% of Python3 online submissions for Reverse Linked List.

> recursively
> 去recursive先去找到底，之後再慢慢的把答案從尾巴串接起來

---

try_2.py: O(n)

* Runtime: 28 ms, faster than 97.07% of Python3 online submissions for Reverse Linked List.
* Memory Usage: 15.4 MB, less than 38.23% of Python3 online submissions for Reverse Linked List.

> iteratively
> 直接把每個都往前指，就可以直接reverse了

---

try_3.py: O(n) O(1)

* Runtime: 28 ms, faster than 97.76% of Python3 online submissions for Reverse Linked List.
* Memory Usage: 15.3 MB, less than 70.12% of Python3 online submissions for Reverse Linked List.

> 將值都往頭丟即可

---

try_4.py: O(n) O(n)

* Runtime: 32 ms, faster than 90.08% of Python3 online submissions for Reverse Linked List.
* Memory Usage: 20.4 MB, less than 6.34% of Python3 online submissions for Reverse Linked List.

> recursion => 拿到倒數第二個，之後從倒數第一個開始往後接倒數第二個