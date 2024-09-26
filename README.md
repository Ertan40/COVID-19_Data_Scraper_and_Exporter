# COVID-19 Data Scraper and Exporter
 This Python script scrapes COVID-19 statistics from Worldometers, processes the data, and exports the results into an Excel file. It also provides a summary of the global COVID-19 case numbers directly in the terminal.

## Features
- Fetches and parses COVID-19 statistics (total cases, deaths, recoveries) from Worldometers.
- Extracts tabular data (country-wise statistics) from the site and stores it into a structured format.
- Cleans the data by removing columns that lack useful information (NewCases, NewDeaths).
- Exports the cleaned data into an Excel file (covid_statistics.xlsx).
- Provides a summary of total global COVID-19 cases, deaths, and recoveries.
## Prerequisites
To run the script, you need to have the following installed on your machine:

- Python 3.x
- The required Python libraries:
   - requests
   - pandas
   - beautifulsoup4
   - openpyxl (for Excel export)
## Installation
1. Clone this repository:
```sh
git clone https://github.com/yourusername/covid-data-scraper.git
cd covid-data-scraper
```
2. Install the required Python packages:
```sh
pip install -r requirements.txt
```
You can manually install the libraries with:
```sh
pip install requests beautifulsoup4 pandas openpyxl
```
## Usage
1. Run the script to fetch the data and create an Excel file:
```sh
python covid_data_scraper.py
```
2. The script will output the following information in the terminal:
- Total global COVID-19 cases
- Total deaths due to COVID-19
- Total recovered COVID-19 patients
Example output:
```python
Total COVID-19 cases in the world: 704,753,890
Total deaths due to COVID-19 in the world: 7,010,681
Total COVID-19 patients recovered in the world: 675,619,811
```
3. The country-wise data will be saved in an Excel file named covid_statistics.xlsx in the same directory.
## Excel File Format
The Excel file will have the following columns:

- Country, Other: The name of the country or region.
- TotalCases: Total reported COVID-19 cases.
- TotalDeaths: Total reported deaths due to COVID-19.
- TotalRecovered: Total number of recovered cases.
- ActiveCases: Currently active cases.
- Serious, Critical: Number of serious/critical cases.
- TotalTests: Total number of COVID-19 tests performed.
- Population: Population of the country or region.
## Error Handling
- If the script cannot retrieve the data, it will raise an appropriate error message. Ensure that your internet connection is stable, and that the Worldometers website is accessible.
- If the structure of the website changes, the script might not function correctly. Updates to the scraping logic may be required.
## Note
The script fetches real-time data from Worldometers, so the output might change over time. Additionally, if the website's structure changes, the scraper might need updates to handle the new HTML structure.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you have any questions or feedback, feel free to reach out at ertandonmez1@gmail.com.
