# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_boolean_target

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BooleanTarget(object):

        def __init__(self):
            self.ran = False

        def __bool__(self):
            return False

        def __call__(self):
            self.ran = True
    target = BooleanTarget()
    thread = threading.Thread(target=target)
    thread.start()
    thread.join()
    self.assertTrue(target.ran)
