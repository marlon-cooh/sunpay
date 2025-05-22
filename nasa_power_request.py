import requests #type: ignore
import pandas as pd #type: ignore
import json, timeit

parameters = [
    'CLRSKY_SFC_SW_DWN',
    'ALLSKY_SFC_SW_DWN',
    'ALLSKY_KT',
    'WS2M',
    'WS10M',
    'WS50M',
    'T2M',
    'T10M',
    'TS',
    'QV2M',
    'RH2M',
    'PRECTOTCORR',
    'PS',
    'WD2M',
    'WD10M',
    'WD50M',
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
    'U2M',
    'U10M',
    'U50M',
    'MIDDAY_INSOL',
    'V2M',
    'V10M',
    'V50M',
    'PBLTOP',
    'PW',
    'SLP',
    'RHOA',
    'ZENITH_LUMINANCE'
]

parameters_subset = parameters[1]
lon, lat = 3.997587, -73.756138
date_range = ['20190101', '20190301']

daily_api = f'https://power.larc.nasa.gov/api/temporal/monthly/point?parameters={parameters_subset}&community=RE&longitude={lon}&latitude={lat}&start={date_range[0]}&end={date_range[1]}&format=JSON'
monthly_api = f'https://power.larc.nasa.gov/api/temporal/monthly/point?parameters={parameters_subset}&community=RE&longitude={lon}&latitude={lat}&format=CSV&start=2020&end=2021'
test_api = f"https://power.larc.nasa.gov/api/temporal/monthly/point?start=2022&end=2024&latitude={lat}&longitude={lon}&community=re&parameters={parameters_subset}&format=csv&header=true&time-standard=utc"

def make_request():
    return requests.get(test_api).text

# # Measure the time taken for the API request
# execution_time = timeit.timeit(make_request, number=1)
# print(f"API request took {execution_time:.2f} seconds")

response = make_request()
# irradiance_from_rq = response["properties"]["parameter"][parameters_subset]
# df = pd.DataFrame({
#     "date": list(irradiance_from_rq.keys()),
#     "irradiance": list(irradiance_from_rq.values())
# })
# df["date"] = pd.to_datetime(df["date"])
# print(df)

print(response)