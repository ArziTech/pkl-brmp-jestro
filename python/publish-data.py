import time
import random
import json
from datetime import datetime
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/rainfall"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

location = "Malang"

try:
    while True:
        rainfall = round(random.uniform(0, 150), 2)
        created_at = datetime.now().isoformat()

        payload = {
            "location": location,
            "value": rainfall,
            "created_at": created_at
        }

        # Kirim ke MQTT
        client.publish("sensor/rainfall", json.dumps(payload))

        # Cetak hanya jam:menit:detik agar mudah dibaca
        print(f"📤 {datetime.now().strftime('%H:%M:%S')} | "
              f"Data terkirim ke sensor/rainfall lokasi={location}, "
              f"curah_hujan={rainfall} mm")

        humidity = round(random.uniform(0, 150), 2)
        created_at = datetime.now().isoformat()

        payload = {
            "location": location,
            "value": humidity,
            "created_at": created_at
        }

        # Kirim ke MQTT
        client.publish("sensor/humidity", json.dumps(payload))

        # Cetak hanya jam:menit:detik agar mudah dibaca
        print(f"📤 {datetime.now().strftime('%H:%M:%S')} | "
              f"Data terkirim ke sensor/humidity: lokasi={location}, "
              f"humidity={humidity}") 

        soil_moisture = round(random.uniform(0, 150), 2)
        created_at = datetime.now().isoformat()

        payload = {
            "location": location,
            "value": soil_moisture,
            "created_at": created_at
        }

        # Kirim ke MQTT
        client.publish("sensor/soil_moisture", json.dumps(payload))

        # Cetak hanya jam:menit:detik agar mudah dibaca
        print(f"📤 {datetime.now().strftime('%H:%M:%S')} | "
              f"Data terkirim ke sensor/soil_moisture: lokasi={location}, "
              f"soil_moisture={soil_moisture}") 

        time.sleep(60)  # tunggu 1 menit
except KeyboardInterrupt:
    print("\n⏹ Dihentikan oleh user")
    client.disconnect()
