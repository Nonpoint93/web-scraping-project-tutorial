from bs4 import BeautifulSoup
import pandas as pd

class Utils:
    
    """Utility class."""

    def __init__(self):
        pass

    def find_all_tables(self, html):
        """Find all the tables.
        """
        soup = BeautifulSoup(html.text, 'html.parser')
        tables = soup.find_all('table')
        return tables
    
    def process_data(self, df):
        
        """
        Cleans the DataFrame by:
        - Replacing '$', commas, and spaces with NaN.
        - Dropping rows and columns that are entirely empty or contain only NaN.
    
        Parameters:
            df (pd.DataFrame): The DataFrame to process.
    
        Returns:
            pd.DataFrame: The cleaned DataFrame.
        """
        
        df = df.replace({'\$': pd.NA, ',': pd.NA}, regex=True)
        df.dropna(inplace=True, axis=1, how='all')
        df.dropna(inplace=True, axis=0, how='all')
        return df

    def convert_table_to_dataframe(self, table):
        
        """Convert a BeautifulSoup table to a pandas DataFrame."""
        
        rows = table.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [item.text.strip() for item in cols]
            data.append([item for item in cols if item])
    
        df = pd.DataFrame(data,  columns=["Concept", "Figure"])
        return self.process_data(df)

