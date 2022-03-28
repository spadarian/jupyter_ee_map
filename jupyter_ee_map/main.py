import ee
import ipyleaflet


class EEMap(ipyleaflet.Map):
    """Widget to display Google Earth Engine Images.

    Parameters
    ----------
    events : dict
        Events to track. With a signature {'str': function}
        The keys should be one of following events:
        ['click', 'dblclick', 'mousedown', 'mouseup', 'mouseover', 'mouseout',
        'mousemove', 'contextmenu', 'preclick'].
        The events send a copy of the `EEMap` class and a list with the coordinates
        (lat, long) to the callback functions. Default is None.
    **kwargs :
        Extra parameters for ipyleaflet.Map.

    Attributes
    ----------
    ee_layers : list
        EE layers added to the map with the `add_ee_layer` function.

    """

    def __init__(self, events=None, **kwargs):
        super(EEMap, self).__init__(**kwargs)
        self._handle_interactions(events)
        self.ee_layers = []

    def _handle_interactions(self, events=None):
        if events is not None:
            def on_event(**args):
                if args['type'] in events.keys():
                    coords = args['coordinates']
                    f = events[args['type']]
                    f(self, coords)
            self.on_interaction(on_event)

    def add_ee_layer(self, raw_img, vis=None, **kwargs):
        """Add a EE layer to the map.

        Parameters
        ----------
        raw_img : ee.image.Image
            Image without visualisation parameters.
        vis : dict
            Visualisation parameters. Default is None.
        **kwargs :
            Extra parameters for ipyleaflet.TileLayer.

        """
        if vis is not None:
            img = raw_img.visualize(**vis)
        else:
            img = raw_img
        self.add_layer(
            ipyleaflet.TileLayer(url=self._get_tileLayer_url(img),
                                 **kwargs)
        )
        self.ee_layers.append(raw_img)

    @staticmethod
    def _get_tileLayer_url(ee_image_object):
        map_id = ee.Image(ee_image_object).getMapId()
        fetcher = map_id['tile_fetcher']
        return fetcher.url_format
