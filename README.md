# data-processing-analysis
This code aims to use data collected in real scenerios [EdgeWorkloadsTraces](https://github.com/xumengwei/EdgeWorkloadsTraces) to improve the simulation for the optimization problem raised on the paper [A robust optimization approach for placement of applications in edge computing considering latency uncertainty](https://www.sciencedirect.com/science/article/pii/S0305048324000318#sec3).

Since the dataset is not allowed to share, if you need access, please contact the owner directly.

This simulation is based on small-sized network, which means a network with 5 edge nodes and 10 regions. The dataset includes a bunch of sites from different cities in China. In order to pick out the optimum 10 cities to analyze their average network latency, the selection is limited to the eastern region of China. Additionally, 5 of these 10 cities should have at least 2 sites, one of which will be regarded as an edge node. According to our analysis, BGP sites are not suitable to be included because those would lead to excessive variance. 

The selected sites are as following:

`dc_ids = ['shanghai-telecom', 'wuxi-telecom_unicom_cmcc', 'suzhou-telecom', 'wuhan-telecom', 'xiamen-telecom']`

`region_ids = ['shanghai-telecom-2', 'wuxi-telecom-2', 'suzhou-telecom-2', 'wuhan-telecom-3', 'xiamen-telecom_unicom_cmcc', 'jinan-telecom', 'wuhu-telecom', 'qingdao-telecom', 'wenzhou-telecom', 'hangzhou-telecom']`

Before the simulation starts, we need to input average network latency for each pair of regions and edge nodes, and the proportion of demand of each region. For average network latency, it is calculated from the RTT values in the dataset. One-week data is proved to be representative enough to show their CDF patterns. Compared to the patterns of the whole 1-month dataset, the only difference is the length of the tails, which is inevitable. For the proportion of demand, there are no direct clues, so it is estimated from the proportion of the total number of cores of the PMs in the 10 different cities.

Average latency is generated in `/notebooks/create-latency-matrix.ipynb`; the proportion of demand is generated in `/notebooks/demand-estimate.ipynb`.

During the simulation, network latency for each pair of regions and edge nodes needs to be input repetitively in order to evaluate the accuracy of the solution of the optimization problem. This part of work is based on Ekaterina's contribution [network-latency-analysis](https://github.com/qubelka/network-latency-analysis/tree/main). Here we use a list of various distributions to fit for each pair of edge nodes respectively within one week. First, the distribution methods whose `p > 0.05` are sorted out. Then the top 5 methods with most occurrences across all the links are further selected: `{'fisk', 'genpareto', 'nakagami', 'gamma'}`.

For the process of selection and the comparison of the distributions, they are generated in `/notebooks/create-latency-matrix.ipynb`. The plots are saved in `/datasets/split-rtt-files/cleandata/all-dist`.
