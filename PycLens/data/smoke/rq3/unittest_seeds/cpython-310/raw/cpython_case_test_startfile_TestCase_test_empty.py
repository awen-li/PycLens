# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_startfile.py
# case: TestCase_test_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.change_cwd(path.dirname(sys.executable)):
        empty = path.join(path.dirname(__file__), 'empty.vbs')
        startfile(empty)
        startfile(empty, 'open')
    startfile(empty, cwd=path.dirname(sys.executable))
