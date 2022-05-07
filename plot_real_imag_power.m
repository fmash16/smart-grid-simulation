% define figure properties
opts.Colors     = get(groot,'defaultAxesColorOrder');
opts.saveFolder = '/home/void/thesis/charts/';
%opts.saveFolder = '/home/void/thesis/charts/';
opts.width      = 8;
opts.height     = 6;
opts.fontType   = 'Times New Roman';
opts.fontSize   = 10;
destFile        = "/home/void/thesis/charts/load50_real_imag_power.png"
ftoread = '/home/void/thesis/smart-grid-simulation/final/output/LOAD50_data.csv'

% create new figure
fig = figure; clf

% Plot figure
%ftoread = '/home/void/thesis/loads/load_all.csv'


fid=fopen(ftoread)
%data=textscan(fid, '%s%s%d%d%d','Delimiter',',','HeaderLines',1)
data=textscan(fid, '%s%f%f%f%f%f%f%f%f%f','Delimiter',',','HeaderLines',8)
fclose(fid)

%x = datetime(data{2},'InputFormat','HH:mm');
x = datetime(data{1},'InputFormat','yyyy-MM-dd HH:mm:ss XXX','TimeZone','GMT','Format','HH:mm:ss');
y1 = data{3};
y2 = data{4};
%y=sqrt(y1.^2+y2.^2)
%plot(x,y0,'LineWidth',2)
%hold on
plot(x,y1,'LineWidth',2)
hold on
plot(x,y2,'LineWidth',2)

% axis tight
xlabel('time of day (24h)')
ylabel('Power (W)')
%legend('Demand','Solar Power Output','Battery Output','north')
legend('Measured Real Power','Measured Imaginary Power','Location','north')
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
