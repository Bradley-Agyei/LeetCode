class Solution(object):
    def meetingRoomsII(self, intervals):
        # sort starting and ending times 
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        # init start_pointer, end_pointer, total_rooms, current_count, length of intervals
        length_of_intervals = len(intervals)
        start_pointer, end_pointer = 0, 0
        total_rooms, current_count = 0, 0

        # ensure in bounds 
        while start_pointer < length_of_intervals:
            # condition -> if start_pointer < end_pointer. increment count and pointer 
            if start_times[start_pointer] < end_times[end_pointer]:
                current_count += 1
                start_pointer += 1
            # else -> decrement count and increment end pointer
            else:
                current_count -= 1
                end_pointer += 1 
            # update total_rooms 
            total_rooms = max(total_rooms, current_count)

        # return total rooms 
        return total_rooms 

# time complexity: O(n log n)
# space complexity: O(n)
        