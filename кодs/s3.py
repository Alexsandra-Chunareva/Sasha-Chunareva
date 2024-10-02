def main():
    import datetime
    from time import sleep
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    for _ in range(5):
        print(current_time)
        sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

if __name__ == '__main__':
    main()