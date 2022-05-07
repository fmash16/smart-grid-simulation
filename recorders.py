#! /usr/bin/python3

loadBus = [34, 47, 70, 73, 74, 83, 178, 208, 225, 248, 249, 264, 276, 289, 314,
        320, 327, 337, 342, 349, 387, 388, 406, 458, 502, 522, 539, 556, 562,
        563, 611, 614, 619, 629, 639, 676, 682, 688, 701, 702, 755, 778, 780,
        785, 813, 817, 835, 860, 861, 886, 896, 898, 899, 900, 906]

phases = ['A', 'B', 'A', 'A', 'A', 'B', 'B', 'C', 'A', 'B', 'B', 'C', 'B', 'A', 'B', 'C', 'C', 'C', 'C', 'A', 'A', 'A', 'B', 'C', 'A', 'B', 'C', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'B', 'B', 'B', 'B', 'C', 'B', 'B', 'C', 'C', 'B', 'B', 'A', 'C', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A']

for i in range(len(loadBus)):
    print("""
// Load %(number)d
object multi_recorder {
    name LOAD%(number)d_data;
    file output/LOAD%(number)d_data.csv;
    interval 60;
    property LOAD%(number)d:base_power_%(phase)c, Bus%(bus)d:measured_power.real, Bus%(bus)d:measured_power.imag, inv_%(number)d_sol:VA_Out.real, inv_%(number)d_batt:VA_Out.real, Bus%(bus)d:measured_voltage_%(phase)c.real, Bus%(bus)d:measured_voltage_%(phase)c.imag, Bus%(bus)d:measured_current_%(phase)c.real, Bus%(bus)d:measured_current_%(phase)c.imag, batt_%(number)d:state_of_charge;
}
    """ % {'number' : i+1, 'bus' : loadBus[i], 'phase' : phases[i]})

    # print("""
# // Load %(number)d
# object multi_recorder {
    # name LOAD%(number)d_data;
    # file output/LOAD%(number)d_data.csv;
    # interval 60;
    # property LOAD%(number)d:base_power_%(phase)c, LOAD%(number)d:measured_power.real, Bus%(bus)d:measured_voltage_%(phase)c.real, Bus%(bus)d:measured_current_%(phase)c.real;
# }
    # """ % {'number' : i+1, 'bus' : loadBus[i], 'phase' : phases[i]})

    # print("Bus%(bus)d:measured_current_%(phase)c, " % {'bus' : loadBus[i], 'phase' : phases[i]})
    # print("LOAD%(number)d:voltage_%(phase)c.real, " % {'number' : i+1, 'phase' : phases[i]})
