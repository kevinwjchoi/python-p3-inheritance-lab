# #!/usr/bin/env python

# from user import User

# import random

# class Teacher(User):

#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self._knowledge = [""]

#     @property
#     def knowledge(self):
#         """This is the knowledge property"""
#         return self._knowledge
    
#     @knowledge.setter
#     def knowledge(self, knowledge):
#         """"Check knowledge is a list, and greater than 0 length"""
#         if isinstance(knowledge, list) and len(knowledge) > 0:
#             self._knowledge = knowledge
#         else: 
#             print("Not long enough ")

        
#     def teach(self):
#         pass

#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [""]

    @property
    def knowledge(self):
        """This is the knowledge property"""
        return self._knowledge
    
    @knowledge.setter
    def knowledge(self, knowledge):
        """"Check knowledge is a list, and greater than 0 length"""
        if isinstance(knowledge, list) and len(knowledge) > 0:
            self._knowledge = knowledge
        else: 
            print("Not long enough ")

        
    def teach(self):
        i = random.randint(0,len(self.knowledge)-1)
        return self.knowledge[i]