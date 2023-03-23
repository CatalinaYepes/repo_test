# 🤓 CONTRIBUTE TO THE EARTHQUAKE CONSEQUENCE DATABASE (ECD)

[[_TOC_]]

## Minimum information required in the ECD

If you would like to include information from a past earthquake event, 
please make sure to collect, at least, the following information and to
store it following the proposed structure and file naming.

<details><summary>👀 See the structure and minimum information required</summary>

```
Folder_Name
│   README.md
│   earthquake_information.csv  
│
└───Gorund_Shaking
│   │   README.md
│   │   ground_shaking.png
│   │
│   └───Recording_Stations
│   │   │   README.md
│   │   │   recording_stations.png
│   │   │   Stations_Unique.csv
│   │   │   Stations_Source1.csv
│   │   │   
│   │   │   referece_data1.csv
│   │   │   ...
│   │
│   └───Rupture
│   │   │   README.md
│   │   │   earthquake_ruptures.png
│   │   │   rupture_reference.pdf
│   │   │   
│   │   │   earthquake_rupture_model_.xml
│   │   │   ...
│   │
│   └───Shake_Map
│   │   │   README.md
│   │   │  ShakeMap_Ref1.png
│   │   │   …
│  
└───Impact
│   │   README.md
│   │   Impact_All_ID_0.csv
│   │   Impact_Buildings_ID_1.csv
│   │   Impact_Human_ID_1.csv
│   
└───OpenQuake_gmfs
│   │   README.md
│   │   site_model.csv
│   │   site_model_stations.csv
│   │   stationlist_all.csv
│   │   stationlist_seismic.csv
│   │   gmf_median_no_stations.png
│   │   gmf_median_with_stations_all.png
│   │   gmf_median_with_stations_seismic.png
│   │   site_model.png
│   │   gmpe_logic_tree_GEM.xml
│   │   gmpe_logic_tree_USGS.xml
│   │   job_no_stations.ini
│   │   job_with_stations_all.ini
│   │   job_with_stations_seismic.ini
│   │
│   └───Sensitivity
│   │   README.md
│   │   oq_calcs_summary.csv
│   │   log_rup-1.txt
│   │   log_rup-2.txt
│   │   log_rup-....txt
│   │   job_rup-1.ini
│   │   job_rup-2.ini
│   │   job_rup-....ini
│   │
└───References
│   │   README.md
│   │   file1.pdf
│   │   file2.pdf
│   │   ...
└─
```

</details>


## 0. Create a folder for the event

### 0.1 Get familiar with the event

A very complete compilation of the bibliography could be available at: http://www.isc.ac.uk/event_bibliography/bibsearch.php


### 0.2  Initialize the event folder using existing USGS data

(!!! Work in progress)

Using the notebook `0_initialize_folder_with_usgs.ipynb`, the modeller can indicate the name of the event, magnitude and USGS code to generate the initial structure.

The notebook:
 - Creates folders and subfolders with the USGS data
 - READMEs and summaries
 - Run basic notebooks (wip)


## 1. Ground_Shaking/Recording_Stations

Download all recording station information available. Store the information in the raw format, with the corresponding links in the `README.md` file.\
The original data should keep, as much as possible, the original format.\
_NOTE: USGS stores the information in the file `stations.json` available at `earthquake.usgs.gov/earthquakes/eventpage/EVENT_ID/shakemap/stations`.
If the file is empty, do not include it in the database._

- Using the notebook `1_station_json_usgs_to_csv.ipynb`, it is possible to create the `Stations_USGS.csv` file starting from the `stations.json`. The code filters the entrances with null values, adjusts the file to the standard format, and shows a map with the USGS reported recording stations (not saved).

- For the other sources of information, a file `Stations_SourceName.csv` should be generated.\
The files must include the columns `['STATION_ID', 'STATION_NAME', 'LATITUDE', 'LONGITUDE', 'STATION_TYPE', 'REFERENCES']`, and at least one intensity measure type with its corresponding uncertainty, for example, `['PGA_VALUE', 'PGA_LN_SIGMA']`.\
_NOTE: For MMI, the uncertainty should be in the form of `MMI_STDDEV`_

