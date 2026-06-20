# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_getmembers_descriptors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):
        dd = _BrokenDataDescriptor()
        md = _BrokenMethodDescriptor()

    def pred_wrapper(pred):

        class Empty(object):
            pass

        def wrapped(x):
            if '__name__' in dir(x) and hasattr(Empty, x.__name__):
                return False
            return pred(x)
        return wrapped
    ismethoddescriptor = pred_wrapper(inspect.ismethoddescriptor)
    isdatadescriptor = pred_wrapper(inspect.isdatadescriptor)
    self.assertEqual(inspect.getmembers(A, ismethoddescriptor), [('md', A.__dict__['md'])])
    self.assertEqual(inspect.getmembers(A, isdatadescriptor), [('dd', A.__dict__['dd'])])

    class B(A):
        pass
    self.assertEqual(inspect.getmembers(B, ismethoddescriptor), [('md', A.__dict__['md'])])
    self.assertEqual(inspect.getmembers(B, isdatadescriptor), [('dd', A.__dict__['dd'])])
