# -*- encoding: utf-8 -*-

import math
from GA import GA

class TSP(object):
      def __init__(self, aLifeCount = 250,):
            self.initCitys()
            self.lifeCount = aLifeCount
            self.ga = GA(aCrossRate = 0.7, 
                  aMutationRage = 0.02, 
                  aLifeCount = self.lifeCount, 
                  aGeneLenght = len(self.citys), 
                  aMatchFun = self.matchFun())

      def initCitys(self):
            self.citys = []
            self.citys.append((16, 3))
            self.citys.append((17,39))
            self.citys.append((12, 31))
            self.citys.append((10, 60))
            self.citys.append((30, 29))
            self.citys.append((40, 4))
            self.citys.append((10, 38))
            self.citys.append((11, 40))
            self.citys.append((29, 22))
            self.citys.append((55, 45))

            self.citys.append((160, 35))
            self.citys.append((170, 88))
            self.citys.append((120, 31))
            self.citys.append((100, 60))
            self.citys.append((99, 55))
            self.citys.append((78, 87))
            self.citys.append((100, 38))
            self.citys.append((111, 40))
            self.citys.append((64, 22))
            self.citys.append((123, 123))

            
      def distance(self, order):
            distance = 0.0
            for i in range(-1, len(self.citys) - 1):
                  index1, index2 = order[i], order[i + 1]
                  city1, city2 = self.citys[index1], self.citys[index2]
                  distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
            return distance


      def matchFun(self):
            return lambda life: 1.0 / self.distance(life.gene)

      def run(self, n = 0):
            while n > 0:
                  self.ga.next()
                  distance = self.distance(self.ga.best.gene)
                  print (self.ga.generation, float('%.5f'% distance),self.ga.best.gene)
                  n -= 1

def main():
      tsp = TSP()
      tsp.run(500)

main()


