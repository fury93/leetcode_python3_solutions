class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        allDamage, maxLevelDamage = 0, 0
        for levelDamage in damage:
            allDamage += levelDamage
            maxLevelDamage = max(maxLevelDamage, levelDamage)
        
        return allDamage - min(armor, maxLevelDamage) + 1