# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: NTEventLogHandlerTest_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    logtype = 'Application'
    elh = win32evtlog.OpenEventLog(None, logtype)
    num_recs = win32evtlog.GetNumberOfEventLogRecords(elh)
    try:
        h = logging.handlers.NTEventLogHandler('test_logging')
    except pywintypes.error as e:
        if e.winerror == 5:
            raise unittest.SkipTest('Insufficient privileges to run test')
        raise
    r = logging.makeLogRecord({'msg': 'Test Log Message'})
    h.handle(r)
    h.close()
    self.assertLess(num_recs, win32evtlog.GetNumberOfEventLogRecords(elh))
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    found = False
    GO_BACK = 100
    events = win32evtlog.ReadEventLog(elh, flags, GO_BACK)
    for e in events:
        if e.SourceName != 'test_logging':
            continue
        msg = win32evtlogutil.SafeFormatMessage(e, logtype)
        if msg != 'Test Log Message\r\n':
            continue
        found = True
        break
    msg = 'Record not found in event log, went back %d records' % GO_BACK
    self.assertTrue(found, msg=msg)
