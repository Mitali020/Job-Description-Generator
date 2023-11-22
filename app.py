from flask import Flask
from main import JobDescriptionGenerator

app = Flask(__name__)

# Path to the configuration file
config_file_path = 'config.json'

# Create an instance of JobDescriptionGenerator using the config file path
generator = JobDescriptionGenerator(config_file_path)

@app.route('/test', methods=['GET'])
def test():
    """Endpoint to generate a job description"""
    # Call the generated_job_description method to generate a job description
    output = generator.generated_job_description()
    return output

if __name__ == "__main__":
    # Run the Flask application on host 0.0.0.0 (all available network interfaces) and port 5000
    app.run(host='0.0.0.0', port=5000)
