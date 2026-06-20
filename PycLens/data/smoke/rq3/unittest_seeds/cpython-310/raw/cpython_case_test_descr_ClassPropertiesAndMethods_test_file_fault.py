# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_file_fault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_stdout = sys.stdout

    class StdoutGuard:

        def __getattr__(self, attr):
            sys.stdout = sys.__stdout__
            raise RuntimeError('Premature access to sys.stdout.%s' % attr)
    sys.stdout = StdoutGuard()
    try:
        print('Oops!')
    except RuntimeError:
        pass
    else:
        self.fail("Didn't raise RuntimeError")
    finally:
        sys.stdout = test_stdout
