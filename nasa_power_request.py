import requests #type: ignore
import pandas as pd #type: ignore
import timeit

parameters = [
    'CLRSKY_SFC_SW_DWN',
    'ALLSKY_SFC_SW_DWN',
    'ALLSKY_KT',
    'ALLSKY_SFC_UV_INDEX',
    'ALLSKY_SRF_ALB',
    'ALLSKY_SFC_SW_UP',
    'ALLSKY_SFC_SW_DNI',
    'ALLSKY_SFC_SW_DIFF',
    'ALLSKY_SFC_LW_DWN',
    'ALLSKY_SFC_LW_UP',
    'CLOUD_AMT_DAY',
    'DIRECT_ILLUMINANCE',
    'GLOBAL_ILLUMINANCE',
    'DIFFUSE_ILLUMINANCE',
    'ALLSKY_SFC_PAR_TOT',
    'ALLSKY_SFC_UVA',
    'ALLSKY_SFC_UVB',
    'CLRSKY_SRF_ALB',
    'CLRSKY_SFC_LW_DWN',
    'CLRSKY_SFC_LW_UP',
    'CLRSKY_SFC_PAR_TOT',
    'CLRSKY_SFC_SW_DIFF',
    'CLRSKY_SFC_SW_DNI',
    'CLRSKY_SFC_SW_UP',
    'CLOUD_OD',
]

def request_parameters(params, lon, lat, date_range=[2020, 2024]) -> pd.DataFrame:
    """
        Returns a cleaned dataset of the parameters fetched from the NASA PowerLarc database.
            Arguments:
                * params: list of parameters to be fetched from the database.
                * lon: longitude of the location.
                * lat: latitude of the location.
                * date_range: list of dates to be fetched from the database, in this case set between 2020-01 and 2024-01..
            Returns:
                * dt : dataset of params along a specified time, in this case set between 2020-01 and 2024-01.
    """
   
    # API URL request, output in JSON format.
    api = f'https://power.larc.nasa.gov/api/temporal/monthly/point?start={date_range[0]}&end={date_range[1]}&latitude={lat}&longitude={lon}&community=re&parameters={params}&format=JSON&header=false&time-standard=utc'

    # GET request to the API.
    response = requests.get(api).json()
    # Extract the data from the response in JSON format.
    json_response = response["properties"]["parameter"][params]
    # Removing annual average values that can not be interpreted with datetime methods.
    clean_dict = {k:v for k, v in json_response.items() if not k.endswith('13')}
    
    # Convert the dictionary to a DataFrame.
    df = pd.DataFrame(
        {
            "date" : clean_dict.keys(),
            "value" : clean_dict.values()
        }
    )
    
    df['date'] = pd.to_datetime(df['date'], format='%Y%m')
    df['month'] = df['date'].dt.month
    
    # Show dataset for analysis.
    df = df[['month', 'value']]
    return df

if __name__ == "__main__":
    
    exec_time = timeit.timeit(
        'request_parameters(params=parameters[1], lon=3.997587, lat=-73.756138)',
        globals=globals(),
        number=1
    )
    
    print(f"Execution time: {exec_time:.4f} seconds")
    
    # dataset = request_parameters(
    #     params=parameters[1],
    #     lon=3.997587,
    #     lat=-73.756138
    #     # date_range=[2020, 2024]
    # )
    
    # print(dataset.head())