import requests
from bs4 import BeautifulSoup


def get_package_names(url):
    """
    Fetches the package names from the given URL.

    Args:
        url (str): The URL of the Google Play Store games page.

    Returns:
        list: A list of package names.
    """

    response = requests.get(url)
    page = BeautifulSoup(response.text, "html.parser")
    package_names = []
    a_tags = page.find_all("a")

    for a_tag in a_tags:
        href = a_tag["href"]
        if len(href.split("?id="))>1:
            package_name=href.split("?id=")[1]
            package_names.append(package_name)
        else:
            pass
    return package_names