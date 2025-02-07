# missing import statements should be added here
import wikipedia
from images import get_wikipedia_page_thumbnail_url, download_image_from_url

def prompt_for_image():
    """
    Prompts the user for the name of a Wikipedia page and obtains the URL of the thumbnail image of the page.
    
    return url, page_name: str, str
    """
    search_query = input("Enter name of a personality: ")
    try:
        results = list(wikipedia.search(search_query, results=3))
        print("Select a name from the following list:")
        for i in range(len(results)):
            print("{}. {}".format(i+1, results[i]))
        number = input("Enter the number of the desired name: ")
    except Exception as e:
        print(f"Error: Unable to find image for the given name: {e}")
        return None, None
    return results, number
    
def convert_image_to_cartoon(image_path):
    """
    Converts an image to a cartoon given the image_path.
    """
    pass
    # TODO (and remove the pass statement above)


    
if __name__ == "__main__":
    prompt_for_image()
    # TODO (and remove the pass statement above)

