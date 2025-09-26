
import pynetbox
import ipaddress
import sys

# --- NetBox Connection Details ---
# IMPORTANT: Replace these placeholders with your actual NetBox URL and API token.
# You can generate a token in NetBox under your user profile.
NETBOX_URL = 'http://202.163.112.238'
NETBOX_TOKEN = '2649f4f85ef074b389751b61410a46950fcb680d'

# --- Site and Prefix Data ---
# The site name to associate with the prefixes.
SITE_NAME = 'Quetta'

# A list of dictionaries defining the prefix ranges and their descriptions.
# The 'end' prefix is inclusive.
prefix_data = [
    {
        'start': '2400:ADC0:0200::/48',
        'end': '2400:ADC0:020F::/48',
        'description': 'Google'
    },
    {
        'start': '2400:ADC0:0210::/48',
        'end': '2400:ADC0:021F::/48',
        'description': 'Facebook'
    },
    {
        'start': '2400:ADC0:0220::/48',
        'end': '2400:ADC0:022F::/48',
        'description': 'Akamai'
    },
    {
        'start': '2400:ADC0:0230::/48',
        'end': '2400:ADC0:023F::/48',
        'description': 'Netflix'
    },
    {
        'start': '2400:ADC0:0240::/48',
        'end': '2400:ADC0:02FF::/48',
        'description': 'Reserved Prefixes'
    }
]


def main():
    """
    Main function to connect to NetBox and add the IPv6 prefixes.
    """
    try:
        nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
        nb.http_session.verify = False  # Set to True if your NetBox uses a trusted SSL certificate
    except Exception as e:
        print(f"Error connecting to NetBox: {e}")
        sys.exit(1)

    print(f"Successfully connected to NetBox at {NETBOX_URL}")

    # Step 1: Find the site object for Hyderabad.
    try:
        site = nb.dcim.sites.get(name=SITE_NAME)
        if not site:
            print(f"Error: Site '{SITE_NAME}' not found in NetBox. Please create it first.")
            sys.exit(1)
    except Exception as e:
        print(f"Error finding site '{SITE_NAME}': {e}")
        sys.exit(1)

    print(f"Found site '{site.name}' (ID: {site.id})")

    # Step 2: Iterate through the prefix ranges and add each one.
    total_prefixes = 0
    for data in prefix_data:
        start_network = ipaddress.IPv6Network(data['start'])
        end_network = ipaddress.IPv6Network(data['end'])
        
        # Get the integer representation of the addresses for easy iteration.
        start_int = int(start_network.network_address)
        end_int = int(end_network.network_address)
        
        print(f"\nProcessing range: {data['start']} - {data['end']} with description '{data['description']}'")

        # Iterate from the start prefix to the end prefix.
        current_int = start_int
        while current_int <= end_int:
            current_address = ipaddress.IPv6Address(current_int)
            prefix_to_add = ipaddress.IPv6Network(f'{current_address}/48')
            
            payload = {
                'prefix': str(prefix_to_add),
                'description': data['description'],
                'site': site.id,
            }
            
            try:
                # Add the prefix to NetBox.
                nb.ipam.prefixes.create(**payload)
                print(f"  > Added prefix: {prefix_to_add}")
                total_prefixes += 1
            except pynetbox.core.query.RequestError as e:
                # This will catch errors like 'Prefix already exists'.
                if 'already exists' in str(e):
                    print(f"  - Prefix {prefix_to_add} already exists, skipping.")
                else:
                    print(f"  > Error adding {prefix_to_add}: {e}")
            except Exception as e:
                print(f"  > Unexpected error adding {prefix_to_add}: {e}")

            # Increment to the next /48 prefix.
            current_int += 2**80  # This is the size of a /48 prefix
    
    print(f"\nScript finished. Total prefixes processed: {total_prefixes}")


if __name__ == '__main__':
    main()