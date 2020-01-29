import pathlib
import os

def generate_dotenv():
    dotenv_path = pathlib.Path(os.getcwd()) / '.env'

    apikey = input("UW Open Data API key: ")

    with open(str(dotenv_path.absolute()), 'w') as f:
        f.write('UW_OPENDATA_API_KEY={}'.format(apikey))
        f.write('\n')

if __name__ == "__main__":
    generate_dotenv()