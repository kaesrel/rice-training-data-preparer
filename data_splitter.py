import os, random
import math
import config
import preprocess_state as state

class DataSplitter:
    def __init__(self) -> None:
        pass

    def split_data(self, class_name):
        train = config.train
        valid = config.valid
        test = config.test
        if not math.isclose(train+valid+test, 1.0, rel_tol=1e-5):
            print("What the heck???")
            return None


        random.seed(config.random_seed)

        files = os.listdir(f"{config.folder['output']}/{class_name}")
        random.shuffle(files, random.random)

        beg = 0
        end = int(len(files)*train)
        state.train_files = files[beg:end]
        beg = end
        end = int(len(files)*(train + valid))
        state.valid_files = files[beg:end]
        beg = end
        end = int(len(files)*(train + valid + test))
        state.test_files = files[beg:end]


        # print(f"{state.train_files} | {state.valid_files} | {state.test_files}")




datasplitter = DataSplitter()


# if __name__ == "__main__":
#     datasplitter.split_data(0.6, 0.2, 0.2)