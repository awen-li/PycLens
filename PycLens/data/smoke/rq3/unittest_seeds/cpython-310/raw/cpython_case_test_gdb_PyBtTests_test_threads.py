# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyBtTests_test_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cmd = "\nfrom threading import Thread\n\nclass TestThread(Thread):\n    # These threads would run forever, but we'll interrupt things with the\n    # debugger\n    def run(self):\n        i = 0\n        while 1:\n             i += 1\n\nt = {}\nfor i in range(4):\n   t[i] = TestThread()\n   t[i].start()\n\n# Trigger a breakpoint on the main thread\nid(42)\n\n"
    gdb_output = self.get_stack_trace(cmd, cmds_after_breakpoint=['thread apply all py-bt'])
    self.assertIn('Waiting for the GIL', gdb_output)
    gdb_output = self.get_stack_trace(cmd, cmds_after_breakpoint=['thread apply all py-bt-full'])
    self.assertIn('Waiting for the GIL', gdb_output)
