import USdata

density = {}
list_population = []
list_area = []

for i in USdata.population:
    list_population.append(USdata.population[i])

for i in USdata.area:
    list_area.append(USdata.area[i])

## 人口密度の計算
density_value = [x / y for (x, y) in zip(list_population, list_area)]

## dict(density)にkey(州名)とvalue(人口密度)を入れる
for index, country in enumerate(USdata.population):
    for j in range(len(density_value)):
        if index == j:
            density[country] = density_value[j]

## 州名の入力
country_input = input('州を英字で入力してください: ')
## 人口密度の出力
print(density[country_input])