The table below presents an example of the suggested format.

| STATION_ID | STATION_NAME  | LATITUDE | LONGITUDE | STATION_TYPE | REFERENCES   | SOIL_TYPE | PGA_VALUE | PGA_LN_SIGMA | SA(0.3)_VALUE | SA(0.3)_LN_SIGMA | VS30 | VS30_TYPE |
|------------|---------------|----------|-----------|--------------|--------------|-----------|-----------|--------------|---------------|------------------|------|-----------|
| CANAP      | ANAPOIMA      | 4.5502   | -74.5141  | seismic      | Stations_SGC | ROCA      | 0.012341  | 0            | 0.015501      | 0                | 800  | measured  |
| CARBE      | ARBELAEZ      | 4.253    | -74.437   | seismic      | Stations_SGC | ROCA      | 0.023483  | 0            | 0.036099      | 0                | 800  | measured  |
| CARME      | ARMENIA       | 4.55     | -75.66    | seismic      | Stations_SGC | SUELO     | 0.011135  | 0            | 0.020943      | 0                | 400  | measured  |
| CBOG2      | GAVIOTAS      | 4.601    | -74.06    | seismic      | Stations_SGC | COLUVION  | 0.09279   | 0            | 0.127546      | 0                | 550  | measured  |
| CBUC1      | FLORIDABLANCA | 7.072    | -73.074   | seismic      | Stations_SGC | ROCA      | 0.018366  | 0            | 0.018812      | 0                | 800  | measured  |
| CIBA1      | IBAGUE        | 4.447    | -75.235   | seismic      | Stations_SGC | SUELO     | 0.019531  | 0            | 0.025926      | 0                | 324  | inferred  |
| CIBA3      | IBAGUE        | 4.4319   | -75.188   | seismic      | Stations_SGC | SUELO     | 0.013338  | 0            | 0.024665      | 0                | 539  | inferred  |


- Using the notebook `1_stations_unique.ipynb`, generate the `Stations_Unique.csv`.\
This notebook:
     - If only one source of data exists, then the `Stations_Unique.csv` file is not required.
     - If multiple data sources are available, it creates the `Stations_Unique.csv`, by combining all sources named `Stations_SourceName.csv` and using the priority indicated by the modeller (which should also be indicated in the README).
     - Generates the plot `recording_stations.png`

- To verify the integrity of the files, run ```pytest tests/test_stations.py``` from the home folder


## 2. Ground_Shaking/Ruptures

- Download all rupture information available. Store it in the raw format, with the corresponding links in the `README.md` file.\
_NOTE: USGS stores the information in the file `rupture.json` (named in the repo as `rupture_USGS.json`) available at https://earthquake.usgs.gov/earthquakes/eventpage/EVENT_CODE/shakemap/ under the `Downloads` drop-down menu._

- Using the notebook `2_rupture_usgs_json_to_oq_rupture_xml.ipynb`, it is possible to create the `earthquake_rupture_model_USGS.xml` file starting from the `rupture_USGS.json`. The code parses the information to follow the OpenQuake format.

- For the other sources of information, prepare the OpenQuake rupture file and save it as  `earthquake_rupture_model_SOURCE.xml`.\
_NOTE: multiple rupture definitions are available at http://equake-rc.info/SRCMOD/searchmodels/allevents/. The finite source rupture model, if not explicitly indicated, can be inferred from the FSP (`*.fsp`) link._  

