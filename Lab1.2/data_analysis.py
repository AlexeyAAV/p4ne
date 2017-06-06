from matplotlib import pyplot
from openpyxl import load_workbook
def getvalue(x): return x.value
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
x = list(map(getvalue, sheet['A'][1:]))
y = list(map(getvalue, sheet['B'][1:]))
y1 = list(map(getvalue, sheet['C'][1:]))
print(x)
print(y)
print (y1)
pyplot.plot(x,y)
pyplot.plot(x,y1)
pyplot.show()
