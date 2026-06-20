# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_old_threading_api

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = threading.Thread()
    with self.assertWarnsRegex(DeprecationWarning, 'get the daemon attribute'):
        t.isDaemon()
    with self.assertWarnsRegex(DeprecationWarning, 'set the daemon attribute'):
        t.setDaemon(True)
    with self.assertWarnsRegex(DeprecationWarning, 'get the name attribute'):
        t.getName()
    with self.assertWarnsRegex(DeprecationWarning, 'set the name attribute'):
        t.setName('name')
    e = threading.Event()
    with self.assertWarnsRegex(DeprecationWarning, 'use is_set()'):
        e.isSet()
    cond = threading.Condition()
    cond.acquire()
    with self.assertWarnsRegex(DeprecationWarning, 'use notify_all()'):
        cond.notifyAll()
    with self.assertWarnsRegex(DeprecationWarning, 'use active_count()'):
        threading.activeCount()
    with self.assertWarnsRegex(DeprecationWarning, 'use current_thread()'):
        threading.currentThread()
