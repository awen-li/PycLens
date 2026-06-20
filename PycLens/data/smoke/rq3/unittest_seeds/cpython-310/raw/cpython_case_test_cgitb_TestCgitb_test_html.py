# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgitb.py
# case: TestCgitb_test_html

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        raise ValueError('Hello World')
    except ValueError as err:
        html = cgitb.html(sys.exc_info())
        self.assertIn('ValueError', html)
        self.assertIn(str(err), html)
