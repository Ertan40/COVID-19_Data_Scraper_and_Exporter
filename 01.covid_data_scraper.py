from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.worldometers.info/coronavirus/"


def fetch_data():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch data: {str(e)}")


def retrieve_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    main_div = soup.find_all('div', class_='maincounter-number')
    if not main_div:
        raise Exception("Main div not found!")

    covid_cases = []
    for div in main_div:
        span = div.find('span')
        if span:
            covid_cases.append(span.text.strip())
        else:
            raise Exception("Span not found!")

    return covid_cases


def retrieve_table_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='table')
    if not table:
        raise Exception("Table not found!")

    rows = table.find_all('tr')[1:]  # Skip the header row
    table_info = []
    for row in rows:
        columns = row.find_all('td')
        row_data = [col.text.strip() if col.text.strip() else 'N/A' for col in columns][1:15]
        table_info.append(row_data)

    return table_info


def retrieve_headers(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='table')
    if not table:
        raise Exception("Table not found!")

    headers = [th.text.strip() for th in table.find_all('th')][1:15]
    return headers


def process_data_for_excel(html):
    curr_data = retrieve_table_data(html)
    headers = retrieve_headers(html)

    df = pd.DataFrame(curr_data, columns=headers)

    # Drop columns if they exist
    columns_to_drop = ['NewCases', 'NewDeaths']
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], axis=1, inplace=True)

    # Save to Excel file
    df.to_excel('covid_statistics.xlsx', index=False)
    print("Excel file has been created successfully!")
    return df.head(5)


if __name__ == "__main__":
    html_data = fetch_data()

    # Fetch and print summary data
    cases = retrieve_data(html_data)
    print(f"Total COVID-19 cases in the world: {cases[0]}")
    print(f"Total deaths due to COVID-19 in the world: {cases[1]}")
    print(f"Total COVID-19 patients recovered in the world: {cases[2]}")
    print()

    # Process table data and export to Excel
    dataframe = process_data_for_excel(html_data)
    print()
    print(dataframe)