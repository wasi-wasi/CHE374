# Importing libraries
import matplotlib.pyplot as plt
import numpy as np


def contractor(dragline_payments,annual_flat_fee_perc,engagement_fee,tax_deduc,employee_induc,WAAC,wage):
    npv_0 = (engagement_fee)*(1-tax_deduc)
    npv_1 = (employee_induc[0]+(wage[0][0]+wage[0][1])*(1+annual_flat_fee_perc)+dragline_payments)*(1-tax_deduc)
    npv_2 = (dragline_payments + ((wage[1][0])+wage[1][1])*(1+annual_flat_fee_perc))*(1-tax_deduc)
    npv_3 = (employee_induc[1]+(wage[2][0]+wage[2][1])*(1+annual_flat_fee_perc))*(1-tax_deduc)
    npv_4 = ((wage[3][0]+wage[3][1])*(1+annual_flat_fee_perc))*(1-tax_deduc)
    npv_5 = (employee_induc[2]+(wage[4][0]+wage[4][1])*(1+annual_flat_fee_perc))*(1-tax_deduc)
    npv = npv_0 + npv_1/(1+WAAC)**1 + npv_2/(1+WAAC)**2 + npv_3/(1+WAAC)**3 + npv_4/(1+WAAC)**4 + npv_5/(1+WAAC)**5
    return npv



def move(major_serv,ong_maint,tax_deduc,WAAC,steer_susp_adj,unkwn_cost,drag_op,fuel_oth):
    npv1_0 = (steer_susp_adj + unkwn_cost)*(1-tax_deduc);
    npv1_1 = (ong_maint + drag_op[0] + fuel_oth[0])*(1-tax_deduc)
    npv1_2 = (ong_maint + drag_op[1] + fuel_oth[1])*(1-tax_deduc)
    npv1_3 = (ong_maint + drag_op[2] + fuel_oth[2] + major_serv)*(1-tax_deduc)
    npv1_4 = (ong_maint + drag_op[3] + fuel_oth[3])*(1-tax_deduc)
    npv1_5 = (ong_maint + drag_op[4] + fuel_oth[4])*(1-tax_deduc)
    npv_1 = npv1_0 + npv1_1/(1+WAAC)**1 + npv1_2/(1+WAAC)**2 + npv1_3/(1+WAAC)**3 + npv1_4/(1+WAAC)**4 + npv1_5/(1+WAAC)**5
    return npv_1

#variable used in both calculation --makes sense if we change these
WAAC = 0.09
tax_deduc = 0.3


#variable in poption 1
engagement_fee = -750*10**3
dragline_payments = 9.5*10**6  #check if this is market rate
employee_induc =  [-1*10**6,-250000,-250000] #
wage = [[-6000000,-1080000],[-6400000,-1140000],[-7650000,-1200000],[-8100000,-1365000],[-9500000,-1650000]] #vary
annual_flat_fee_perc = 0.15;

#variable in option 2
steer_susp_adj = -1100000
unkwn_cost = -10000000
ong_maint = -300000 #
drag_op = [-260000,-286000,-314600,-346060,-380666]  #vary this
fuel_oth = [-2000000,-2200000,-2420000,-2662000,-2928200] #
major_serv = -150000

# tax = []
# npv_1 =[]
# npv_2 =[]
# for i in range(0,500):
#     tax.append(i*7/3000)
#     npv_1.append(contractor(dragline_payments,annual_flat_fee_perc,engagement_fee,tax[i],employee_induc,WAAC,wage))
#     npv_2.append(move(major_serv,ong_maint,tax[i],WAAC,steer_susp_adj,unkwn_cost,drag_op,fuel_oth))
#
#
# plt.plot(tax, npv_1, color='r', label='Contractor')
# plt.plot(tax, npv_2, color='g', label='Move')
# plt.xlabel("Tax Rate")
# plt.ylabel("Net Present Value")
# plt.title("Net Present Value vs Tax Rate")
# plt.grid()
plt.show()
## Above tax rate == 1, net present value of contractor is higher than moving
#
# waac = []
# npv_1 =[]
# npv_2 =[]
# for i in range(0,500):
#     waac.append(i/4000)
#     npv_1.append(contractor(dragline_payments,annual_flat_fee_perc,engagement_fee,tax_deduc,employee_induc,waac[i],wage))
#     npv_2.append(move(major_serv,ong_maint,tax_deduc,waac[i],steer_susp_adj,unkwn_cost,drag_op,fuel_oth))
#
#
# plt.plot(waac, npv_1, color='r', label='Contractor')
# plt.plot(waac, npv_2, color='g', label='Move')
# plt.xlabel("WAAC")
# plt.ylabel("Net Present Value")
# plt.title("Net Present Value vs Discount Rate")
# plt.grid()
# plt.show()
###


### Case increase drag operators salary by i%
# drag_op_var = np.array([-260000,-286000,-314600,-346060,-380666])
# npv_1 = []
# npv_2 = []
# drag_var = []
# i_var = []
# i_var_1 = []
#
#
# for i in range(0,400):
#     i_var.append(1+i/400)
#     drag_var.append(drag_op_var*(1+i/400))
#     npv_1.append(contractor(dragline_payments,annual_flat_fee_perc,engagement_fee,tax_deduc,employee_induc,WAAC,wage))
#     npv_2.append(move(major_serv,ong_maint,tax_deduc,WAAC,steer_susp_adj,unkwn_cost,drag_var[i],fuel_oth))
#     i_var_1.append(i/4)
#
#
# plt.plot(i_var_1, npv_1, color='r', label='Contractor')
# plt.plot(i_var_1, npv_2, color='g', label='Move')
# plt.xlabel("Percentage Increase")
# plt.ylabel("Net Present Value")
# plt.title("Net Present Value vs % Increase in Drag Operator Salary")
# plt.grid()
# plt.show()

### Case decrease wage salary by i%
# wager = np.array([[-6000000,-1080000],[-6400000,-1140000],[-7650000,-1200000],[-8100000,-1365000],[-9500000,-1650000]])
# npv_1 = []
# npv_2 = []
# wage_var = []
# i_var = []
# i_var_1 = []
#
#
# for i in range(0,400):
#     i_var.append(i/400)
#     wage_var.append(wager*(i/400))
#     npv_1.append(contractor(dragline_payments,annual_flat_fee_perc,engagement_fee,tax_deduc,employee_induc,WAAC,wage_var[i]))
#     npv_2.append(move(major_serv,ong_maint,tax_deduc,WAAC,steer_susp_adj,unkwn_cost,drag_op,fuel_oth))
#     i_var_1.append(i/4)
#
# plt.plot(i_var_1, npv_1, color='r', label='Contractor')
# plt.plot(i_var_1, npv_2, color='g', label='Move')
# plt.xlabel("Decrease in Wages")
# plt.ylabel("Net Present Value")
# plt.title("Net Present Value vs %Decrease in Wages")
# plt.grid()
# plt.show()












