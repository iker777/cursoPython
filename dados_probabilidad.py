import random
from bokeh.io import output_file, show
from bokeh.plotting import figure 
import estadisticas

def dices_throws_simulation():
    all_throws = []
    throws = range(2)

    for _ in throws:
        dice1 = random.randint(1, 7)
        dice2 = random.randint(1, 7) 
        dices_puntuation = dice1 + dice2
        all_throws.append(dices_puntuation)

    return sum(all_throws) / len(all_throws)

if __name__ == '__main__':
    output_file("normal_distribution.html")

    simulation_times = range(20)
    mean_throws = []

    for _ in simulation_times:
        simulation = dices_throws_simulation()
        mean_throws.append(simulation)
    
    x_mean = estadisticas.media(mean_throws)
    standard_desviation = []

    for i in simulation_times:
        standard_desviation.append(mean_throws[i] / x_mean) 

    range_bar_chart = [round(i*0.1, 2) for i in range(20)]
    len_bar = len(range_bar_chart)
    bar_cuantity = []

    for i in range(len_bar):
        bar_proportion = 0

        for mean in standard_desviation:
            if range_bar_chart[i] == range_bar_chart[-1]:
                if mean > range_bar_chart[i]:
                    bar_proportion += 1

            if mean > range_bar_chart[i] and mean < range_bar_chart[i + 1]:
                bar_proportion += 1
            
        bar_cuantity.append(bar_proportion)
     
    p = figure(x_range=range_bar_chart, plot_height=350, title="Distribución Normal de 2 dados", toolbar_location=None, tools="")

    p.vbar(x=str(range_bar_chart), top=bar_cuantity, width=0.9)

    # p.xgrid.grid_line_color = None
    # p.y_range.start = 0

    show(p)