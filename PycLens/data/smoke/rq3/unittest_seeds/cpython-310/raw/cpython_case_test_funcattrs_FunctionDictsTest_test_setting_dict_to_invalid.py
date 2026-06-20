# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionDictsTest_test_setting_dict_to_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.cannot_set_attr(self.b, '__dict__', None, TypeError)
    from collections import UserDict
    d = UserDict({'known_attr': 7})
    self.cannot_set_attr(self.fi.a.__func__, '__dict__', d, TypeError)
