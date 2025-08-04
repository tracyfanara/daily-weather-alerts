import os
from dotenv import load_dotenv
from utils.map_sources import MAPS
from scheduler.run_daily import download_maps, send_email

load_dotenv()

def main():
maps = download_maps(MAPS)
send_email(maps)

if __name__ == "__main__":
main()
