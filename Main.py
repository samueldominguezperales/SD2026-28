import time

def ciclo():
    cnt = 0
    while True:
        print(f"{cnt}: Ciclo en ejecución...")
        cnt += 1
        time.sleep(1)

if __name__ == "_main_":
    ciclo()