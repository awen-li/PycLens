# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_enter_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestCM(object):

        def __enter__(self):
            result.append(1)

        def __exit__(self, *exc_details):
            result.append(3)
    result = []
    cm = TestCM()
    with self.exit_stack() as stack:

        @stack.callback
        def _exit():
            result.append(4)
        self.assertIsNotNone(_exit)
        stack.enter_context(cm)
        self.assertIs(stack._exit_callbacks[-1][1].__self__, cm)
        result.append(2)
    self.assertEqual(result, [1, 2, 3, 4])
