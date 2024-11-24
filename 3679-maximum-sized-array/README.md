<h2><a href="https://leetcode.com/problems/maximum-sized-array">Maximum Sized Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given a positive integer <code>s</code>, let <code>A</code> be a 3D array of dimensions<!-- notionvc: f8069282-c5f5-4da1-91b8-fa0c1c168ea1 --> <code>n &times; n &times; n</code>, where each element <code>A[i][j][k]</code> is defined as:</p>

<ul>
	<li><code>A[i][j][k] = i * (j OR k)</code>, where <code>0 &lt;= i, j, k &lt; n</code>.</li>
</ul>

<p>Return the <strong>maximum</strong> possible value of <code>n</code> such that the <strong>sum</strong> of all elements in array <code>A</code> does not exceed <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Elements of the array <code>A</code> for <code>n = 2</code><strong>:</strong>

	<ul>
		<li><code>A[0][0][0] = 0 * (0 OR 0) = 0</code></li>
		<li><code>A[0][0][1] = 0 * (0 OR 1) = 0</code></li>
		<li><code>A[0][1][0] = 0 * (1 OR 0) = 0</code></li>
		<li><code>A[0][1][1] = 0 * (1 OR 1) = 0</code></li>
		<li><code>A[1][0][0] = 1 * (0 OR 0) = 0</code></li>
		<li><code>A[1][0][1] = 1 * (0 OR 1) = 1</code></li>
		<li><code>A[1][1][0] = 1 * (1 OR 0) = 1</code></li>
		<li><code>A[1][1][1] = 1 * (1 OR 1) = 1</code></li>
	</ul>
	</li>
	<li>The total sum of the elements in array <code>A</code> is 3, which does not exceed 10, so the maximum possible value of <code>n</code> is 2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Elements of the array <code>A</code> for <code>n = 1</code>:

	<ul>
		<li><code>A[0][0][0] = 0 * (0 OR 0) = 0</code></li>
	</ul>
	</li>
	<li>The total sum of the elements in array <code>A</code> is 0, which does not exceed 0, so the maximum possible value of <code>n</code> is 1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s &lt;= 10<sup>15</sup></code></li>
</ul>
