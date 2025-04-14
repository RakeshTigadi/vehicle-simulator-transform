import random
import asyncio
from datetime import datetime

# Condense will inject this during runtime
try:
    from condense import output
except ImportError:
    class DummyOutput:
        async def send(self, x):
            print(f"(DEV) Sent: {x}")
    output = DummyOutput()

vins = ['VIN001', 'VIN002', 'VIN003']

async def start():
    while True:
        for vin in vins:
            data = {
                "vin": vin,
                "speed": round(random.uniform(40, 100), 2),
                "timestamp": datetime.utcnow().isoformat()
            }
            await output.send(data)
            print(f"✅ Emitted: {data}")
        await asyncio.sleep(5)
