<h2><a href="https://leetcode.com/problems/find-the-last-marked-nodes-in-tree">Find the Last Marked Nodes in Tree</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>There exists an <strong>undirected</strong> tree with <code>n</code> nodes numbered <code>0</code> to <code>n - 1</code>. You are given a 2D integer array <code>edges</code> of length <code>n - 1</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates that there is an edge between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code> in the tree.</p>

<p>Initially, <strong>all</strong> nodes are <strong>unmarked</strong>. After every second, you mark all unmarked nodes which have <strong>at least</strong> one marked node <em>adjacent</em> to them.</p>

<p>Return an array <code>nodes</code> where <code>nodes[i]</code> is the last node to get marked in the tree, if you mark node <code>i</code> at time <code>t = 0</code>. If <code>nodes[i]</code> has <em>multiple</em> answers for any node <code>i</code>, you can choose<strong> any</strong> one answer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">edges = [[0,1],[0,2]]</span></p>

<p><strong>Output:</strong> [2,2,1]</p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/01/screenshot-2024-06-02-122236.png" style="width: 450px; height: 217px;" /></p>

<ul>
	<li>For <code>i = 0</code>, the nodes are marked in the sequence: <code>[0] -&gt; [0,1,2]</code>. Either 1 or 2 can be the answer.</li>
	<li>For <code>i = 1</code>, the nodes are marked in the sequence: <code>[1] -&gt; [0,1] -&gt; [0,1,2]</code>. Node 2 is marked last.</li>
	<li>For <code>i = 2</code>, the nodes are marked in the sequence: <code>[2] -&gt; [0,2] -&gt; [0,1,2]</code>. Node 1 is marked last.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">edges = [[0,1]]</span></p>

<p><strong>Output:</strong> [1,0]</p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/01/screenshot-2024-06-02-122249.png" style="width: 350px; height: 180px;" /></p>

<ul>
	<li>For <code>i = 0</code>, the nodes are marked in the sequence: <code>[0] -&gt; [0,1]</code>.</li>
	<li>For <code>i = 1</code>, the nodes are marked in the sequence: <code>[1] -&gt; [0,1]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">edges = [[0,1],[0,2],[2,3],[2,4]]</span></p>

<p><strong>Output:</strong> [3,3,1,1,1]</p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/03/screenshot-2024-06-03-210550.png" style="height: 240px; width: 450px;" /></p>

<ul>
	<li>For <code>i = 0</code>, the nodes are marked in the sequence: <code>[0] -&gt; [0,1,2] -&gt; [0,1,2,3,4]</code>.</li>
	<li>For <code>i = 1</code>, the nodes are marked in the sequence: <code>[1] -&gt; [0,1] -&gt; [0,1,2] -&gt; [0,1,2,3,4]</code>.</li>
	<li>For <code>i = 2</code>, the nodes are marked in the sequence: <code>[2] -&gt; [0,2,3,4] -&gt; [0,1,2,3,4]</code>.</li>
	<li>For <code>i = 3</code>, the nodes are marked in the sequence: <code>[3] -&gt; [2,3] -&gt; [0,2,3,4] -&gt; [0,1,2,3,4]</code>.</li>
	<li>For <code>i = 4</code>, the nodes are marked in the sequence: <code>[4] -&gt; [2,4] -&gt; [0,2,3,4] -&gt; [0,1,2,3,4]</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= edges[i][0], edges[i][1] &lt;= n - 1</code></li>
	<li>The input is generated such that <code>edges</code> represents a valid tree.</li>
</ul>
