function [batt_power_in] = batt_controller(batt_soc, load)

    avg_price = 35;
    setpoint = 0.55 * 20000;

    if batt_soc < 0.1
        batt_power_in = -3000;
    elseif load < setpoint
        batt_power_in = -0.4*20000*3000 / load;
    else
        batt_power_in = 0.5*20000*3000 / load;
    end
