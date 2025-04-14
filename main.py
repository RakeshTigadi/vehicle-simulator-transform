import random
import asyncio
from datetime import datetime

vins = ['VIN001', 'VIN002', 'VIN003']

# This function is required by Condense to start the logic
async def start():
    while True:
        for vin in vins:
            data = {
                "vin": vin,
                "speed": round(random.uniform(30, 100), 2),
                "timestamp": datetime.utcnow().isoformat()
            }
            await output.send(data)
            print(f"✅ Emitted: {data}")
        await asyncio.sleep(5)  # emit every 5 seconds
