#Задача "Потоковая запись в файлы":
#Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её
import time
import threading

#Необходимо создать функцию write_words(word_count, file_name)

def write_words(word_count, file_name: str):

    #word_count - количество записываемых слов,
    #file_name - название файла, куда будут записываться слова.

    with open(file_name, 'w', encoding='utf-8') as file:

    #Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>"
    # в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
        for i in range(word_count + 1):
            if i == 0:
                continue
            time.sleep(0.1)
            file.write(f'Какое-то слово № {i}' + '\n')


    #В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

        print(f'Завершилась запись в файл {file_name}')

#Также измерьте время затраченное на выполнение функций и потоков.

time_start_f = time.time()

#После создания файла вызовите 4 раза функцию write_words

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end_f = time.time()
time_elapsed_f = time_end_f - time_start_f
print(f'Работа функций {time_elapsed_f}')

time_start_t = time.time()

#После вызовов функций создайте 4 потока для вызова этой функции

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

#Запустите эти потоки методом start
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

#сделать остановку основного потока при помощи join.
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time_end_t = time.time()
time_elapsed_t = time_end_t - time_start_t
print(f'Работа потоков {time_elapsed_t}')










