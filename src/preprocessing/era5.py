import cdsapi

client = cdsapi.Client()

dataset = "reanalysis-era5-single-levels"

request = {
    "product_type": ["reanalysis"],
    "variable": [
        "2m_temperature",
    ],
    "year": ["2024"],
    "month": ["01"],
    "day": ["01"],
    "time": ["12:00"],
    "data_format": "netcdf",
    "download_format": "unarchived",
}

client.retrieve(
    dataset,
    request,
    "data/raw/era5/era5_test.nc"
)

print("Download completed successfully!")