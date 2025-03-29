import ee
import numpy as np
from sklearn.cluster import KMeans
from datetime import date
from typing import Dict

ee.Initialize()

def analyze_crop_health(start_date: date, end_date: date, coordinates: list) -> Dict:
    farm_geom = ee.Geometry.Polygon(coordinates)
    
    collection = (ee.ImageCollection('COPERNICUS/S2_SR')
                 .filterBounds(farm_geom)
                 .filterDate(start_date.isoformat(), end_date.isoformat())
                 .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)))
    
    image = ee.Image(collection.sort('CLOUDY_PIXEL_PERCENTAGE').first())
    ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')
    
    ndvi_array = np.array(ndvi.sampleRectangle(region=farm_geom).get('NDVI').getInfo())
    rows, cols = ndvi_array.shape
    X = ndvi_array.reshape(rows * cols, 1)
    X = X[~np.isnan(X)]
    
    if len(X) == 0:
        return {
            "healthy": 0,
            "moderate": 0,
            "stressed": 0,
            "ndvi_image_url": None
        }
    
    kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
    labels = kmeans.labels_
    
    return {
        "healthy": float(np.percentile(X[labels == 2], 90)),
        "moderate": float(np.percentile(X[labels == 1], 50)),
        "stressed": float(np.percentile(X[labels == 0], 10)),
        "ndvi_image_url": ndvi.getThumbURL({'min': -1, 'max': 1, 'palette': ['red', 'yellow', 'green']})
    }