from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')  # Crea un archivo llamado 'graficado_simple.html'
    fig = figure()  # Meter en la variable fig una figura
    
    total_vals = int(input('Cuantos valores quieres graficar?'))  
    x_vals = list(range(total_vals))  # Crea una seguida con el rango de datos
    y_vals = [2*x**2 for x in x_vals]

    fig.line(x_vals, y_vals, line_width=2)  # Definir como va a ser el gráfico 
    show(fig)  # Enseña el gráfico