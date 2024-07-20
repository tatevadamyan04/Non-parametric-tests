#Мы будем использовать критерий Вилкоксона для связанных выборок.
from scipy import stats

# Данные измерений
before = [150, 160, 165, 145, 155]
after_10min = [140, 155, 150, 130, 135]

wilcoxon_stat, p_value = stats.wilcoxon(before, after_10min)

print(f"Wilcoxon test: Statistic = {wilcoxon_stat}, p-value = {p_value}")

# Вывод
alpha = 0.05
if p_value < alpha:
    print("Отвергаем нулевую гипотезу: Есть статистически значимые различия между первым и вторым измерениями.")
else:
    print("Не отвергаем нулевую гипотезу: Нет статистически значимых различий между первым и вторым измерениями.")