from flask import Flask, render_template
import folium
import folium.plugins as plugins

app = Flask(__name__)

@app.route('/',methods=['GET'])
def ap():
    m = folium.Map(location=[20, 0], zoom_start=2, tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',attr='hi')
    green_gasdata = [
    [37.7749, -122.4194, 0.2],    # San Francisco, USA
    [40.7128, -74.0060, 0.8],     # New York City, USA
    [34.0522, -118.2437, 0.5],    # Los Angeles, USA
    [41.8781, -87.6298, 0.6],     # Chicago, USA
    [47.6062, -122.3321, 0.4],    # Seattle, USA
    [51.5074, -0.1278, 0.7],      # London, UK
    [48.8566, 2.3522, 0.3],       # Paris, France
    [35.6895, 139.6917, 0.9],     # Tokyo, Japan
    [39.9042, 116.4074, 0.8],     # Beijing, China
    [55.7558, 37.6176, 0.6],      # Moscow, Russia
    [39.9042, 32.8597, 0.5],      # Ankara, Turkey
    [48.2082, 16.3738, 0.4],      # Vienna, Austria
    [40.4168, -3.7038, 0.6],      # Madrid, Spain
    [52.3676, 4.9041, 0.3],       # Amsterdam, Netherlands
    [41.9028, 12.4964, 0.5],      # Rome, Italy
    [31.7683, 35.2137, 0.7],      # Jerusalem, Israel
    [59.9343, 30.3351, 0.4],      # Saint Petersburg, Russia
    [37.5665, 126.978, 0.6],      # Seoul, South Korea
    [55.9533, -3.1883, 0.5],      # Edinburgh, Scotland
    [-33.8688, 151.2093, 0.7],    # Sydney, Australia
    [-23.5505, -46.6333, 0.5],    # São Paulo, Brazil
    [19.4326, -99.1332, 0.6],     # Mexico City, Mexico
    [1.3521, 103.8198, 0.4],      # Singapore
    [6.5244, 3.3792, 0.5],        # Lagos, Nigeria
    [45.4215, -75.6972, 0.4],     # Ottawa, Canada
    [55.6761, 12.5683, 0.3],      # Copenhagen, Denmark
    [-26.2041, 28.0473, 0.5],     # Johannesburg, South Africa
    [43.6511, -79.347015, 0.6],   # Toronto, Canada
    [28.6139, 77.2090, 0.7],      # New Delhi, India
    [19.0760, 72.8777, 0.6],      # Mumbai, India
    [12.9716, 77.5946, 0.5],      # Bengaluru, India
    [22.5726, 88.3639, 0.4],      # Kolkata, India
    [13.0827, 80.2707, 0.5],      # Chennai, India
    [23.0225, 72.5714, 0.6],      # Ahmedabad, India
    [17.385044, 78.486671, 0.7],  # Hyderabad, India
    [28.7041, 77.1025, 0.6],      # Delhi, India (alternate)
    [30.7333, 76.7794, 0.4],      # Chandigarh, India
    [8.5241, 76.9366, 0.5],       # Kochi, India
    [-33.4489, -70.6693, 0.5],    # Santiago, Chile
    [-12.0464, -77.0428, 0.4],    # Lima, Peru
    [3.139, 101.6869, 0.5],       # Kuala Lumpur, Malaysia
    [13.7563, 100.5018, 0.6],     # Bangkok, Thailand
    [14.5995, 120.9842, 0.5],     # Manila, Philippines
    [10.8231, 106.6297, 0.4],     # Ho Chi Minh City, Vietnam
    [-6.2088, 106.8456, 0.6],     # Jakarta, Indonesia
    [19.0760, 72.8777, 0.6],      # Mumbai, India
    [28.6139, 77.2090, 0.7],      # New Delhi, India
    [30.0444, 31.2357, 0.5],      # Cairo, Egypt
    [25.276987, 55.296249, 0.7],  # Dubai, UAE
    [41.0082, 28.9784, 0.6],      # Istanbul, Turkey
    [37.9838, 23.7275, 0.4],      # Athens, Greece
    [38.7223, -9.1399, 0.5],      # Lisbon, Portugal
    [59.3293, 18.0686, 0.4],      # Stockholm, Sweden
    [59.9139, 10.7522, 0.3],      # Oslo, Norway
    [47.3769, 8.5417, 0.5],       # Zurich, Switzerland
    [50.8503, 4.3517, 0.5],       # Brussels, Belgium
    [40.7306, -73.9352, 0.7],     # New York City, USA
    [34.0522, -118.2437, 0.5],    # Los Angeles, USA
    [37.7749, -122.4194, 0.2],    # San Francisco, USA
    [48.8566, 2.3522, 0.3],       # Paris, France
    [55.6761, 12.5683, 0.3],      # Copenhagen, Denmark
    [40.4168, -3.7038, 0.6],      # Madrid, Spain
    [52.3676, 4.9041, 0.3],       # Amsterdam, Netherlands
    [51.5074, -0.1278, 0.7],      # London, UK
    [37.5665, 126.978, 0.6],      # Seoul, South Korea
    [19.4326, -99.1332, 0.6],     # Mexico City, Mexico
    [13.0827, 80.2707, 0.5],      # Chennai, India
    [-33.8688, 151.2093, 0.7],    # Sydney, Australia
    [1.3521, 103.8198, 0.4],      # Singapore
    [55.9533, -3.1883, 0.5],      # Edinburgh, Scotland
    [39.9042, 32.8597, 0.5],      # Ankara, Turkey
    [28.7041, 77.1025, 0.6],      # Delhi, India (alternate)
    [-23.5505, -46.6333, 0.5],    # São Paulo, Brazil
    [31.7683, 35.2137, 0.7],      # Jerusalem, Israel
    [6.5244, 3.3792, 0.5],        # Lagos, Nigeria
    [45.4215, -75.6972, 0.4],     # Ottawa, Canada
    [55.7558, 37.6176, 0.6],      # Moscow, Russia
    [8.5241, 76.9366, 0.5],       # Kochi, India
    [30.7333, 76.7794, 0.4],      # Chandigarh, India
    [22.5726, 88.3639, 0.4],      # Kolkata, India
    [12.9716, 77.5946, 0.5],      # Bengaluru, India
    [17.385044, 78.486671, 0.7],  # Hyderabad, India
    [-26.2041, 28.0473, 0.5],     # Johannesburg, South Africa
    [43.6511, -79.347015, 0.6],   # Toronto, Canada
    [38.7223, -9.1399, 0.5],      # Lisbon, Portugal
    [55.9533, -3.1883, 0.5],      # Edinburgh, Scotland
    [49.2827, -123.1207, 0.4],    # Vancouver, Canada
    [59.9343, 30.3351, 0.4],      # Saint Petersburg, Russia
    [45.4654, 9.1859, 0.6],       # Milan, Italy
    [42.3601, -71.0589, 0.6],     # Boston, USA
    [39.9042, 32.8597, 0.5],      # Ankara, Turkey
    [40.7128, -74.0060, 0.8],     # New York City, USA
    [43.0742, -89.3833, 0.4],     # Madison, USA
    [39.9042, 32.8597, 0.5],      # Ankara, Turkey
    [41.8781, -87.6298, 0.6],     # Chicago, USA
    [48.8566, 2.3522, 0.3],       # Paris, France
    [55.6761, 12.5683, 0.3],      # Copenhagen, Denmark
    [52.3676, 4.9041, 0.3],       # Amsterdam, Netherlands
    [40.4168, -3.7038, 0.6],      # Madrid, Spain
    [37.5665, 126.978, 0.6],      # Seoul, South Korea
    [19.4326, -99.1332, 0.6],     # Mexico City, Mexico
    [13.0827, 80.2707, 0.5],      # Chennai, India
    [-33.8688, 151.2093, 0.7],    # Sydney, Australia
    [1.3521, 103.8198, 0.4],      # Singapore
    [55.9533, -3.1883, 0.5],      # Edinburgh, Scotland
    [39.9042, 32.8597, 0.5],      # Ankara, Turkey
    [-23.5505, -46.6333, 0.5],    # São Paulo, Brazil
    [31.7683, 35.2137, 0.7],      # Jerusalem, Israel
    [6.5244, 3.3792, 0.5],        # Lagos, Nigeria
    [45.4215, -75.6972, 0.4],     # Ottawa, Canada
    [55.7558, 37.6176, 0.6],      # Moscow, Russia
    [30.7333, 76.7794, 0.4],      # Chandigarh, India
    [22.5726, 88.3639, 0.4],      # Kolkata, India
    [12.9716, 77.5946, 0.5],      # Bengaluru, India
    [17.385044, 78.486671, 0.7],  # Hyderabad, India
    [-26.2041, 28.0473, 0.5],     # Johannesburg, South Africa
    [43.6511, -79.347015, 0.6],   # Toronto, Canada
    [38.7223, -9.1399, 0.5],      # Lisbon, Portugal
    [55.9533, -3.1883, 0.5],      # Edinburgh, Scotland
    [49.2827, -123.1207, 0.4],    # Vancouver, Canada
    [59.9343, 30.3351, 0.4],      # Saint Petersburg, Russia
    [45.4654, 9.1859, 0.6],       # Milan, Italy
    [42.3601, -71.0589, 0.6],     # Boston, USA
    [39.9042, 32.8597, 0.5],      # Ankara, Turkey
    ]
    plugins.HeatMap(green_gasdata, radius=25).add_to(m)
    return render_template('m.html')

if __name__ == "__main__":
    app.run(debug=True, port=1456)