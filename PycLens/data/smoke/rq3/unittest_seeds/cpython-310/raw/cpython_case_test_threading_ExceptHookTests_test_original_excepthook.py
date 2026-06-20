# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ExceptHookTests_test_original_excepthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def run_thread():
        with support.captured_output('stderr') as output:
            thread = ThreadRunFail(name='excepthook thread')
            thread.start()
            thread.join()
        return output.getvalue()

    def threading_hook(args):
        print('Running a thread failed', file=sys.stderr)
    default_output = run_thread()
    with support.swap_attr(threading, 'excepthook', threading_hook):
        custom_hook_output = run_thread()
        threading.excepthook = threading.__excepthook__
        recovered_output = run_thread()
    self.assertEqual(default_output, recovered_output)
    self.assertNotEqual(default_output, custom_hook_output)
    self.assertEqual(custom_hook_output, 'Running a thread failed\n')
