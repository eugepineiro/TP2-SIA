import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

x_vals = []   # generation number
fit_min_vals = []  # fitness minimum value
fit_mean_vals = []  # fitness mean value
gen_div_vals = []  # genetic diversity value
fit_max_vals = []  # fitness maximum value

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,figsize=(12,8))





def update_plots(generation, fit_min, fit_mean, gen_div,fit_max):
    x_vals.append(generation)
    fit_min_vals.append(fit_min)
    fit_mean_vals.append(fit_mean)
    gen_div_vals.append(gen_div)
    fit_max_vals.append(fit_max)
    # print(x_vals)
    # print(fit_min_vals)
    # print(fit_mean_vals)
    # print(gen_div_vals)

    ax1.cla()
    ax1.scatter(x_vals, fit_min_vals, label="Fitness minimum value",color="cornflowerblue")
    ax1.legend(loc="upper left",frameon=False)
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness minimum value")

    ax2.cla()
    ax2.scatter(x_vals, fit_mean_vals, label="Fitness mean value",color="indianred")
    ax2.legend(loc="upper left",frameon=False)
    ax2.set_xlabel("Generation")
    ax2.set_ylabel("Fitness mean value")

    ax3.cla()
    ax3.scatter(x_vals, gen_div_vals, label="Genetic diversity value",color="darkorange")
    ax3.legend(loc="upper left",frameon=False)
    ax3.set_xlabel("Generation")
    ax3.set_ylabel("Genetic diversity value (%)")

    ax4.cla()
    ax4.scatter(x_vals, fit_max_vals, label="Fitness maximum value",color="seagreen")
    ax4.legend(loc="upper left",frameon=False)
    ax4.set_xlabel("Generation")
    ax4.set_ylabel("Fitness maximum value")
    plt.pause(0.5)

def init_plot(char_class):
    fig.suptitle('Stats for class {char_class}'.format(char_class=char_class), fontsize=16)
    # ax1.scatter(x_vals, fit_min_vals, label="Fitness minimum value",color="cornflowerblue")
    # ax1.legend(loc="upper left",frameon=False)
    
    # ax2.scatter(x_vals, fit_mean_vals, label="Fitness mean value",color="indianred")
    # ax2.legend(loc="upper left",frameon=False)
    
    # ax3.scatter(x_vals, gen_div_vals, label="Genetic diversity value",color="darkorange")
    # ax3.legend(loc="upper left",frameon=False)
    

def show():
    plt.show()

