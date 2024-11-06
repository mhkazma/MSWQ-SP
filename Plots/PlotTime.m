
% Define cases and observation labels for NET1
cases = {'CS1_MSX1', 'CS1_MSX2', 'CS1_MSX3', 'CS2_MSX1', 'CS3_MSX1'};
observations = {'4 sensors', '6 sensors'};
time_data_det_4 = [];
time_data_det_6 = [];
time_data_trace_4 = [];
time_data_trace_6 = [];

% Loop through each case
for i = 1:length(cases)
    case_name = cases{i};

    % Access the time data for LogDet and Trace
    time_det = results.(sprintf('time_det_%s', case_name));
    time_trace = results_trace.(sprintf('time_trace_%s', case_name));

    % Concatenate the time data for 4 and 6 sensors separately
    time_data_det_4 = [time_data_det_4, cell2mat(time_det(1, :))];
    time_data_det_6 = [time_data_det_6, cell2mat(time_det(2, :))];
    time_data_trace_4 = [time_data_trace_4, cell2mat(time_trace(1, :))];
    time_data_trace_6 = [time_data_trace_6, cell2mat(time_trace(2, :))];
end

% Prepare data for box plots
time_data_det = [time_data_det_4(:), time_data_det_6(:)];
time_data_trace = [time_data_trace_4(:), time_data_trace_6(:)];


%% For NET2
% Define observations for 12 and 18 sensors
observations_net2 = {'12 sensors', '18 sensors'};
time_data_det_12 = [];
time_data_det_18 = [];
time_data_trace_12 = [];
time_data_trace_18 = [];

% Only consider the case CS2_MSX1 for NET2
case_name = 'CS2';

% Access the time data for LogDet and Trace
time_det = results.(sprintf('time_det_%s', case_name));
time_trace = results_trace.(sprintf('time_trace_%s', case_name));

% Concatenate the time data for 12 and 18 sensors separately
time_data_det_12 = cell2mat(time_det(1, :));  % Row 1 for 12 sensors
time_data_det_18 = cell2mat(time_det(2, :));  % Row 2 for 18 sensors
time_data_trace_12 = cell2mat(time_trace(1, :));  % Row 1 for 12 sensors
time_data_trace_18 = cell2mat(time_trace(2, :));  % Row 2 for 18 sensors

% Prepare data for box plots
time_data_det_net2 = [time_data_det_12(:), time_data_det_18(:)];
time_data_trace_net2 = [time_data_trace_12(:), time_data_trace_18(:)];

%%

% Define font sizes and other settings
sys.fs1 = 10; 
sys.fs2 = 12;

% Create the figure with 1 row and 2 columns
figure('Position', [300 100 430 230]);  % Increased width to accommodate two subplots

% First subplot for NET1
subplot(1, 2, 1);  % Set the first subplot
set(gca, 'Position', [0.01, 0.2, 0.45, 0.7]); % Adjust as needed
hold on;

% Define custom colors
logdet_color = [0.2 0.6 0.8];  % Light blue for LogDet
trace_color = [0.8 0.4 0.4];   % Light red for Trace

% Define secondary colors with light green and light yellow
logdet_color2 = [0.6 0.8 0.5]; % Light green
trace_color2 = [0.9 0.9 0.5];  % Light yellow

% Adjust positions for each sensor count and type to avoid overlap
positions_det = (1:numel(observations)) - 0.2;  % Shift LogDet slightly left
positions_trace = (1:numel(observations)) + 0.2; % Shift Trace slightly right

% Plot LogDet Optimization Time with adjusted positions
b1 = boxplot(time_data_det, 'Positions', positions_det, 'Labels', [], ...
    'Widths', 0.3, 'Colors', logdet_color, 'Symbol', '');
set(b1, 'LineWidth', 1.5); % Thicker line for visibility

% Plot Trace Optimization Time with adjusted positions
b2 = boxplot(time_data_trace, 'Positions', positions_trace, 'Labels', [], ...
    'Widths', 0.3, 'Colors', trace_color, 'Symbol', '');
set(b2, 'LineWidth', 1.5); % Thicker line for visibility

% Calculate mid positions between LogDet and Trace for custom x-tick labels
mid_positions = (positions_det + positions_trace) / 2;

