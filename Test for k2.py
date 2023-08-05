#Different buildings (different k2)
from thermostats import Thermostat

#k2 from 0.1 to 0.2
min_k2, max_k2 = 10, 21
scaling_factor = 100

Tpfr, T_error = 70, 3
T_range = [67, 73]

Jan = [43, 43, 42, 42, 42, 41, 41, 41, 41, 44,\
       47, 49, 51, 53, 54, 54, 54, 53, 50, 49,\
       47, 46, 45, 44, 43, 43, 42, 42, 42, 41 ]

Feb = [49, 48, 48, 47, 47, 46, 46, 45, 48, 51,\
       55, 57, 59, 61, 62, 63, 62, 61, 59, 57,\
       55, 53, 52, 51, 49, 48, 48, 47, 47, 46 ]

Mar = [54, 52, 51, 50, 49, 49, 48, 50, 54, 58,\
       61, 64, 66, 67, 69, 69, 69, 68, 66, 63,\
       61, 59, 57, 55, 54, 52, 51, 50, 49, 49 ]

Apr = [60, 58, 57, 56, 55, 54, 54, 58, 62, 66,\
       69, 71, 74, 76, 77, 78, 78, 77, 75, 71,\
       69, 66, 64, 62, 60, 58, 57, 56, 55, 54 ]

May = [67, 65, 64, 62, 61, 60, 62, 65, 69, 72,\
       76, 79, 81, 83, 85, 86, 86, 86, 84, 81,\
       77, 75, 72, 69, 67, 65, 64, 62, 61, 60 ]

Jun = [74, 72, 70, 69, 67, 66, 68, 71, 76, 80,\
       83, 86, 90, 92, 94, 95, 95, 95, 93, 90,\
       86, 83, 80, 77, 74, 72, 70, 69, 67, 66 ]

Jul = [76, 74, 72, 71, 69, 68, 69, 72, 77, 81,\
       85, 89, 92, 94, 96, 97, 98, 97, 96, 92,\
       88, 85, 82, 79, 76, 74, 72, 71, 69, 68 ]

Aug = [74, 72, 70, 68, 67, 66, 66, 69, 74, 78,\
       82, 86, 89, 92, 94, 95, 95, 94, 92, 87,\
       84, 81, 78, 76, 74, 72, 70, 68, 67, 66 ]

Sep = [66, 64, 63, 62, 61, 60, 59, 61, 66, 70,\
       74, 77, 80, 83, 84, 85, 85, 84, 80, 76,\
       74, 71, 69, 67, 66, 64, 63, 62, 61, 60 ]

Oct = [55, 54, 53, 52, 51, 51, 50, 50, 54, 58,\
       62, 66, 68, 70, 71, 72, 71, 68, 65, 63,\
       60, 59, 57, 55, 55, 54, 53, 52, 51, 51 ]

Nov = [45, 44, 44, 43, 43, 42, 42, 42, 44, 47,\
       50, 53, 55, 57, 58, 58, 58, 55, 53, 51,\
       49, 48, 47, 46, 45, 44, 44, 43, 43, 42 ]

Dec = [42, 42, 41, 41, 41, 41, 40, 40, 41, 43,\
       45, 47, 49, 51, 52, 52, 52, 50, 48, 47,\
       45, 44, 44, 43, 42, 42, 41, 41, 41, 41 ]

month_1 = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", \
         7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

month_2 = {1: Jan, 2: Feb, 3: Mar, 4: Apr, 5: May, 6: Jun, \
         7: Jul, 8: Aug, 9: Sep, 10: Oct, 11: Nov, 12: Dec}

