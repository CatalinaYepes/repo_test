# IMPACT DATA COLLECTION

Information at different administrative regions has been collected:

- **ID_0:** Refers to metrics reported at national level
- **ID_1:** Refers to metrics reported at administrative level 1, States (Entidades Federativas)
- **ID_2:** Refers to metrics reported at administrative level 2, Municipalities (Municipios)

When available, building level information is included.


## Building Impact

Datasets with the physical damage substained by buildings due to the earthquake and its induced effects.

- `Impact_All_ID_0.csv`: National level impact statistics from multiple sources (indicated in the REFERENCE column).
- `Impact_Buildings_detailed.csv`: Unified database of building damage information from `Datos_Abiertos_Puebla.zip`, `sismosmexico_Puebla.zip` and `CICM-SMIE-2017.zip`.
- `Buildings_ID_1.csv`: Unified damaged building databased from Tena_Colunga_et_al_2020_a, Tena_Colunga_et_al_2020_a, Jara_et_al_2019, Singh_et_al_2018, and EID.


## Human Impact
- `Impact_Human_ID_1.csv`: Database of human impact information from [Wikipedia], EID, NOAA, and USGS.
- `Impact_Human_ID_2.csv`: Database of human impact information from `Datos_Abiertos_Puebla.zip`.


## Economic Losses
Few references indicate the economic losses related to the event, and most of them provide a total value for the overall losses.


## Reported impact metrics

- `AFFECTED_POPULATION`: Number of people reported as affected due to the earthquake occurance and its secondary effects. No differentiation regarding the level of affectance is included. The metric reports the population affected from immediate impacts, such as deaths, injuries, being homeless, being displaced, or being evacuated because of building damaged, as well as population affected by induced earthquake effects, such as landslides, tsunamis or burns from fires.

- `BUILDINGS_AFFECTED`: ?XXXX? MAYBE TO DELETE XXXX???

- `BUILDINGS_COLLAPSED`: Number of buildings reported as collapsed or totally destroyed.

- `BUILDINGS_DAMAGED`: Number of buildings that reported any level of damage due to the earthquake and its secondary effects.

- `CAUSE_OF_INJURY/DEATH`:

- `COMMENTS`:

- `DISPLACED_POPULATION`: Number of people who are reported as having been left homeless, evacuated, or sheltered due to the significant damage to their homes.

- `ECONOMIC_LOSSES`: Economic losses reported after the earthquake (it might include or not inderect losses). Currency units based on the source of reference.

- `FATALITIES`: Number of people who have died due to the earthquake (either directly or indirectly) and other phenomena such as tsunamis, landslides, etc.

- `TAXONOMY` or `GEM_TAXONOMY`: String identifying the pyisical characteristics and useage of the buildings. See more details on GEM Taxonomy in [Silva et al. 2022](https://doi.org/10.1007/s13753-022-00400-x)

- `INDUCED_EFFECTS`: Other phenomena that occurred as a result of earthquake, such as tsunamis, landslides, liquefaction, avalanche, floods, fire, eruptions, etc.

- `INJURIES`: Number of people physically injured due to the earthquake occurance (directly or indirectly). 

- `INSURED_LOSSES`: Economic insured losses reported as a consequence of the earthquake 

- `REFERENCE`:

- `OCCUPANCY`:


