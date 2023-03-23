# GEMSA - Global Earthquake Scenario Archive

Check database in file [GEM_ECD.csv](./GEM_ECD.csv)

## ✨ Metadata

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

- `Tectonic region type:` Tectonic features associated to the event. For example, active shallow crust, subduction interface, subduction intraslab, stable continental.

- `Fault mechanisim:` Faulting motion that produced the earthquake: strike-slip fault, normal fault, thrust fault (reverse fault).

- `USGS_ID:` Unique identifier in the USGS scenarios service.


> **Note**
> For the definition of the parameters for building and human impact data, check the `Impact` folder in each event.