% Set y-axis label and title for NET1
ylabel('Time (sec)', 'FontSize', sys.fs2, 'Interpreter', 'latex', 'FontName', 'Times New Roman');
title('(a) Net1', 'FontSize', sys.fs2, 'Interpreter', 'latex', 'FontName', 'Times New Roman');
set(gca, 'FontSize', sys.fs1, 'YGrid', 'on', 'XGrid', 'off');  % Enable only Y grid

% Set custom x-ticks and labels at the mid positions
set(gca, 'XTick', mid_positions, 'XTickLabel', observations);

% Set custom x-axis limits to avoid starting from zero
xlim([0.5, numel(observations) + 0.5]);  % Adjust based on the number of observations
ylim([2 9])

% Customize box colors for each plot (LogDet and Trace)
h1 = findobj(gca, 'Tag', 'Box');
for j = 1:length(h1)
    if mod(j, 2) == 1
        % Set color for LogDet
        patch(get(h1(j), 'XData'), get(h1(j), 'YData'), logdet_color2, 'FaceAlpha', .5);
    else
        % Set color for Trace
        patch(get(h1(j), 'XData'), get(h1(j), 'YData'), trace_color2, 'FaceAlpha', .5);
    end
end

% Add a custom legend with sample color boxes for LogDet and Trace
h_det = plot(NaN, NaN, 's', 'MarkerSize', 10, 'MarkerFaceColor', logdet_color, 'MarkerEdgeColor', logdet_color);
h_trace = plot(NaN, NaN, 's', 'MarkerSize', 10, 'MarkerFaceColor', trace_color, 'MarkerEdgeColor', trace_color);
legend([h_det, h_trace], {'Logdet', 'Trace'}, 'Interpreter', 'latex', 'FontSize', sys.fs1, 'Location', 'northwest');

% Box for NET1
box on;
hold off;

% Second subplot for NET2
subplot(1, 2, 2);  % Set the second subplot
set(gca, 'Position', [0.52, 0.2, 0.45, 0.7]); % Adjust as needed
hold on;

% Define NET2 observation labels
observations_net2 = {'12 sensors', '18 sensors'};

% Adjust positions for NET2 data
positions_det_net2 = (1:numel(observations_net2)) - 0.2;
positions_trace_net2 = (1:numel(observations_net2)) + 0.2;

% Plot LogDet Optimization Time with adjusted positions
b3 = boxplot(time_data_det_net2, 'Positions', positions_det_net2, 'Labels', [], ...
    'Widths', 0.3, 'Colors', logdet_color, 'Symbol', '');
set(b3, 'LineWidth', 1.5);

b4 = boxplot(time_data_trace_net2, 'Positions', positions_trace_net2, 'Labels', [], ...
    'Widths', 0.3, 'Colors', trace_color, 'Symbol', '');
set(b4, 'LineWidth', 1.5);

% Calculate mid positions and set x-tick labels for NET2
mid_positions_net2 = (positions_det_net2 + positions_trace_net2) / 2;
set(gca, 'XTick', mid_positions_net2, 'XTickLabel', observations_net2);

% Set y-axis label and title for NET2
title('(b) Net2', 'FontSize', sys.fs2, 'Interpreter', 'latex', 'FontName', 'Times New Roman');
ylabel('Time (sec)', 'FontSize', sys.fs2, 'Interpreter', 'latex', 'FontName', 'Times New Roman');
set(gca, 'FontSize', sys.fs1, 'YGrid', 'on', 'XGrid', 'off');  % Enable only Y grid
xlim([0.5, numel(observations_net2) + 0.5]);
ylim([30 95])
% Customize box colors for each plot (LogDet and Trace) in NET2 subplot
h2 = findobj(gca, 'Tag', 'Box');
for j = 1:length(h2)
    if mod(j, 2) == 1
        patch(get(h2(j), 'XData'), get(h2(j), 'YData'), logdet_color2, 'FaceAlpha', .5);
    else
        patch(get(h2(j), 'XData'), get(h2(j), 'YData'), trace_color2, 'FaceAlpha', .5);
    end
end

box on;
hold off;

% Save as EPS
 print('Optimization-Time-NET1_NET2', '-depsc2', '-r600');
% To save a tightly cropped image
%exportgraphics(gcf, 'Optimization-Time-NET1_NET2.eps', 'ContentType', 'vector', 'Resolution', 600, 'BackgroundColor', 'none');

 
 %% Analysis of the time NET1
