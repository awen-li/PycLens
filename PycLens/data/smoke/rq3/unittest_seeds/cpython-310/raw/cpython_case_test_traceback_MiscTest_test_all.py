# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: MiscTest_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = set()
    denylist = {'print_list'}
    for name in dir(traceback):
        if name.startswith('_') or name in denylist:
            continue
        module_object = getattr(traceback, name)
        if getattr(module_object, '__module__', None) == 'traceback':
            expected.add(name)
    self.assertCountEqual(traceback.__all__, expected)
