"""Re-run the whole Mach 3 LO fighter entry analysis.

Usage (from any directory; path has spaces, so quote it):
    python3 "<...>/calc/run_all.py"
Requires Python >= 3.9 and numpy; matplotlib optional (plots skipped if missing).
Outputs: calc/out/*.md, *.csv, *.json, *.png. All inputs live in assumptions.py.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(HERE)

import assumptions  # noqa: E402
import step1_atmos_thermal  # noqa: E402
import step2_constraints  # noqa: E402
import step3_sizing  # noqa: E402
import step4_sanity  # noqa: E402

if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    with open(os.path.join(HERE, 'out', 'assumptions_register.md'), 'w') as f:
        f.write('# Assumption register (generated from assumptions.py)\n\n' + assumptions.dump_markdown() + '\n')
    for step in (step1_atmos_thermal, step2_constraints, step3_sizing, step4_sanity):
        print(f'\n===== {step.__name__} =====')
        step.main()
    print('\nAll outputs written to', os.path.join(HERE, 'out'))
