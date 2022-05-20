% t = linspace(0, 1);
% F = optimizef(t);
% plot(t,F,'LineWidth',2)
% hold on
% plot([x_min,x_min],[-2,8],'g--');
% plot([x_max,x_max],[-2,8],'g--');
% legend('bill(x)','discomfort(x)')
% xlabel({'x';'Tradeoff region between the green lines'})

current_clearing_price = 5;     % unit in taka
desired_demand = 1.500 * 5/60;  % unit in kWh

x_min = 0.05;
x_max = 0.15;

k = 5;

x = 0:0.01:0.15;
f1 = current_clearing_price*x;
f2 = k*(x-desired_demand).^2;
plot(x,f1);
hold on;
plot(x,f2,'r');
grid on;

opt_Function = @(x)[current_clearing_price*x; k*(x-desired_demand)^2];
numberOfVars = 1;
[x, fval] = gamultiob

goal = [current_clearing_price*x_min, 0];
weight = [1,0];
x0 = 0.1;
x = fgoalattain(opt_Function, x0, goal, weight, [], [], [], [], x_min, x_max)
% plot([x,x], [-2,8], 'r-')
% x = particleswarm(opt_Function, 2)
%x = fmincon(opt_Function, x0, [], [], [], [], x_min, x_max)
