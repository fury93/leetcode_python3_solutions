"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        idToIndex, subordinates = {}, None
        for i, employee in enumerate(employees):
            idToIndex[employee.id] = i

        totalImportance, subordinates = 0, [id]
        while subordinates:
            employeeId = subordinates.pop()
            employee = employees[idToIndex[employeeId]]
            totalImportance += employee.importance
            subordinates.extend(employee.subordinates)

        return totalImportance
            