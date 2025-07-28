import requests
from bs4 import BeautifulSoup

htmlTagsToIgnore = ["body"]
idsToIgnore = ["scottish-gifts-gordon-castle-gin-personalised-presents"]
cssToIgnore = ["template-index js-theme-loaded"]

def get_all_text_from_url(url):
    try:
        # Fetch the HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Instantiate soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and remove all elements with the specified id
        for element in htmlTagsToIgnore:
            tags = soup.find_all(id=element)
            for tag in tags:
                temp = tag.decompose()

        text_content = soup.get_text(separator='\n', strip=True)
        return text_content

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():

    # Open output file for writing
    output_filename = f"output.txt"
    with open(output_filename, "w") as out_file:

        # Open links file for reading and read each URL line by line 
        with open("links.txt", "r") as links_file:
            #Separate URL content in the output file with a newline


            #For each link
            for url in links_file:
                out_file.write(f'{url}\n')
                # Skip if no valid URL
                url = url.strip()
                if not url:
                    continue

                #Process the URL
                text = get_all_text_from_url(url)

                #Write to file and print error if not
                if text:
                    out_file.write(text)
                
                else:
                    print("Failed to fetch text.")









if __name__ == "__main__":
    main()
