import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
import sys
from tqdm import tqdm
import re
from tqdm.contrib.concurrent import process_map
from multiprocessing import Pool

go_file = open(
    os.path.join(os.getcwd(), "data", "top100", "go", "dataset.jsonl"),
    encoding="utf-8",
    errors="ignore",
)
go_df = pd.read_json(
    go_file,
    encoding_errors="ignore",
    lines=True,
    orient="records",
    dtype={"msg": list, "added": list, "deleted": list},
)
