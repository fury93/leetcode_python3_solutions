<h2><a href="https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag">Maximum Number of People That Can Be Caught in Tag</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are playing a game of tag with your friends. In tag, people are divided into two teams: people who are &quot;it&quot;, and people who are not &quot;it&quot;. The people who are &quot;it&quot; want to catch as many people as possible who are not &quot;it&quot;.</p>

<p>You are given a <strong>0-indexed</strong> integer array <code>team</code> containing only zeros (denoting people who are <strong>not</strong> &quot;it&quot;) and ones (denoting people who are &quot;it&quot;), and an integer <code>dist</code>. A person who is &quot;it&quot; at index <code>i</code> can catch any <strong>one</strong> person whose index is in the range <code>[i - dist, i + dist]</code> (<strong>inclusive</strong>) and is <strong>not</strong> &quot;it&quot;.</p>

<p>Return <em>the <strong>maximum</strong> number of people that the people who are &quot;it&quot; can catch</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> team = [0,1,0,1,0], dist = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The person who is &quot;it&quot; at index 1 can catch people in the range [i-dist, i+dist] = [1-3, 1+3] = [-2, 4].
They can catch the person who is not &quot;it&quot; at index 2.
The person who is &quot;it&quot; at index 3 can catch people in the range [i-dist, i+dist] = [3-3, 3+3] = [0, 6].
They can catch the person who is not &quot;it&quot; at index 0.
The person who is not &quot;it&quot; at index 4 will not be caught because the people at indices 1 and 3 are already catching one person.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> team = [1], dist = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong>
There are no people who are not &quot;it&quot; to catch.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> team = [0], dist = 1
<strong>Output:</strong> 0
<strong>Explanation:
</strong>There are no people who are &quot;it&quot; to catch people.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= team.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= team[i] &lt;= 1</code></li>
	<li><code>1 &lt;= dist &lt;= team.length</code></li>
</ul>
