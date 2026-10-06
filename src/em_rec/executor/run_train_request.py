import argparse
import re

from em_rec.requests.loader import load_request_config

DATASET_NAME_PATTERN_FIX=re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$")


def parse_args():
    run_parser= argparse.ArgumentParser()
    run_parser.add_argument("request_source_path", type=str)

    return run_parser.parse_args()


def validate_dataset_name(value: object) -> None:
    if not isinstance(value, str):
        raise ValueError("Dataset name is not a string")
    if not value.strip():
        raise ValueError("Dataset name is empty")
    if not DATASET_NAME_PATTERN_FIX.fullmatch(value):
        raise ValueError("Invalid dataset name")


def validate_dataset_version(value:object)->None: 
    if not isinstance(value, int):
        raise ValueError("Dataset version not a number")
    if not 0<= value <=99:
        raise ValueError("Dataset version must be in range between 0 and 99")


def validate_dataset_config(dataset: object) ->None:
    if not isinstance(dataset, dict):
        raise ValueError("Dataset not found")
    validate_dataset_name(dataset.get("name"))
    validate_dataset_version(dataset.get("version"))


def validate_request_config(request_data: object) -> None:
    if not isinstance(request_data, dict):
        raise ValueError("Request config is invalid")
    validate_dataset_config(request_data.get("dataset"))



def run_train_request(request_path):
    request_data= load_request_config(request_path)
    validate_request_config(request_data=request_data)
    ds=load_dataset(ds_config)


def main():
    run_args= parse_args()
    run_train_request(run_args.request_source_path)

if __name__ == "__main__":
    main()