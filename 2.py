# Мы используем критерий Фридмана для связанных выборок.

from scipy import stats

# Данные измерений
before = [150, 160, 165, 145, 155]
after_10min = [140, 155, 150, 130, 135]
after_30min = [130, 130, 120, 130, 125]

# Применение критерия Фридмана
friedman_stat, p_value = stats.friedmanchisquare(before, after_10min, after_30min)

print(f"Friedman test: Statistic = {friedman_stat}, p-value = {p_value}")

# Вывод
alpha = 0.05
if p_value < alpha:
    print("Отвергаем нулевую гипотезу: Есть статистически значимые различия между измерениями.")
else:
    print("Не отвергаем нулевую гипотезу: Нет статистически значимых различий между измерениями.")