% % Sample data vector
% data_4 = time_data_det(:,1);
% 
% % Calculate statistics
% mean_val = mean(data_4);             % Mean
% median_val = median(data_4);         % Median
% min_val = min(data_4);               % Minimum
% max_val = max(data_4);               % Maximum
% percentile_25 = prctile(data_4, 25); % 25th percentile (Q1)
% percentile_75 = prctile(data_4, 75); % 75th percentile (Q3)
% iqr_val = iqr(data_4);               % Interquartile range
% std_dev = std(data_4);               % Standard deviation
% 
% % Display the results
% fprintf('Mean: %.2f\n', mean_val);
% fprintf('Median: %.2f\n', median_val);
% fprintf('Min: %.2f\n', min_val);
% fprintf('Max: %.2f\n', max_val);
% fprintf('25th Percentile (Q1): %.2f\n', percentile_25);
% fprintf('75th Percentile (Q3): %.2f\n', percentile_75);
% fprintf('Interquartile Range (IQR): %.2f\n', iqr_val);
% fprintf('Standard Deviation: %.2f\n', std_dev);
% 
% %% Sample data vector
% data_6 = time_data_det(:,2);
% 
% % Calculate statistics
% mean_val = mean(data_6);             % Mean
% median_val = median(data_6);         % Median
% min_val = min(data_6);               % Minimum
% max_val = max(data_6);               % Maximum
% percentile_25 = prctile(data_6, 25); % 25th percentile (Q1)
% percentile_75 = prctile(data_6, 75); % 75th percentile (Q3)
% iqr_val = iqr(data_6);               % Interquartile range
% std_dev = std(data_6);               % Standard deviation
% 
% % Display the results
% fprintf('Mean: %.2f\n', mean_val);
% fprintf('Median: %.2f\n', median_val);
% fprintf('Min: %.2f\n', min_val);
% fprintf('Max: %.2f\n', max_val);
% fprintf('25th Percentile (Q1): %.2f\n', percentile_25);
% fprintf('75th Percentile (Q3): %.2f\n', percentile_75);
% fprintf('Interquartile Range (IQR): %.2f\n', iqr_val);
% fprintf('Standard Deviation: %.2f\n', std_dev);
% 
% 
% %% Analysis of the time NET1
% % Sample data vector
% data_4_trace = time_data_trace(:,1);
% 
% % Calculate statistics
% mean_val = mean(data_4_trace);             % Mean
% median_val = median(data_4_trace);         % Median
% min_val = min(data_4_trace);               % Minimum
% max_val = max(data_4_trace);               % Maximum
% percentile_25 = prctile(data_4_trace, 25); % 25th percentile (Q1)
% percentile_75 = prctile(data_4_trace, 75); % 75th percentile (Q3)
% iqr_val = iqr(data_4_trace);               % Interquartile range
% std_dev = std(data_4_trace);               % Standard deviation
% 
% % Display the results
% fprintf('Mean: %.2f\n', mean_val);
% fprintf('Median: %.2f\n', median_val);
% fprintf('Min: %.2f\n', min_val);
% fprintf('Max: %.2f\n', max_val);
% fprintf('25th Percentile (Q1): %.2f\n', percentile_25);
% fprintf('75th Percentile (Q3): %.2f\n', percentile_75);
% fprintf('Interquartile Range (IQR): %.2f\n', iqr_val);
% fprintf('Standard Deviation: %.2f\n', std_dev);
% 
% %% Sample data vector
% data_6_trace = time_data_trace(:,2);
% 
% % Calculate statistics
% mean_val = mean(data_6_trace);             % Mean
% median_val = median(data_6_trace);         % Median
% min_val = min(data_6_trace);               % Minimum
% max_val = max(data_6_trace);               % Maximum
% percentile_25 = prctile(data_6_trace, 25); % 25th percentile (Q1)
% percentile_75 = prctile(data_6_trace, 75); % 75th percentile (Q3)
% iqr_val = iqr(data_6_trace);               % Interquartile range
% std_dev = std(data_6_trace);               % Standard deviation
% 
% % Display the results
% fprintf('Mean: %.2f\n', mean_val);
% fprintf('Median: %.2f\n', median_val);
% fprintf('Min: %.2f\n', min_val);
% fprintf('Max: %.2f\n', max_val);
% fprintf('25th Percentile (Q1): %.2f\n', percentile_25);
% fprintf('75th Percentile (Q3): %.2f\n', percentile_75);
% fprintf('Interquartile Range (IQR): %.2f\n', iqr_val);
% fprintf('Standard Deviation: %.2f\n', std_dev);


