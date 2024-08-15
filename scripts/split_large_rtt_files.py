import pandas as pd
import numpy as np
import os


def split_rtt_file():
    for chunk in pd.read_csv(DATASET_LOCATION.rstrip("/") + "/SITE_RTT_clean.csv",
                             usecols=["from_site_id", "to_site_id", "rtt", "type", "biz_ts"],
                             chunksize=1000000,
                             dtype={"from_site_id": str,
                                    "to_site_id": str,
                                    "rtt": np.float32,
                                    "loss": np.float32,
                                    "type": str,
                                    "biz_ts": str}
                             ):
        df_by_from_site_id = chunk.groupby("from_site_id")
        for (site_id, side_id_df) in df_by_from_site_id:
            filename = DATASET_LOCATION + "/split-rtt-files/{}.csv".format(site_id)
            side_id_df.to_csv(filename, mode='a', header=not os.path.exists(filename))

        df_by_to_site_id = chunk.groupby("to_site_id")
        for (site_id, side_id_df) in df_by_to_site_id:
            filename = DATASET_LOCATION + "/split-rtt-files/{}.csv".format(site_id)
            side_id_df.to_csv(filename, mode='a', header=not os.path.exists(filename))


DATASET_LOCATION = "../datasets/large-imc21"
split_rtt_file()

