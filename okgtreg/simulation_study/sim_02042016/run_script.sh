#!/usr/bin/env bash

python -u script.py 1 > script-model-1-sim100.out
python -u script.py 2 > script-model-2-sim100.out
python -u script.py 3 > script-model-3-sim100.out
python -u script.py 4 > script-model-4-sim100.out

# nohup parallel -j 4 < run_script.sh &