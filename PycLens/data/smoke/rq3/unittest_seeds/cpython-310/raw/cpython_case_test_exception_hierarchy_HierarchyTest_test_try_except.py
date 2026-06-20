# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_hierarchy.py
# case: HierarchyTest_test_try_except

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = 'some_hopefully_non_existing_file'
    try:
        open(filename)
    except FileNotFoundError:
        pass
    else:
        self.fail('should have raised a FileNotFoundError')
    self.assertFalse(os.path.exists(filename))
    try:
        os.unlink(filename)
    except FileNotFoundError:
        pass
    else:
        self.fail('should have raised a FileNotFoundError')
