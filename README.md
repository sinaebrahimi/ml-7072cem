# ml-7072cem

Sina Ebrahimi assignments in **7072CEM** (Machine Learning) module for JanMay 2324 semester, Coventry University.

**Project Title:**

*Classifying 5G Network Slices Based on User Requirements and Charactersitics*

**Dataset Description: (imported from [Kaggle](https://www.kaggle.com/datasets/amohankumar/network-slicing-in-5g))**

*16 Features (X):*

1. LTE/5g Category - User Equipment categories or classes to define the performance specifications
2. Time (NO DESCRIPTION WAS AVAILABLE)
3. Packet Loss Rate - number of packets not received divided by the total number of packets sent.
4. Packet Delay - The time for a packet to be received.
5. IoT (NO DESCRIPTION WAS AVAILABLE)
6. LTE/5G (NO DESCRIPTION WAS AVAILABLE)
7. GBR - Guaranteed Bit Rate
8. Non-GBR - Non-Guaranteed Bit Rate
9. AR/VR/Gaming (NO DESCRIPTION WAS AVAILABLE)
10. Healthcare - Usage in Healthcare (1 or 0)
11. Industry 4.0 - Usage in Digital Enterprises(1 or 0)
12. IoT Devices - Usage
13. Public Safety - Usage for public welfare and safety purposes (1 or 0)
14. Smart City & Home - usage in daily household chores
15. Smart Transportation - usage in public transportation
16. Smartphone - whether used for smartphone cellular data

*The target variable (y) is as follows:*

**Slice type **- network configuration that allows multiple networks (virtualized and independent) (1: eMBB, 2: URLLC, 3: mMTC)


The objective is to predict the slice type of the user (in the test set) based on the different characteristics outlined in the features. This can yield various advantages. For instance, this data can be utilized in the resource allocation mechanisms of 5G. By categorizing the user's slice type based on these characteristics, the algorithm will perform slice-aware resource allocation in the Radio Access Network (RAN) and/or Core Network (CN) for each user according to their slice type. Put simply, this exemplar algorithm depends on the slice type to determine the allocation of resources to the user.

This paper specifically examines the initial phase of the algorithm mentioned earlier. During this phase, we anticipate the users' slice type based on their characteristics, prior to the user initiating any signaling requests to the network controller to indicate their slice type. This information may be inaccessible for several reasons, such as the absence of slicing support in the User Equipment (UE). Another situation in which we could employ this categorization is to decrease the number of signaling messages exchanged between the user and the network, thereby minimizing user latency.
