<h2><a href="https://leetcode.com/problems/maximum-total-area-occupied-by-pistons">Maximum Total Area Occupied by Pistons</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>There are several pistons in an old car engine, and we want to calculate the <strong>maximum</strong> possible area <strong>under</strong> the pistons.</p>

<p>You are given:</p>

<ul>
	<li>An integer <code>height</code>, representing the <strong>maximum</strong> height a piston can reach.</li>
	<li>An integer array <code>positions</code>, where <code>positions[i]</code> is the current position of piston <code>i</code>, which is equal to the current area <strong>under</strong> it.</li>
	<li>A string <code>directions</code>, where <code>directions[i]</code> is the current moving direction of piston <code>i</code>, <code>&#39;U&#39;</code> for up, and <code>&#39;D&#39;</code> for down.</li>
</ul>

<p>Each second:</p>

<ul>
	<li>Every piston moves in its current direction 1 unit. e.g., if the direction is up, <code>positions[i]</code> is incremented by 1.</li>
	<li>If a piston has reached one of the ends, i.e., <code>positions[i] == 0</code> or <code>positions[i] == height</code>, its direction will change.</li>
</ul>

<p>Return the <em>maximum possible area</em> under all the pistons.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">height = 5, positions = [2,5], directions = &quot;UD&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>The current position of the pistons has the maximum possible area under it.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">height = 6, positions = [0,0,6,3], directions = &quot;UUDU&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p>After 3 seconds, the pistons will be in positions <code>[3, 3, 3, 6]</code>, which has the maximum possible area under it.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= height &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= positions.length == directions.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= positions[i] &lt;= height</code></li>
	<li><code>directions[i]</code> is either <code>&#39;U&#39;</code> or <code>&#39;D&#39;</code>.</li>
</ul>
