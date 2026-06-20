# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_pop_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = []
    with self.exit_stack() as stack:

        @stack.callback
        def _exit():
            result.append(3)
        self.assertIsNotNone(_exit)
        new_stack = stack.pop_all()
        result.append(1)
    result.append(2)
    new_stack.close()
    self.assertEqual(result, [1, 2, 3])
