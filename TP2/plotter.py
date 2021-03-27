import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

x_vals = []   # generation number
fit_min_vals = []  # fitness minimum value
fit_mean_vals = []  # fitness mean value
gen_div_vals = []  # genetic diversity value
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,figsize=(12,8))


# def animate(i):
#     print(fit_min_vals)
#     print(x_vals)
#     ax1.cla()
#     ax1.plot(x_vals, fit_min_vals, label="Fitness minimum value")
#     ax1.legend(loc="upper left")

#     ax2.cla()
#     ax2.plot(x_vals, fit_min_vals, label="Fitness mean value")
#     ax2.legend(loc="upper left")

#     ax3.cla()
#     ax3.plot(x_vals, fit_min_vals, label="Genetic diversity value")
#     ax3.legend(loc="upper left")
#     plt.tight_layout()


# fig = plt.figure(figsize=(12,8))
# ax1 = plt.subplot(221)
# ax2 = plt.subplot(222)
# ax3 = plt.subplot(223)
# plt.style.use('fivethirtyeight')
# ani = FuncAnimation(plt.gcf(),animate, interval=1000)




def update_plots(generation, fit_min, fit_mean, gen_div):
    x_vals.append(generation)
    fit_min_vals.append(fit_min)
    fit_mean_vals.append(fit_mean)
    gen_div_vals.append(gen_div)
    print(x_vals)
    print(fit_min_vals)
    print(fit_mean_vals)
    print(gen_div_vals)
    ax1.cla()
    
    ax1.scatter(x_vals, fit_min_vals, label="Fitness minimum value",color="cornflowerblue")
    ax1.legend(loc="upper left",frameon=False)

    ax2.cla()
    
    ax2.scatter(x_vals, fit_mean_vals, label="Fitness mean value",color="indianred")
    ax2.legend(loc="upper left",frameon=False)
    ax3.cla()
    
    ax3.scatter(x_vals, gen_div_vals, label="Genetic diversity value",color="darkorange")
    ax3.legend(loc="upper left",frameon=False)
    plt.pause(0.5)

def init_plot():

    ax1.scatter(x_vals, fit_min_vals, label="Fitness minimum value",color="cornflowerblue")
    ax1.legend(loc="upper left",frameon=False)
    
    ax2.scatter(x_vals, fit_mean_vals, label="Fitness mean value",color="indianred")
    ax2.legend(loc="upper left",frameon=False)
    
    ax3.scatter(x_vals, gen_div_vals, label="Genetic diversity value",color="darkorange")
    ax3.legend(loc="upper left",frameon=False)
    

def show():
    plt.show()

