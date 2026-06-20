# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorShutdownTest_test_interpreter_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-c', 'if 1:\n            from concurrent.futures import {executor_type}\n            from time import sleep\n            from test.test_concurrent_futures import sleep_and_print\n            if __name__ == "__main__":\n                context = \'{context}\'\n                if context == "":\n                    t = {executor_type}(5)\n                else:\n                    from multiprocessing import get_context\n                    context = get_context(context)\n                    t = {executor_type}(5, mp_context=context)\n                t.submit(sleep_and_print, 1.0, "apple")\n            '.format(executor_type=self.executor_type.__name__, context=getattr(self, 'ctx', '')))
    self.assertFalse(err)
    self.assertEqual(out.strip(), b'apple')
