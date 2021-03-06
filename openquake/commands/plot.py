# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2015-2018 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.
import numpy
from openquake.baselib import sap, general
from openquake.commonlib import util


def make_figure(indices, n, imtls, spec_curves, other_curves=(), label=''):
    """
    :param indices: the indices of the sites under analysis
    :param n: the total number of sites
    :param imtls: ordered dictionary with the IMTs and levels
    :param spec_curves: a dictionary of curves sid -> levels
    :param other_curves: dictionaries sid -> levels
    :param label: the label associated to `spec_curves`
    """
    # NB: matplotlib is imported inside since it is a costly import
    import matplotlib.pyplot as plt

    fig = plt.figure()
    n_imts = len(imtls)
    n_sites = len(indices)
    for i, site in enumerate(indices):
        for j, imt in enumerate(imtls):
            imls = imtls[imt]
            imt_slice = imtls(imt)
            ax = fig.add_subplot(n_sites, n_imts, i * n_imts + j + 1)
            ax.grid(True)
            ax.set_xlabel('site %d, %s' % (site, imt))
            if j == 0:  # set Y label only on the leftmost graph
                ax.set_ylabel('PoE')
            if spec_curves is not None:
                ax.loglog(imls, spec_curves[site][imt_slice], '--',
                          label=label)
            for r, curves in enumerate(other_curves):
                ax.loglog(imls, curves[site][imt_slice], label=str(r))
            ax.legend()
    return plt


def get_hcurves(dstore):
    hcurves = {name: dstore['hcurves/' + name] for name in dstore['hcurves']}
    return hcurves.pop('mean'), hcurves.values()


@sap.Script
def plot(calc_id, other_id=None, sites='0', imti='all'):
    """
    Hazard curves plotter.
    """
    # read the hazard data
    haz = util.read(calc_id)
    other = util.read(other_id) if other_id else None
    oq = haz['oqparam']
    if imti == 'all':
        imtls = oq.imtls
    else:
        imti = int(imti)
        imt = list(oq.imtls)[imti]
        imls = oq.imtls[imt]
        imtls = general.DictArray({imt: imls})
    indices = numpy.array(list(map(int, sites.split(','))))
    n_sites = len(haz['sitecol'])
    if not set(indices) <= set(range(n_sites)):
        invalid = sorted(set(indices) - set(range(n_sites)))
        print('The indices %s are invalid: no graph for them' % invalid)
    valid = sorted(set(range(n_sites)) & set(indices))
    print('Found %d site(s); plotting %d of them' % (n_sites, len(valid)))
    if other is None:
        mean_curves, others = get_hcurves(haz)
        plt = make_figure(valid, n_sites, imtls, mean_curves, others, 'mean')
    else:
        mean1, _ = get_hcurves(haz)
        mean2, _ = get_hcurves(other)
        plt = make_figure(valid, n_sites, imtls, mean1,
                          [mean2], 'reference')
    plt.show()


plot.arg('calc_id', 'a computation id', type=int)
plot.arg('other_id', 'optional id of another computation', type=int)
plot.opt('sites', 'comma-separated string with the site indices')
plot.opt('imti', 'IMT index')
