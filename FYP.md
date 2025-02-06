data/constant.py -> change row anchors depending on data set

data/dataloader.py -> image preprocessing, train/test split
trg is done on last img of every clip (20.png)

testing configs -> mycarry_culane.py & mycarry_tusimple.py

fyp_demo.py
python fyp_demo.py configs/mycarry_culane.py --test_model culane_18.pth
python fyp_demo.py configs/mycarry_tusimple.py --test_model tusimple_18.pth

### MODEL RUNNING REQUIREMENTS
1) folder with video frames e.g. test_00
2) .txt with files paths e.g. test_00.txt
output - file w annotated video framese/.avi video