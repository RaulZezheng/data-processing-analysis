import pandas as pd
import os


def split_file(city_name):
    filename = DATASET_LOCATION.rstrip("/") + "/VM_CPU_{}.csv".format(city_name)
    if os.path.exists(filename):
        os.remove(filename)
    for chunk in pd.read_csv(DATASET_LOCATION.rstrip("/") + "/VM_CPU.csv",
                             # 'vm_id', 'site_id', 'pub_down_flow', 'pub_up_flow', 'pub_down_bw',
                             # 'pub_up_bw', 'pri_down_flow', 'pri_up_flow', 'pri_down_bw', 'pri_up_bw',
                             # 'report_ts'
                             chunksize=1000000,
                             ):
        shanghai_df = chunk.loc[chunk["site_id"].str.startswith(city_name)].copy()
        shanghai_df.to_csv(filename, mode='a', header=not os.path.exists(filename), index=False, index_label=False)

DATASET_LOCATION = "../datasets/large-imc21"

cities = ["changzhou", "wuxi", "hefei", "wuhu", "suzhou", "shanghai"]
for city in cities:
    split_file(city)

