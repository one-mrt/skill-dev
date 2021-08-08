from IPython.core.display import display_pdf
import pandas as pd
import math as mt
from IPython.display import display


# DataFrame

display('====== DataFrame =====')
df = pd.DataFrame({'col1':[1,2],'col2':[3,4]})
display(df)

display('===========')
df = pd.DataFrame([[1,2,3],[2,3,4]],
            columns=['foo','bar','baz'],
            index=['foobar','foobaz']
            )
display(df)

print('===========')

dataFrame = pd.read_csv('X:/10-GitProject/skill-dev/file/data_sf.csv', sep=',')

# Методы head() и tail()
print()
print('==== head() - Показывает первые строки ===')
print()
football = pd.read_csv('./file/data_sf.csv')
display(football.head())

print()
print('=== tail() - показывает последние строки')
print()

display(football.tail())

print()
print('===== info() - получени более детальной информации о колонках')
print()

display(football.info(verbose=True,memory_usage='deep'))

print()
print('===== Получение информации о датафрейме: describe')
print()

display(football.describe())

print('==========')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(football.describe(include=['object']))


# Индексация и извлечение данных: статистические методы

print('===== Индексация и извлечение данных: статистические методы ====')
print()

df = pd.DataFrame(
                [[i,i+1.2,i+2,'hi'] for i in range(10)],
                columns=['foo','bar','baz','foobar']
            )

display(df.mean())

print('=======')
display('Средний возраст',football.Age.mean())
display('Стандартно отклонение',football.Age.std())
display(football.Composure)
display('Стандартное отклонение коротких пасов', football.ShortPassing.std())
display('Сумма заработных плат за год',football.Wage.sum())
display('Минимальная стоимость футболиста',football.Value.min())

display('Футболисты которым больше двадцати лет', football[football.Age > 20])
display('Футболисты которым больше среднего возраста все футболистов')
print(football[football.Age > football.Age.mean()])
print(football[(football.Age < football.Age.mean()) & (football.Club == 'Juventus')])
print(football[(football.Age < football.Age.mean()) & (football.Club == 'FC Barcelona')].Wage.mean())

print()
print('=================')
print()

print('Средняя скорость футболистов, заралата которых выше среднего',
        football[football.Wage > football.Wage.mean()].SprintSpeed.mean())

print('Средняя скорость футболистов, заралата которых ниже среднего',
        football[football.Wage < football.Wage.mean()].SprintSpeed.mean())

print('Какую позицию занимает футболист с самой высокой зарплатой',
        football[football.Wage == football.Wage.max()].Name,
        football[football.Wage == football.Wage.max()].Position)

display("Сколько пенальти забили бразильские футболисты за период",
        football[football.Nationality == 'Brazil'].Penalties.sum())

#display_pdf()

display('Средний возраст игроков, у которых точноть удара головой больше 50 - ',
        round(football[football.HeadingAccuracy > 50].Age.mean(),2))

display('''Возраст самого молодого игрока, у которого хладнокровие и реакция
            превышают 90% от максимального значения''',
        football[(football.Composure
                    > ((football.Composure.max()/100) * 90))
                & (football.Reactions
                    > ((football.Reactions.max()/100) * 90))].Age.min())

display('''На скольо средняя ракции самых взросллых игроков больше
        средней реакции самых молодых игроков''',
        round(football[football.Age
                        == football.Age.max()].Reactions.mean()
                - football[football.Age
                        == football.Age.min()].Reactions.mean(),2))

display('''Из какой страны происходит больше всего игроков, чья стоимость
            превышает среднее значение?''',
        football[football.Value
                    > football.Value.mean()
                ].Nationality.describe(include=['object']))

display('''Во сколько раз средняя зарплата голкипера с максимальным значением
        показателя "Рефлексы" выше средней зарплаты голкипера с максимальным
        значеним показателя "Владения мячом - ''',
        round(football[(football.Position == 'GK')
                        & (football.GKReflexes
                            == football.GKReflexes.max())].Wage.mean()
            / football[(football.Position == 'GK')
                        & (football.GKHandling
                            == football.GKHandling.max())].Wage.mean(),2))

fb = pd.read_csv('./file/data_sf.csv')

display('''Определить, во сколько раз средняя сила удра самых агрессивных
        игроков выше средней силы удара игроков с минимальной агрессией''',
        round(fb[fb.Aggression == fb.Aggression.max()].ShotPower.mean()
            / fb[fb.Aggression == fb.Aggression.min()].ShotPower.mean(),2))