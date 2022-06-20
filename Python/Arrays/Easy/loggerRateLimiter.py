class Logger(object):
    def __init__(self):
        # dictionary DS
        self.message_dict = {}

    def shouldPrintMessage(self, timestamp, message):
        # return True if message is not in dictionary already 
        if message not in self.message_dict:
            # add message to dict
            self.message_dict[message] = timestamp
            # return True 
            return True 

        # if we've seen this message before and more than 10 seconds have passed, add to dict and update timestamp
        if timestamp - self.message_dict[message] >= 10:
            self.message_dict[message] = timestamp 
            return True 

        return False 

#Time comp: O(1)
#Space comp: O(M) - size of incoming messages 