import tkinter as tk
from tkinter import ttk
import requests


# Define the Pastebin API endpoint and credentials
PASTEBIN_API_ENDPOINT = 'https://pastebin.com/api/api_post.php'
PASTEBIN_API_DEV_KEY = 'https://pastebin.com/api/api_post.php'
PASTEBIN_API_USER_KEY = 'ESLuNubbvmkeJWuN9MxICyprJzhY48wV'

# Define a function to upload a string to Pastebin and return the resulting URL


def upload_to_pastebin(text):
    payload = {
        'api_dev_key': PASTEBIN_API_DEV_KEY,
        'api_user_key': PASTEBIN_API_USER_KEY,
        'api_option': 'paste',
        'api_paste_code': text,
    }
    response = requests.post(PASTEBIN_API_ENDPOINT, data=payload)
    if response.status_code == 200 and response.text.startswith('https://pastebin.com/'):
        return response.text.strip()
    else:
        return None


def get_pokemon_info():
    # Clear existing labels and progress bars
    Name_Label.config(text="")
    Pokemon_type.config(text="")
    H_label.config(text="")
    W_label.config(text="")
    Progress_Bar_HP.config(value=0)
    Progress_Bar_Attact.config(value=0)
    Progress_Bar_Defense.config(value=0)
    Progress_Bar_SA.config(value=0)
    Progress_Bar_SD.config(value=0)
    Progress_Bar_Speed.config(value=0)

    # Get the name of the Pokemon
    pokemon_name = Entry_Pokemon.get()

    # Make a GET request to the PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    # Check if the Pokemon name is valid
    if response.status_code != 200:
        error_dialog = tk.Toplevel(root)
        error_dialog.title("Error")
        error_dialog.geometry("200x50")
        error_label = tk.Label(error_dialog, text="Invalid Name Please Try Again...")
        error_label.pack()
        return

    # Get the Pokemon data
    pokemon_data = response.json()

    # Display the Pokemon data
    Name_Label.config(text=pokemon_data['name'].capitalize())
    types = ", ".join([t['type']['name'] for t in pokemon_data['types']])
    Pokemon_type.config(text=f"Type(s): {types}")
    H_label.config(text=f"Height: {pokemon_data['height'] / 10:.1f} m")
    W_label.config(text=f"Weight: {pokemon_data['weight'] / 10:.1f} kg")
    Progress_Bar_HP.config(value=pokemon_data['stats'][0]['base_stat'])
    Progress_Bar_Attact.config(value=pokemon_data['stats'][1]['base_stat'])
    Progress_Bar_Defense.config(value=pokemon_data['stats'][2]['base_stat'])
    Progress_Bar_SA.config(value=pokemon_data['stats'][3]['base_stat'])
    Progress_Bar_SD.config(value=pokemon_data['stats'][4]['base_stat'])
    Progress_Bar_Speed.config(value=pokemon_data['stats'][5]['base_stat'])


# Create a window to hold the GUI
root = tk.Tk()
root.title("Pokédex")


# Create a Label to prompt the user for a Pokemon name
Pok_Name_l = tk.Label(root, text="Enter Pokemon Name: ")
Pok_Name_l.grid(row=0, column=0)

# Create an Entry to input Pokemon name
Entry_Pokemon = tk.Entry(root)
Entry_Pokemon.grid(row=0, column=1)

# Create a Button to get Pokemon information
Info_button = tk.Button(root, text="Get Pokemon's Informantion", command=get_pokemon_info,background="lightblue")
Info_button.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

# Create a LabelFrame to display Pokemon information
info_frame = tk.LabelFrame(root, text="Pokemon Info " ,border=5 ,background='lightblue')
info_frame.grid(row=2, column=0, columnspan=2, padx=(0, 10), sticky="nsew")

# Create a Label to display Pokemon name
Name_Label = tk.Label(info_frame, text="")
Name_Label.pack()

# Create a Label to display Pokemon type(s)
Pokemon_type = tk.Label(info_frame, text="")
Pokemon_type.pack()

# Create a Label to display Pokemon height
H_label = tk.Label(info_frame, text="")
H_label.pack()

