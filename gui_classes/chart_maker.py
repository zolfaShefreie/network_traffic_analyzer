import pandas as pd
from matplotlib import pyplot as plt

class ChartMaker:
    def __init__(self, data_dict, path, x='number', label='protocol'):
        self.df = pd.DataFrame(data_dict)
        self.path = path
        self.x = x
        self.label = label

    def draw(self):
        self.df.plot.pie(y=self.x, labels=self.df[self.label], colors=['blue', 'teal', 'darkturquoise', 'skyblue', 'navy'])
        plt.savefig(self.path)
        plt.close('all')

