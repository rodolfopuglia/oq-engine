"""
Module :mod:`nhe.source.area` defines :class:`AreaSource`.
"""
from nhe.source.point import PointSource


class AreaSource(PointSource):
    """
    Area source represents uniform seismicity occurring over a geographical
    region.

    :param polygon:
        An instance of :class:`nhe.common.geo.Polygon` that defines
        source's area.
    :param area_discretization:
        Float number, polygon discretization spacing in kilometers.
        See :meth:`iter_ruptures`.

    Other parameters (except ``location``) are the same as for
    :class:`~nhe.source.point.PointSource`.
    """
    def __init__(self, source_id, name, tectonic_region_type, mfd,
                 polygon, area_discretization, *args, **kwargs):
        super(AreaSource, self).__init__(
            source_id, name, tectonic_region_type, mfd, *args,
            location=None, **kwargs
        )
        self.polygon = polygon
        self.area_discretization = area_discretization

    def iter_ruptures(self, temporal_occurrence_model):
        """
        See :meth:`nhe.source.base.SeismicSource.iter_ruptures`
        for description of parameters and return value.

        Area sources are treated as a collection of point sources
        (see :mod:`nhe.source.point`) with uniform parameters.
        Ruptures of area source are just a union of ruptures
        of those point sources. The actual positions of the implied
        point sources form a uniformly spaced grid on the polygon.
        Polygon's method :meth:`~nhe.geo.polygon.Polygon.discretize`
        is used for finding point sources location. Constructor's
        parameter ``area_discretization`` is used as polygon's griding
        spacing (not to be confused with rupture surface's
        :meth:`mesh_spacing <nhe.surface.base.BaseSurface.get_mesh>`).

        The ruptures' occurrence rates are rescaled with respect to number
        of points the polygon discretizes to.
        """
        locations = list(self.polygon.discretize(self.area_discretization))
        rate_scaling_factor = 1.0 / len(locations)
        for location in locations:
            ruptures_at_location = self._iter_ruptures_at_location(
                temporal_occurrence_model, location, rate_scaling_factor
            )
            for rupture in ruptures_at_location:
                yield rupture
