import random
import imp

"""
Title: Ocean
Author: Bailey Reid
Date: 29/07/22
Version: 1.0
Purpose: To Create The Infomation That The Main File Uses To Create The Visable Maze
"""

defultM = [['wb', 'wt', 'wp', 'wt', 'wt', 'wt', 'wl', 'ed', 'wb', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'ws'],
['wg', 'ed', 'wu', 'eb', 'et', 'et', 'et', 'ej', 'wg', 'eb', 'et', 'et', 'et', 'ep', 'et', 'et', 'et', 'et', 'es', 'wg'],
['wg', 'ec', 'et', 'ei', 'wb', 'wt', 'wt', 'wt', 'wj', 'eg', 'wb', 'wt', 'ws', 'eg', 'wb', 'wt', 'wp', 'ws', 'eg', 'wg'],
['wx', 'wt', 'ws', 'eg', 'wu', 'eb', 'et', 'et', 'et', 'ej', 'wg', 'ed', 'wg', 'eg', 'wg', 'ed', 'wc', 'wj', 'eg', 'wg'],
['wg', 'ed', 'wg', 'ec', 'et', 'ej', 'wb', 'wt', 'wt', 'wt', 'wj', 'eg', 'wg', 'eg', 'wu', 'ec', 'ep', 'et', 'ei', 'wg'],
['wg', 'eg', 'wx', 'wt', 'wt', 'wp', 'wi', 'eb', 'et', 'et', 'et', 'ei', 'wg', 'ex', 'el', 'wn', 'eg', 'wd', 'eg', 'wg'],
['wg', 'eg', 'wu', 'eb', 'el', 'wc', 'wi', 'eg', 'wb', 'wt', 'wl', 'eg', 'wg', 'eg', 'wd', 'eb', 'ej', 'wu', 'eg', 'wg'],
['wg', 'ex', 'et', 'ei', 'wn', 'ed', 'wg', 'eg', 'wg', 'eb', 'et', 'ej', 'wg', 'eg', 'wg', 'eg', 'wd', 'eb', 'ej', 'wg'],
['wg', 'eg', 'wd', 'ec', 'et', 'ei', 'wu', 'eg', 'wg', 'eg', 'wr', 'wt', 'wj', 'eg', 'wg', 'eg', 'wg', 'eg', 'wr', 'wi'],
['wg', 'eg', 'wc', 'wt', 'wl', 'ec', 'et', 'ej', 'wg', 'ec', 'et', 'et', 'et', 'ej', 'wu', 'eg', 'wg', 'ex', 'es', 'wg'],
['wg', 'ec', 'ep', 'et', 'es', 'wb', 'wt', 'wt', 'wq', 'wt', 'wt', 'wt', 'wt', 'ws', 'eb', 'ej', 'wu', 'ex', 'ei', 'wg'],
['wx', 'wl', 'eg', 'wd', 'eg', 'wg', 'er', 'ep', 'et', 'ep', 'et', 'et', 'es', 'wg', 'eg', 'wd', 'eb', 'eq', 'ej', 'wg'],
['wg', 'eb', 'ei', 'wg', 'eg', 'wc', 'wl', 'eg', 'wd', 'eu', 'wr', 'wl', 'eg', 'wu', 'eg', 'wg', 'eg', 'wb', 'wt', 'wi'],
['wg', 'ec', 'ei', 'wg', 'ec', 'et', 'et', 'ej', 'wx', 'wl', 'er', 'et', 'ea', 'et', 'ej', 'wg', 'eg', 'wg', 'ed', 'wg'],
['wx', 'wl', 'eg', 'wc', 'wp', 'wp', 'wt', 'wp', 'wj', 'ed', 'wr', 'wl', 'eu', 'wr', 'wt', 'wj', 'eg', 'wg', 'eg', 'wg'],
['wg', 'er', 'eq', 'es', 'wc', 'wj', 'ed', 'wg', 'eb', 'eq', 'et', 'es', 'wn', 'eb', 'et', 'et', 'ej', 'wu', 'eg', 'wg'],
['wx', 'wt', 'ws', 'ex', 'et', 'et', 'ei', 'wg', 'eg', 'wr', 'ws', 'ec', 'et', 'ej', 'wr', 'wt', 'wl', 'eb', 'ei', 'wg'],
['wg', 'ed', 'wu', 'eg', 'wb', 'wl', 'eg', 'wg', 'ec', 'es', 'wc', 'wt', 'wt', 'wl', 'eb', 'et', 'ep', 'eq', 'ei', 'wg'],
['wg', 'ec', 'et', 'ej', 'wg', 'er', 'ej', 'wx', 'ws', 'ec', 'et', 'et', 'et', 'et', 'ej', 'wd', 'eu', 'wd', 'eg', 'wg'],
['wc', 'wt', 'wt', 'wt', 'wq', 'wt', 'wt', 'wq', 'wq', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'wq', 'wt', 'wj', 'eu', 'wu']]


class Ocean():
    '''Takes the list above and turns it into the maze that gets displayed by the main file'''
    """
    Ocean class
    """
    WIDTH = 20
    HEIGHT = 20
    tmap = defultM
    def print(self):
        for row in self.tmap:
            for col in row:
                print(col,end ='')
            print()
    def get(self, row,col):
        return self.tmap[row][col]