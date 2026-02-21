from datetime import datetime


def print_current_time():
    now = datetime.now()
    print(f"現在時刻: {now.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    print_current_time()
