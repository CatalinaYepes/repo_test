# -------------------------------------------------------------------------------------
#   CONFIGURATION
# -------------------------------------------------------------------------------------

# Dependencies
import os
import pandas as pd
import pytest
import re

# -------------------------------------------------------------------------------------
#   INITIALIZATION
# -------------------------------------------------------------------------------------

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

# -------------------------------------------------------------------------------------
#   CHECK FOR EMPTY FOLDERS
# -------------------------------------------------------------------------------------

# Check or empty folders
@pytest.mark.parametrize('country', df.Country.unique())
def test_empty_country_folder(country):
    idx = df.Country == country
    check_null = df.loc[idx, 'Event_Folder'].isnull().values.all()
    error_msg = f"No event folders found for {country}"
    assert not check_null, error_msg


# -------------------------------------------------------------------------------------
#   CHECK FOR EVENT NAME FORMAT
# -------------------------------------------------------------------------------------

# Check that event name folder follows required format
@pytest.mark.parametrize('event', df[edx].Event_Folder)
def test_event_name(event):
    # Count number of components
    str_split = event.split("_")
    fmt_msg = f"{event} does not satisfy event name format: <DATE>_<MAG>_<NAME>"
    assert len(str_split) == 3, fmt_msg
    # Check date format
    date = str_split[0]
    dtm_msg = f"{date} substring of {event} does not satisfy date format: YYYYMMDD"
    assert len(date) == 8, dtm_msg
    # Check magnitude format
    mag = str_split[1]
    mag_msg = f"{mag} substring of {event} does not satisfy magnitude format: MX.X"
    assert re.match(r"M[0-9].[0-9]", mag), mag_msg
    
    
# -------------------------------------------------------------------------------------
#   CHECK FOR MINIMUM REQUIRED FOLDERS AND FILES
# -------------------------------------------------------------------------------------
    
# Check for README file
@pytest.mark.parametrize('event', df[edx].Event_Path)
def test_readme_file_exists(event):
    file_path = os.path.join(event, "README.md")
    error_msg = f"Required readme ({file_path}) does not exist"
    assert os.path.exists(file_path), error_msg
    
# Check for earthquake_information.csv file
@pytest.mark.parametrize('event', df[edx].Event_Path)
def test_eqinfo_file_exists(event):
    file_path = os.path.join(event, "earthquake_information.csv")
    error_msg = f"Required readme ({file_path}) does not exist"
    assert os.path.exists(file_path), error_msg
    
# Check for required folders
required_subfolders = [
    os.path.join("Ground_Shaking", "Recording_Stations"),
    os.path.join("Ground_Shaking", "Rupture"),
    os.path.join("Ground_Shaking", "Shake_Map"),
    os.path.join("OpenQuake_gmfs"),
    os.path.join("Impact"),
]
@pytest.mark.parametrize('subfolder', required_subfolders)
@pytest.mark.parametrize('event', df[edx].Event_Path)
def test_event_subfolders_exist(event, subfolder):
    folder_path = os.path.join(event, subfolder)
    error_msg = f"Required subfolder {folder_path} does not exist"
    assert os.path.exists(folder_path), error_msg

# Check for Stations_Unique implemented in `test_stations.py`

# Check that at least one rupture file exist in `test_ruptures.py`


# # Check that at least one shakemap file exists
# @pytest.mark.parametrize('event', df[edx].Event_Path)
# def test_shakemap_file_exists(event):
#     shakemap_path = os.path.join(event, "Ground_Shaking", "Shake_Map")
#     prefix, suffix = "shakemap", ".kmz"
#     if os.path.exists(shakemap_path):
#         rupture_files = [file for file in os.listdir(shakemap_path)
#                         if file.startswith(prefix) and file.endswith(suffix)]
#         error_msg = f"At least one shakemap file does not exist in {shakemap_path}"
#         assert len(rupture_files) > 0, error_msg
#     else: # avoid duplicate check on required (sub)folders
#         pass

# # Check for OQ GMFs CSV
# @pytest.mark.parametrize('event', df[edx].Event_Path)
# def test_oq_gmfs_exist(event):
#     oq_path = os.path.join(event, "OpenQuake_gmfs")
#     file_path = os.path.join(oq_path, "gmf_scenario.csv")
#     error_msg = f"Required OQ input ({file_path}) does not exist"
#     if os.path.exists(oq_path):
#         assert os.path.exists(file_path), error_msg
#     else: # avoid duplicate check on required (sub)folders
#         pass

# # Check for OQ GMFs CSV
# @pytest.mark.parametrize('event', df[edx].Event_Path)
# def test_oq_job_exists(event):
#     oq_path = os.path.join(event, "OpenQuake_gmfs")
#     prefix, suffix = "job", ".ini"
#     if os.path.exists(oq_path):
#         job_files = [file for file in os.listdir(oq_path)
#                      if file.startswith(prefix) and file.endswith(suffix)]
#         error_msg = f"At least one OQ job does not exist in {oq_path}"
#         assert len(job_files) > 0, error_msg
#     else: # avoid duplicate check on required (sub)folders
#         pass

# # Check for OQ Observations CSV
# @pytest.mark.parametrize('event', df[edx].Event_Path)
# def test_oq_observations_exists(event):
#     oq_path = os.path.join(event, "OpenQuake_gmfs")
#     file_path = os.path.join(oq_path, "observations.csv")
#     error_msg = f"Required OQ input ({file_path}) does not exist"
#     if os.path.exists(oq_path):
#         assert os.path.exists(file_path), error_msg
#     else: # avoid duplicate check on required (sub)folders
#         pass

# # Check for impact file
# @pytest.mark.parametrize('event', df[edx].Event_Path)
# def test_impact_exists(event):
#     impact_path = os.path.join(event, "Impact")
#     file_path = os.path.join(impact_path, "Impact_All_ID_0.csv")
#     error_msg = f"Required Impact file ({file_path}) does not exist"
#     if os.path.exists(impact_path):
#         assert os.path.exists(file_path), error_msg
#     else: # avoid duplicate check on required (sub)folders
#         pass

