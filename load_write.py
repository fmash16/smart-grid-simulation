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
}

object player {
    name LOAD%(number)d_player;
    file data/loads/load_profile_%(number)d.player;
}

// Distributed Generation
object inverter {
    name inv_%(number)d_sol;
    parent Bus%(bus)d;
    generator_mode CONSTANT_PF;
    generator_status ONLINE;
    inverter_type PWM;
    power_factor 1.0;
    inverter_efficiency 0.96;
    rated_power 10 kVA;
    flags DELTAMODE;
    object solar {
        name solar_%(number)d;
        parent inv_%(number)d_sol;
        generator_mode SUPPLY_DRIVEN;
        generator_status ONLINE;
        panel_type SINGLE_CRYSTAL_SILICON;
        area 100;
        tilt_angle 47.0;
	efficiency 0.135;
	orientation_azimuth 180; //equator-facing (South)
	orientation FIXED_AXIS;
	SOLAR_TILT_MODEL SOLPOS;
	SOLAR_POWER_MODEL FLATPLATE;
        flags DELTAMODE;
    };
}

object inverter {
    name inv_%(number)d_batt;
    generator_status ONLINE;
    inverter_type FOUR_QUADRANT;
    four_quadrant_control_mode LOAD_FOLLOWING;
    parent Bus%(bus)d;
    sense_object Bus%(bus)d;
    rated_power 3000.0;		//Per phase rating
    inverter_efficiency .95;
    charge_on_threshold 1.5 kW;
    charge_off_threshold 1.7 kW;
    discharge_off_threshold 2 kW;
    discharge_on_threshold 3 kW;
    max_discharge_rate 3 kW;
    max_charge_rate 3 kW;
    charge_lockout_time 1;
    discharge_lockout_time 1;
    flags DELTAMODE;

    // rated_power 15 kW;        //Per phase rating
    // inverter_efficiency .95;
    // charge_on_threshold 7 kW;
    // charge_off_threshold 9 kW;
    // discharge_off_threshold 9.1 kW;
    // discharge_on_threshold 9.5 kW;
    // max_discharge_rate 4 kW;
    // max_charge_rate 4 kW;
    // charge_lockout_time 1;
    // discharge_lockout_time 1;
}
object battery {
    name batt_%(number)d;
    parent inv_%(number)d_batt;
    use_internal_battery_model TRUE;
    battery_type LI_ION;
    rated_power 3 kW;
    nominal_voltage 240;
    battery_capacity 50 kWh;
    round_trip_efficiency 0.81;
    state_of_charge 0.5;
    generator_mode SUPPLY_DRIVEN;
    flags DELTAMODE;
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

// Distributed Generation
object inverter {
    name inv_%(number)d_sol;
    parent Bus%(bus)d;
    generator_mode CONSTANT_PF;
    generator_status ONLINE;
    inverter_type PWM;
    power_factor 1.0;
    inverter_efficiency 0.96;
    rated_power 10 kVA;
    flags DELTAMODE;
    object solar {
        name solar_%(number)d;
        parent inv_%(number)d_sol;
        generator_mode SUPPLY_DRIVEN;
        generator_status ONLINE;
        panel_type SINGLE_CRYSTAL_SILICON;
        area 100;
        tilt_angle 47.0;
	efficiency 0.135;
	orientation_azimuth 180; //equator-facing (South)
	orientation FIXED_AXIS;
	SOLAR_TILT_MODEL SOLPOS;
	SOLAR_POWER_MODEL FLATPLATE;
        flags DELTAMODE;
    };
}

object inverter {
    name inv_%(number)d_batt;
    generator_status ONLINE;
    inverter_type FOUR_QUADRANT;
    four_quadrant_control_mode LOAD_FOLLOWING;
    parent Bus%(bus)d;
    sense_object Bus%(bus)d;
    rated_power 3000.0;		//Per phase rating
    inverter_efficiency .95;
    charge_on_threshold 1.5 kW;
    charge_off_threshold 1.7 kW;
    discharge_off_threshold 2 kW;
    discharge_on_threshold 3 kW;
    max_discharge_rate 3 kW;
    max_charge_rate 3 kW;
    charge_lockout_time 1;
    discharge_lockout_time 1;
    flags DELTAMODE;

    // rated_power 15 kW;        //Per phase rating
    // inverter_efficiency .95;
    // charge_on_threshold 7 kW;
    // charge_off_threshold 9 kW;
    // discharge_off_threshold 9.1 kW;
    // discharge_on_threshold 9.5 kW;
    // max_discharge_rate 4 kW;
    // max_charge_rate 4 kW;
    // charge_lockout_time 1;
    // discharge_lockout_time 1;
}
object battery {
    name batt_%(number)d;
    parent inv_%(number)d_batt;
    use_internal_battery_model TRUE;
    battery_type LI_ION;
    rated_power 3 kW;
    nominal_voltage 240;
    battery_capacity 50 kWh;
    round_trip_efficiency 0.81;
    state_of_charge 0.5;
    generator_mode SUPPLY_DRIVEN;
    flags DELTAMODE;
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

// Distributed Generation
object inverter {
    name inv_%(number)d_sol;
    parent Bus%(bus)d;
    generator_mode CONSTANT_PF;
    generator_status ONLINE;
    inverter_type PWM;
    power_factor 1.0;
    inverter_efficiency 0.96;
    rated_power 10 kVA;
    flags DELTAMODE;
    object solar {
        name solar_%(number)d;
        parent inv_%(number)d_sol;
        generator_mode SUPPLY_DRIVEN;
        generator_status ONLINE;
        panel_type SINGLE_CRYSTAL_SILICON;
        area 100;
        tilt_angle 47.0;
	efficiency 0.135;
	orientation_azimuth 180; //equator-facing (South)
	orientation FIXED_AXIS;
	SOLAR_TILT_MODEL SOLPOS;
	SOLAR_POWER_MODEL FLATPLATE;
        flags DELTAMODE;
    };
}

object inverter {
    name inv_%(number)d_batt;
    generator_status ONLINE;
    inverter_type FOUR_QUADRANT;
    four_quadrant_control_mode LOAD_FOLLOWING;
    parent Bus%(bus)d;
    sense_object Bus%(bus)d;
    rated_power 3000.0;		//Per phase rating
    inverter_efficiency .95;
    charge_on_threshold 1.5 kW;
    charge_off_threshold 1.7 kW;
    discharge_off_threshold 2 kW;
    discharge_on_threshold 3 kW;
    max_discharge_rate 3 kW;
    max_charge_rate 3 kW;
    charge_lockout_time 1;
    discharge_lockout_time 1;
    flags DELTAMODE;

    // rated_power 15 kW;        //Per phase rating
    // inverter_efficiency .95;
    // charge_on_threshold 7 kW;
    // charge_off_threshold 9 kW;
    // discharge_off_threshold 9.1 kW;
    // discharge_on_threshold 9.5 kW;
    // max_discharge_rate 4 kW;
    // max_charge_rate 4 kW;
    // charge_lockout_time 1;
    // discharge_lockout_time 1;
}
object battery {
    name batt_%(number)d;
    parent inv_%(number)d_batt;
    use_internal_battery_model TRUE;
    battery_type LI_ION;
    rated_power 3 kW;
    nominal_voltage 240;
    battery_capacity 50 kWh;
    round_trip_efficiency 0.81;
    state_of_charge 0.5;
    generator_mode SUPPLY_DRIVEN;
    flags DELTAMODE;
}
    """ % {'number' : i+1, 'bus' : loadBus[i], 'phase' : phases[i]})
