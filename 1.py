import scipy.stats as stats

# Данные выборки
x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]

# Применение критерия Манна-Уитни
u_stat, p_value = stats.mannwhitneyu(x1, y1, alternative='two-sided')

print(f"Mann-Whitney U test: U-statistic = {u_stat}, p-value = {p_value}")

# Вывод
alpha = 0.05
if p_value < alpha:
    print("Отвергаем нулевую гипотезу: Есть статистически значимые различия между выборками.")
else:
    print("Не отвергаем нулевую гипотезу: Нет статистически значимых различий между выборками.")
