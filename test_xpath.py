import requests
import re
import time
from lxml import html


def test_xpaths(manager_id="49850"):  # Using Miroslav Klose's ID as default
    """Test all XPaths for the manager contracts page."""

    # Define XPaths
    xpaths = {
        "TABLE": ".//table[contains(@class, 'items')]",
        "ROWS": ".//tbody/tr[not(contains(@class, 'extrarow'))]",
        "CLUB_LINK": ".//td[contains(@class, 'hauptlink')]/a/@href",
        "CLUB_NAME": ".//td[contains(@class, 'hauptlink')]/a/text()",
        "ROLE": ".//td[contains(@class, 'hauptlink')]/br/following-sibling::text()",
        "START_DATE": ".//td[position()=3]/text()",
        "END_DATE": ".//td[position()=4]//i/text()"
    }

    # The URL
    url = f"https://www.transfermarkt.com/-/stationen/trainer/{manager_id}"

    # Headers to avoid blocking
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"Testing XPaths on URL: {url}")

    try:
        # Make the request with a timeout
        start_time = time.time()
        response = requests.get(url, headers=headers, timeout=10)
        request_time = time.time() - start_time

        print(f"Request completed in {request_time:.2f} seconds with status code {response.status_code}")

        if response.status_code != 200:
            print(f"Failed to fetch page: Status code {response.status_code}")
            return False

        # Parse the HTML
        page = html.fromstring(response.content)

        # Test each XPath
        results = {}

        # Test TABLE XPath
        table = page.xpath(xpaths["TABLE"])
        results["TABLE"] = len(table) > 0
        print(f"TABLE: {'✅ Found' if results['TABLE'] else '❌ Not found'} ({len(table)} elements)")

        if not results["TABLE"]:
            print("Table not found, can't test further XPaths")
            return False

        # Test ROWS XPath
        rows = table[0].xpath(xpaths["ROWS"])
        results["ROWS"] = len(rows) > 0
        print(f"ROWS: {'✅ Found' if results['ROWS'] else '❌ Not found'} ({len(rows)} elements)")

        if not results["ROWS"]:
            print("Rows not found, can't test further XPaths")
            return False

        # Test the rest of the XPaths on the first row
        first_row = rows[0]

        for xpath_name in ["CLUB_LINK", "CLUB_NAME", "ROLE"]:
            elements = first_row.xpath(xpaths[xpath_name])
            results[xpath_name] = len(elements) > 0

            value = elements[0].strip() if results[xpath_name] else "N/A"
            print(f"{xpath_name}: {'✅ Found' if results[xpath_name] else '❌ Not found'} => {value}")

        # Special handling for dates to extract only the actual dates
        for xpath_name in ["START_DATE", "END_DATE"]:
            elements = first_row.xpath(xpaths[xpath_name])
            results[xpath_name] = len(elements) > 0

            if results[xpath_name]:
                # Get the raw text
                raw_text = elements[0].strip()

                # Extract just the date part if it exists in parentheses
                date_match = re.search(r"\((.*?)\)", raw_text)
                if date_match:
                    value = date_match.group(1)
                else:
                    # For expected dates or dates without parentheses
                    if "expected" in raw_text:
                        value = raw_text.replace("expected", "").strip()
                    else:
                        value = raw_text
            else:
                value = "N/A"

            print(f"{xpath_name}: {'✅ Found' if results[xpath_name] else '❌ Not found'} => {value}")

        # Overall result
        all_passed = all(results.values())
        print(f"\nOverall result: {'✅ All XPaths passed' if all_passed else '❌ Some XPaths failed'}")

        # If all passed, show a sample of the data
        if all_passed:
            print("\nSample data from first row:")

            club_link = first_row.xpath(xpaths["CLUB_LINK"])[0]
            club_id = club_link.split("/")[-1]
            club_name = first_row.xpath(xpaths["CLUB_NAME"])[0].strip()
            role = first_row.xpath(xpaths["ROLE"])[0].strip()

            # Extract clean dates
            start_date_raw = first_row.xpath(xpaths["START_DATE"])[0].strip()
            start_date_match = re.search(r"\((.*?)\)", start_date_raw)
            start_date = start_date_match.group(1) if start_date_match else start_date_raw

            end_date_raw = first_row.xpath(xpaths["END_DATE"])[0].strip()
            end_date_match = re.search(r"\((.*?)\)", end_date_raw)
            if "expected" in end_date_raw:
                end_date = end_date_raw.replace("expected", "").strip()
            else:
                end_date = end_date_match.group(1) if end_date_match else end_date_raw

            print(f"Manager ID: {manager_id}")
            print(f"Club: {club_name} (ID: {club_id})")
            print(f"Role: {role}")
            print(f"Start Date: {start_date}")
            print(f"End Date: {end_date}")

        return all_passed

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return False
    except Exception as e:
        print(f"Error parsing page: {e}")
        import traceback
        traceback.print_exc()
        return False


# For direct testing when running this file
if __name__ == "__main__":
    manager_id = "49850"  # Default is Miroslav Klose
    test_xpaths(manager_id)
