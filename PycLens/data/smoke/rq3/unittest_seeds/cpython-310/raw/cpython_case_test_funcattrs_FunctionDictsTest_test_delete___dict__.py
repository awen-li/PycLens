# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionDictsTest_test_delete___dict__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        del self.b.__dict__
    except TypeError:
        pass
    else:
        self.fail('deleting function dictionary should raise TypeError')
