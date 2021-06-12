import serial
from datetime import datetime
from db_connection import DatabaseConnection
from email_provider import send_gmail
import os


def main():
    arduino = serial.Serial(port="COM4", baudrate=9600, timeout=.1)
    db = DatabaseConnection()
    previous_signal = ""
    is_email_sent = False
    
    while True:
        signal = arduino.read().decode("utf-8")
        arduino.reset_input_buffer()
        
        if signal != "" and signal != previous_signal:
            db.save(datetime.utcnow().isoformat())
            previous_signal = signal
            breach_time = datetime.utcnow().isoformat()

            if not is_email_sent:
                send_gmail("bandic.bilal.eng@gmail.com", os.environ.get("GMAIL_PASSWORD"), "haruns97hs@gmail.com", "Intrusion detected!!!!!!!", f"Breach made at: {breach_time}")
                is_email_sent = True



if __name__ == "__main__":
    main()