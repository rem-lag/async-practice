import asyncio
import aiofiles
import datetime


async def test_fn(x):
    # if x == 3:
    #     raise NameError
    y = x + 1
    await asyncio.sleep(1)
    # await a_sleep()
    # time.sleep(1)
    print(y, datetime.datetime.now())
    return x


async def run_cmd(i):
    proc = await asyncio.create_subprocess_shell(
            'python practice/test_run.py',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    if stderr:
        print(stderr.decode())

    async with aiofiles.open(f'practice/output/run{i}.txt', mode='w') as f:
        await f.write(stdout.decode())


# async def main():
#     args_list = [1,2,3]
#     res = await asyncio.gather(
#         *(test_fn(i) for i in args_list),
#         return_exceptions=True
#     )

#     print(res)

async def main():
    args_list = [1,2,3]
    res = await asyncio.gather(
        *(run_cmd(i) for i in args_list)
    )

    print(res)

if __name__ == '__main__':

    asyncio.run(main())
    # r = []
    # for i in args_list:
    #     c = non_test(i)
    #     r.append(c)
    # print(r)