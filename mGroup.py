import pandas as pd
from IPython.display import display
from pandas.core.reshape.pivot import pivot_table

# Что такое группировка данных

fb = pd.read_csv('./file/data_sf.csv')

s = fb.Nationality.value_counts()

display(s)
print('=================')
display(s.index)
print('=================')
display(s.index[0])
print('=================')
display(len(s.index))
print('=================')
display('Россия',s['Russia'])
print('=================')
display(fb[fb.Nationality == 'Russia'].Club)
print('=================')
display(s.loc[s>11])
print('=================')
print(fb.Club.value_counts())
print('=================')
display(fb.Nationality.value_counts(normalize=True))
print('=================')
display(f'''{round(fb.Nationality.value_counts(normalize=True).Russia
        * 100,2)}%''')
print('=================')
s = fb.Position.value_counts(normalize=True)
display('''Данные об игроках каких позиций (Position) занимают более
        10% датасета?\n''',
        s.loc[s>0.1])
print('=================')
display('''Данные об игроках каких позиций (Position) занимают
        менее 1% датасета?\n''',
        fb.Position.value_counts(normalize=True)
        .loc[fb.Position.value_counts(normalize=True)<0.01])
print('=================')
display(fb.Age.value_counts())
print('=================')
display(fb.Wage.value_counts())
print('=================')
display(fb.Wage.value_counts(bins=4))
print('=================')
s = fb.Wage.value_counts(bins=4)
display(fb.loc[(fb.Wage > s.index[3].left) & (fb.Wage <= s.index[3].right)])

print('=================')
small_fb = fb[fb.columns[0:7]].head(25)
s = small_fb.Wage.value_counts(bins=4)
display(s)
s.index
s.index[3]
print('=================')
display(s.index[3].left)
print('=================')
display(s.index[3].right)
print('=================')
small_fb.Wage > s.index[3].left
display(small_fb.loc[(small_fb.Wage > s.index[3].left) & (small_fb.Wage <= s.index[3].right)])

print('=================')

print('''В какие пределах находятся худшие 20% процентов показателей точности
        ударов ногой\n''',fb.FKAccuracy.value_counts(bins=5))

print('=================')

print('''Какие показатели точности ударов ногой демонстрирует большинство
        футболистов\n''',fb.FKAccuracy.value_counts(normalize=True))

# Фукнкци unique и nunique и преобразование серии value_counts в датафрейм

print('=================')
s = small_fb.Nationality.value_counts()
print(s.index)
print(len(s.index))


# Список уникальных элементов из серии

print('=================')
display(small_fb.Nationality.unique())

# Подсчет количества уникальных значений

print('=================')
display(len(small_fb.Nationality.unique()))
print('=================')
display(small_fb.Nationality.nunique())
print('=================')
display(small_fb.Nationality.count())
print('=================---///')
display(len(small_fb.Nationality.value_counts()))


# Преобразование серии value_counts в датафрейм

print('=================---///')

s = small_fb.Nationality.value_counts()
s_fb = s.reset_index()
display(s_fb)

print('=================---///')

# переименование столбцов дата фрейма

s_fb.columns = ['Страна', 'Количество игроков']
display(s_fb)

print('=================---///')

display('''Процент испанских футболистов зарплата находится
        впределах 25% минимума от наблюдаемого уровня зарпалат среди
        испанских игроков\n''',
        round(fb[fb.Nationality
                == 'Spain'].Wage.value_counts(bins=4, normalize=True) * 100))

print('=================---///')

display('''Количество национальностей, к которым относятся футболисты,
        выступающие за клуб Manchester United - ''',
        fb[fb.Club == 'Manchester United'].Nationality.nunique())

print('=================---///')

display('''Два футболиста из Бразилии, выступающие за клуб Ювентус\n''',
        fb[(fb.Nationality == 'Brazil') & (fb.Club == 'Juventus')].Name.unique())

print('=================---///')

clubCount = fb[fb.Age > 35].Club.value_counts().reset_index()
clubCount.columns = ['Клуб','Кол.игроков']

display('''Какой из клубов насчитывает большее количество футболистов возрастом
        старше 35 лет - \n''',clubCount)

print('=================---///')
display('''Разбить всех футболистов родом из Аргентины на 4 равные группы
        по возрасту\n''',
        fb[fb.Nationality == 'Argentina'].Age.value_counts(bins=4))


