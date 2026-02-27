import asyncio


async def write_number(filename,n):
    with open(filename,"w") as file:
        for i in range(1,n+1):
            file.write(str(i)+"\n")
            await asyncio.sleep(1)


async def main():
    t1 = write_number("Task1.txt",10)
    t2 = write_number("Task2.txt",10)
    t3 = write_number("Task3.txt",10)

    await asyncio.gather(t1,t2,t3)

asyncio.run(main())

