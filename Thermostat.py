from math import sin
from math import pi
from math import exp
from collections import deque

class Thermostat(object):

    def __init__(self, temp_data):
        """
        Get the temperature data
        """
        self.daily_temp = temp_data
        """
        k1 is the building’s projected heat capacity –
        the amount of electricity required by HVAC to change the building’s temperature by 1 F.
        k2 = k * area is the projected conductance rate,
        the rate at which the building loses heat to or gains heat from the outside.
        k1 and k2 has unit (kWh/F)
        """
        self.k1, self.k2 = 1, 0.1
        """
        p_t denotes the dynamic electricity price
        pb and ps are the baseline and scale of the prices
        """
        self.pb, self.ps = 0.2, 0.11
        self.p_t = {i : self.pb - self.ps * sin(2 * pi * (i + 1) / 24) for i in range(24)}
        """
        a and b are preference parameter for optimized model, and the default value indicate that users would be
        willing to pay an extra $0.0125 per hour to lower the room temperature from 74 to 73 or an extra $0.0425
        per hour for a decrease from 76 to 75.
        """
        self.a = -7.5 * 0.002
        self.b = -5 * 0.002

    def set_k1(self, k1):
        """
        Set different k1 for different HVAC system, the larger k1, the more effecient of the HVAC system
        """
        self.k1 = k1

    def get_k1(self):
        return self.k1

    def set_k2(self, k2):
        """
        Set differnet k2 for different target buinding, the larger k2, the building is easier to lose or gain heat from the outside
        """
        self.k2 = k2

    def get_k2(self):
        return self.k2

    def set_pb(self, pb):
        """
        Set different baseline electricity price 
        """
        self.pb = pb

    def get_pb(self):
        return self.pb

    def set_ps(self, ps):
        """
        Set the variation rate of the dynamic elecricity price 
        """
        self.ps = ps

    def get_ps(self):
        return self.ps

    def get_p_t(self):
        return self.p_t
    """
    Set different a and b, smaller a and b(that is the absulate value of a and b is larger) indicates the users are willing
    to pay more money to get a more comfortable temperature
    """
    def set_a(self, a):
        self.a = a

    def get_a(self):
        return self.a

    def set_b(self, a):
        self.a = a

    def get_b(self):
        return self.a
        

    def cal_cost(self, T_ini_now, X_tar_now, now):       
        """
        now is the time from 1 to 24 which determines the electricity price
        """
        if now >= 24:
            now %= 24
        cost = -self.p_t[now] * self.k1 * abs(T_ini_now - X_tar_now)
        return cost

    def cal_temp(self, T_out_prev, X_tar_prev, t = 1):
        """
        Calculate the temperature in current period
        """
        T_ini_now = T_out_prev + (X_tar_prev - T_out_prev) * exp(-(self.k2 / self.k1) * t)
        return T_ini_now
        
    def cal_utility_rigid(self, T_out_prev, X_tar_prev, X_tar_now, now):
        """
        The total utility from current to the end of planning horizon is modeled as a dynamic programming question,
        Here the function is to calculate the utility at a certain time
        """
        if now >= 24:
            now %= 24
        utility = -self.p_t[now] * self.k1 * abs(T_out_prev + (X_tar_prev - T_out_prev) *  exp(-k2 / k1) - X_tar_now)
        return utility

#Traditional model
    def cal_traditional(self, tar_temp, error):
        if len(self.daily_temp) < 25:
            print("Please input at least 25 temperature data for calculting traditional model cost!")
            return
    #Temperature range
        trad = [tar_temp - error, tar_temp + error]
    #initial indoor temperature
        T_inside_temp = [self.daily_temp[0]]
        cost_trad, comf_trad, temp_set = 0, 0, []
        for time in range(24):
            if T_inside_temp[-1] > trad[1]:
                X_tar = trad[0]
            elif T_inside_temp[-1] < trad[0]:
                X_tar = trad[1]
            else:
                X_tar = (trad[0] + trad[1]) // 2
            temp_set.append(X_tar)
            cost_trad += self.cal_cost(T_inside_temp[-1], X_tar, time)
            comf_trad += self.cal_comf(T_inside_temp[-1], tar_temp)
            temp_next_period = self.cal_temp(self.daily_temp[time], X_tar)
            T_inside_temp.append(temp_next_period)
        return (-cost_trad, -comf_trad, temp_set)

