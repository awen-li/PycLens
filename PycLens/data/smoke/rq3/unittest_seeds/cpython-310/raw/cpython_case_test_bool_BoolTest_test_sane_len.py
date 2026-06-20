# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_sane_len

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for badval in ['illegal', -1, 1 << 32]:

        class A:

            def __len__(self):
                return badval
        try:
            bool(A())
        except Exception as e_bool:
            try:
                len(A())
            except Exception as e_len:
                self.assertEqual(str(e_bool), str(e_len))
