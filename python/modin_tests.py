"""
Demonstrates Pandas vs Modin performance numbers.
Examples taken from Intel official Modin docs page:
https://www.intel.com/content/www/us/en/developer/articles/technical/modin-step-by-step-guide-to-accelerating-pandas.html#gs.o2d2nt
"""

import modin.pandas as md
# import numpy as np
import pandas as pd
from time import time

# Generate once and comment out
# arr = np.random.randint(low=10, high=1000, size=(2**15, 2**10))
# np.savetxt("data.csv", arr, delimiter=",")

df_pd = pd.read_csv("data.csv")
df_md = md.read_csv("data.csv")


# mean operation
start_pd = time()
df_pd.mean(axis=0)
end_pd = time()
diff_pd = end_pd - start_pd

start_md = time()
df_md.mean(axis=0)
end_md = time()
diff_md = end_md - start_md

print(f"Mean: Pandas: {diff_pd} seconds")
print(f"Mean: Modin: {diff_md} seconds")
print(f"Speed up: {round(diff_pd/diff_md, 4)}")
print("*" * 50)


# concat operation. Concat the dataframe to itself
start_pd = time()
pd.concat([df_pd, df_pd], axis=0)
end_pd = time()
diff_pd = end_pd - start_pd

start_md = time()
md.concat([df_md, df_md], axis=0)
end_md = time()
diff_md = end_md - start_md

print(f"Concat: Pandas: {diff_pd} seconds")
print(f"Concat: Modin: {diff_md} seconds")
print(f"Speed up: {round(diff_pd/diff_md, 4)}")
print("*" * 50)

# applymap
start_pd = time()
df_pd.applymap(lambda i: i*2)
end_pd = time()
diff_pd = end_pd - start_pd

start_md = time()
df_md.applymap(lambda i: i*2)

end_md = time()
diff_md = end_md - start_md

print(f"Applymap: Pandas: {diff_pd} seconds")
print(f"Applymap: Modin: {diff_md} seconds")
print(f"Speed up: {round(diff_pd/diff_md, 4)}")
print("*" * 50)

"""
Output:
Mean: Pandas: 0.1625680923461914 seconds
Mean: Modin: 0.07974386215209961 seconds
Speed up: 2.0386
**************************************************
Concat: Pandas: 0.29066920280456543 seconds
Concat: Modin: 0.018330812454223633 seconds
Speed up: 15.8569
**************************************************
Applymap: Pandas: 17.906212329864502 seconds
Applymap: Modin: 0.1000661849975586 seconds
Speed up: 178.9437
**************************************************
"""
