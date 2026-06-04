import os

current_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(current_dir)
file_path = os.path.join(PROJECT_ROOT, 'website_bot.properties')


def read_property(file_path):
    separator = "="
    dictionary = {}
    try:
        # logging.info(f"Reading Property File From Path...{file_path}")
        with open(file_path, 'r') as f:
            for line in f:
                if separator in line:
                    # Find the name and value by splitting the string
                    name, value = line.split(separator, 1)
                    # Assign key value pair to dict
                    # strip() removes white space from the ends of strings

                    dictionary[name.strip()] = value.strip()
    except Exception as error:
        # logging.error(f"Unable To Read Properties File...{error}")
        return f"unable to read properties file {error}"
    else:
        # logging.info(f"Properties Dictionary...{dictionary}")
        return dictionary


properties = read_property(file_path)
