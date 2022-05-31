class Solution(object):
    def courseScheduleII(self, numCourses, pre_requisites):
        # init course_list, visited_set, cycle_set, output_list
        output_list = []
        visited_set, cycle_set = set(), set()

        # create course_list (adjacency list)
        course_list = { i:[] for i in range(numCourses)}
        # append pre_req to course_list
        for course, pre_req in pre_requisites:
            course_list[course].append(pre_req)

        # dfs function for course completion 
        def courseCompletion(courses):
            # base case if courses in cycle_set
            if courses in cycle_set:
                return False

            # base case if courses in visited_set
            if courses in visited_set:
                return True 
            
            # add course to cycle_set
            cycle_set.add(courses)

            # iterate through the courss and its pre_reqs 
            for pre in course_list[courses]:
                if courseCompletion(pre) == False:
                    return False
                
            cycle_set.remove(courses)
            visited_set.add(courses)
            output_list.append(courses)

            return True 
            
        # iterate through numCourses and run dfs function
        for c in range(numCourses):
            if courseCompletion(c) == False:
                return []
        return output_list 
            
