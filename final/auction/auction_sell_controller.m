function [bid, quantity_A, quantity_B, quantity_C] = auction_controller(current_price, avg_price, std_dev, demand_A, demand_B, demand_C)

    % User defined settings
    base_setpoint = 7000;

    % range: lowest supply user is comfortable with
    range = 60000;

    % ramp settings: high=0.360, low=0.667
    ramp = 0.667; 

    demand = (demand_A + demand_B + demand_C) * 20000;
    
    bid = avg_price + (base_setpoint-demand) * ramp * std_dev / range;

    if std_dev == 0
        quantity = demand;
    else
        quantity = demand + (current_price - avg_price) * range / (ramp * std_dev);
    end

    ratio = quantity/demand;
    quantity_A = demand_A * ratio;
    quantity_B = demand_B * ratio;
    quantity_C = demand_C * ratio;
