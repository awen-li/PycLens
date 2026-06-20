# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: AttributeErrorTests_test_getattr_has_name_and_obj_for_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def blech(self):
            return
    obj = A()
    try:
        obj.bluch()
    except AttributeError as exc:
        self.assertEqual('bluch', exc.name)
        self.assertEqual(obj, exc.obj)
