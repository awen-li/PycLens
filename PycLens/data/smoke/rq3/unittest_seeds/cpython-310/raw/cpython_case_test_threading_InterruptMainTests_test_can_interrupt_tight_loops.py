# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: InterruptMainTests_test_can_interrupt_tight_loops

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cont = [True]
    started = [False]
    interrupted = [False]

    def worker(started, cont, interrupted):
        iterations = 100000000
        started[0] = True
        while cont[0]:
            if iterations:
                iterations -= 1
            else:
                return
            pass
        interrupted[0] = True
    t = threading.Thread(target=worker, args=(started, cont, interrupted))
    t.start()
    while not started[0]:
        pass
    cont[0] = False
    t.join()
    self.assertTrue(interrupted[0])
