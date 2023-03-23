#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import glob
import pandas as pd

from plots import stations_plot, gdf_epicentre


# Get list of countries
skip_folders = ["src", "tests"]
root_dir = os.path.dirname(os.getcwd())
country_folders = [folder for folder in os.listdir(root_dir) if folder
                   not in skip_folders
                   and os.path.isdir(os.path.join(root_dir, folder))
                   and not folder.startswith(".")]

# Get list of events
events=[]
for country in country_folders:
    events += [folder for folder in os.listdir(os.path.join(root_dir, country))
              if os.path.isdir(os.path.join(root_dir, country, folder))]

# Get list of events with README in the home folder
events2 = [os.path.dirname(name) for name in 
           glob.glob(os.path.join('..', '*', '*', 'README.md'))]

#%% Create 'Stations_USGS.csv'
limit = 'Costa_Rica'

for event in events2:
    # Ignore DRAFT folders
    if 'DRAFT_' in event:
        # print((f'\x1b[0;31m Ignore {event} \x1b[0m'))
        continue
    elif not limit in event:
        continue
    print(event)
    
    # Get station file to plot
    try:
        file_name = glob.glob(os.path.join('..', '*', event, '*', 
                                           '*', 'Stations_Unique.csv'))[0]
    except IndexError:
        try:
            file_name = glob.glob(os.path.join('..', '*', event, '*', 
                                           '*', 'Stations_*.csv'))[0]
        except IndexError as e:
            print(e)
 
    country = event.split(os.sep)[1]
    # Convert json file to ECD desired format
    df = pd.read_csv(file_name)
    
    # Create figure
    title = f'Recording stations {event}'
    if country in ['Chile', 'Colombia', 'Ecuador']:
        fig, ax = stations_plot(df, title=title, legend_orientation='vertical')
    else:
        fig, ax = stations_plot(df, title=title)
    
    # Add epicenter in figure
    ref_rupture = glob.glob(os.path.join(event, '*', 'Rupture', 
                                     'earthquake_rupture_model_USGS.xml'))[0]
    epi = gdf_epicentre(ref_rupture)
    print(epi)
    ax.scatter(epi.geometry.x, epi.geometry.y, 
               s=500, marker='*', color='gold', edgecolor='grey',
               zorder=2)
    
    # Save figure
    output_path = os.path.join(event,'Ground_Shaking',
                               'Recording_Stations', 'recording_stations.png')
    fig.savefig(output_path, facecolor="w", 
                dpi=300,
                bbox_inches='tight')
    print('figure saved in', output_path)

    
    
#%% Correct Stations_Unique.csv files

# Event name
event = [] # '19830331_M5.6_Popayan'

if event:
    events = glob.glob(f'../*/{event}/*/*/Stations_Unique.csv')
    if not events:
        print(f'Stations_Unique.csv not available for {event}')
else:
    # Run all events in Database
    events = glob.glob('../*/*/*/*/Stations_Unique.csv')

events = [
    '../Colombia/20080524_M5.9_Quetame/Ground_Shaking/Recording_Stations/Stations_Unique.csv', 
    '../Mexico/20170919_M7.1_Puebla/Ground_Shaking/Recording_Stations/Stations_Unique.csv', 
    '../Costa_Rica/20171113_Mw6.5_Puntarenas/Ground_Shaking/Recording_Stations/Stations_Unique.csv', 
    '../Chile/20140401_M8.2_Iquique/Ground_Shaking/Recording_Stations/Stations_Unique.csv', 
    '../Chile/20150916_M8.3_Illapel/Ground_Shaking/Recording_Stations/Stations_Unique.csv', 
    '../Chile/20100227_M8.8_Maule/Ground_Shaking/Recording_Stations/Stations_Unique.csv', 
    ]

for event in events:
    event_name = event.split('/')[2]
    print(f'\x1b[0;32m \n {event_name} \x1b[0m')
    df = pd.read_csv(event)
    
    # Rename columns
    df2 = recording_stations.check_format(df)
    
    if len(df2) != 0:
        # Remove empty columns
        empty = df.isnull().all()    
        if empty.any():
            print('\nCheck empty')
            print(empty)
        df2.dropna(axis=1, how='all', inplace=True)
        
        # Add missing columns
        df2['STATION_TYPE'] = 'seismic'
        df2['UNCERTAINTY'] = 0.001
    
        # Remove USGS stations
        df2 = df2[df2.REFERENCES != 'USGS_Recording_stations']
        df2 = df2[df2.REFERENCES != 'USGS_Recording_Stations']
        print(df2.REFERENCES.unique())
        df2.to_csv(event, index=False)
    else:
        os.remove(event)
        print("File removed. Need to create it from USGS")


#%% Rename REFERENCES

files = glob.glob('../*/*/*/*/Stations_Unique.csv')

if not files:
    print('No files called stationlist.csv')

# Dictionary with data to replace in REFERENCES
sources = {
    'Unique_Recording_Station.csv': 'Station_Unique.csv',
    'SGS_Recording_Stations': 'Stations_SGS',
    'USGS_Recording_Stations': 'Stations_USGS',
    'USGS_Recording_stations': 'Stations_USGS',
    'BMF_1999': 'BMF_1999',
    'UNAM_Recording_stations': 'Stations_UNAM',
    'CDMX_GEO_DATA_And_Cires_Recording_Stations': 'Stations_CDMX_GEO_DATA_And_Cires',
    'Cires_Recording_Stations_And_Guillermo_Diaz_Fanas_2020': 'Stations_Cires_And_Guillermo_Diaz_Fanas_2020',
    'Casado_et_al_2001': 'Casado_et_al_2001',
    'CSN_Recording_Stations': 'Stations_CSN',
    'CSN_Recording_stations': 'Stations_CSN',
    'CSN_Recording_Stations_and_GEERI_llapel_Earthquake_2015': 'Stations_CSN_and_GEERI_llapel_Earthquake_2015',
    }  
  
for file_path in files:
    print(' !!', file_path.split('/')[2])
    df = pd.read_csv(file_path)
    
    print(*df.REFERENCES.unique(), sep='\n')
    
    df.REFERENCES.replace(sources, inplace=True)
    df.to_csv(file_path, encoding='utf-8', index=False)
    
    # Adjust README
    folder = os.path.dirname(file_path)
    readme = os.path.join(folder, 'README.md')
    
    # Read original README
    f = open(readme, 'r')
    content = f.read()
    f.close
    
    # Modify content
    for source in sources.keys():
        new_source = sources[source]
        if content.find(source) != -1:
            content = content.replace(source, new_source)
    
    f=open(os.path.join(folder, 'README.md'), 'w')
    f.write(content)
    f.close()



    


    