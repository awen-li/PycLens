# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LogRecordTest_test_optional

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = logging.makeLogRecord({})
    NOT_NONE = self.assertIsNotNone
    NOT_NONE(r.thread)
    NOT_NONE(r.threadName)
    NOT_NONE(r.process)
    NOT_NONE(r.processName)
    log_threads = logging.logThreads
    log_processes = logging.logProcesses
    log_multiprocessing = logging.logMultiprocessing
    try:
        logging.logThreads = False
        logging.logProcesses = False
        logging.logMultiprocessing = False
        r = logging.makeLogRecord({})
        NONE = self.assertIsNone
        NONE(r.thread)
        NONE(r.threadName)
        NONE(r.process)
        NONE(r.processName)
    finally:
        logging.logThreads = log_threads
        logging.logProcesses = log_processes
        logging.logMultiprocessing = log_multiprocessing