#Rigid model
    max_utility = -float("inf")
    def cal_rigid(self, range_temp, future_time):
        if len(self.daily_temp) < 24 + future_time:
            print("Please input at least " + str(24 + future_time)+ \
                  " temperature data for calculting rigid model cost!")
            return
        #initial indoor temperature
        T_inside_temp = [self.daily_temp[0]]
        if T_inside_temp[-1] > range_temp[1]:
            X_tar_previous = range_temp[1]
        elif T_inside_temp[-1] < range_temp[0]:
            X_tar_previous = range_temp[0]
        else:
            X_tar_previous = (range_temp[0] + range_temp[1]) // 2
        temp_set = []
        temp_set.append(X_tar_previous)
        temp_now = self.cal_temp(self.daily_temp[0], X_tar_previous)
        T_inside_temp = [temp_now]
        X_tar_now = None
        for time in range(1, 24):
            self.max_utility = -float("inf")
            for temp in range(range_temp[0], range_temp[1] + 1):
                copy = self.max_utility
                self.cal_rigid_helper(0, temp, T_inside_temp[-1], range_temp, time + future_time, future_time)
                if self.max_utility > copy:
                    X_tar_now = temp
                elif not X_tar_now:
                    if self.daily_temp[time] > range_temp[1]:
                        X_tar_now = range_temp[0]
                    else:
                        X_tar_now = range_temp[1]
            temp_set.append(X_tar_now)
            temp_next = self.cal_temp(self.daily_temp[time], X_tar_now)
            T_inside_temp.append(temp_next)
        cost_rigid, comf_rigid = 0, 0
        for i in range(len(T_inside_temp)):
            cost_rigid += self.cal_cost(T_inside_temp[i], temp_set[i], i)
            comf_rigid += self.cal_comf(T_inside_temp[i], (range_temp[0] + range_temp[1]) / 2)
        return (-cost_rigid, -comf_rigid, temp_set)
    
#Use recursion function to find the maximum utility at certain time
    def cal_rigid_helper(self, utility, X_tar_now, temp_now, range_temp, time, future_time):
        if future_time <= 0:
            if utility > self.max_utility:
                self.max_utility = utility
            return
        cur_utility = self.cal_cost(temp_now, X_tar_now, time - future_time)
        for X_tar_next in range(range_temp[0], range_temp[1] + 1):
            temp_next = self.cal_temp(self.daily_temp[time - future_time], X_tar_now)
            if  range_temp[0] <= temp_next <= range_temp[1]:
                self.cal_rigid_helper(utility + cur_utility, X_tar_next, temp_next, range_temp, time, future_time - 1)

#Optimizing model
    def cal_opti(self, range_temp, future_time):
        if len(self.daily_temp) < 24 + future_time:
            print("Please input at least " + str(24 + future_time)+ \
                  " temperature data for calculting rigid model cost!")
            return
        #initial indoor temperature
        T_inside_temp = [self.daily_temp[0]]
        if T_inside_temp[-1] > range_temp[1]:
            X_tar_previous = range_temp[1]
        elif T_inside_temp[-1] < range_temp[0]:
            X_tar_previous = range_temp[0]
        else:
            X_tar_previous = (range_temp[0] + range_temp[1]) // 2
        temp_set = []
        temp_set.append(X_tar_previous)
        temp_now = self.cal_temp(self.daily_temp[0], X_tar_previous)
        T_inside_temp = [temp_now]
        X_tar_now = None
        for time in range(1, 24):
            self.max_utility = -float("inf")
            for temp in range(range_temp[0], range_temp[1] + 1):
                copy = self.max_utility
                self.cal_opti_helper(0, temp, T_inside_temp[-1], range_temp, time + future_time, future_time)
                if self.max_utility > copy:
                    X_tar_now = temp
                elif not X_tar_now:
                    if self.daily_temp[time] > range_temp[1]:
                        X_tar_now = range_temp[0]
                    else:
                        X_tar_now = range_temp[1]
            temp_set.append(X_tar_now)
            temp_next = self.cal_temp(self.daily_temp[time], X_tar_now)
            T_inside_temp.append(temp_next)
        cost_opti, comf_opti = 0, 0
        for i in range(len(T_inside_temp)):
            cost_opti += self.cal_cost(T_inside_temp[i], temp_set[i], i)
            comf_opti += self.cal_comf(T_inside_temp[i], (range_temp[0] + range_temp[1]) / 2)
        return (-cost_opti, -comf_opti, temp_set)

    def cal_opti_helper(self, utility, X_tar_now, temp_now, range_temp, time, future_time):
        if future_time <= 0:
            if utility > self.max_utility:
                self.max_utility = utility
            return
        cur_utility = self.cal_cost(temp_now, X_tar_now, time - future_time)
        T_pfr = (range_temp[0] + range_temp[1]) / 2
        cur_comf = self.inte_comf(temp_now, T_pfr, time - future_time, X_tar_now)
        for X_tar_next in range(range_temp[0], range_temp[1] + 1):
            temp_next = self.cal_temp(self.daily_temp[time - future_time], X_tar_now)
            if  range_temp[0] <= temp_next <= range_temp[1]:
                self.cal_opti_helper(utility + cur_utility + cur_comf, X_tar_next, temp_next, range_temp, time, future_time - 1)

#Do (Simulate) integration of the total uncomfortableness at a period of time     
    def inte_comf(self, T_inside_now, T_pfr, time, X_tar_now):
        total_comf = 0
        for i in range(10):
            T_inside_tem = self.cal_temp(self.daily_temp[time], X_tar_now, i / 10)
            total_comf += self.cal_comf(T_inside_tem, T_pfr) / 10
        return total_comf

#Calculate the uncomfortableness at certain time
    def cal_comf(self, T_inside_now, T_pfr):
        res = self.a * ((T_inside_now - T_pfr) ** 2) \
              + self.b * abs(T_inside_now - T_pfr)
        return res

