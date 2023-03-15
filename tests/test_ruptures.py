# -----------------------------------------------------------------------------
#   CONFIGURATION
# -----------------------------------------------------------------------------

# Dependencies
import os
import pandas as pd
import pytest
import glob

from openquake.hazardlib import sourceconverter, nrml
from src.get_rupture_info import repture_xml_to_df

def get_rupture(filename):
    [rup_node] = nrml.read(filename)
    conv = sourceconverter.RuptureConverter(rupture_mesh_spacing=2)
    rup = conv.convert_node(rup_node)
    return rup


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
#   CHECKS THAT AT LEAST ONE RUPTURE FILE EXISTS
# -----------------------------------------------------------------------------
    
@pytest.mark.parametrize('event', df[edx].Event_Path)
def test_rupture_files_exist(event):
    ruptures = glob.glob(os.path.join(event, "Ground_Shaking", "Rupture", 
                                      'earthquake_rupture_model_*.xml'))
    error_msg = "At least one `earthquake_rupture_model_*.xml` required"
    assert len(ruptures) > 0, error_msg
    

# -----------------------------------------------------------------------------
#   CHECKS RUPTURE WITH OQ FORMAT
# -----------------------------------------------------------------------------
ruptures = glob.glob(os.path.join('**', 'earthquake_rupture_model_*.xml'),
                     recursive=True)
@pytest.mark.parametrize('rup_file', ruptures)
def test_oq_rupture_file(rup_file):
    get_rupture(rup_file)


# -----------------------------------------------------------------------------
#   CHECK INFORMATION ACROSS RUPTURE FILES
# -----------------------------------------------------------------------------
    
@pytest.mark.parametrize('event', df[edx].Event_Path)
def test_rupture_info(event):
    ruptures = glob.glob(os.path.join(event, "Ground_Shaking", "Rupture", 
                                      'earthquake_rupture_model_*.xml'))
    
    # Create DataFrame with rupture information
    df = [ ]
    for rupfile in sorted(ruptures):
        source = os.path.basename(rupfile)
        # print(source)
        _, rup_df = repture_xml_to_df(rupfile)
        rup_df.index = [source]
        df.append(rup_df)    
    df = pd.concat(df)

    # Check that STRIKES are consistent
    vmin = df.strike.min()
    vmax = df.strike.max()
    dif = vmax - vmin
    if dif != dif:
        dif = 0 # No value reported
    error_msg = "Rupture strike with differences > 90 degrees"
    # Exclude specific events with strikes close to 0 or 360
    exclude = ['Colombia/19990125_M6.1_Armenia',
               'Chile/20150916_M8.3_Illapel',
               'El_Salvador/20010213_M6.6_SanSalvador']

    if not event in exclude:
        assert abs(dif) < 90, error_msg
    
    # Check that DIPS are consistent
    vmin = df.dip.min()
    vmax = df.dip.max()
    dif = vmax - vmin
    if dif != dif:
        dif = 0 # No value reported
    error_msg = "Rupture dip with differences > 40 degrees"
    assert abs(dif) < 40, error_msg

    # Check that RAKEs are consistent
    vmin = df.rake.min()
    vmax = df.rake.max()
    dif = vmax - vmin
    error_msg = "Rupture rake with differences > 30 degrees"

    # Exclude specific events with rakes too different
    exclude = ['Chile/19600522_M9.5_Valdivia',
               'Chile/20140401_M8.2_Iquique',
               'Chile/20150916_M8.3_Illapel',
               'Costa_Rica/20171113_M6.5_Puntarenas']

    if not event in exclude:
        assert abs(dif) < 30, error_msg

    # Check MAGNITUDE consistence
    mag = float(event.split('_')[-2].replace('M',''))
    vmin = df.mag.min()
    vmax = df.mag.max()
    dif = max(abs(vmax - mag), abs(vmin - mag))
    error_msg = f"Magnitudes differing > 0.5 units with respect to Mw {mag}"
    assert abs(dif) < 0.5, error_msg

    # Check that DEPTH are consistent
    vmin = df.depth.min()
    vmax = df.depth.max()
    dif = vmax - vmin
    error_msg = "Rupture depth with differences > 25 km"
    # Exclude specific events with differing depth data
    exclude = ['Colombia/19830331_M5.6_Popayan',
               'Mexico/20170908_M8.2_Chiapas']
    if not event in exclude:
        assert abs(dif) < 25, error_msg


# -----------------------------------------------------------------------------
#   CHECKS FOR README
# -----------------------------------------------------------------------------

@pytest.mark.parametrize('event', df[edx].Event_Path)
def test_readme_content(event):

    file_path = glob.glob(os.path.join(event, 
                                       'Ground_Shaking','Rupture', 
                                       'README.md'))
    
    # Check that README exist
    error_msg = "Missing README file"
    assert len(file_path) == 1, error_msg
    
    
    readme = open(file_path[0], 'r')
    content = readme.read()
    readme.close    
    
    # Check that image with ruptures exist
    txt = '[](earthquake_ruptures.png)'
    error_msg = "`earthquake_ruptures.png` not included in README"
    assert content.find(txt) != -1, error_msg
    
    # Check that References are included
    txt = '## References' 
    error_msg = "References not included in README"
    assert content.find(txt) != -1, error_msg
    
    # Check that table with rupture details exist
    txt = '## Rupture details\n' 
    error_msg = 'Missing `Rupture details` in README'
    assert content.find(txt) != -1, error_msg
    
    # Verify content for rupture details
    for txt in ['Mecanism', 'Tectonic region type']:
        line = [line for line in content.split('\n') if txt in line][0]
        line = line.replace(' ', '')
        value = line.split('|')[2]
        assert value != '', f'Missing `{txt}` in README'

#%%
event='El_Salvador/20010213_M6.6_SanSalvador'

test_rupture_files_exist(event)
# test_oq_rupture_file(rup_file)
test_rupture_info(event)