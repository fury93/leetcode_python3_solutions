class Solution:
    def build_lcp(self, s, sa):
        """
        Kasai algorithm to build LCP
        s: string
        sa: suffix array
        rank: inverse suffix array

        k: number of common prefixes between suffixes
        """
        n = len(sa)
        rank = [0] * n
        for i in range(n):
            rank[sa[i]] = i

        k = 0
        lcp = [0] * n
        for i in range(n):
            if rank[i] == n - 1:
                k = 0
                continue
            j = sa[rank[i] + 1]
            while i + k < n and j + k < n and s[i + k] == s[j + k]:
                k += 1
            lcp[rank[i]] = k
            k = max(k - 1, 0)
        return lcp

    def sort_bucket(self, s, buckets, order):
        d = defaultdict(list)
        for bucket in buckets: 
            key = s[bucket : bucket + order]
            d[key].append(bucket)

        result = []
        for k, v in sorted(d.items()):
            if len(v) > 1: 
                result.extend(self.sort_bucket(s, v, order << 1))  # or `order * 2`
            else: 
                result.append(v[0])
        print(d)
        return result 

    def suffix_array_manber_myers(self, s): 
        return self.sort_bucket(s, (range(len(s))), 1)

    def countDistinct(self, s: str) -> int:
        """
        Example:
        -----
        String: azaza
        -----
        Total number of substrings: n(n + 1) / 2
        -------------------
        a az aza azaz azaza
        z za zaz zaza
        a az aza
        z za
        z
        --------------------
        15
        """
        sa = self.suffix_array_manber_myers(s)
        lcp = self.build_lcp(s, sa)
        n = len(s)
        return ((n * (n + 1)) // 2) - sum(lcp)