# Create a Label to display Pokemon weight
W_label = tk.Label(info_frame, text="")
W_label.pack()


# Create a frame to display Pokemon stats
Frame_of_stats = tk.LabelFrame(root, text="Pokemon Stats",border=5,background="lightblue")
Frame_of_stats.grid(row=8, column=1, padx=(0,10), sticky="nsew")

# Create a Frame to display Pokemon HP stat
# Create a Frame to display Pokemon attact stat
hp_frame = tk.Frame(Frame_of_stats)
hp_frame.grid(row=0, column=1, padx=10, pady=10)

# Create a Label to display Pokemon Attack stat
Attact_S_L = tk.Label(Frame_of_stats, text="HP",border=4)
Attact_S_L.grid(row=0, column=0, padx=10, pady=10)

# Create a ProgressBar to display Pokemon HP stat
Progress_Bar_HP = ttk.Progressbar(
    hp_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
Progress_Bar_HP.grid(row=0, column=1)

# Create a Frame to display Pokemon attact stat
attack_frame = tk.Frame(Frame_of_stats)
attack_frame.grid(row=1, column=1, padx=10, pady=10)

# Create a Label to display Pokemon Attack stat
Attact_S_L = tk.Label(Frame_of_stats, text="Attack")
Attact_S_L.grid(row=1, column=0, padx=10, pady=10)

# Create a ProgressBar to display Pokemon HP stat
Progress_Bar_Attact = ttk.Progressbar(attack_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
Progress_Bar_Attact.grid(row=1, column=1)

# Create a Frame to display Pokemon defense stat
defense_frame = tk.Frame(Frame_of_stats)
defense_frame.grid(row=2, column=1, padx=10, pady=10)

# Create a Label to display Pokemon Defense stat
De_S_L = tk.Label(Frame_of_stats, text="Defense")
De_S_L.grid(row=2, column=0, padx=10, pady=10)

# Create a ProgressBar to display Pokemon defense stat
Progress_Bar_Defense = ttk.Progressbar(
    defense_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
Progress_Bar_Defense.grid(row=0, column=1)

# Create a Frame to display Pokemon defense stat
sp_frame = tk.Frame(Frame_of_stats)
sp_frame.grid(row=3, column=1, padx=10, pady=10)

# Create a Label to display Pokemon Special Attack stat
Special_A_S_l = tk.Label(Frame_of_stats, text="Special Attack")
Special_A_S_l.grid(row=3, column=0, padx=10, pady=10)

# Create a ProgressBar to display Pokemon defense stat
Progress_Bar_SA = ttk.Progressbar(
    sp_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
Progress_Bar_SA.grid(row=0, column=1)

# Create a Frame to display Pokemon defense stat
spd_frame = tk.Frame(Frame_of_stats)
spd_frame.grid(row=4, column=1, padx=10, pady=10)

# Create a Label to display Pokemon Special Defense stat
Special_D_S_L = tk.Label(Frame_of_stats, text="Special Defense")
Special_D_S_L.grid(row=4, column=0, padx=10, pady=10)

# Create a ProgressBar to display Pokemon special defense stat
Progress_Bar_SD = ttk.Progressbar(
    spd_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
Progress_Bar_SD.grid(row=0, column=1)

# Create a Frame to display Pokemon defense stat
speed_frame = tk.Frame(Frame_of_stats)
speed_frame.grid(row=5, column=1, padx=10, pady=10)

# Create a Label to display Pokemon Speed stat
S_S_L = tk.Label(Frame_of_stats, text="Speed")
S_S_L.grid(row=5, column=0, padx=10, pady=10)

# Create a ProgressBar to display Pokemon speed stat
Progress_Bar_Speed = ttk.Progressbar(
    speed_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
Progress_Bar_Speed.grid(row=0, column=1)

# # Create a ProgressBar to display Pokemon stats
# progress_bar = ttk.Progressbar(
#     root, orient=tk.HORIZONTAL, length=200, mode='determinate')
# progress_bar.grid(row=6, column=0, columnspan=2)

# Start the GUI main loop
root.mainloop()
