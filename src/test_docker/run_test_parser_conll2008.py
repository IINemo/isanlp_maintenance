from . import run_test_default

run_test = lambda *args, **kwargs: run_test_default.run_test(sleep_time=60, *args, **kwargs)

clean = run_test_default.clean
    