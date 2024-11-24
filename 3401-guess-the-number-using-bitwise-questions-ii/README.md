<h2><a href="https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii">Guess the Number Using Bitwise Questions II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>There is a number <code>n</code> between <code>0</code> and <code>2<sup>30</sup> - 1</code> (both inclusive) that you have to find.</p>

<p>There is a pre-defined API <code>int commonBits(int num)</code> that helps you with your mission. But here is the challenge, every time you call this function, <code>n</code> changes in some way. But keep in mind, that you have to find the <strong>initial value of </strong><code>n</code>.</p>

<p><code>commonBits(int num)</code> acts as follows:</p>

<ul>
	<li>Calculate <code>count</code> which is the number of bits where both <code>n</code> and <code>num</code> have the same value in that position of their binary representation.</li>
	<li><code>n = n XOR num</code></li>
	<li>Return <code>count</code>.</li>
</ul>

<p>Return <em>the number</em> <code>n</code>.</p>

<p><strong>Note:</strong> In this world, all numbers are between <code>0</code> and <code>2<sup>30</sup> - 1</code> (both inclusive), thus for counting common bits, we see only the first 30 bits of those numbers.</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 2<sup>30</sup> - 1</code></li>
	<li><code>0 &lt;= num &lt;= 2<sup>30</sup> - 1</code></li>
	<li>If you ask for some <code>num</code> out of the given range, the output wouldn&#39;t be reliable.</li>
</ul>
