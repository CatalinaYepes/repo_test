# IMPACT DATA COLLECTION

## Files description

Information at different administrative regions has been collected:
- **ID_0:** Refers to metrics reported at national level
- **ID_1:** Refers to metrics reported at administrative level 1
- **ID_2:** Refers to metrics reported at administrative level 2
- **ID_3:** Refers to metrics reported at administrative level 3
- `Note:` When available, building level information is included.


### Building impact files 
Datasets with the physical damage substained by buildings due to the earthquake and its induced effects.

- `Impact_All_ID_0.csv`: National level impact statistics from multiple sources (indicated in the REFERENCE column).
- `Impact_Buildings_ID_0.csv`: National level damaged buildings data based on damage levels and/or construction material from multiple sources (indicated in the REFERENCE column).
- `Impact_Buildings_ID_1.csv`: Damaged building data at administrative level 1 from multiple sources (indicated in the REFERENCE column).
- `Impact_Buildings_ID_2.csv`: Damaged building data at administrative level 2 from multiple sources (indicated in the REFERENCE column).
- `Impact_Buildings_ID_3.csv`: Damaged building data at administrative level 3 from multiple sources (indicated in the REFERENCE column).


### Human impact files

- `Impact_Human_ID_1.csv`: Data of human impact information at administrative level 1 from multiple sources (indicated in the REFERENCE column).
- `Impact_Human_ID_2.csv`: Data of human impact information at administrative level 2 from multiple sources (indicated in the REFERENCE column).
- `Impact_Human_ID_3.csv`: Data of human impact information at administrative level 3 from multiple sources (indicated in the REFERENCE column).



## Reported metrics description

- `Year:`: Year of phenomenon occurrence.

- `Country:` Country where the epicenter of the event was located.

- `Region:` Name of the region where EQ happened.  

- `Event_Name:`  The name of the event based on local sources.

- `Local_Date:` Date of occurrence at the location of the even. Format: dd/mm/yyyy.

- `Local_Time:` Local time of occurrence (sources: USGS). Format: HH/MM/SS.

- `Latitude:` Latitude of the epicenter (sources: USGS).

- `Longitude:` Longitude of the epicenter (sources: USGS).

- `Depth_(km):` Hypocentral depth (sources: USGS).

- `Mw:` Moment magnitude (sources: USGS).

- `Max_Intensity_(MMI):` Modified Mercalli Intensity (MMI) (source: USGS).

- `USGS_ID:` Unique identifier  

- `Tectonic region type:` Tectonic features associated to the event. For example, active shallow crust, subduction interface, subduction intraslab, stable continental.

- `Fault mechanisim:` Faulting motion that produced the earthquake: strike-slip fault, normal fault, thrust fault (reverse fault).

- `Fatalities:` Number of people that died due to the earthquake direct or indirect effects (such as ground shaking, tsunamis, landslides, etc.
Fatalities = Direct deaths (shaking) + indirect deaths (due to tsunamis, landslide, heart attack,...) + Missing

- `Injured:` Number of people physically injured due to the earthquake occurance (directly or indirectly). It considers all level of injuries.
Injured = Direct injuries + indirect injuries

- `Displaced_Population:` Number of people who are reported as having been displaced, relocated, or evacuated due to the significant damage to their homes. If there are some sources in which the number of Homeless and Sheltered have been presented separately, adding the extra columns with the related headers is recommended.

- `Affected_Population:` Number of people reported as affected due to the earthquake occurance and its secondary effects. No differentiation regarding the level of affectance is included. The metric reports the population affected from immediate impacts, such as deaths, injuries, being homeless, being displaced, or being evacuated because of building damaged, as well as population affected by induced earthquake effects, such as landslides, tsunamis or burns from fires. 

- `Buildings_Damaged:` Number of buildings that reported any level of damage due to the earthquake and its secondary effects (Slight, Moderate, Extensive, Partially collapsed, Near collapse, and so on). Moreover, the number of buildings was reported as affected. 

- `Buildings_Collapsed:` Number of buildings reported as collapsed or totally destroyed.

- `Occupancy:` Refers to the use, or intended use, of a building or portion of a building, for the shelter or support of persons or property. When more detailed data is provided, the occupancy for which it is applicable (Residential, Commercial, Industrial, Education, Health, Churches, Lifelines, etc.)

- `GEM_Taxonomy:` String identifying the physical characteristics and usage of the buildings according to GEM building taxonomy. See more details on GEM Taxonomy in [Silva et al. 2022](https://link.springer.com/article/10.1007/s13753-022-00400-x).

- `Economic_Losses` Economic losses reported after the earthquake (it might include or not indirect losses). Preferably based on a reliable estimate in USD; otherwise, currency units are based on the source of reference. The currency unit should be mentioned in an extra column. Add multiple rows for sources reporting multiple currencies.

- `Insured_Losses:` Economic damages are covered by insurance companies. Preferably based on a reliable estimate in USD; otherwise, currency units are based on the source of reference. The currency unit should be mentioned in an extra column.

- `Induced_Effects:` Other phenomena that occurred as a result of earthquake, such as tsunamis, landslides, liquefaction, avalanche, floods, fire, eruptions, etc.

- `Reference:` Source of the reported information.