import requests, timeit #type: ignore
import pandas as pd #type: ignore
import numpy as np #type: ignore

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
    
    # Convert any negative values of fetched param to NaN.
    df.loc[df['value'] <= 0, 'value'] = np.nan
    
    # Removing missing values.
    df.dropna(inplace=True)
    return df.value.mean()

def pvout(yearly_irr, pr=0.8):
    """
        Calculates the output of the PV system.
            Arguments:
                * yearly_irr: yearly irradiation in kWh/m2/year.
                * pr: performance ratio of the PV system.
            Returns:
                * pvout: output of the PV system in kWh/kWp/year.
    """    
    # Output of the PV system in kWh/kWp/year.
    pvout = yearly_irr * pr
    return pvout

def required_peak_power(monthly_value, pvout):
    """
        Sizes the PV system based on the monthly value of the parameter.
            Arguments:
                * monthly_value: monthly value of the parameter in kWh/month.
                * pvout: output of the PV system in kWh/kWp/year.
            Returns:
                * peak_power: size of the PV system in kWp.
    """
    yearly_value = monthly_value * 12
    peak_power = yearly_value / pvout
    return peak_power

def no_of_panels(peak_power, nominal_power=0.620):
    """
        Calculates the number of panels required for the PV system.
            Arguments:
                * peak_power: size of the PV system in kWp.
                * nominal_power: nominal power of the panel in kWp.
            Returns:
                * no_of_panels: number of panels required for the PV system.

    """
    no_of_panels = peak_power / nominal_power
    return no_of_panels

def energy_produced(yearly_irr, efficiency, ind_area=2.53, pr=0.8):
    """
        Calculates the energy produced by the PV system.
            Arguments:
                * yearly_irr: yearly irradiation in kWh/m2/year.
                * efficiency: efficiency of the PV system.
            Returns:
                * energy_produced: energy produced by the PV system in kWh/year.
    """
    # Area of the panel array in m2.
    area = no_of_panels * ind_area
    
    # Energy produced by the PV system in kWh/year.
    energy_produced = yearly_irr * efficiency * area * pr
    return energy_produced

def fetch_request_parameters_time(runs):
    """
    Benchmarks the execution time of the request_parameters function.
    Arguments:
        * runs: Number of times to run the benchmark.
    """
    total_time = 0
    for i in range(runs):
        exec_time = timeit.timeit(
            'request_parameters(params=parameters[1], lon=3.997587, lat=-73.756138)',
            globals=globals(),
            number=1
        )
        total_time += exec_time
        print(f"Run {i+1}: {exec_time:.4f} seconds")
    average_time = total_time / runs
    print(f"\nAverage execution time over {runs} runs: {average_time:.4f} seconds")

if __name__ == "__main__":
    
    # Inputs.
    # Location coordinates.
    dataset = request_parameters(
        params=parameters[1],
        lon=3.997587,
        lat=-73.756138
        # date_range=[2020, 2024]
    )
    
    # User consumption.
    user_consumption = 1000 # kWh/month
    
    yearly_irr = dataset * 365.25
    # Calculate the output of the PV system.
    pvout = pvout(yearly_irr)
    
    # Calculate the size of the PV system.
    peak_power = required_peak_power(user_consumption, pvout)
    
    # Calculate the number of panels required for the PV system.
    no_of_panels = no_of_panels(peak_power)
    
    # Calculate the energy produced by the PV system.
    energy_produced = energy_produced(yearly_irr, efficiency=0.2315)
    
    # Print the results.
    print(f"User consumption: {user_consumption} kWh/month")
    print(f"Yearly irradiation: {yearly_irr:.2f} kWh/m2/year")
    print(f"Output of the PV system: {pvout:.2f} kWh/kWp/year")
    print(f"Size of the PV system: {peak_power:.2f} kWp")
    print(f"Number of panels required: {no_of_panels:.2f}")
    print(f"Energy produced by the PV system: {energy_produced:.2f} kWh/year")
    
    
    