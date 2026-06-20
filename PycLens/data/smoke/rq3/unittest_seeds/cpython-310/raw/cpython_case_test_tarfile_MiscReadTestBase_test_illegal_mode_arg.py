# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_illegal_mode_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(tmpname, 'wb'):
        pass
    with self.assertRaisesRegex(ValueError, 'mode must be '):
        tar = self.taropen(tmpname, 'q')
    with self.assertRaisesRegex(ValueError, 'mode must be '):
        tar = self.taropen(tmpname, 'rw')
    with self.assertRaisesRegex(ValueError, 'mode must be '):
        tar = self.taropen(tmpname, '')
