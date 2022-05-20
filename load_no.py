#! /usr/bin/python3

loadBus = [34, 47, 70, 73, 74, 83, 178, 208, 225, 248, 249, 264, 276, 289, 314,
        320, 327, 337, 342, 349, 387, 388, 406, 458, 502, 522, 539, 556, 562,
        563, 611, 614, 619, 629, 639, 676, 682, 688, 701, 702, 755, 778, 780,
        785, 813, 817, 835, 860, 861, 886, 896, 898, 899, 900, 906]

phases = ['A', 'B', 'A', 'A', 'A', 'B', 'B', 'C', 'A', 'B', 'B', 'C', 'B', 'A', 'B', 'C', 'C', 'C', 'C', 'A', 'A', 'A', 'B', 'C', 'A', 'B', 'C', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'B', 'B', 'B', 'B', 'C', 'B', 'B', 'C', 'C', 'B', 'B', 'A', 'C', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A']

for i in range(0,15):
    print("""
// Load %(number)d
object load {
    name LOAD%(number)d;
    parent Bus%(bus)d;
    phases %(phase)c;
    nominal_voltage 240.00;
    // base_power_%(phase)c LOAD%(number)d_player.value*1052.631579;
    // base_power_%(phase)c LOAD%(number)d_player.value*8052.631579;
    base_power_%(phase)c LOAD%(number)d_player.value*2;
    power_fraction_%(phase)c 1;
    power_pf_%(phase)c 0.8;
    flags DELTAMODE;
}

object player {
    name LOAD%(number)d_player;
    file data/loads/load_profile_%(number)d.player;
}

    """ % {'number' : i+1, 'bus' : loadBus[i], 'phase' : phases[i]})

for i in range(15,40):
    print("""
// Load %(number)d
object load {
    name LOAD%(number)d;
    parent Bus%(bus)d;
    phases %(phase)c;
    nominal_voltage 240.00;
    // base_power_%(phase)c LOAD%(number)d_player.value*1052.631579;
    // base_power_%(phase)c LOAD%(number)d_player.value*8052.631579;
    base_power_%(phase)c LOAD%(number)d_player.value*4;
    power_fraction_%(phase)c 1;
    power_pf_%(phase)c 0.8;
}

object player {
    name LOAD%(number)d_player;
    file data/loads/load_profile_%(number)d.player;
}

    """ % {'number' : i+1, 'bus' : loadBus[i], 'phase' : phases[i]})

for i in range(40,55):
    print("""
// Load %(number)d
object load {
    name LOAD%(number)d;
    parent Bus%(bus)d;
    phases %(phase)c;
    nominal_voltage 240.00;
    // base_power_%(phase)c LOAD%(number)d_player.value*1052.631579;
    // base_power_%(phase)c LOAD%(number)d_player.value*8052.631579;
    base_power_%(phase)c LOAD%(number)d_player.value*8;
    power_fraction_%(phase)c 1;
    power_pf_%(phase)c 0.8;
}

object player {
    name LOAD%(number)d_player;
    file data/loads/load_profile_%(number)d.player;
}

    """ % {'number' : i+1, 'bus' : loadBus[i], 'phase' : phases[i]})
