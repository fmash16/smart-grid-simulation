% define figure properties
opts.Colors     = get(groot,'defaultAxesColorOrder');
opts.saveFolder = '/home/void/thesis/charts/';
%opts.saveFolder = '/home/void/thesis/charts/';
opts.width      = 8;
opts.height     = 6;
opts.fontType   = 'Times New Roman';
opts.fontSize   = 10;
destFile        = "/home/void/thesis/charts/load11_battery.png"
ftoread = '/home/void/thesis/smart-grid-simulation/final/output/LOAD11_data.csv'
%ftoread = '/home/void/thesis/loads/load_all.csv'

% create new figure
fig = figure; clf


fid=fopen(ftoread)
%data=textscan(fid, '%s%s%d%d%d','Delimiter',',','HeaderLines',1)
data=textscan(fid, '%s%f%f%f%f%f%f%f%f%f%f','Delimiter',',','HeaderLines',8)
fclose(fid)

%x = datetime(data{2},'InputFormat','HH:mm');
x = datetime(data{1},'InputFormat','yyyy-MM-dd HH:mm:ss XXX','TimeZone','GMT','Format','HH:mm:ss');
y1 = data{3};
y2 = data{5};
y3 = data{6};
y4 = data{11};
%y=sqrt(y1.^2+y2.^2)
%plot(x,y0,'LineWidth',2)
%hold on

colororder({'k','k'})
yyaxis left
plot(x,y1,'LineWidth',2)
hold on
[Peak, PeakIdx] = max(y1);
text(x(PeakIdx), Peak, sprintf('Peak=%6.2f W', Peak));

plot(x,y2,'LineWidth',2)
hold on
[Peak, PeakIdx] = max(y2);
text(x(PeakIdx), Peak, sprintf('Max=%6.2f W', Peak));

plot(x,y3,'LineWidth',2)
hold on

colororder({'b','y','g'})

% axis tight
xlabel('time of day (24h)')
ylabel('Power (W)')

yyaxis right
plot(x,y4,'LineWidth',2)
[Peak, PeakIdx] = min(y4);
text(x(PeakIdx), Peak, sprintf('Min=%f', Peak));
ylabel('State of Charge')
colororder({'r'})

% set text properties
set(fig.Children, ...
    'FontName',     'Times New Roman', ...
    'FontSize',     21);

legend('Measured Real Power','Solar Power Output','Battery output','SOC','Location','southoutside','NumColumns',2)
axis on
grid on

% set text properties
set(fig.Children, ...
    'FontName',     'Times New Roman', ...
    'FontSize',     21);

% remove unnecessary white space
t1 = datetime(2019,04,21,0,0,0,'TimeZone','GMT');
t2 = datetime(2019,04,22,0,0,0,'TimeZone','GMT');
tick_locations = t1:hours(1):t2;
set(gca,'XTick',tick_locations);
datetick('x','HH:mm','keeplimits', 'keepticks')
set(gca,'XMinorTick','on','YMinorTick','on')
set(gca,'LooseInset',max(get(gca,'TightInset'), 0.02))
f=gca
% export to png
%fig.PaperPositionMode   = 'auto';
%print([opts.saveFolder 'load_lower'], '-dpng', '-r600');

exportgraphics(f,destFile,'Resolution',1000);
