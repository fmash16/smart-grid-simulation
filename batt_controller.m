function [batt_power_out] = batt_controller(batt_soc, load, price)

    avg_price = 35;
    setpoint = 0.55 * 20000;

    if batt_soc < 0.1
        batt_power_out = -3000;
    elseif (load < setpoint && price < avg_price)
        batt_power_out = -0.4*20000*3000 / load;
    else
        batt_power_out = 0.5*20000*3000 / load;
    end
