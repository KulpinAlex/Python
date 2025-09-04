import os
import time
import asyncio
import aiohttp
from prettytable import PrettyTable
from pathlib import Path


async def download_img(link, filename, links, status_arr):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                if response.status == 200:
                    with open(filename, 'wb') as f:
                        f.write(await response.read())
                    links.append(link)
                    status_arr.append('Успех')
                else:
                    links.append(link)
                    status_arr.append('Ошибка')
    except:
        links.append(link)
        status_arr.append('Ошибка')


def print_table(link_arr, status_arr):
    requests_table = PrettyTable()
    requests_table.field_names = ['Ссылка', 'Статус']
    requests_table.align['Ссылка'] = 'l'
    requests_table.add_rows([link_arr[i], status_arr[i]] for i in range(len(link_arr)))
    print(requests_table)


def get_file_path():
    result = input()
    if Path(result).exists() and Path(result).is_dir() and os.access(result, os.W_OK):
        return result
    else:
        return get_file_path()


async def async_input():
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input)


async def main():
    start_time = time.time()
    status_arr = []
    links = []
    file_path = get_file_path()
    i = 0
    tasks = []
    while True:
        link = await async_input()
        if not link:
            if any(task.done() == False for task in tasks):
                print('задачи еще не завершены')
            break
        task = asyncio.create_task(download_img(link, f'{file_path}/{i}.jpg', links, status_arr))
        tasks.append(task)
        i += 1

    await asyncio.gather(*tasks)

    print_table(links, status_arr)
    print("Work time = %.2f" % (time.time() - start_time))


if __name__ == '__main__':
    asyncio.run(main())
