import pandas as pd


class DataframeProcessService:

    def add_new_columns_to_dataframe(self, records: pd.DataFrame) -> pd.DataFrame:
        records['length_of_text'] = records['text'].str.len()
        return records
