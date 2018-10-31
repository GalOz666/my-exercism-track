import gc
import random
from string import ascii_uppercase
import os

#
# garbage collection method to get all class names ?
#
#                 for obj in gc.get_objects():
#                     if isinstance(obj, 'Robot'):
#                         if str(obj) == new_name:
#                             continue
#                 		  else:
#                     		  break
#
#             return new_name

name_roster = []

class Robot:

    global name_roster

    def rand_unique_name(self):

        random.seed(os.urandom(1024))

        while True:
            letters = "".join((random.choice(ascii_uppercase) for _ in range(2)))
            numbers = "".join(str(i) for i in (random.choice(range(10)) for _ in range(3)))
            new_name = letters + numbers
            if new_name in name_roster:
                continue
            else:
                break

        return new_name

    def __init__(self):
        self.name = self.rand_unique_name()
        name_roster.append(self.name)

    def __str__(self):
       return self.name

    def reset(self):
        new_name = self.rand_unique_name()
        
        if self.name:
            name_roster.remove(self.name)
        name_roster.append(new_name)

        self.name = new_name
