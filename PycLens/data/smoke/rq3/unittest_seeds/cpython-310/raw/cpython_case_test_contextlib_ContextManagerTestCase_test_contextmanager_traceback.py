# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_contextmanager_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @contextmanager
    def f():
        yield
    try:
        with f():
            1 / 0
    except ZeroDivisionError as e:
        frames = traceback.extract_tb(e.__traceback__)
    self.assertEqual(len(frames), 1)
    self.assertEqual(frames[0].name, 'test_contextmanager_traceback')
    self.assertEqual(frames[0].line, '1/0')

    class RuntimeErrorSubclass(RuntimeError):
        pass
    try:
        with f():
            raise RuntimeErrorSubclass(42)
    except RuntimeErrorSubclass as e:
        frames = traceback.extract_tb(e.__traceback__)
    self.assertEqual(len(frames), 1)
    self.assertEqual(frames[0].name, 'test_contextmanager_traceback')
    self.assertEqual(frames[0].line, 'raise RuntimeErrorSubclass(42)')

    class StopIterationSubclass(StopIteration):
        pass
    for stop_exc in (StopIteration('spam'), StopIterationSubclass('spam')):
        with self.subTest(type=type(stop_exc)):
            try:
                with f():
                    raise stop_exc
            except type(stop_exc) as e:
                self.assertIs(e, stop_exc)
                frames = traceback.extract_tb(e.__traceback__)
            else:
                self.fail(f'{stop_exc} was suppressed')
            self.assertEqual(len(frames), 1)
            self.assertEqual(frames[0].name, 'test_contextmanager_traceback')
            self.assertEqual(frames[0].line, 'raise stop_exc')
