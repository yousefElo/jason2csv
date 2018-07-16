import json
import pandas

path = input("input json file  : ")
fileName = path.split("\\")[-1]

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

df = pandas.read_json(path)
df.to_csv(fileName + '.csv')

print('>> csv file created successfully >>:  {}'.format(fileName + '.csv'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
