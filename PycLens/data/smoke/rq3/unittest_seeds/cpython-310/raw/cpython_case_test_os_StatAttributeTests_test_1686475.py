# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: StatAttributeTests_test_1686475

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.stat('c:\\pagefile.sys')
    except FileNotFoundError:
        self.skipTest('c:\\pagefile.sys does not exist')
    except OSError as e:
        self.fail('Could not stat pagefile.sys')
