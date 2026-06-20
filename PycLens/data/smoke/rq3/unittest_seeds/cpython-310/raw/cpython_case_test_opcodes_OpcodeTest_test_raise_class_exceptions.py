# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_opcodes.py
# case: OpcodeTest_test_raise_class_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AClass(Exception):
        pass

    class BClass(AClass):
        pass

    class CClass(Exception):
        pass

    class DClass(AClass):

        def __init__(self, ignore):
            pass
    try:
        raise AClass()
    except:
        pass
    try:
        raise AClass()
    except AClass:
        pass
    try:
        raise BClass()
    except AClass:
        pass
    try:
        raise BClass()
    except CClass:
        self.fail()
    except:
        pass
    a = AClass()
    b = BClass()
    try:
        raise b
    except AClass as v:
        self.assertEqual(v, b)
    else:
        self.fail('no exception')
    try:
        raise DClass(a)
    except DClass as v:
        self.assertIsInstance(v, DClass)
    else:
        self.fail('no exception')
