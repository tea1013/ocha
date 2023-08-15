import matplotlib.pyplot as plt


class ExperimentObserver:
    def __init__(
        self,
        exp_name: str,
        epoch: int,
        description: str,
    ) -> None:
        self.exp_name = exp_name
        self.epoch = epoch
        self.description = description

        self.train_losses = []
        self.valid_losses = []
        self.train_scores = []
        self.valid_scores = []

    def append(
        self,
        train_loss: float,
        valid_loss: float,
        train_score: float,
        valid_score: float,
    ) -> None:
        self.train_losses.append(train_loss)
        self.valid_losses.append(valid_loss)
        self.train_scores.append(train_score)
        self.valid_scores.append(valid_score)

    def plot(self, save_path: str) -> None:
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 7))

        ax[0].plot(range(1, self.epoch + 1), self.train_losses, label="train")
        ax[0].plot(range(1, self.epoch + 1), self.valid_losses, label="valid")
        ax[0].set_xlabel("Epoch", fontsize=14)
        ax[0].set_ylabel("Loss", fontsize=14)
        ax[0].grid(color="black", linestyle="-", linewidth=0.1)
        ax[0].tick_params(labelsize=14)
        ax[0].legend(fontsize=14)

        ax[1].plot(range(1, self.epoch + 1), self.train_scores, label="train")
        ax[1].plot(range(1, self.epoch + 1), self.valid_scores, label="valid")
        ax[1].set_xlabel("Epoch", fontsize=14)
        ax[1].set_ylabel("Score", fontsize=14)
        ax[1].grid(color="black", linestyle="-", linewidth=0.1)
        ax[1].tick_params(labelsize=14)
        ax[1].legend(fontsize=14)

        fig.suptitle(f"{self.exp_name}\n{self.description}", fontsize=14)

        plt.savefig(save_path)
