event based risk
================

============== ===================
checksum32     515,431,980        
date           2019-02-18T08:36:47
engine_version 3.4.0-git9883ae17a5
============== ===================

num_sites = 7, num_levels = 1

Parameters
----------
=============================== ==================
calculation_mode                'event_based_risk'
number_of_logic_tree_samples    0                 
maximum_distance                {'default': 200.0}
investigation_time              10000.0           
ses_per_logic_tree_path         1                 
truncation_level                3.0               
rupture_mesh_spacing            2.0               
complex_fault_mesh_spacing      2.0               
width_of_mfd_bin                0.1               
area_source_discretization      None              
ground_motion_correlation_model 'JB2009'          
minimum_intensity               {}                
random_seed                     24                
master_seed                     42                
ses_seed                        42                
avg_losses                      True              
=============================== ==================

Input files
-----------
======================= ============================================================
Name                    File                                                        
======================= ============================================================
exposure                `exposure_model.xml <exposure_model.xml>`_                  
gsim_logic_tree         `gsim_logic_tree.xml <gsim_logic_tree.xml>`_                
job_ini                 `job.ini <job.ini>`_                                        
occupants_vulnerability `vulnerability_model.xml <vulnerability_model.xml>`_        
source_model_logic_tree `source_model_logic_tree.xml <source_model_logic_tree.xml>`_
======================= ============================================================

Composite source model
----------------------
========= ======= =============== ================
smlt_path weight  gsim_logic_tree num_realizations
========= ======= =============== ================
b1        1.00000 trivial(1)      1               
========= ======= =============== ================

Required parameters per tectonic region type
--------------------------------------------
====== ===================== ========= ========== ==========
grp_id gsims                 distances siteparams ruptparams
====== ===================== ========= ========== ==========
0      '[BooreAtkinson2008]' rjb       vs30       mag rake  
====== ===================== ========= ========== ==========

Realizations per (GRP, GSIM)
----------------------------

::

  <RlzsAssoc(size=1, rlzs=1)
  0,'[BooreAtkinson2008]': [0]>

Number of ruptures per tectonic region type
-------------------------------------------
================ ====== ==================== ============ ============
source_model     grp_id trt                  eff_ruptures tot_ruptures
================ ====== ==================== ============ ============
source_model.xml 0      Active Shallow Crust 482          482         
================ ====== ==================== ============ ============

Estimated data transfer for the avglosses
-----------------------------------------
7 asset(s) x 1 realization(s) x 1 loss type(s) x 1 losses x 8 bytes x 30 tasks = 1.64 KB

Exposure model
--------------
=============== ========
#assets         7       
#taxonomies     1       
deductibile     absolute
insurance_limit absolute
=============== ========

======== ======= ====== === === ========= ==========
taxonomy mean    stddev min max num_sites num_assets
tax1     1.00000 0.0    1   1   7         7         
======== ======= ====== === === ========= ==========

Slowest sources
---------------
====== ========= ==== ===== ===== ============ ========= ========== ========= ========= =======
grp_id source_id code gidx1 gidx2 num_ruptures calc_time split_time num_sites num_split weight 
====== ========= ==== ===== ===== ============ ========= ========== ========= ========= =======
0      1         S    0     2     482          0.03918   0.0        7.00000   1         2.00000
====== ========= ==== ===== ===== ============ ========= ========== ========= ========= =======

Computation times by source typology
------------------------------------
==== ========= ======
code calc_time counts
==== ========= ======
S    0.03918   1     
==== ========= ======

Information about the tasks
---------------------------
================== ========= ========= ========= ======= =======
operation-duration mean      stddev    min       max     outputs
read_source_models 0.00823   NaN       0.00823   0.00823 1      
only_filter        0.00456   NaN       0.00456   0.00456 1      
sample_ruptures    0.05868   NaN       0.05868   0.05868 1      
get_eid_rlz        9.926E-04 2.316E-04 8.035E-04 0.00180 28     
================== ========= ========= ========= ======= =======

Data transfer
-------------
================== ============================================= ========
task               sent                                          received
read_source_models converter=305 B fnames=116 B                  1.49 KB 
only_filter        srcs=1.12 KB srcfilter=253 B dummy=14 B       1.23 KB 
sample_ruptures    param=2.85 KB sources=1.29 KB srcfilter=220 B 68.68 KB
get_eid_rlz        self=54.66 KB                                 10.71 KB
================== ============================================= ========

Slowest operations
------------------
======================== ========= ========= ======
operation                time_sec  memory_mb counts
======================== ========= ========= ======
total sample_ruptures    0.05868   2.23828   1     
iter_ruptures            0.03869   0.0       1     
total get_eid_rlz        0.02779   0.25391   28    
total read_source_models 0.00823   0.20703   1     
saving ruptures          0.00482   0.0       1     
total only_filter        0.00456   1.43750   1     
store source_info        0.00216   0.0       1     
store source model       0.00190   0.0       1     
reading exposure         7.193E-04 0.0       1     
======================== ========= ========= ======