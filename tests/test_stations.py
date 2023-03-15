# -----------------------------------------------------------------------------
#   CONFIGURATION
# -----------------------------------------------------------------------------

# Dependencies
import os
import pandas as pd
import pytest
import re
import glob

# -----------------------------------------------------------------------------
#   INITIALIZATION
# -----------------------------------------------------------------------------

# Determine all relevant country folders
skip_folders = ["src", "tests"]
country_folders = [folder for folder in os.listdir('.') if folder
                   not in skip_folders
                   and os.path.isdir(folder)
                   and not folder.startswith(".")]

# Determine all relevant event folders
event_folders = dict.fromkeys(country_folders)
for country in country_folders:
    event_folders[country] = [folder for folder in os.listdir(country)
                              if os.path.isdir(os.path.join(country, folder))]

# Arrange DataFrame with event paths
df = pd.DataFrame(
                  event_folders.items(),
                  columns=['Country', 'Event_Folder'],
                 ).explode('Event_Folder')
df['Event_Path'] = df.Country + os.sep + df.Event_Folder
draft_prefix = "DRAFT_"
edx = ~df.Event_Folder.str.startswith(draft_prefix) # non-draft indices


# -----------------------------------------------------------------------------
#   CHECKS FOR `Stations_USGS.csv` FILE
# -----------------------------------------------------------------------------
    
@pytest.mark.parametrize('event', df[edx].Event_Path)
def test_stations_files_exist(event):
    station_path = os.path.join(event, "Ground_Shaking", "Recording_Stations")
    
    # Check USGS files exist
    # Skip events with no USGS data
    skip_events = ['Colombia/20041115_M7.2_Pizarro']
    if not any(event in s for s in skip_events):
        # stationlist.json
        file_path = os.path.join(station_path, "stationlist.json")
        error_msg = "Required `stationlist.json` file does not exist"
        assert os.path.exists(file_path), error_msg
    
        # Stations_USGS.csv
        file_path = os.path.join(station_path, "Stations_USGS.csv")
        error_msg = "Required `Stations_USGS.csv` file does not exist"
        assert os.path.exists(file_path), error_msg

    # Check `Stations_Unique.csv` exist
    # If only one reference is available, then don't check Stations_Unique
    stations = glob.glob(os.path.join(station_path, 'Stations_*.csv'))
    if len(stations) > 1:
        file_path = os.path.join(station_path, "Stations_Unique.csv")
        error_msg = "Required `Stations_Unique.csv` file does not exist"
        assert os.path.exists(file_path), error_msg

    # Check `README.md` exist
    file_path = os.path.join(station_path, "README.md")
    error_msg = "Required `README.md` file does not exist"
    assert os.path.exists(file_path), error_msg
    
    # Check `recording_stations.png` exist
    file_path = os.path.join(station_path, "recording_stations.png")
    error_msg = "Required `recording_stations.png` file does not exist"
    assert os.path.exists(file_path), error_msg


# -----------------------------------------------------------------------------
#   CHECKS FOR CONTENTS IN `Stations_XXX.csv` FILE
# -----------------------------------------------------------------------------

@pytest.mark.parametrize('event', df[edx].Event_Path)
def test_stations_contents(event):
    stations = glob.glob(os.path.join(event, 
                                       'Ground_Shaking','Recording_Stations', 
                                       'Stations_*.csv'))
    for s_file in stations:
        df = pd.read_csv(s_file)
        file_name = os.path.basename(s_file)
        
        # Check mandatory columns
        cols = ['STATION_ID', 'STATION_NAME', 'LATITUDE', 'LONGITUDE',
                'STATION_TYPE', 'REFERENCES']
        missing = set(cols) - set(df.columns)
        error_msg = f'{file_name}: Missing columns: {missing}'
        assert len(missing) == 0, error_msg

        # Check NO empty columns in mandatory cols
        cols_no_empty = [x for x in cols if x != 'STATION_NAME']
        empty = df[cols_no_empty].isnull().any()
        error_msg = f'{file_name}: Columns with empty values: {empty}'
        assert empty.any() == False, error_msg

        # Check if coordinates are sufficiently close:
        lon = df.LONGITUDE.max() - df.LONGITUDE.min()
        error_msg = f'{file_name}: Longitudes with +{lon} difference'
        assert abs(lon) < 50., error_msg
        lat = df.LATITUDE.max() - df.LATITUDE.min()
        error_msg = f'{file_name}: Latitudes with +{lat} difference'
        assert abs(lat) < 30., error_msg

        # Check empty columns
        empty = df.isnull().all()
        error_msg = f'{file_name}: Columns with all empty values: {empty}'
        assert empty.all() == False, error_msg
        
        # Identify columns with IMT values
        imts = ['MMI', 'PGA', 'PGV', 
                'SA(0.3)', 'SA(0.6)', 'SA(1.0)', 'SA(3.0)']
        vals = [x[:-6] for x in df.columns if x.endswith('_VALUE')]
        sigma = [x[:-9] for x in df.columns if x.endswith('_LN_SIGMA')]
        if 'MMI_STDDEV' in df.columns:
            sigma.append('MMI')
        #  Each IMT has a corresponding uncertanty column
        missing = set(vals).difference(set(sigma))
        error_msg = f'{file_name}: IMTs missing uncertainty column: {missing}'
        assert set(vals) == set(sigma), error_msg
        # IMTs are supported in the suported list (imts)
        unknow = set(vals) - set(imts)
        error_msg = f'{file_name}: File contains unknow IMTs: {unknow}'
        assert set(imts).issuperset(set(vals)), error_msg
        
        # Check IMTs units
        if 'PGA_VALUE' in df.columns:
            max_val = df['PGA_VALUE'].max()
            error_msg = f'{file_name}: Check PGA units. PGA max = {max_val}'            
            assert max_val <= 2, error_msg # To be increased if necessary
        
        if 'MMI_VALUE' in df.columns:
            max_val = df['MMI_VALUE'].max()
            error_msg = f'{file_name}: Check MMI units. MMI max = {max_val}'            
            assert max_val <= 10, error_msg

        # Check supported STATION_TYPE
        sup_types = ['seismic', 'macroseismic']
        in_types = df['STATION_TYPE'].unique()
        unknow = set(sup_types) - set(in_types)
        error_msg = f'{file_name}: unknow STATION_TYPE: {unknow}'
        assert set(sup_types).issuperset(set(in_types)), error_msg


# -----------------------------------------------------------------------------
#   CHECKS FOR README
# -----------------------------------------------------------------------------

@pytest.mark.parametrize('event', df[edx].Event_Path)
def test_readme_content(event):
    file_path = glob.glob(os.path.join(event, 
                                       'Ground_Shaking','Recording_Stations', 
                                       'README.md'))[0]
    readme = open(file_path, 'r')
    content = readme.read()
    readme.close    
    
    txt = '[](recording_stations.png)' 
    error_msg = "`recording_stations.png` not included in README"
    assert content.find(txt) != -1, error_msg

    txt = '## Reference datasets' 
    error_msg = "References not included in README"
    assert content.find(txt) != -1, error_msg

    
# %%
event = 'Colombia/20041115_M7.2_Pizarro'
event = 'Mexico/20170919_M7.1_Puebla'
test_stations_files_exist(event)
test_readme_content(event)
test_stations_contents(event)