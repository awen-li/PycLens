# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LogRecordTest_test_multiprocessing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    multiprocessing_imported = 'multiprocessing' in sys.modules
    try:
        self.assertEqual(logging.logMultiprocessing, True)
        LOG_MULTI_PROCESSING = True
        r = logging.makeLogRecord({})
        self.assertEqual(r.processName, 'MainProcess')
        results = self._extract_logrecord_process_name(1, LOG_MULTI_PROCESSING)
        self.assertEqual('MainProcess', results['processName'])
        self.assertEqual('MainProcess', results['r1.processName'])
        self.assertEqual('MainProcess', results['r2.processName'])
        import multiprocessing
        (parent_conn, child_conn) = multiprocessing.Pipe()
        p = multiprocessing.Process(target=self._extract_logrecord_process_name, args=(2, LOG_MULTI_PROCESSING, child_conn))
        p.start()
        results = parent_conn.recv()
        self.assertNotEqual('MainProcess', results['processName'])
        self.assertEqual(results['processName'], results['r1.processName'])
        self.assertEqual('MainProcess', results['r2.processName'])
        p.join()
    finally:
        if multiprocessing_imported:
            import multiprocessing
