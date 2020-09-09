import numpy as np, matplotlib.pyplot as plt
with sns.color_palette("husl", 8):
   _ = plt.plot(np.c_[np.zeros(8), np.arange(8)].T)
