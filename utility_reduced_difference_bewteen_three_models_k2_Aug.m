k2 = [0.1 : 0.01 : 0.2];
%Aug
utility_trad = [9.445302161327328, 10.212118740121499, 10.98323544732111, 11.697400486067142, 12.406630248345405, 13.121692991818552, 13.88624937969346, 14.654975023082976, 15.411516730687778, 16.18439831824954, 16.960907096282124];
utility_rigid = [8.789305210800524, 9.393670842876357, 10.173290370093358, 10.846102919318898, 11.397450767140514, 12.098783191545323, 12.931256987044256, 13.558182136800562, 14.244395250920801, 14.988606612345643, 15.700968785271483];
utility_opti = [7.851655433041307, 8.604123835296958, 9.36930674161729, 10.102859640199135, 10.821915627781083, 11.671429132456588, 12.457609876333754, 13.14946871753565, 13.8729932511946, 14.651243131567476, 15.362589300590134];
total_utility_trad = sum(utility_trad) * 30;
total_utility_rigid = sum(utility_rigid) * 30;
total_utility_opti = sum(utility_opti) * 30;
'The total reduced utility of rigid model over traditional model: '
total_utility_rigid / total_utility_trad
'The total reduced utility of optimized model over traditional model: '
total_utility_opti / total_utility_trad
plot(k2, utility_trad, 'g', 'linewidth', 1.8);
grid on;
%axis([1,12,3,20]);
title('Utility reduced by cost and uncomfortableness with the three models with different k2 in Aug');
xlabel('k2');
ylabel('Daily averaged reduced utility');
hold on;
plot(k2, utility_rigid, 'b', 'linewidth', 1.8);
grid on;
plot(k2, utility_opti, 'r', 'linewidth', 1.8);
grid on;

legend('Traditional model', 'Rigid model', 'Optimized model');
