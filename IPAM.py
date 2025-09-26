import pandas as pd
import requests
import json
import os

# --- Configuration ---
NETBOX_URL = 'http://202.163.112.238/api/'
NETBOX_TOKEN = '225330b0c23f4f53e6b2c25902fd9ba3ae36e55d'
EXCEL_FILE = 'prefixes.xlsx'

# Ensure the column names in your Excel sheet match these
SITE_COLUMN = 'Site'
IPV6_PREFIX_COLUMN = 'IPv6 Prefix'
DESCRIPTION_COLUMN = 'Description'

# --- Functions ---
def get_site_ids():
    """
    Fetches all sites from NetBox and returns a dictionary mapping site names to IDs.
    """
    headers = {
        'Authorization': f'Token {NETBOX_TOKEN}',
        'Accept': 'application/json',
    }
    sites_url = f'{NETBOX_URL}dcim/sites/'
    
    try:
        response = requests.get(sites_url, headers=headers)
        response.raise_for_status()
        sites = response.json().get('results', [])
        
        site_map = {site['name']: site['id'] for site in sites}
        return site_map
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sites from NetBox: {e}")
        return None

def read_excel_to_json(excel_file, site_map):
    """
    Reads an Excel file and converts data into a JSON list, including the site ID.
    """
    if not os.path.exists(excel_file):
        raise FileNotFoundError(f"The file '{excel_file}' was not found.")

    try:
        df = pd.read_excel(excel_file)
        
        required_columns = [SITE_COLUMN, IPV6_PREFIX_COLUMN, DESCRIPTION_COLUMN]
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"Excel sheet must contain all columns: {required_columns}")

        prefixes_list = []
        for index, row in df.iterrows():
            site_name = str(row[SITE_COLUMN]).strip()
            if site_name not in site_map:
                print(f"Skipping prefix '{row[IPV6_PREFIX_COLUMN]}' for unknown site: '{site_name}'")
                continue
                
            prefixes_list.append({
                'prefix': row[IPV6_PREFIX_COLUMN],
                'description': row[DESCRIPTION_COLUMN],
                'site': site_map[site_name]
            })
        
        return prefixes_list
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

def upload_to_netbox(data_list):
    """
    Uploads a list of IPv6 prefixes to NetBox.
    """
    headers = {
        'Authorization': f'Token {NETBOX_TOKEN}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    
    upload_url = f'{NETBOX_URL}ipam/prefixes/'
    
    for item in data_list:
        try:
            payload = json.dumps(item)
            response = requests.post(upload_url, data=payload, headers=headers)
            response.raise_for_status()
            
            print(f"Successfully uploaded prefix: {item['prefix']} for site ID: {item['site']}")
        except requests.exceptions.HTTPError as err:
            print(f"Failed to upload prefix {item['prefix']}: {err}")
            print(f"Response content: {err.response.text}")
        except Exception as e:
            print(f"An error occurred for prefix {item['prefix']}: {e}")

# --- Main execution ---
if __name__ == '__main__':
    print("Starting the NetBox IPv6 prefix automation script...")
    
    # Step 1: Get all sites from NetBox
    site_map = get_site_ids()
    if not site_map:
        print("Could not retrieve sites. Exiting.")
    else:
        print(f"Found {len(site_map)} sites in NetBox.")
    
        # Step 2: Read the Excel sheet and convert to JSON format
        prefixes_data = read_excel_to_json(EXCEL_FILE, site_map)
        
        if prefixes_data:
            print(f"Found {len(prefixes_data)} prefixes to upload.")
            
            # Step 3: Upload the data to NetBox
            upload_to_netbox(prefixes_data)
        else:
            print("No data to upload. Please check the Excel file and script configuration.")
        
    print("Script finished.")

