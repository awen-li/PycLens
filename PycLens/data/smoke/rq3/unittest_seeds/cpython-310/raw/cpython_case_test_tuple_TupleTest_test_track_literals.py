# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tuple.py
# case: TupleTest_test_track_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (x, y, z) = (1.5, 'a', [])
    self._not_tracked(())
    self._not_tracked((1,))
    self._not_tracked((1, 2))
    self._not_tracked((1, 2, 'a'))
    self._not_tracked((1, 2, (None, True, False, ()), int))
    self._not_tracked((object(),))
    self._not_tracked(((1, x), y, (2, 3)))
    self._tracked(([],))
    self._tracked(([1],))
    self._tracked(({},))
    self._tracked((set(),))
    self._tracked((x, y, z))
