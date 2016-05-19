t = [1 : 12];
utility_trad = [27.69, 18.27, 11.65, 7.26, 5.50, 9.86, 11.45, 9.44, 6.07, 10.72, 24.27, 29.66];
utility_rigid = [12.44, 8.81, 6.06, 4.88, 5.64, 9.09, 9.91, 8.79, 5.70, 5.92, 11.17, 13.45];
utility_opti = [12.14, 8.42, 5.06, 3.85, 5.20, 8.28, 9.31, 7.85, 4.87, 5.15, 10.65, 13.04];
total_utility_trad = sum(utility_trad) * 30;
total_utility_rigid = sum(utility_rigid) * 30;
total_utility_opti = sum(utility_opti) * 30;
'The total reduced utility of rigid model over traditional model: '
total_utility_rigid / total_utility_trad
'The total reduced utility of optimized model over traditional model: '
total_utility_opti / total_utility_trad
plot(t, utility_trad, 'g', 'linewidth', 1.8);
grid on;
axis([1,12,3,20]);
title('Utility reduced by cost and uncomfortableness with the three models');
xlabel('Month');
ylabel('Daily averaged reduced utility');
hold on;
plot(t, utility_rigid, 'b', 'linewidth', 1.8);
grid on;
plot(t, utility_opti, 'r', 'linewidth', 1.8);
grid on;

legend('Traditional model', 'Rigid model', 'Optimized model');
