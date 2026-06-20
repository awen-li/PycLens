# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_exclude_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class whatever(Enum):
        this = 'that'
        these = 'those'

        def really(self):
            return 'no, not %s' % self.value
    self.assertIsNot(type(whatever.really), whatever)
    self.assertEqual(whatever.this.really(), 'no, not that')
