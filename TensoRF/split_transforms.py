import json
import os
import random
from pathlib import Path

# 配置
input_path = 'data/my_cup/transforms.json'
output_dir = Path('data/my_cup')
train_ratio = 0.8
val_ratio = 0.1  # 剩下的是 test

with open(input_path, 'r') as f:
    data = json.load(f)

frames = data['frames']
random.shuffle(frames)

n_total = len(frames)
n_train = int(n_total * train_ratio)
n_val = int(n_total * val_ratio)
n_test = n_total - n_train - n_val

frames_train = frames[:n_train]
frames_val = frames[n_train:n_train + n_val]
frames_test = frames[n_train + n_val:]

def write_split(name, frames):
    data_split = data.copy()
    data_split['frames'] = frames
    out_path = output_dir / f'transforms_{name}.json'
    with open(out_path, 'w') as f:
        json.dump(data_split, f, indent=2)
    print(f"Wrote {len(frames)} frames to {out_path}")

write_split('train', frames_train)
write_split('val', frames_val)
write_split('test', frames_test)