%% Analysis of the time NET1
% Sample data vector
data_12 = time_data_det_12(:,1);

% Calculate statistics
mean_val = mean(data_12);             % Mean
median_val = median(data_12);         % Median
min_val = min(data_12);               % Minimum
max_val = max(data_12);               % Maximum
percentile_25 = prctile(data_12, 25); % 25th percentile (Q1)
percentile_75 = prctile(data_12, 75); % 75th percentile (Q3)
iqr_val = iqr(data_12);               % Interquartile range
std_dev = std(data_12);               % Standard deviation

% Display the results
fprintf('Mean: %.2f\n', mean_val);
fprintf('Median: %.2f\n', median_val);
fprintf('Min: %.2f\n', min_val);
fprintf('Max: %.2f\n', max_val);
fprintf('25th Percentile (Q1): %.2f\n', percentile_25);
fprintf('75th Percentile (Q3): %.2f\n', percentile_75);
fprintf('Interquartile Range (IQR): %.2f\n', iqr_val);
fprintf('Standard Deviation: %.2f\n', std_dev);

%% Sample data vector
data_18 = time_data_det_18(:,2);

% Calculate statistics
mean_val = mean(data_18);             % Mean
median_val = median(data_18);         % Median
min_val = min(data_18);               % Minimum
max_val = max(data_18);               % Maximum
percentile_25 = prctile(data_18, 25); % 25th percentile (Q1)
percentile_75 = prctile(data_18, 75); % 75th percentile (Q3)
iqr_val = iqr(data_18);               % Interquartile range
std_dev = std(data_18);               % Standard deviation

% Display the results
fprintf('Mean: %.2f\n', mean_val);
fprintf('Median: %.2f\n', median_val);
fprintf('Min: %.2f\n', min_val);
fprintf('Max: %.2f\n', max_val);
fprintf('25th Percentile (Q1): %.2f\n', percentile_25);
fprintf('75th Percentile (Q3): %.2f\n', percentile_75);
fprintf('Interquartile Range (IQR): %.2f\n', iqr_val);
fprintf('Standard Deviation: %.2f\n', std_dev);


%% Analysis of the time NET1
% Sample data vector
data_4_trace_12 = time_data_trace_12(:,1);

% Calculate statistics
mean_val = mean(data_4_trace_12);             % Mean
median_val = median(data_4_trace_12);         % Median
min_val = min(data_4_trace_12);               % Minimum
max_val = max(data_4_trace_12);               % Maximum
percentile_25 = prctile(data_4_trace_12, 25); % 25th percentile (Q1)
percentile_75 = prctile(data_4_trace_12, 75); % 75th percentile (Q3)
iqr_val = iqr(data_4_trace_12);               % Interquartile range
std_dev = std(data_4_trace_12);               % Standard deviation

% Display the results
fprintf('Mean: %.2f\n', mean_val);
fprintf('Median: %.2f\n', median_val);
fprintf('Min: %.2f\n', min_val);
fprintf('Max: %.2f\n', max_val);
fprintf('25th Percentile (Q1): %.2f\n', percentile_25);
fprintf('75th Percentile (Q3): %.2f\n', percentile_75);
fprintf('Interquartile Range (IQR): %.2f\n', iqr_val);
fprintf('Standard Deviation: %.2f\n', std_dev);

%% Sample data vector
data_6_trace_18 = time_data_trace_18(:,2);

% Calculate statistics
mean_val = mean(data_6_trace_18);             % Mean
median_val = median(data_6_trace_18);         % Median
min_val = min(data_6_trace_18);               % Minimum
max_val = max(data_6_trace_18);               % Maximum
percentile_25 = prctile(data_6_trace_18, 25); % 25th percentile (Q1)
percentile_75 = prctile(data_6_trace_18, 75); % 75th percentile (Q3)
iqr_val = iqr(data_6_trace_18);               % Interquartile range
std_dev = std(data_6_trace_18);               % Standard deviation

% Display the results
fprintf('Mean: %.2f\n', mean_val);
fprintf('Median: %.2f\n', median_val);
fprintf('Min: %.2f\n', min_val);
fprintf('Max: %.2f\n', max_val);
fprintf('25th Percentile (Q1): %.2f\n', percentile_25);
fprintf('75th Percentile (Q3): %.2f\n', percentile_75);
fprintf('Interquartile Range (IQR): %.2f\n', iqr_val);
fprintf('Standard Deviation: %.2f\n', std_dev);