function [bid, quantity_A] = auction_controller(current_price, avg_price, std_dev, demand_A)

    shortage = 0;

    % User defined settings
    base_setpoint = 5000;

    % ramp settings: high=0.360, low=0.667
    ramp = 0.5; 

    % range: lowest reduction in supply user is comfortable with
    range = 1000 * (1-ramp);

    demand = (demand_A) * 2;
    
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

    quantity_A = demand_A * ratio * 2;

    fileID = fopen('exp.txt','a');
    fprintf(fileID,'%6.2f       %6.2f\n', demand, quantity_A);

    %quantity_A = demand_A * ratio * 2;
