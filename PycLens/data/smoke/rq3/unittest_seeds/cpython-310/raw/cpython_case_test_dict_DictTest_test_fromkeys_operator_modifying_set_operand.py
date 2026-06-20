# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_fromkeys_operator_modifying_set_operand

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(int):

        def __hash__(self):
            return 13

        def __eq__(self, other):
            if len(d) > 1:
                d.clear()
            return False
    d = {}
    d = {X(1), X(2)}
    try:
        dict.fromkeys(d)
    except RuntimeError:
        pass
