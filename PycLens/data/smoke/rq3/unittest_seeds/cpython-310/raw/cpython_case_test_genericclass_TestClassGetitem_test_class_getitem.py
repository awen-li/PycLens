# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestClassGetitem_test_class_getitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    getitem_args = []

    class C:

        def __class_getitem__(*args, **kwargs):
            getitem_args.extend([args, kwargs])
            return None
    C[int, str]
    self.assertEqual(getitem_args[0], (C, (int, str)))
    self.assertEqual(getitem_args[1], {})
