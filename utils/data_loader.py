from glob import glob
import pandas as pd

def load_subtitles_dataset(dataset_path):
    subtitles_paths = glob(dataset_path + '/*.ass')

    scripts = []
    episode_num = []
    for path in subtitles_paths:
        # read lines with specified encoding
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:  # Specify encoding
            lines = file.readlines()
            lines = lines[27:]  # Skip the first 27 lines
            lines = [",".join(line.split(',')[9:]) for line in lines]
        lines = [line.replace('\\N', ' ') for line in lines]
        script = " ".join(lines)

        # Extract episode number from the filename
        episodes = int(path.split('-')[-1].split('.')[0].strip())

        # Debugging: Print the episode number and the script length
        print(f"Processing file: {path}, Episode: {episodes}, Script length: {len(script)}")

        scripts.append(script)
        episode_num.append(episodes)

    df = pd.DataFrame.from_dict({"episode": episode_num, "script": scripts})
    return df
