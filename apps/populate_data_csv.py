import pandas as pd
import logging
from datetime import datetime
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("airflow.task")
LOGGER.info('initialise data dictionary....')
data_dict = {'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

             'Gender': ["Male", "Female", "Female", "Male",
                        "Male", "Female", "Male", "Male",
                        "Female", "Male"],

             'Age': [20, 21, 19, 18, 25, 26, 32, 41, 20, 19],

             'Annual Income(k$)': [10, 20, 30, 10, 25, 60, 70,
                                   15, 21, 22],

             'Spending Score': [30, 50, 48, 84, 90, 65, 32, 46,
                                12, 56]}

# Create DataFrame
LOGGER.info(f' pushing data to data frame...')
data = pd.DataFrame(data_dict)
path='/home/airflow/gcs/data/'
file = f'Customers_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.csv'
LOGGER.info(f'Genrating customers data file {file} at path: {path}')
# Write to CSV file
data.to_csv(f"{path}/{file}",sep=',',index=False)