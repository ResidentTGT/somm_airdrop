import os
import math
import collections
import numpy as np
import pandas as pd
from tqdm import tqdm
from typing import Dict, List, Mapping, Sequence, Union
import json
import time
from pathlib import Path
from utils import plot_reward_distribution

# In terms of SOMM
OLD_PARTICIPATION_REWARD = 3200000
NEW_PARTICIPATION_REWARD = 4000000

# Transform to uSOMM
OLD_PARTICIPATION_REWARD = 3200000 * 1e6
NEW_PARTICIPATION_REWARD = 4000000 * 1e6

Wallet = str

wallet_rewards: Dict[Wallet, float] = {}

json_path = Path('../token_rewards/somm_app_rewards_usomm.json').resolve()
json_path.parent.mkdir(exist_ok=True, parents=True)

with open(json_path, 'r') as fp:
    wallet_rewards = json.load(fp)

diff = (NEW_PARTICIPATION_REWARD - OLD_PARTICIPATION_REWARD)/len(wallet_rewards)
print("Difference in tokens for each account:", diff/1e6)

for wallet, reward in wallet_rewards.items():
    wallet_rewards[wallet] = round(reward+diff)

print("Sum of sommelier app rewards: ",
      round(sum(wallet_rewards.values())/1e6))

json_path = Path('../token_rewards/new_somm_app_rewards_usomm.json').resolve()
json_path.parent.mkdir(exist_ok=True, parents=True)

with open(json_path, 'w') as fp:
    json.dump(wallet_rewards, fp)

for wallet, reward in wallet_rewards.items():
    wallet_rewards[wallet] = reward/1e6   

plot_reward_distribution(wallet_rewards, save_path=Path(
        "../plots/new_somm_app_rewards.png").resolve(), title="Sommelier App Users SOMM Rewards")
