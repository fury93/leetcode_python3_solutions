<h2><a href="https://leetcode.com/problems/number-of-subsequences-with-odd-sum">Number of Subsequences with Odd Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an array <code>nums</code>, return the number of <span data-keyword="subsequence-array">subsequences</span> with an odd sum of elements.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The odd-sum subsequences are: <code>[<u><strong>1</strong></u>, 1, 1]</code>, <code>[1, <u><strong>1</strong></u>, 1],</code> <code>[1, 1, <u><strong>1</strong></u>]</code>, <code>[<u><strong>1, 1, 1</strong></u>]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The odd-sum subsequences are: <code>[<u><strong>1</strong></u>, 2, 2]</code>, <code>[<u><strong>1, 2</strong></u>, 2],</code> <code>[<u><strong>1</strong></u>, 2, <b><u>2</u></b>]</code>, <code>[<u><strong>1, 2, 2</strong></u>]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
