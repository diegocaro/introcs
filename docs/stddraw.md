# stddraw

stddraw.py

The stddraw module defines functions that allow the user to create a
drawing.  A drawing appears on the canvas.  The canvas appears
in the window.  As a convenience, the module also imports the
commonly used Color objects defined in the color module.

## setCanvasSize
```python
setCanvasSize(w=512, h=512)
```

Set the size of the canvas to w pixels wide and h pixels high.
Calling this function is optional. If you call it, you must do
so before calling any drawing function.

## setXscale
```python
setXscale(min=0.0, max=1.0)
```

Set the x-scale of the canvas such that the minimum x value
is min and the maximum x value is max.

## setYscale
```python
setYscale(min=0.0, max=1.0)
```

Set the y-scale of the canvas such that the minimum y value
is min and the maximum y value is max.

## setPenRadius
```python
setPenRadius(r=0.005)
```

Set the pen radius to r, thus affecting the subsequent drawing
of points and lines. If r is 0.0, then points will be drawn with
the minimum possible radius and lines with the minimum possible
width.

## setPenColor
```python
setPenColor(c=<color.Color object at 0x10888d7b8>)
```

Set the pen color to c, where c is an object of class color.Color.
c defaults to stddraw.BLACK.

## setFontFamily
```python
setFontFamily(f='Helvetica')
```

Set the font family to f (e.g. 'Helvetica' or 'Courier').

## setFontSize
```python
setFontSize(s=12)
```

Set the font size to s (e.g. 12 or 16).

## point
```python
point(x, y)
```

Draw on the background canvas a point at (x, y).

## line
```python
line(x0, y0, x1, y1)
```

Draw on the background canvas a line from (x0, y0) to (x1, y1).

## circle
```python
circle(x, y, r)
```

Draw on the background canvas a circle of radius r centered on
(x, y).

## filledCircle
```python
filledCircle(x, y, r)
```

Draw on the background canvas a filled circle of radius r
centered on (x, y).

## rectangle
```python
rectangle(x, y, w, h)
```

Draw on the background canvas a rectangle of width w and height h
whose lower left point is (x, y).

## filledRectangle
```python
filledRectangle(x, y, w, h)
```

Draw on the background canvas a filled rectangle of width w and
height h whose lower left point is (x, y).

## square
```python
square(x, y, r)
```

Draw on the background canvas a square whose sides are of length
2r, centered on (x, y).

## filledSquare
```python
filledSquare(x, y, r)
```

Draw on the background canvas a filled square whose sides are of
length 2r, centered on (x, y).

## polygon
```python
polygon(x, y)
```

Draw on the background canvas a polygon with coordinates
(x[i], y[i]).

## filledPolygon
```python
filledPolygon(x, y)
```

Draw on the background canvas a filled polygon with coordinates
(x[i], y[i]).

## text
```python
text(x, y, s)
```

Draw string s on the background canvas centered at (x, y).

## picture
```python
picture(pic, x=None, y=None)
```

Draw pic on the background canvas centered at (x, y).  pic is an
object of class picture.Picture. x and y default to the midpoint
of the background canvas.

## clear
```python
clear(c=<color.Color object at 0x10888d780>)
```

Clear the background canvas to color c, where c is an
object of class color.Color. c defaults to stddraw.WHITE.

## save
```python
save(f)
```

Save the window canvas to file f.

## show
```python
show(msec=inf)
```

Copy the background canvas to the window canvas, and
then wait for msec milliseconds. msec defaults to infinity.

## hasNextKeyTyped
```python
hasNextKeyTyped()
```

Return True if the queue of keys the user typed is not empty.
Otherwise return False.

## nextKeyTyped
```python
nextKeyTyped()
```

Remove the first key from the queue of keys that the the user typed,
and return that key.

## mousePressed
```python
mousePressed()
```

Return True if the mouse has been left-clicked since the
last time mousePressed was called, and False otherwise.

## mouseX
```python
mouseX()
```

Return the x coordinate in user space of the location at
which the mouse was most recently left-clicked. If a left-click
hasn't happened yet, raise an exception, since mouseX() shouldn't
be called until mousePressed() returns True.

## mouseY
```python
mouseY()
```

Return the y coordinate in user space of the location at
which the mouse was most recently left-clicked. If a left-click
hasn't happened yet, raise an exception, since mouseY() shouldn't
be called until mousePressed() returns True.

## pause
```python
pause(ms)
```

Pause for a given number of milliseconds. This function will sleep
the process to share the processor with other programas.

