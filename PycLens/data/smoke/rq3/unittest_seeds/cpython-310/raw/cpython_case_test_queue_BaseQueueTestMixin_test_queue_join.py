# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_queue.py
# case: BaseQueueTestMixin_test_queue_join

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = self.type2test()
    self.queue_join_test(q)
    self.queue_join_test(q)
    try:
        q.task_done()
    except ValueError:
        pass
    else:
        self.fail('Did not detect task count going negative')
