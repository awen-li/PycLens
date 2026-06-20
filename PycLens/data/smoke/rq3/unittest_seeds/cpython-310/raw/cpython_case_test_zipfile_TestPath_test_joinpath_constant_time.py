# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_joinpath_constant_time

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = zipfile.Path(self.huge_zipfile())
    entries = jaraco.itertools.Counter(root.iterdir())
    for entry in entries:
        entry.joinpath('suffix')
    assert entries.count == self.HUGE_ZIPFILE_NUM_ENTRIES
