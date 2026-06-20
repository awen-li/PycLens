# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_track_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (x, y, z, w) = (1.5, 'a', (1, None), [])
    self._not_tracked({})
    self._not_tracked({x: (), y: x, z: 1})
    self._not_tracked({1: 'a', 'b': 2})
    self._not_tracked({1: 2, (None, True, False, ()): int})
    self._not_tracked({1: object()})
    self._tracked({1: []})
    self._tracked({1: ([],)})
    self._tracked({1: {}})
    self._tracked({1: set()})
