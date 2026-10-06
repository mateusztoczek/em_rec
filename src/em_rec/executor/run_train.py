import argparse

def parse_args():
    run_parser= argparse.ArgumentParser()
    run_parser.add_argument("config", type=str)

    return run_parser.parse_args()

def run_train_job(config):
    exec_config= load_config(config)

    ds=load_dataset(config.dataset)
    save_results(ds,config)


def main():
    run_args= parse_args()
    run_train_job(run_args.config)

if __name__ == "__main__":
    main()