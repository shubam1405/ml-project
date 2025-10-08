import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

    '''
    Explanation:

        Using @dataclass automatically generates the __init__ method for you.

        This class stores paths for your datasets.

        os.path.join ensures your code works on any OS (Windows, Linux, etc.).

        train.csv, test.csv, and data.csv will be stored inside the artifacts folder.

        Why we do this:

        Keeps file paths in one place.

        Easy to modify later without touching the main ingestion logic.

        Makes your code cleaner and maintainable.
            
    
    '''

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        '''
        
        Explanation:

When you create a DataIngestion object, it automatically creates a DataIngestionConfig object and stores it in self.ingestion_config.

This means anywhere inside this class, you can access your paths like self.ingestion_config.train_data_path.
        
        '''

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            '''
             os.path.dirname(...) → Gets the folder name (artifacts in this case).

            os.makedirs(..., exist_ok=True) → Creates the folder if it doesn’t exist.

            exist_ok=True → Prevents error if folder already exists.

            Why we do this:

            Ensures the folder exists before saving files to it.
            '''
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)  
            '''
            Keeps a backup of raw data before any transformations.

            Useful for reproducibility and debugging.
            '''

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            '''
            Saves train and test datasets into artifacts/train.csv and artifacts/test.csv.

            Structured like raw data, ready for transformation or model training.
            
            '''
            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
            '''
            After ingestion, it returns paths so other parts of your pipeline (like data transformation) can use them
            '''
        except Exception as e:
            raise CustomException(e,sys)
        
        '''
        
        Any error in reading, splitting, or saving is caught.

        Raises a custom exception that can log the error along with the stack trace.

        Why:

        Makes debugging easier and keeps error handling consistent across your project
        '''
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))



