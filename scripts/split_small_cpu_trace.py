import pandas as pd

DATASET_LOCATION = "../datasets/small-imc21/"
cpu_df = pd.read_csv(DATASET_LOCATION + "s_VM_CPU.csv")
cpu_df = cpu_df.sort_values(by="report_ts")

subset_df = cpu_df[cpu_df["report_ts"] < 1592179200]
subset_df.reset_index(drop=True, inplace=True)

subset_df.to_csv(DATASET_LOCATION + "s_VM_CPU_31.05.2020-14.06.2020.csv", index=False)

subset_df = cpu_df[cpu_df["report_ts"] >= 1592179200]
subset_df.reset_index(drop=True, inplace=True)
subset_df.to_csv(DATASET_LOCATION + "s_VM_CPU_15.06.2020-30.06.2020.csv", index=False)