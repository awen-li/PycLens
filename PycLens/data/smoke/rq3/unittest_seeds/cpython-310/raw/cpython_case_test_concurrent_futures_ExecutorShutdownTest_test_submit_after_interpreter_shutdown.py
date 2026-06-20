# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorShutdownTest_test_submit_after_interpreter_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-c', 'if 1:\n            import atexit\n            @atexit.register\n            def run_last():\n                try:\n                    t.submit(id, None)\n                except RuntimeError:\n                    print("runtime-error")\n                    raise\n            from concurrent.futures import {executor_type}\n            if __name__ == "__main__":\n                context = \'{context}\'\n                if not context:\n                    t = {executor_type}(5)\n                else:\n                    from multiprocessing import get_context\n                    context = get_context(context)\n                    t = {executor_type}(5, mp_context=context)\n                    t.submit(id, 42).result()\n            '.format(executor_type=self.executor_type.__name__, context=getattr(self, 'ctx', '')))
    self.assertIn('RuntimeError: cannot schedule new futures', err.decode())
    self.assertEqual(out.strip(), b'runtime-error')
