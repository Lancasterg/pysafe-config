from example_usage import config


def print_message_n_times():
    for i in range(config.NUM_PRINTS):
        print(f"{config.MESSAGE} {i}")


def main():
    print_message_n_times()


if __name__ == "__main__":
    main()
