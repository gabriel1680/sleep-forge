
import pyActigraphy

raw_atr = pyActigraphy.io.read_raw_atr(input_fname="./data/A15.txt")
print(dir(raw_atr.display_name))



