import asyncio
from bleak import BleakClient

async def send_data(address, data):
    """
    函数简介：
    通过蓝牙将数据发送到设备
    address: 蓝牙设备的地址
    data: 要发送的数据
    注：下面有一个叫做'characteristic_uuid'的东西要替换成您自己设备的UUID！
    """
    async def run(address, data):
        async with BleakClient(address) as client:
            print(f"连接到设备 {address}")
            #查找特征 UUID，需要替换为你设备的特征 UUID
            characteristic_uuid = '0000xxxx-0000-1000-8000-00805f9b34fb'
            #发送数据
            await client.write_gatt_char(characteristic_uuid, data.encode())
            print(f"数据 '{data}' 已发送到 {address}")

    #循环
    asyncio.run(run(address, data))