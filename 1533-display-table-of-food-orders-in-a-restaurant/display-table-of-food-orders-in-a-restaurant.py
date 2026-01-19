class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = defaultdict(lambda: defaultdict(int))
        foods = set()
        for _, table, food in orders:
            foods.add(food)
            tables[table][food] += 1

        sortedFoods = sorted(foods)
        foodToId = {f:i+1 for i, f in enumerate(sortedFoods)}

        res = [["Table"] + sortedFoods]
        template = [0] * (len(sortedFoods) + 1)
        
        for table in sorted(tables.keys(), key = int):
            row = template[::]
            row[0] = table
            for food in tables[table]:
                row[foodToId[food]] = tables[table][food]
            res.append(list(map(str, row)))

        return res