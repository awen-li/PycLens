# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_gc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_fatal_error('\n            import faulthandler\n            import gc\n            import sys\n\n            faulthandler.enable()\n\n            class RefCycle:\n                def __del__(self):\n                    faulthandler._sigsegv()\n\n            # create a reference cycle which triggers a fatal\n            # error in a destructor\n            a = RefCycle()\n            b = RefCycle()\n            a.b = b\n            b.a = a\n\n            # Delete the objects, not the cycle\n            a = None\n            b = None\n\n            # Break the reference cycle: call __del__()\n            gc.collect()\n\n            # Should not reach this line\n            print("exit", file=sys.stderr)\n            ', 9, 'Segmentation fault', function='__del__', garbage_collecting=True)
