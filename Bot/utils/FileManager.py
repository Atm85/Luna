import json


class FileManager:
    @staticmethod
    def read(file):
        with open(file, "r") as f:
            return json.load(f)

    @staticmethod
    def save(data, file):
        with open(file, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def save_default(file, key):
        data = FileManager.read(file)
        if key not in data:
            data[key] = {}
            data[key]["setup_mode"] = 0
            data[key]["enabled"] = True
            data[key]["channel"] = None
            data[key]["message"] = None
            data[key]["image"] = None
            data[key]["pos"] = "center"
            FileManager.save(data, file)
