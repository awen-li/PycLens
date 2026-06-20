# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_track_dynamic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyObject(object):
        pass
    (x, y, z, w, o) = (1.5, 'a', (1, object()), [], MyObject())
    d = dict()
    self._not_tracked(d)
    d[1] = 'a'
    self._not_tracked(d)
    d[y] = 2
    self._not_tracked(d)
    d[z] = 3
    self._not_tracked(d)
    self._not_tracked(d.copy())
    d[4] = w
    self._tracked(d)
    self._tracked(d.copy())
    d[4] = None
    self._not_tracked(d)
    self._not_tracked(d.copy())
    d = dict()
    dd = dict()
    d[1] = dd
    self._not_tracked(dd)
    self._tracked(d)
    dd[1] = d
    self._tracked(dd)
    d = dict.fromkeys([x, y, z])
    self._not_tracked(d)
    dd = dict()
    dd.update(d)
    self._not_tracked(dd)
    d = dict.fromkeys([x, y, z, o])
    self._tracked(d)
    dd = dict()
    dd.update(d)
    self._tracked(dd)
    d = dict(x=x, y=y, z=z)
    self._not_tracked(d)
    d = dict(x=x, y=y, z=z, w=w)
    self._tracked(d)
    d = dict()
    d.update(x=x, y=y, z=z)
    self._not_tracked(d)
    d.update(w=w)
    self._tracked(d)
    d = dict([(x, y), (z, 1)])
    self._not_tracked(d)
    d = dict([(x, y), (z, w)])
    self._tracked(d)
    d = dict()
    d.update([(x, y), (z, 1)])
    self._not_tracked(d)
    d.update([(x, y), (z, w)])
    self._tracked(d)
