import numpy
import gdstk


if __name__ == "__main__":

 # The GDSII file is called a library, which contains multiple cells.
    lib = gdstk.Library()

    # Geometry must be placed in cells.
    cell = lib.new_cell("FIRST")   
    # Rectangular repetition
    square = gdstk.regular_polygon((0, 0), 0.2, 4)
    square.repetition = gdstk.Repetition(3, 2, spacing=(1, 1))

    # Regular repetition
    triangle = gdstk.regular_polygon((0, 2.5), 0.2, 3)
    triangle.repetition = gdstk.Repetition(3, 5, v1=(0.4, -0.3), v2=(0.4, 0.2))

    # Explicit repetition
    circle = gdstk.ellipse((3.5, 0), 0.1)
    circle.repetition = gdstk.Repetition(offsets=[(0.5, 1), (2, 0), (1.5, 0.5)])

    # X-explicit repetition
    vline = gdstk.FlexPath([(3, 2), (3, 3.5)], 0.1, simple_path=True)
    vline.repetition = gdstk.Repetition(x_offsets=[0.2, 0.6, 1.4, 3.0])

    # Y-explicit repetition
    hline = gdstk.RobustPath((3, 2), 0.05, simple_path=True)
    hline.segment((6, 2))
    hline.repetition = gdstk.Repetition(y_offsets=[0.1, 0.3, 0.7, 1.5])

    main = gdstk.Cell("Main")
    main.add(square, triangle, circle, vline, hline)

    cell.add(main)


    lib.write_gds("first.gds")
    lib.write_oas("first.oas")

    # Optionally, save an image of the cell as SVG.
    cell.write_svg("first.svg")