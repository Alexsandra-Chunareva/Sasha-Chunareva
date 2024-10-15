def week_info(*args):
  days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  gain = list(map(int, input("Введите данные через пробел: ").split()))

  if len(gain) != 7:
    print('Неверное количество дней, их должно быть 7')
  else:
    max_gain = max(gain)
    max_day = days_of_week[gain.index(max_gain)]

    min_gain = min(gain)
    min_day = days_of_week[gain.index(min_gain)]

    weekly_gain = int(sum(gain))
    average_gain = int(sum(gain) / len(gain))

    print(
    f"Максимально прибыльный день: {max_gain} в ({max_day})\n"
    f"Минимальная прибыльный день: {min_gain} в ({min_day})\n"
    f"Средняя прибыль за неделю: {average_gain}\n"
    f"Общаяя прибыль: {weekly_gain}"
    )

week_info()