from clustering import Clustering

price = [1757, 731, 1512, 1923, 1234, 529, 1991, 747, 1775, 1148, 1839, 1877, 1947,
         1386, 1698, 830, 688, 1518, 635, 1909, 502, 712, 1212, 900, 1397, 1382, 1580,
         1765, 872, 1995, 1589, 1952, 758, 1834]


clustering = Clustering(price)
clustering.fit()
clustering.print()

