# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertySubclassTests_test_slots_docstring_copy_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:

        class Foo(object):

            @PropertySubSlots
            def spam(self):
                """Trying to copy this docstring will raise an exception"""
                return 1
    except AttributeError:
        pass
    else:
        raise Exception('AttributeError not raised')
