# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ExceptHookTests_test_custom_excepthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = None

    def hook(hook_args):
        nonlocal args
        args = hook_args
    try:
        with support.swap_attr(threading, 'excepthook', hook):
            thread = ThreadRunFail()
            thread.start()
            thread.join()
        self.assertEqual(args.exc_type, ValueError)
        self.assertEqual(str(args.exc_value), 'run failed')
        self.assertEqual(args.exc_traceback, args.exc_value.__traceback__)
        self.assertIs(args.thread, thread)
    finally:
        args = None
