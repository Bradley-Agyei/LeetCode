class Solution(object):
    def getImportance(self, employees, id):
        # use hashmap to map employee id -> employee
        employee_map = {e.id: e for e in employees}

        # create dfs function to go deep into employees subordinates 
        def countImportance(eid):
            # set employee to eid 
            employee = employee_map[eid]

            # return importance of employee and their subordinates
            return (employee.importance + sum(countImportance(eid) for eid in employee.subordinates))

        # return dfs function passing id
        return countImportance(id)

# time comp: O(N)
# space comp: O(N)