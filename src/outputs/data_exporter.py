thonimport json

class DataExporter:
    def __init__(self, output_file):
        self.output_file = output_file

    def export_data(self, data):
        with open(self.output_file, 'w') as f:
            json.dump(data, f, indent=4)