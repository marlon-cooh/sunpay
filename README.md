# SunPay - Solar System Sizing Tool

## Overview
SunPay is an accurate solar system sizing tool that leverages NASA's POWER (Prediction of Worldwide Energy Resources) database to provide precise solar resource data for optimal system design.

## Features
- Integration with NASA POWER API for accurate solar radiation data
- Comprehensive parameter collection including:
  - Solar radiation metrics (direct, diffuse, global)
  - Meteorological data (temperature, wind speed, humidity)
  - Atmospheric conditions (cloud cover, UV index)
- Flexible date range selection for historical data analysis
- Support for both daily and monthly temporal resolutions

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/sunpay.git

# Navigate to the project directory
cd sunpay

# Install required dependencies
pip install -r requirements.txt
```

## Usage
```python
from nasa_power_request import get_solar_data

# Example usage
date_range = ['20190101', '20190301']
latitude = -73.756138
longitude = 3.997587

# Get solar data
data = get_solar_data(date_range, latitude, longitude)
```

## API Parameters
The tool collects various parameters from NASA POWER database including:
- `ALLSKY_SFC_SW_DWN`: All-sky surface shortwave downward irradiance
- `ALLSKY_KT`: Clearness index
- `T2M`: Temperature at 2 meters
- `WS2M`: Wind speed at 2 meters
- And many more meteorological parameters

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
[Add your license here]

## Acknowledgments
- NASA POWER Project for providing the solar resource data
- [Add any other acknowledgments]

## Contact
[Add your contact information]