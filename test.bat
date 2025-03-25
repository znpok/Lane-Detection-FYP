@echo off
echo Running extraction script...

python vid_preprocess.py
python fyp_demo_auto.py configs/mycarry_culane.py --test_model culane_18.pth