for i in range(1, 13):
    print(f"Different k2 results in {month_1[i]}: \n")
    thermostat1 = Thermostat(month_2[i])

    #Calculate traditional model
    cost_set_trad, comf_set_trad, temp_set_trad = [], [], []
    for k2 in range(min_k2, max_k2):
        thermostat1.set_k2(k2 / scaling_factor)
        (cost, comf, target_temp) = thermostat1.cal_traditional(Tpfr, T_error)
        cost_set_trad.append((k2 / scaling_factor, cost))
        comf_set_trad.append((k2 / scaling_factor, comf))
        temp_set_trad.append(target_temp)

    utility_set_trad = [((i + 10) / 100, cost_set_trad[i][1] + comf_set_trad[i][1]) \
                        for i in range(len(cost_set_trad))]

    print("For traditional thermostat: ")
    print("  Cost with different k2: ")
    print(cost_set_trad)
    print("\n")
    print("  Uncomfortableness with different k2: ")
    print(comf_set_trad)
    print("\n")
    print("  Total utility with different k2: ")
    print(utility_set_trad)
    utility = [utility_set_trad[i][1] for i in range(len(utility_set_trad))]
    print(utility)
    print("\n")


    #Calculate rigid model
    cost_set_rigid, comf_set_rigid, temp_set_rigid = [], [], []
    for k2 in range(min_k2, max_k2):
        thermostat1.set_k2(k2 / scaling_factor)
        (cost, comf, target_temp) = thermostat1.cal_rigid(T_range, 3)
        cost_set_rigid.append((k2 / scaling_factor, cost))
        comf_set_rigid.append((k2 / scaling_factor, comf))
        temp_set_rigid.append(target_temp)

    utility_set_rigid = [((i + 10) / 100, cost_set_rigid[i][1] + comf_set_rigid[i][1]) \
                         for i in range(len(cost_set_rigid))]

    impro_cost_rigid_trad = [((i + 10) / 100, cost_set_trad[i][1] - cost_set_rigid[i][1]) \
                             for i in range(len(cost_set_rigid))]

    impro_utility_rigid_trad = [((i + 10) / 100, utility_set_trad[i][1] - utility_set_rigid[i][1]) \
                        for i in range(len(utility_set_rigid))]

    print("For rigid thermostat: ")
    print("  Cost with different k2: ")
    print(cost_set_rigid)
    print("\n")
    print("  Uncomfortableness with different k2: ")
    print(comf_set_rigid)
    print("\n")
    print("  Total utility with different k2: ")
    print(utility_set_rigid)
    utility = [utility_set_rigid[i][1] for i in range(len(utility_set_rigid))]
    print(utility)
    print("\n")
    print("  Total cost improvement with different k2: ")
    print(impro_cost_rigid_trad)
    print("\n")
    print("  Total utility improvement with different k2: ")
    print(impro_utility_rigid_trad)
    print("\n")


    #Calculate optimized model
    cost_set_opti, comf_set_opti, temp_set_opti = [], [], []
    for k2 in range(min_k2, max_k2):
        thermostat1.set_k2(k2 / scaling_factor)
        (cost, comf, target_temp) = thermostat1.cal_opti(T_range, 3)
        cost_set_opti.append((k2 / scaling_factor, cost))
        comf_set_opti.append((k2 / scaling_factor, comf))
        temp_set_opti.append(target_temp)

    utility_set_opti = [((i + 10) / 100, cost_set_opti[i][1] + comf_set_opti[i][1]) \
                         for i in range(len(cost_set_opti))]

    impro_cost_opti_trad = [((i + 10) / 100, cost_set_trad[i][1] - cost_set_opti[i][1]) \
                             for i in range(len(cost_set_opti))]

    impro_utility_opti_rigid = [((i + 10) / 100, utility_set_rigid[i][1] - utility_set_opti[i][1]) \
                        for i in range(len(utility_set_opti))]

    print("For optimized thermostat: ")
    print("  Cost with different k2: ")
    print(cost_set_opti)
    print("\n")
    print("  Uncomfortableness with different k2: ")
    print(comf_set_opti)
    print("\n")
    print("  Total utility with different k2: ")
    print(utility_set_opti)
    utility = [utility_set_opti[i][1] for i in range(len(utility_set_opti))]
    print(utility)
    print("\n")
    print("  Total cost improvement with different k2: ")
    print(impro_cost_opti_trad)
    print("\n")
    print("  Total utility improvement compared to rigid model with different k2: ")
    print(impro_utility_opti_rigid)
    print("\n")




