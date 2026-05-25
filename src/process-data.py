import pandas as pd
import glob

def main():
    files = glob.glob("../data/raw/*.csv")

    dfs = [pd.read_csv(file) for file in files]

    combined_df = pd.concat(dfs, ignore_index=True)

    combined_df.to_csv("../data/processed/clean_data.csv", index=False)

if __name__ == "__main__":
    main()


