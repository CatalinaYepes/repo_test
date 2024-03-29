#!/bin/bash

oq engine --run job_rup-Melgar_et_al_2018_gmpe-GEM_seismic.ini --log-file log_rup-Melgar_et_al_2018_gmpe-GEM_seismic.txt
oq engine --run job_rup-Melgar_et_al_2018_gmpe-GEM_all.ini --log-file log_rup-Melgar_et_al_2018_gmpe-GEM_all.txt
oq engine --run job_rup-Melgar_et_al_2018_gmpe-USGS_seismic.ini --log-file log_rup-Melgar_et_al_2018_gmpe-USGS_seismic.txt
oq engine --run job_rup-Melgar_et_al_2018_gmpe-USGS_all.ini --log-file log_rup-Melgar_et_al_2018_gmpe-USGS_all.txt
oq engine --run job_rup-SSN_gmpe-GEM_seismic.ini --log-file log_rup-SSN_gmpe-GEM_seismic.txt
oq engine --run job_rup-SSN_gmpe-GEM_all.ini --log-file log_rup-SSN_gmpe-GEM_all.txt
oq engine --run job_rup-SSN_gmpe-USGS_seismic.ini --log-file log_rup-SSN_gmpe-USGS_seismic.txt
oq engine --run job_rup-SSN_gmpe-USGS_all.ini --log-file log_rup-SSN_gmpe-USGS_all.txt
oq engine --run job_rup-USGS_gmpe-GEM_seismic.ini --log-file log_rup-USGS_gmpe-GEM_seismic.txt
oq engine --run job_rup-USGS_gmpe-GEM_all.ini --log-file log_rup-USGS_gmpe-GEM_all.txt
oq engine --run job_rup-USGS_gmpe-USGS_seismic.ini --log-file log_rup-USGS_gmpe-USGS_seismic.txt
oq engine --run job_rup-USGS_gmpe-USGS_all.ini --log-file log_rup-USGS_gmpe-USGS_all.txt
