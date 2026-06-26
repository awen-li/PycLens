# Source Generated with Decompyle++
# File: cpython-310-ede5174b77bb.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import threading
    import traceback
    entered_g = threading.Event()
    leave_g = threading.Event()
    thread_info = []
    
    def f123():
        g455()

    
    def g455():
        thread_info.append(threading.get_ident())
        entered_g.set()
    # WARNING: Decompyle incomplete

    t = threading.Thread(f123, **('target',))
    t.start()
    entered_g.wait()
    self.assertEqual(len(thread_info), 1)
    thread_id = thread_info[0]
    d = sys._current_exceptions()
    for tid in d:
        self.assertIsInstance(tid, int)
        self.assertGreater(tid, 0)
    main_id = threading.get_ident()
    self.assertIn(main_id, d)
    self.assertIn(thread_id, d)
    (None, None, None)(d.pop, main_id())
    (exc_type, exc_value, exc_tb) = d.pop(thread_id)
    stack = traceback.extract_stack(exc_tb.tb_frame)
    for filename, lineno, funcname, sourceline in enumerate(stack):
        if funcname == 'f123':
            pass
        
        self.fail("didn't find f123() on thread's call stack")
        self.assertEqual(sourceline, 'g456()')
        (filename, lineno, funcname, sourceline) = stack[i + 1]
        self.assertEqual(funcname, 'g455')
        self.assertTrue(sourceline.startswith('if leave_g.wait('))
        leave_g.set()
        t.join()
        return None

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
