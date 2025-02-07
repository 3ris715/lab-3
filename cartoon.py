# missing import statements should be added here
import wikipedia
import cv2
from images import get_wikipedia_page_thumbnail_url, download_image_from_url

def prompt_for_image():
    """
    Prompts the user for the name of a Wikipedia page and obtains the URL of the thumbnail image of the page.
    
    return url, page_name: str, str
    """
    search_query = input("Enter name of a personality: ")
    try:
        results = list(wikipedia.search(search_query, results=3))
        print("\nSelect a name from the following list:")
        for i in range(len(results)):
            print("{}. {}".format(i+1, results[i]))
        number = int(input("Enter the number of the desired name: "))
        name = results[number-1]
        url = get_wikipedia_page_thumbnail_url(name)
        print("\n({})".format(url))
        save_path = download_image_from_url(url, name)
        return save_path

    except Exception as e:
        print("Error: Unable to find image for the given name: {}\n".format(name))
        return None

    
def convert_image_to_cartoon(image_path):
    """
    Converts an image to a cartoon given the image_path.
    """
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurImage = cv2.medianBlur(image, 1)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 200, 200)
    cartoon = cv2.bitwise_and(color, color, mask = edges)
    cv2.imwrite(image_path, cartoon)
    print("Your image is called {}".format(image_path))
    
    return image_path
    
if __name__ == "__main__":

    found_image = None
    while found_image == None:
        found_image = prompt_for_image()

    convert_image_to_cartoon(found_image)

