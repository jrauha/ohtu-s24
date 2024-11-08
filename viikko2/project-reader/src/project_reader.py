from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def _get_dev_dependencies(self, data):
        try:
            dev = data["group"]["dev"]["dependencies"]
            print(dev)
        except KeyError:
            return {}

        return dev

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = toml.loads(content)
        try:
            poetry_data = data["tool"]["poetry"]
        except KeyError as e:
            raise KeyError(f"Poetry data not found: {e}")

        return Project(
            poetry_data.get("name", "-"),
            poetry_data.get("description", "-"),
            poetry_data.get("license", "-"),
            poetry_data.get("authors", {}),
            poetry_data.get("dependencies", {}),
            self._get_dev_dependencies(poetry_data),
        )
