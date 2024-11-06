%Script to plot all the hydraulic patterns used in JEM-WQSP paper
%by: Mohamad H. Kazma 
%date: November 1,2025

%% Clear data files
clear 
clc

%% Specify network choices
%Choose network
%for 3 node network set = 1 (Three-node Network)
%Network = 1;
%for 11 node network set = 2 (Net1)
Network = 2;
%for large node network set = 3 (Net2)
%Network = 3; 

%% load inputs inputs
if Network == 1
    load("3N_Dy_obswater.mat","nN","JunctionIndex","ReservoirIndex" ...
        ,"TankIndex")
    load("3N_Dy_Observability.mat");
elseif Network == 2
    load("Net1_Dy_obswater.mat","nN","JunctionIndex","ReservoirIndex" ...
        ,"TankIndex")
    % Load data from the first file and rename variables
    data1 = load("Net1_Dy_Observability_CS1_MSX1.mat", "BaseDemand", "PatternVal");
    BaseDemand_CS1 = data1.BaseDemand;
    PatternVal_CS1 = data1.PatternVal;
    % Load data from the second file and rename variables
    data2 = load("Net1_Dy_Observability_CS2_MSX1.mat", "BaseDemand", "PatternVal");
    BaseDemand_CS2 = data2.BaseDemand;
    PatternVal_CS2 = data2.PatternVal;
    % Load data from the third file and rename variables
    data3 = load("Net1_Dy_Observability_CS3_MSX1.mat", "BaseDemand");
    data3_2 = load("Net1_Dy_Observability_CS3_Pattern.mat", "PatternVal");
    BaseDemand_CS3 = data3.BaseDemand;
    PatternVal_CS3 = data3_2.PatternVal;
elseif Network == 3
    load("Net2_Dy_Observability_CS1.mat");
    % load("Net1_Dy_obswater.mat","nN","JunctionIndex","ReservoirIndex" ...
    %     ,"TankIndex")
end

%% Plotting BaseDemand
sys.fs1 = 14; 
sys.fs2 = 20;
% Example plot for BaseDemand from each file
h(1) = figure;
% Plot grouped bars
b = bar(JunctionIndex, [BaseDemand_CS1; BaseDemand_CS2; BaseDemand_CS3]', ...
    'grouped', 'BarWidth', 1);

% Set custom colors for each bar series
b(1).FaceColor = [0.2, 0.6, 0.8];  % Color for BaseDemand_CS1 (light blue)
b(2).FaceColor = [0.8, 0.4, 0.4];  % Color for BaseDemand_CS2 (light red)
b(3).FaceColor = [0.4, 0.7, 0.4];  % Color for BaseDemand_CS3 (light green)

% Set axes properties
ax01 = gca;
box on
grid off
set(ax01,'FontSize',sys.fs1);
ax01.YAxis.LineWidth = 0.8;
ax01.XAxis.LineWidth = 0.8;
ax01.TickLength = [0.03, 0.03];

% Set figure position and sizeand c
ax1 = h(1);
set(h(1), 'Position', [300 100 720 230]);

text(0.05, 0.9, '(a) Net1', ...
     'FontSize', sys.fs2, 'Interpreter', 'latex', 'FontName', 'Times New Roman', ...
     'Units', 'normalized');

% Add labels and legend
ylabel('Base Demand (GPM)', 'interpreter','latex','FontName','Times New Roman','FontSize',sys.fs2);
xlabel('Junction Index', 'interpreter','latex','FontName','Times New Roman','FontSize',sys.fs2);

leg1 = legend({'Base Demand $1$', 'Base Demand $2$', 'Base Demand $3$'});
set(leg1,'Interpreter','latex');
set(leg1,'FontSize',sys.fs2);

% adjust legend position
rect1 = [0.64, 0.76, .2, .2];
leg1.ItemTokenSize(1) = 17;
 
print('Base-Demand-NET1','-depsc2','-r600')


%% Plotting PatternVal over time (1 to 24 hours)
sys.fs1 = 14; 
sys.fs2 = 18;

% Define time range (1 to 24 hours)
time = 1:24;

% Create a new figure
h(2) = figure;

% Plot line graphs with markers for each series
stairs(time, PatternVal_CS1, 'LineWidth', 3,'Color', [0.2, 0.6, 0.8]);  % PatternVal CS1 (light blue)
hold on;
stairs(time, PatternVal_CS2, 'LineWidth', 3,'LineStyle','-.','Color', [0.8, 0.4, 0.4]);  % PatternVal CS2 (light red)
stairs(time, PatternVal_CS3, 'LineWidth', 3,'LineStyle',':','Color', [0.4, 0.7, 0.4]);  % PatternVal CS3 (light green)
hold off;

% Set axes properties
ax02 = gca;
box on;
grid off;
set(ax02, 'FontSize', sys.fs1);
ax02.YAxis.LineWidth = 0.8;
ax02.XAxis.LineWidth = 0.8;
ax02.TickLength = [0.01, 0.01];

% Set x-axis ticks every 6 hours and limit x-axis range from 1 to 24
% set(ax02, 'XTick', 1:6:24);
set(ax02, 'XLim', [1 24]);

% Set figure position and size
set(h(2), 'Position', [300 100 720 230]);

text(0.85, 0.9, '(b) Net1', ...
     'FontSize', sys.fs2, 'Interpreter', 'latex', 'FontName', 'Times New Roman', ...
     'Units', 'normalized');

% Add labels and legend
ylabel('Pattern', 'Interpreter', 'latex', 'FontName', 'Times New Roman', 'FontSize', sys.fs2);
xlabel('Time (hr)', 'Interpreter', 'latex', 'FontName', 'Times New Roman', 'FontSize', sys.fs2);

% Create a legend
leg2 = legend({'Pattern $1$', 'Pattern $2$', 'Pattern $3$'});
set(leg2, 'Interpreter', 'latex');
set(leg2, 'FontSize', sys.fs2);

% Adjust legend position
rect2 = [0.15, 0.65, .2, .2];
set(leg2, 'Position', rect2);
leg2.ItemTokenSize(1) = 17;

% % Save the plot as an EPS file with high resolution
print('PatternVal-NET1', '-depsc2', '-r600');