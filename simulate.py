import matplotlib.pyplot as plot
import numpy as np
from matplotlib import style

style.use("ggplot")
#style.use('bmh')
#style.use('dark_background')

np.random.seed(10)

class Simulation:
    probabilities=[]
    def __init__(self, number_of_peoples, number_of_experiments):
        self.number_of_peoples = number_of_peoples
        self.number_of_experiments = number_of_experiments
        #self.simulation()

    
    def simulation(self):
        shared_birthday = 0
        total_number_of_experiments = 0
        
        number_of_people = self.number_of_peoples

        for experiment_index in range(0, self.number_of_experiments):
            dates = np.random.choice(range(1,366), size=(number_of_people))
            if len(np.unique(dates)) != len(dates):
                shared_birthday+=1
            total_number_of_experiments +=1
            probability = shared_birthday/total_number_of_experiments
            self.probabilities.append(probability)
        
        plot.plot(self.probabilities)
        plot.title("Output of "+str(self.number_of_experiments)+" Experiments, converging to " + str(self.probabilities[-1]))
        plot.show()
