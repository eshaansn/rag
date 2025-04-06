import argparse
from database.data_utils import clear_database

def main():
    # Check if the database should be cleared (using the --clear flag).
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    # parser.add_argument("--add", type=str, default="chroma", help="Database type.")
    # parser.add_argument("--config", type=str, default="configs/config.yaml", help="Path to the config file.")
 
    
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    # Create (or update) the data store.

    # print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()