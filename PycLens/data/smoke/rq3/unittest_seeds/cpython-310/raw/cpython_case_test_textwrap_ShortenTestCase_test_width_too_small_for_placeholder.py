# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: ShortenTestCase_test_width_too_small_for_placeholder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    shorten('x' * 20, width=8, placeholder='(......)')
    with self.assertRaises(ValueError):
        shorten('x' * 20, width=8, placeholder='(.......)')
