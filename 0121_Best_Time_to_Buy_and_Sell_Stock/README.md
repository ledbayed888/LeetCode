Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

---

try_1.py:
* Runtime: 56 ms, faster than 98.09% of Python3 online submissions for Best Time to Buy and Sell Stock.
* Memory Usage: 13.9 MB, less than 74.71% of Python3 online submissions for Best Time to Buy and Sell Stock.

> straightforward

---

try_2.py:
* Runtime: 56 ms, faster than 98.09% of Python3 online submissions for Best Time to Buy and Sell Stock.
* Memory Usage: 13.8 MB, less than 93.10% of Python3 online submissions for Best Time to Buy and Sell Stock.

> one pass
> 	* store min price and find max profit as looping

---

try_3.py: O(n) O(n)

* Runtime: 1128 ms, faster than 49.74% of Python3 online submissions for Best Time to Buy and Sell Stock.
* Memory Usage: 25.2 MB, less than 53.99% of Python3 online submissions for Best Time to Buy and Sell Stock

> dp紀錄0~當前位置的最小值是誰 O(n)
> 之後再跑一次loop去找最大profit即可

---

try_4.py: O(n) O(n)

* Runtime: 2619 ms, faster than 5.01% of Python3 online submissions for Best Time to Buy and Sell Stock.
* Memory Usage: 25 MB, less than 42.99% of Python3 online submissions for Best Time to Buy and Sell Stock.

> dp
