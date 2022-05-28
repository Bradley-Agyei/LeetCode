class Solution(object):
    def courseSchedule(self, num_courses, pre_requisites):
        # set up hashmap with crs --> empty list 
        courses_map = {i:[] for i in range(num_courses)}

        # append pre_req to list in hashmap 
        for course, pre_req in pre_requisites:
            courses_map[course].append(pre_req)

        # visitSet to make sure that we dont visit a course twice 
        visit_set = set()

        # dfs function 
        def dfs(courses):
            # base case to see if we already visited course
            if courses in visit_set:
                return False

            # base case if pre_req list is already empty 
            if courses_map[courses] == []:
                return True
            
            # add course to visitSet
            visit_set.add(courses) 

            # loop through to check pre_req and recursively call dfs 
            for pre_courses in courses_map[courses]:
                if not dfs(pre_courses):
                    return False 

            # remove course from visitSet 
            visit_set.remove(courses)

            # if course can be completed, set [] to pre_req list
            courses_map[courses] = []
            return True 

        # loop through num_courses and call dfs 
        for courses in range(num_courses):
            if not dfs(courses):
                return False 
        return True 

