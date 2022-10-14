import time

import numpy
import test
import tools
import train

modelPath = f"models/{int(time.time())}"

print(modelPath)
print("Formatting")

# tools.format("numpy/train_basic", 0, 5000)
# tools.format("numpy/test_basic", 10000, 500)

# tools.format_given_result_turn("numpy/train_basic", 0, 20000,20000,0)
# tools.format_given_result_turn_skip("numpy/train_mid", 40000, 20000,20000,0, 10)
# tools.format_given_result_turn("numpy/test_basic", 10000, 5000, 5000, 0)
# tools.combineDatasets("numpy/train_basic_x.npy", "numpy/train_basic_y.npy", "numpy/train_mid_x.npy", "numpy/train_mid_y.npy", "numpy/combined")


tools.format_given_result_turn_skip("numpy/train_mid_tie", 0, 300000, 300000, 300000, 0)
tools.format_given_result_turn_skip("numpy/test_mid_tie", 100000, 500, 500, 500, 10)

print("Training")
train.run_train(modelPath, 
    "numpy/train_mid_tie_x.npy",
    "numpy/train_mid_tie_y.npy",
    10)

print("Testing")
test.run_test(modelPath, 
    "numpy/test_mid_tie_x.npy", 
    "numpy/test_mid_tie_y.npy")

# tools.format_mate_in_1()