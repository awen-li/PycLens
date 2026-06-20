# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_instance_bypass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Example(object):
        pass
    cm = Example()
    cm.__exit__ = object()
    stack = self.exit_stack()
    self.assertRaises(AttributeError, stack.enter_context, cm)
    stack.push(cm)
    self.assertIs(stack._exit_callbacks[-1][1], cm)
