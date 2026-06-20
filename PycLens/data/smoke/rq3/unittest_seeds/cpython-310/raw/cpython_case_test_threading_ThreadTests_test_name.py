# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        pass
    thread = threading.Thread(name='myname1')
    self.assertEqual(thread.name, 'myname1')
    thread = threading.Thread(name=123)
    self.assertEqual(thread.name, '123')
    thread = threading.Thread(target=func, name='myname2')
    self.assertEqual(thread.name, 'myname2')
    with mock.patch.object(threading, '_counter', return_value=2):
        thread = threading.Thread(name='')
        self.assertEqual(thread.name, 'Thread-2')
    with mock.patch.object(threading, '_counter', return_value=3):
        thread = threading.Thread()
        self.assertEqual(thread.name, 'Thread-3')
    with mock.patch.object(threading, '_counter', return_value=5):
        thread = threading.Thread(target=func)
        self.assertEqual(thread.name, 'Thread-5 (func)')
