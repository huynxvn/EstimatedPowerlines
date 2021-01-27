import numpy as np
from GreatCircle import *
def cull(cand):

    for pole in cand.keys():
        score1 = sum([cand[p] for p in cand.keys() if great_circle_distance(pole,p)<10])
        score2 = sum([cand[p] for p in cand.keys() if great_circle_distance(pole,p)<20])
        score3 = sum([cand[p] for p in cand.keys() if great_circle_distance(pole,p)<30])
        finalscore = 0.3*score1 + 0.2*score2 + 0.05*score3
        if finalscore > cand[pole]:
            cand[pole] = 0

    cand = {key: val for key, val in cand.items() if val != 0}
    return cand

def candidates(roads):
    '''
    returns a dictionary of roads that
    :param roads:
    :return:
    '''
    roads = np.array(roads)
    cand = {}
    for road in roads:

        cand[road[0]] = 100
        cand[road[-1]] = 100
        cum_line_len = 0
        '''
        if len(road) == 2:
            line_len=great_circle_distance(road[0],road[1])
            if line_len>25:

                num_poles = int(line_len//35)+1

                for j in range(num_poles):

                    location = ((num_poles-j)/(num_poles+1))*np.array(road[0])+((j+1)/(num_poles+1))*np.array(road[1])
                    location = tuple(location)
                    cand[location] = 70
                    '''
        for i in range(len(road)-1):
            line_len=great_circle_distance(road[i],road[i+1])
            cum_line_len = cum_line_len + line_len

            if line_len>25:

                num_poles = max(2, int(line_len//35))

                for j in range(num_poles):

                    location = ((num_poles-j)/(num_poles+1))*np.array(road[i])+((j+1)/(num_poles+1))*np.array(road[i+1])
                    location = tuple(location)
                    if location not in cand.keys():

                        cand[location] = 70
                        cum_line_len = 0
                    else:
                        cand[location] = max(cand[location],70)
                        cum_line_len = 0

            if road[i+1] not in cand.keys():
                cand[road[i+1]] = 60
            else:
                cand[road[i+1]] = max(cand[road[i+1]],30)


    return cand



