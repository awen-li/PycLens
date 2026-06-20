# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: MemoryHandlerTest_test_race_between_set_target_and_flush

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MockRaceConditionHandler:

        def __init__(self, mem_hdlr):
            self.mem_hdlr = mem_hdlr
            self.threads = []

        def removeTarget(self):
            self.mem_hdlr.setTarget(None)

        def handle(self, msg):
            thread = threading.Thread(target=self.removeTarget)
            self.threads.append(thread)
            thread.start()
    target = MockRaceConditionHandler(self.mem_hdlr)
    try:
        self.mem_hdlr.setTarget(target)
        for _ in range(10):
            time.sleep(0.005)
            self.mem_logger.info('not flushed')
            self.mem_logger.warning('flushed')
    finally:
        for thread in target.threads:
            threading_helper.join_thread(thread)
