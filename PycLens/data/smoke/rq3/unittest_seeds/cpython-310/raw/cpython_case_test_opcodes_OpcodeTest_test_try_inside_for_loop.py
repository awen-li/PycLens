# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_opcodes.py
# case: OpcodeTest_test_try_inside_for_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 0
    for i in range(10):
        n = n + i
        try:
            1 / 0
        except NameError:
            pass
        except ZeroDivisionError:
            pass
        except TypeError:
            pass
        try:
            pass
        except:
            pass
        try:
            pass
        finally:
            pass
        n = n + i
    if n != 90:
        self.fail('try inside for')
