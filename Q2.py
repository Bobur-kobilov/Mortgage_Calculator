#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:06:59 2018

@author: boburjonkobilov
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:22:22 2018

@author: boburjonkobilov
"""


downpayment_portion=0.25
annual_salary=float(input("Enter your annual salary:"))
portion_salary=float(input("Enter the percentage of your salary to save, as a decimal:"))
cost_house=float(input("Enter the cost of your house:"))
semiannual_raise=float(input("Enter your semiannual raise"))
sum_semiannual_raise_salary=annual_salary
downpayment_required=cost_house*downpayment_portion
savings=0
current_savings=0
#current_savings=(annual_salary/12)*portion_salary

count=0
while (savings<downpayment_required):
        savings+=current_savings
        count=count+1
        if count==1:
            current_savings=(annual_salary/12)*portion_salary
        elif count%6==0:
            sum_semiannual_raise_salary+= sum_semiannual_raise_salary*semiannual_raise
            current_savings=(sum_semiannual_raise_salary/12)*portion_salary
        else:
            current_savings=(sum_semiannual_raise_salary/12)*portion_salary
            
        
print("Number of months:",count)        
    
   