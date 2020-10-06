from bokeh.plotting import figure, output_file, show
from random import randint

if __name__ == '__main__':
    x = [second for second in range(10)]
    y = [crazy_temperature*randint(-4, 4) for crazy_temperature in range(10)]

    # output to static HTML file
    output_file("crazy_temperature.html")

    # create a new plot
    p = figure(title="Random data bro", x_axis_label='x', y_axis_label='y')

    # add a new line
    p.line(x, y, legend_label='Random Shit', line_width=7)

    # show the results
    show(p)

# import numpy as np

# from bokeh.plotting import figure, output_file, show

# # prepare some data
# N = 4000
# x = np.random.random(size=N) * 100
# y = np.random.random(size=N) * 100
# radii = np.random.random(size=N) * 1.5
# colors = [
#     "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
# ]

# # output to static HTML file (with CDN resources)
# output_file("color_scatter.html", title="color_scatter.py example", mode="cdn")

# TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

# # create a new plot with the tools above, and explicit ranges
# p = figure(tools=TOOLS, x_range=(0, 100), y_range=(0, 100))

# # add a circle renderer with vectorized colors and sizes
# p.circle(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

# # show the results
# show(p)

# import numpy as np

# from bokeh.io import output_file, show
# from bokeh.plotting import figure
# from bokeh.util.hex import axial_to_cartesian

# output_file("hex_coords.html")

# q = np.array([0,  0, 0, -1, -1,  1, 1])
# r = np.array([0, -1, 1,  0,  1, -1, 0])

# p = figure(plot_width=400, plot_height=400, toolbar_location=None)
# p.grid.visible = False

# p.hex_tile(q, r, size=1, fill_color=["firebrick"]*3 + ["navy"]*4,
#            line_color="white", alpha=0.5)

# x, y = axial_to_cartesian(q, r, 1, "pointytop")

# p.text(x, y, text=["(%d, %d)" % (q,r) for (q, r) in zip(q, r)],
#        text_baseline="middle", text_align="center")

# show(p)

# import numpy as np

# from bokeh.io import output_file, show
# from bokeh.plotting import figure
# from bokeh.util.hex import axial_to_cartesian

# output_file("hex_coords.html")

# q = np.array([0,  0, 0, -1, -1,  1, 1])
# r = np.array([0, -1, 1,  0,  1, -1, 0])

# p = figure(plot_width=400, plot_height=400, toolbar_location=None)
# p.grid.visible = False

# p.hex_tile(q, r, size=1, fill_color=["firebrick"]*3 + ["navy"]*4,
#            line_color="white", alpha=0.5)

# x, y = axial_to_cartesian(q, r, 1, "pointytop")

# p.text(x, y, text=["(%d, %d)" % (q,r) for (q, r) in zip(q, r)],
#        text_baseline="middle", text_align="center")

# show(p)