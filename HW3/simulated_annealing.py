import numpy as np
import matplotlib.pyplot as plt
import copy

#number of items
N = 100

#weight limit
W = 3000

# weights of items
w = np.array([430, 763, 965, 848, 481, 336, 346, 381, 252, 218, 234, 906, 398,
       749, 343, 281, 773, 589, 896, 342, 640, 935, 876, 456, 629, 296,
       515, 946, 843, 554, 655, 906, 528, 273, 477, 347, 495, 294, 638,
       552, 607, 815, 394, 608, 694, 905, 826, 528, 739, 628, 810, 709,
       822, 296, 657, 654, 653, 892, 410, 812, 780, 469, 837, 450, 417,
       688, 308, 345, 616, 904, 827, 453, 690, 782, 626, 752, 994, 236,
       924, 303, 881, 617, 241, 559, 337, 930, 352, 922, 377, 865, 825,
       536, 499, 729, 359, 897, 959, 293, 658, 983])

# values of items
v = np.array([25, 27, 15, 25, 13, 15, 18, 24, 25, 30, 12, 18, 28, 30, 20, 26, 24,
       30, 14, 20, 15, 30, 18, 26, 16, 24, 11, 16, 14, 13, 13, 14, 30, 12,
       21, 13, 12, 28, 22, 14, 10, 20, 29, 19, 30, 16, 12, 24, 28, 27, 29,
       18, 16, 27, 30, 29, 17, 19, 26, 12, 24, 15, 27, 16, 15, 15, 19, 14,
       22, 30, 19, 30, 19, 24, 27, 16, 12, 27, 24, 17, 12, 18, 11, 14, 27,
       13, 23, 11, 26, 22, 12, 13, 15, 20, 20, 24, 12, 10, 14, 13])

def simulated_annealing():
    # YOUR CODE HERE

    current_bag = []
    #list of available items
    inds = list(xrange(N))
    trials = 60000
    
    def value(bag):
      val = 0
      if bag == []:
        return val
      else:
        for i in bag:
          val += v[i]
        return val

    def weight(bag):
      weight = 0
      if bag != []:
        for i in bag:
          weight += w[i]
      return weight

    #store values of bag after each iteration
    values_trace = []

    #initialize temperature
    temp = 1

    #track best bag
    best_bag = []

    for t in range(1,trials):
      #decrement temperature
      temp = temp*.999999
      #pick item to add to bag
      next_item = np.random.choice(inds)
      next_bag = current_bag+[next_item]
      inds2 = copy.copy(inds)
      inds2.remove(next_item)

      #if bag is too heavy, remove items randomly one by one until
      #under weight limit
      while weight(next_bag) >= W:
        drop = np.random.choice(next_bag)
        next_bag.remove(drop)
        inds2.append(drop)

      #calculate value difference between current bag and new sample bag
      delta = value(next_bag)-value(current_bag)
      if delta >= 0:
        current_bag = next_bag
        inds = copy.copy(inds2)
        if value(current_bag) > value(best_bag):
          best_bag = copy.copy(current_bag)
        values_trace.append(value(current_bag))

      else:
        a = np.random.random()
        if a < np.exp(delta/temp):
          current_bag = next_bag
          inds = copy.copy(inds2)
          if value(current_bag) > value(best_bag):
            best_bag = copy.copy(current_bag)
          values_trace.append(value(current_bag))

        else:
          values_trace.append(value(current_bag))

    print "Simulated Annealing"
    print "Value:" + str(value(best_bag))
    print "Weight:" + str(weight(best_bag))
    print "Bag:" + str(best_bag)
    return values_trace #np.random.random_integers(200,300, 10) #current_bag



if __name__ == "__main__":
    # Greedy result is maximize v/w
    vw_ratio = sorted(map(lambda x: (x, 1.*v[x]/w[x]), range(N)), key= lambda x: -x[1])
    greedy_val = 0
    greedy_weight = 0
    greedy_bag = []
    index = 0
    while greedy_weight + w[vw_ratio[index][0]] < W:
        greedy_val += v[vw_ratio[index][0]]
        greedy_weight += w[vw_ratio[index][0]]
        greedy_bag += [vw_ratio[index][0]]
        index += 1
    
    print("Greedy Algorithm:\nValue:{}, Weight:{}\nBag:{}".format(greedy_val, greedy_weight, greedy_bag))
    SA_trace = simulated_annealing()
    plt.plot([greedy_val]*len(SA_trace), label="Greedy")
    plt.plot(SA_trace, label="SA")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.show()
    