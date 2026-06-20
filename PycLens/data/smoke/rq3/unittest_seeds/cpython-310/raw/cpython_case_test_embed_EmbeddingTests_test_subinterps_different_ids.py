# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: EmbeddingTests_test_subinterps_different_ids

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for run in self.run_repeated_init_and_subinterpreters():
        (main, *subs, _) = run
        mainid = int(main.id)
        for (i, sub) in enumerate(subs):
            self.assertEqual(sub.id, str(mainid + i + 1))
