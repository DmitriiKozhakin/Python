month_num = int(input('Введите номер месяца от 1 до 12'))
m_list = ['зима', 'весна', 'лето', 'осень']
m_dict = {0: m_list[0], 1: m_list[0], 2: m_list[1], 3: m_list[1], 3: m_list[1],
          4: m_list[2], 5: m_list[2], 6: m_list[2], 7: m_list[3], 8: m_list[3],
          9: m_list[3], 10: m_list[3], 11: m_list[0], }
if 0 < month_num < 13:
    print(m_dict[month_num - 1])
