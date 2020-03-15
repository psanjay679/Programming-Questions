from queue import SimpleQueue

class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

def binSearch(employees, id):

    low = 0
    high = len(employees)

    while low <= high:

        mid = (low + high) >> 1
        if employees[mid].id < id:
            low = mid + 1
        elif employees[mid].id > id:
            high = mid - 1
        else:
            return employees[mid]

    return None



class Solution:

    def getImportance(self, employees, id: int) -> int:
        employees.sort(key=lambda k: k.id)

        e = binSearch(employees, id)
        q = list()
        q.append(e)
        t_sum = 0

        while len(q):
            e = q[-1]
            t_sum += e.importance
            q.pop()

            for i in range(len(e.subordinates)):
                q.append(binSearch(employees, e.subordinates[i]))
        return t_sum


ar = [[101,3,[]],[2,5,[101]]]
employees = list()
for id, importance, subordinates in ar:
    employees.append(Employee(id, importance, subordinates))
id = 2

s = Solution()
print(s.getImportance(employees, id))