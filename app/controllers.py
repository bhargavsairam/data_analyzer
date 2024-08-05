from .models import DataModel

def fetch_data():
    data_model = DataModel(data="Some important data")
    return data_model.get_data()
