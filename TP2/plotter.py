import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

x_vals = []   # generation number
fit_min_vals = []  # fitness minimum value
fit_mean_vals = []  # fitness mean value
gen_div_vals = []  # genetic diversity value
fit_max_vals = []  # fitness maximum value

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,figsize=(12,8)) #2 rows y 2 cols --> 4 graphs 
fig.tight_layout(pad=5.0)

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
    #ax1.legend(loc="upper left",frameon=False)
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness minimum value") 
    ax1.title.set_text("MIN FITNESS")

    ax2.cla()
    ax2.scatter(x_vals, fit_mean_vals, label="Fitness mean value",color="indianred")
    #ax2.legend(loc="upper left",frameon=False)
    ax2.set_xlabel("Generation")
    ax2.set_ylabel("Fitness mean value")
    ax2.title.set_text("MEAN FITNESS")
    
    ax3.cla()
    ax3.scatter(x_vals, gen_div_vals, label="Genetic diversity value",color="darkorange")
    #ax3.legend(loc="upper left",frameon=False)
    ax3.set_xlabel("Generation")
    ax3.set_ylabel("Genetic diversity value (%)")
    ax3.title.set_text("DIVERSITY")

    ax4.cla()
    ax4.scatter(x_vals, fit_max_vals, label="Fitness maximum value",color="seagreen")
    #ax4.legend(loc="upper left",frameon=True)
    ax4.set_xlabel("Generation")
    ax4.set_ylabel("Fitness maximum value")
    ax4.title.set_text("MAX FITNESS")
    plt.pause(0.5)

def init_plot(char_class):
    fig.suptitle('Stats for class {char_class}'.format(char_class=char_class), fontsize=16)
 

def show():  
    with open('min.txt', 'w') as f:
        for min in fit_min_vals: 
            f.write(min)
            f.write('\n')
            
    with open('max.txt', 'w') as f:
        for max in fit_max_vals: 
            f.write(max)
            f.write('\n')
            
    with open('mean.txt', 'w') as f:
        for mean in fit_mean_vals: 
            f.write(mean)
            f.write('\n')  
            
    with open('diversity.txt', 'w') as f:
        for div in gen_div_vals: 
            f.write(div)
            f.write('\n')
             
    plt.show()
    