- If only the nodal plane solutions are available, you can use the [IPT](https://platform.openquake.org/ipt/) to generate the fault plane (it uses the Wells and Coppersmith (1984) equations suggested in Table 2A).

- Using the notebook `2_ruptures_readme_.ipynb`, generate:
     - Generates the plot `earthquake_ruptures.png`
     - Adds/update `README.md` file to include image and rupture details.
     - Include in the `REAME.md` the rupture mecanism and tectonic region type. For reference:
```
Dip = 90°   Rake = 0°    ::  left-lateral strike-slip
Dip = 90°   Rake = 180°  ::  right lateral strike slip
Dip = 45°   Rake = 90°   ::  reverse fault
Dip = 45°   Rake = -90°  ::  normal fault

Other tips: Fault type (Strike-slip, Normal, Thrust/reverse) is derived from rake angle.
    - Rake angles within 30 of horizontal are strike-slip,
    - Rake angles from 30 to 150 are reverse, and 
    - Rake angles from -30 to -150 are normal. 
```


- _NOTE: When complex faults have the following error, the code [correct_complex_sources.py](https://github.com/gem/oq-engine/blob/master/openquake/engine/tools/correct_complex_sources.py) can be used to fix it._\
`Surface does not conform with Aki & Richards convention`


## 3. OpenQuake_gmfs

### 3.1 Create `stationslist.csv` file

This file is the result of filtering and post-processing the `Stations_Unique.csv` file, available in the Recording_Stations folder.

Using the notebook `3_stationslist.ipynb`, it is possible to create the `stationslist.csv` file. The code adjusts the existing data to follow the OpenQuake format.\
This notebook:
- Only selects rows that have no-empty IMT values
- Add VS30 data using reference datasets. Adds the USGS VS30 data missing in the original source.
- Separate files into only seismic stations, and all stations
- Create site_models for the stations
_NOTE: Manual editions to this file might be needed during the calibration process._

### 3.2 Site model

Using the notebook `3_oq_vs30_uniform_grid.ipynb`, it is possible to create a uniform gridded site model file using the USGS vs30 reference data.\
The user defines the grid spacing and the maximum distance from a given hypocenter definition (referenced to a given rupture file). The notebook also saves a map with the Vs30 values.

_NOTE: For calibration, it is convenient to create a fine grid (1 to 2 km) close to the epicentre, and up to a distance in which the estimated PGA <= 0.05g._


### 3.3 OpenQuake files

- Generate the gmpe logic tree files:\
To run OQ for conditioning gmfs, the GMPEs should support separate std_dev (inter and intra). It is possible to define a [ModifiableGMPE](https://github.com/gem/oq-engine/blob/master/openquake/qa_tests_data/event_based/case_28/gmmLt.xml), and assign a `add_between_within_stds.with_betw_ratio = 0.6`.
     - **`gmpe_logic_tree_USGS.xml`**: for USGS, get the GMPEs and weights (check notebook `3_oq_gmmLT_from_usgs_shakemap.ipynb`)
     - **`gmpe_logic_tree_GEM.xml`**: using the tectonic region type of the event, get the GMPEs applicable for the event based on the models available in the Global Hazard Mosaic.
- Copy the reference `READEME.md` and `job_rupture.ini` files and adjust them as appropriate. The modeller decides which rupture model and GMPE logic tree fit better.


### 3.4 Generate job files considering input data from user

Using the notebook `3_oq_prepare_job_files.ipynb`, it is possible to generate the job files for all the combinations the user would like to include: Rupture models, GMPEs, stations.

### 3.5 Run OQ calculation

Run the median gmf using the different rupture solutions and GMPEs. 

### 3.6 Post-process and plot results from openquake

- In Sensitivity folder we should include log files from the oq calcs run
- Run notebook to generate summary table with all oq calcs run
- Prepare job files for the selected rupture and gmpe (minimum abs bias)
- Run plot median_without_stations, median_with_stations_all, median_with_stations_seismic
- Update README.md

## 4. Impact data

The goal is to collect as much information as possible at the minimum geographical detail (building level if available).


## 5. Final details

- Update ECD database, figure and home README using the notebook `6_ecd_readme.ipynb`
- Verify the integrity of all files, run ```pytest tests``` from the home folder
- Create a merge request to include the new events in master


