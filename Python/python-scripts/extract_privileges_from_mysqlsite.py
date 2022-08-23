from bs4 import BeautifulSoup
import requests

def extract_permissions() -> list:
    """This function takes the permission list from the MySQL website

    Returns:
        list: a list of availabe grants in MySQL
    """
    grants = []
    # Address of the MySQL website for the permissions
    url = "https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html"
    # call GET-Request
    responses = requests.get(url)
    # Parse BeautifulSoup HTML Document from source code
    html = BeautifulSoup(responses.text, 'html.parser')
    file = html.find_all("table")
    # print(type(html))
    soup = BeautifulSoup(str(file), 'html.parser')
    file2 = soup.find_all("code")
    for row in file2:
        grant = row.getText()
        if grant[2] not in ascii_lowercase:
            if "[" in grant:
                grant = grant.replace("[", "")
                grant = grant.replace("]", "")
            grants.append(grant)
    return grants
