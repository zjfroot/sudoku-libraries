# -*- coding: iso-8859-15 -*-
import random

class Tools:

    def r(self,within_list):
        return self.random(within_list)

    def r_locations(self,within_list,limit):
        l = []
        while limit > 0:
            r = self.random(within_list)
            l.append(r)
            within_list.remove(r)
            limit -= 1
        return l
    
    def random(self,within_list):
        return random.choice(within_list)

