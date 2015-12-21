from thermostats import Thermostat

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

Tpfr, T_error = 70, 3
T_range = [67, 73]

# Jan
thermostat_1 = Thermostat(Jan)
print("Jan result:")
(cost, comf, temp) = thermostat_1.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_1.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_1.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# Feb
thermostat_2 = Thermostat(Feb)
print("Feb result:")
(cost, comf, temp) = thermostat_2.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_2.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_2.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# Mar
thermostat_3 = Thermostat(Mar)
print("Mar result:")
(cost, comf, temp) = thermostat_3.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_3.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_3.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# Apr
thermostat_4 = Thermostat(Apr)
print("Apr result:")
(cost, comf, temp) = thermostat_4.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_4.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_4.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# May
thermostat_5 = Thermostat(May)
print("May result:")
(cost, comf, temp) = thermostat_5.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_5.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_5.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# Jun
thermostat_6 = Thermostat(Jun)
print("Jun result:")
(cost, comf, temp) = thermostat_6.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_6.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_6.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# Jul
thermostat_7 = Thermostat(Jul)
print("Jul result:")
(cost, comf, temp) = thermostat_7.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_7.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_7.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# Aug
thermostat_8 = Thermostat(Aug)
print("Aug result:")
(cost, comf, temp) = thermostat_8.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_8.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_8.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# Sep
thermostat_9 = Thermostat(Sep)
print("Sep result:")
(cost, comf, temp) = thermostat_9.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_9.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_9.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# Oct
thermostat_10 = Thermostat(Oct)
print("Oct result:")
(cost, comf, temp) = thermostat_10.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_10.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_10.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# Nov
thermostat_11 = Thermostat(Nov)
print("Nov result:")
(cost, comf, temp) = thermostat_11.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_11.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_11.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))

# Dec
thermostat_12 = Thermostat(Dec)
print("Dec result:")
(cost, comf, temp) = thermostat_12.cal_traditional(Tpfr, T_error)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_12.cal_rigid(T_range, 3)
print((cost, comf, cost + comf, temp))
(cost, comf, temp) = thermostat_12.cal_opti(T_range, 3)
print((cost, comf, cost + comf, temp))
