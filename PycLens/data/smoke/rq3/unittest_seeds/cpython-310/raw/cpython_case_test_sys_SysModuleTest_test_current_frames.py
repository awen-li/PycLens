# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_current_frames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import threading
    import traceback
    entered_g = threading.Event()
    leave_g = threading.Event()
    thread_info = []

    def f123():
        g456()

    def g456():
        thread_info.append(threading.get_ident())
        entered_g.set()
        leave_g.wait()
    t = threading.Thread(target=f123)
    t.start()
    entered_g.wait()
    self.assertEqual(len(thread_info), 1)
    thread_id = thread_info[0]
    d = sys._current_frames()
    for tid in d:
        self.assertIsInstance(tid, int)
        self.assertGreater(tid, 0)
    main_id = threading.get_ident()
    self.assertIn(main_id, d)
    self.assertIn(thread_id, d)
    frame = d.pop(main_id)
    self.assertTrue(frame is sys._getframe())
    frame = d.pop(thread_id)
    stack = traceback.extract_stack(frame)
    for (i, (filename, lineno, funcname, sourceline)) in enumerate(stack):
        if funcname == 'f123':
            break
    else:
        self.fail("didn't find f123() on thread's call stack")
    self.assertEqual(sourceline, 'g456()')
    (filename, lineno, funcname, sourceline) = stack[i + 1]
    self.assertEqual(funcname, 'g456')
    self.assertIn(sourceline, ['leave_g.wait()', 'entered_g.set()'])
    leave_g.set()
    t.join()
