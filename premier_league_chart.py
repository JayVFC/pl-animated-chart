from pathlib import Path
import pandas as pd
import matplotlib.colors as mcolors
import bar_chart_race as bcr


# Specify the file path of the csv
file_path = Path(r'C:\Users\JasonW\Desktop\Files\03.  Development\premier_league.csv')

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)
df.set_index('Matchweek', inplace=True)

# Specify colours to use in chart
colours_dict = {
    'Arsenal': '#EF0107',
    'Aston Villa': '#670E36',
    'Bournemouth': '#DA291C',
    'Brentford': '#D20000',
    'Brighton': '#0057B8',
    'Chelsea': '#034694',
    'Crystal Palace': '#C4122E',
    'Everton': '#003399',
    'Fulham': '#000000',
    'Leeds': '#FFCD00',
    'Leicester': '#003090',
    'Liverpool': '#C8102E',
    'Man City': '#6CABDD',
    'Man Utd': '#DA291C',
    'Newcastle': '#231F20',
    "Nott'm Forest": '#E53233',
    'Southampton': '#D71920',
    'Spurs': '#132257',
    'West Ham': '#7A263A',
    'Wolves': '#FDB913'
    }
colours_list = []
for value in colours_dict.values():
    colours_list.append(value)
cmap = mcolors.ListedColormap(colours_list)

manager_sackings = {
    'Matchweek 4': 'Bournemouth sack Parker',
    'Matchweek 5': 'Chelsea sack Tuchel',
    'Matchweek 9': 'Wolves sack Lage',
    'Matchweek 12': 'Villa sack Gerrard',
    'Matchweek 15': 'Southampton sack Hassenhuttl',
    'Matchweek 21': 'Everton sack Lampard',
    'Matchweek 22': 'Leeds sack Marsch',
    'Matchweek 23': 'Southampton sack Jones',
    'Matchweek 27': 'Palace sack Viera',
    'Matchweek 28': 'Spurs sack Conte',
    'Matchweek 29': 'Leicester sack Rogers / Chelsea sack Potter',
    'Matchweek 32': 'Spurs sack Stellini',
    'Matchweek 34': 'Leeds sack Garcia',
    }

def summary(values, ranks):
    current_period = ranks.name
    s = ''
    if current_period in manager_sackings:
        s = manager_sackings[current_period]
    return {'x': .95, 'y': .05, 's': s, 'ha': 'right', 'size': 8}

# Create animated bar chart
bcr.bar_chart_race(
    df = df,
    filename = 'Premier League 2022-23.mp4',
    title = 'Premier League 2022/23',
    sort = 'desc',
    fixed_max = True,
    label_bars = True,
    period_length = 3000,
    steps_per_period = 20,
    n_bars = None,
    cmap = cmap,
    period_summary_func = summary,
)