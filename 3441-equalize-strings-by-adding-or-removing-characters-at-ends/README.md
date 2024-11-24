<h2><a href="https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends">Equalize Strings by Adding or Removing Characters at Ends</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given two strings <code>initial</code> and <code>target</code>, your task is to modify <code>initial</code> by performing a series of operations to make it equal to <code>target</code>.</p>

<p>In one operation, you can add or remove <strong>one character</strong> only at the <em>beginning</em> or the <em>end</em> of the string <code>initial</code>.</p>

<p>Return the <strong>minimum</strong> number of operations required to <em>transform</em> <code>initial</code> into <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">initial = &quot;abcde&quot;, target = &quot;cdef&quot;</span></p>

<p><strong>Output:</strong> 3</p>

<p><strong>Explanation:</strong></p>

<p>Remove <code>&#39;a&#39;</code> and <code>&#39;b&#39;</code> from the beginning of <code>initial</code>, then add <code>&#39;f&#39;</code> to the end.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">initial = &quot;axxy&quot;, target = &quot;yabx&quot;</span></p>

<p><strong>Output:</strong> 6</p>

<p><strong>Explanation:</strong></p>

<table border="1">
	<tbody>
		<tr>
			<th>Operation</th>
			<th>Resulting String</th>
		</tr>
		<tr>
			<td>Add <code>&#39;y&#39;</code> to the beginning</td>
			<td><code>&quot;yaxxy&quot;</code></td>
		</tr>
		<tr>
			<td>Remove from end</td>
			<td><code>&quot;yaxx&quot;</code></td>
		</tr>
		<tr>
			<td>Remove from end</td>
			<td><code>&quot;yax&quot;</code></td>
		</tr>
		<tr>
			<td>Remove from end</td>
			<td><code>&quot;ya&quot;</code></td>
		</tr>
		<tr>
			<td>Add <code>&#39;b&#39;</code> to the end</td>
			<td><code>&quot;yab&quot;</code></td>
		</tr>
		<tr>
			<td>Add <code>&#39;x&#39;</code> to the end</td>
			<td><code>&quot;yabx&quot;</code></td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">initial = &quot;xyz&quot;, target = &quot;xyz&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No operations are needed as the strings are already equal.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= initial.length, target.length &lt;= 1000</code></li>
	<li><code>initial</code> and <code>target</code> consist only of lowercase English letters.</li>
</ul>
