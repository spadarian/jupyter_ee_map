# jupyter_ee_map

This a simple extension of [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet) Map to work with Google Earth Engine images.

To use this library you need a valid Google Earth Engine account and the Python API. You can find more information at https://developers.google.com/earth-engine/python_install.

## Features

* Function to add EE layers.
* Handles Map interactions (e.g.: click) with custom functions.

## Installation

For the latest development version, first get the source from github:

    git clone https://github.com/spadarian/jupyter_ee_map.git

Then navigate into the local ``jupyter_ee_map`` directory and simply run:

    python setup.py install

or:

    python setup.py install --user

## Example

Try this example on a Jupyter notebook.

```python
import jupyter_ee_map
from jupyter_ee_map import EEMap
import ee
ee.Initialize()

# Load a sample Image (elevation)
dem = ee.Image('CGIAR/SRTM90_V4')
```

Let's create a custom function to handle clicks on the map and request the elevation value at the clicked coordinates. Note that the callback functions will receive 2 parameter: a instance of the EEMap and the coordinates ([lat, long]).

```python
def on_click(cls, coords):
    print('Loading data (coords: ', coords, ')... ', end='')
    # Reverse the coordinates to [x, y]
    geom = ee.Geometry.Point(coords[::-1])
    # Iterate through all the EE layers.
    for l in cls.ee_layers:
        # Sample the layers at the clicked coordinates
        ans = l.reduceRegion(reducer='mean', geometry=geom, scale=100).getInfo()
        print(ans, end=' ')
    print('')
```

After this you just need to initialise the EEMap class:

```python
test_map = EEMap(
    center=(48.2082, 16.3779), zoom=4,
    layout={'height':'400px'},
    events={'click': on_click}  # Note the dictionary with the event name as key
)

test_map.add_ee_layer(dem, vis={'min': 0, 'max': 2500})
test_map
```

That will show a map Widget and you would be able to click on it and get the elevation values.

![Demo](https://raw.githubusercontent.com/spadarian/jupyter_ee_map/master/img/demo.gif)
