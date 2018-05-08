from matplotlib import pyplot as plt
from shapely.geometry import box
from shapely.geometry.polygon import Polygon
from descartes import PolygonPatch

fig = plt.figure(1, figsize=(5, 5), dpi=90)
ring_mixed = Polygon([(0, 0), (0, 2), (1, 1),
                      (2, 2), (2, 0), (1, 0.8), (0, 0)])
ax = fig.add_subplot(111)
ring_patch = PolygonPatch(ring_mixed)
ax.add_patch(ring_patch)
p = box(-1, -1, 1, 1)
ax.add_patch(PolygonPatch(p, fc='red'))
ax.add_patch(PolygonPatch(box(-5, -5, -5, 5), fc='red'))

ax.set_title('General Polygon')
xrange = [-10, 10]
yrange = [-10, 10]
ax.set_xlim(*xrange)
ax.set_ylim(*yrange)
ax.set_aspect(1)

# plt.show()

p.exterior.coords.xy[0][0] = 10
print(p.exterior)