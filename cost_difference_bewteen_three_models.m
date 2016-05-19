t = [1 : 12];
cost_trad = [14.32, 10.18, 6.87, 5.18, 4.84, 8.48, 9.57, 8.14, 5.26, 6.49, 12.82, 15.22];
cost_rigid = [10.05, 6.16, 3.44, 3.00, 4.04, 6.96, 7.75, 6.58, 3.44, 3.47, 8.59, 10.82];
cost_opti = [10.12, 6.24, 3.64, 2.98, 4.14, 6.99, 7.80, 6.58, 3.62, 3.58, 8.84, 10.94];
total_cost_trad = sum(cost_trad) * 30;
total_cost_rigid = sum(cost_rigid) * 30;
total_cost_opti = sum(cost_opti) * 30;
'The total cost of rigid model over traditional model: '
total_cost_rigid / total_cost_trad
'The total cost of optimized model over traditional model: '
total_cost_opti / total_cost_trad
plot(t, cost_trad, 'g', 'linewidth', 1.8);
grid on;
axis([1,12,2,15]);
title('Cost with the three models');
xlabel('Month');
ylabel('Daily averaged cost');
hold on;
plot(t, cost_rigid, 'b', 'linewidth', 1.8);
grid on;
plot(t, cost_opti, 'r', 'linewidth', 1.8);
grid on;

legend('Traditional model', 'Rigid model', 'Optimized model');