print('=================---///')
ageSpain = fb[(fb.Nationality == 'Spain')].Age.value_counts(normalize=True).reset_index()
ageSpain.columns = ['Возраст', 'Процент']
display('''Процент футболистов из Испании которые имею возраст 21 год\n''',
        ageSpain)

print('=================---------')

# Функция groupby

print(fb.groupby('Club'))

print('=================---------')

#display(fb.groupby(['Club']).groups)

grouped_fb = fb.groupby(['Club']).Wage.sum()
display(grouped_fb)

print('=================---------')

display(grouped_fb.loc['Ajax'])

print('=================---------')

#display(grouped_fb.loc['Ajax'].Wage)

grouped_fb = fb.groupby(['Club']).Wage.sum().sort_values(ascending=False)
print(grouped_fb.head(5).max())

print('=================---------')

# Задание

groupPosition = fb.groupby(['Position']).Wage.sum()
display(groupPosition.sort_values(ascending=False))

print('=================---------')


display(fb.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean())

print('=================---------')

display(fb.groupby(['Nationality'])[['Wage','Age','ShotPower']]
        .mean()
        .sort_values(['Wage'],ascending=False)
        .head(10))

print('=================---------')

display(fb.loc[fb.Nationality == 'Dominican Republic'][['Name','Club','Wage','Age','ShotPower']])

print('=================---------')

display(fb.groupby(['Position'])[['Wage','Value']]
        .mean()
        .sort_values(['Value','Wage'],ascending=False)
        .head(5))

print('Функция nunique - =================---------')

display(fb.groupby(['Nationality'])[['Club','Name']].nunique())

display()
print('Функция count - =================---------')

display(fb.groupby(['Club']).Name.count())

display()
print('Функция median - =================---------')

display(fb.groupby(['Club']).Dribbling.median())

display()
print('Функция max - =================---------')

display(fb.groupby(['Club']).Strength.max().sort_values(ascending=True))

display()
print('Функция min - =================---------')
display()

display(fb.groupby(['Club']).Balance.min())


# Задание

display()
print('Задание - =================---------')
display()

display('''Подсчитать среднюю и медианную зарплату футболистов из разных
        клубов.В скольких клубах средняя и медианная зарплаты
        совпадают?\n''',
        fb.groupby(['Club']).Wage.agg(['mean','median'])
                [fb.groupby(['Club']).Wage.mean()
                        == fb.groupby(['Club']).Wage.median()].count())

display()
print('Задание - =================---------')
display()

display('''Каков максимальный размер средней зарплаты в этой группе
        клубов\n''',
        fb.groupby(['Club']).Wage
                .agg(['mean','median'])[fb.groupby(['Club']).Wage.mean()
                        == fb.groupby(['Club']).Wage.median()].max())

display()
print('Задание - =================---------')
display()

display('''Как называется клуб, где игроки получают такую зарплату\n''',
        fb.groupby(['Club']).Wage
                .agg(['mean', 'median'])
                        [fb.groupby(['Club']).Wage.mean()
                                == fb.groupby(['Club']).Wage.median()]
                                        .sort_values(
                                                ['mean','median'],
                                                ascending=False).head(1))


display()
print('Задача 1 =================')
display()

display('''С помощью функции groupby посчитать сумму зарплат футболистов клуба
        "Chelsea"\n''',
        fb[fb.Club == 'Chelsea'].groupby(['Club']).Wage.agg(['sum']))

display()
print('Задача 2 =================')
display()

display('''Определить максимальную зарплату футболиста национальности
        Аргентина в возрасте 20 лет''',
        fb[(fb.Nationality=='Argentina') & (fb.Age == 20)].Wage.max())

display()
print('Задача 3 =================')
display()

display('''Определить максимальную зарплату футболиста национальности
        Аргентина в возрасте 30 лет''',
        fb[(fb.Nationality == 'Argentina') & (fb.Age == 30)].Wage.max())

display()
print('Задача 4 =================')
display()

display('''Определить минимальную зарплату футболиста национальности
        Аргентина в возрасте 30 лет''',
        fb[(fb.Nationality == 'Argentina') & (fb.Age == 30)].Wage.min())

display()
print('Задача 4 =================')
display()

display('''Определить максимальную силу и баланс среди игроков клуба
        "FC Barcelona" из Аргентины\n''',
        fb[(fb.Club == 'FC Barcelona') & (fb.Nationality == 'Argentina')]
                [['Strength','Balance']].max())

# Функция pivot_table

pivot = fb.loc[fb.Club
                .isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(values=['Wage'],index=['Nationality'],columns=['Club'],aggfunc='sum')
display(pivot)