function [bid, quantity_A, quantity_B, quantity_C] = auction_controller(current_price, avg_price, std_dev, demand_A, demand_B, demand_C)

    shortage = 0;

    % User defined settings
    base_setpoint = 7000;

    % ramp settings: high=0.360, low=0.667
    ramp = 0.667; 

    % range: lowest reduction in supply user is comfortable with
    range = 1000 * (1-ramp);

    demand = (demand_A + demand_B + demand_C) * 20000;
    
    bid = avg_price + (base_setpoint-demand) * ramp * std_dev / range;

    if std_dev == 0
        quantity = demand;
    else
        quantity = demand + (current_price - avg_price) * range / (ramp * std_dev);
        if quantity < demand
            shortage = shortage + (demand - quantity);
        else
            if shortage > 0
                shortage = shortage - (quantity - demand);
            else
                quantity = demand
            end
        end
    end

    ratio = quantity/demand;

    if isnan(ratio)
        ratio = 1;
    end

    fileID = fopen('exp.txt','a');
    fprintf(fileID,'%6.2f\n', shortage);

    quantity_A = demand_A * ratio * 20000;
    quantity_B = demand_B * ratio * 0;
    quantity_C = demand_C * ratio * 0;
