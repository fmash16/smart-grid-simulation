% define figure properties
opts.Colors     = get(groot,'defaultAxesColorOrder');
opts.saveFolder = '/home/void/thesis/charts/';
%opts.saveFolder = '/home/void/thesis/charts/';
opts.width      = 8;
opts.height     = 6;
opts.fontType   = 'Times';
opts.fontSize   = 10;

% create new figure
fig = figure; clf

% Plot figure
ftoread = '/home/void/thesis/loads/load_all.csv'
%ftoread = '/home//thesis/smart-grid-simulation/final/output/LOAD11_data.csv'
fid=fopen(ftoread)
data=textscan(fid, '%s%s%d%d%d','Delimiter',',','HeaderLines',1)
fclose(fid)

x = datetime(data{2},'InputFormat','HH:mm');
%x = datetime(data{1},'InputFormat','yyyy-MM-dd HH:mm:ss XXX','TimeZone','local','Format','HH:mm:ss');
y = data{4};
plot(x,y,'LineWidth',2)

% add axis labes and legend
% axis tight
xlabel('time of day (24h)')
ylabel('load (W)')
legend('Low Income load','Location','north')

% scaling
% fig.Units               = 'centimeters'
% fig.Position(3)         = opts.width;
% fig.Position(4)         = opts.height;

% set text properties
set(fig.Children, ...
    'FontName',     'Times', ...
    'FontSize',     15);

% remove unnecessary white space
datetick('x','HH:MM')
grid on
set(gca,'LooseInset',max(get(gca,'TightInset'), 0.02))
f=gca
% export to png
fig.PaperPositionMode   = 'auto';
%print([opts.saveFolder 'load_lower'], '-dpng', '-r600');

exportgraphics(f,'/home/void/thesis/charts/load_lower.png','Resolution',600)
