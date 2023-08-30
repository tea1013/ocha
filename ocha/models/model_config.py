import os
from abc import ABC, abstractmethod


class ModelConfig(ABC):
    save_dir: str
    save_file_name: str
    model_file_type: str

    @abstractmethod
    def model_params(self) -> dict:
        pass

    @property
    def save_model_path(self) -> str:
        os.makedirs(f"./models/{self.save_dir}", exist_ok=True)
        return f"./models/{self.save_dir}/{self.save_file_name}.{self.model_file_type}"

    @property
    def save_metrics_path(self) -> str:
        os.makedirs(f"./metrics/{self.save_dir}", exist_ok=True)
        return f"./metrics/{self.save_dir}/{self.save_file_name}.npy"

    @property
    def save_scores_path(self) -> str:
        os.makedirs(f"./scores/{self.save_dir}", exist_ok=True)
        return f"./scores/{self.save_dir}/{self.save_file_name}.npy"

    @property
    def save_params_path(self) -> str:
        os.makedirs(f"./params/{self.save_dir}", exist_ok=True)
        return f"./params/{self.save_dir}/{self.save_file_name}.pickle"
