# data-processing-analysis
This code aims to use data collected in real scenerios [EdgeWorkloadsTraces](https://github.com/xumengwei/EdgeWorkloadsTraces) to improve the simulation for the optimization problem raised on the paper [A robust optimization approach for placement of applications in edge computing considering latency uncertainty](https://www.sciencedirect.com/science/article/pii/S0305048324000318#sec3).

Since the dataset is not allowed to share, if you need access, please contact the owner directly.

This simulation is based on small-sized network, which means a network with 5 edge nodes and 10 regions. The dataset includes a bunch of sites from different cities in China. In order to pick out the optimum 10 cities to analyze their average network latency, the selection is limited to the eastern region of China. Additionally, 5 of these 10 cities should have at least 2 sites, one of which will be regarded as an edge node. According to our analysis, BGP sites are not suitable to be included because those would lead to excessive variance.  

Before the simulation starts, we need to input average network latency for each pair of regions and edge nodes, and the proportion of demand of each region. For average network latency, it is calculated from the RTT values in the dataset. One-week data is proved to be representative enough to show their CDF patterns. Compared to the patterns of the whole 1-month dataset, the only difference is the length of the tails, which is inevitable. For the proportion of demand, there are no direct clues, so it is estimated from the proportion of the total number of cores of the PMs in the 10 different cities.

During the simulation, 
