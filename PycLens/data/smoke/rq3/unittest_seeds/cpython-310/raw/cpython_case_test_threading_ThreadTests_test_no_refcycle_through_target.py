# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_no_refcycle_through_target

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class RunSelfFunction(object):

        def __init__(self, should_raise):
            self.should_raise = should_raise
            self.thread = threading.Thread(target=self._run, args=(self,), kwargs={'yet_another': self})
            self.thread.start()

        def _run(self, other_ref, yet_another):
            if self.should_raise:
                raise SystemExit
    restore_default_excepthook(self)
    cyclic_object = RunSelfFunction(should_raise=False)
    weak_cyclic_object = weakref.ref(cyclic_object)
    cyclic_object.thread.join()
    del cyclic_object
    self.assertIsNone(weak_cyclic_object(), msg='%d references still around' % sys.getrefcount(weak_cyclic_object()))
    raising_cyclic_object = RunSelfFunction(should_raise=True)
    weak_raising_cyclic_object = weakref.ref(raising_cyclic_object)
    raising_cyclic_object.thread.join()
    del raising_cyclic_object
    self.assertIsNone(weak_raising_cyclic_object(), msg='%d references still around' % sys.getrefcount(weak_raising_cyclic_object()))
