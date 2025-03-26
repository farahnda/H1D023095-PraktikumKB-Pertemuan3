import random
import datetime

tasks = []  
def tambahTask(task):
    dataTask = {
        "id": random.randint(100, 999),  
        "task": task,
        "date_added": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(dataTask)
    print(f"Tugas '{task}' berhasil ditambahkan!")

def lihatTasks():
    if not tasks:
        print("Tidak ada tugas saat ini.")
        return
    print("\nDaftar Tugas:")
    for task in tasks:
        print(f"[ID: {task['id']}] {task['task']} - Ditambahkan pada {task['date_added']}")

def hapusTask(task_id):
    global tasks
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Tugas dengan ID {task_id} berhasil dihapus!")
            return
    print("Tugas tidak ditemukan!")

while True:
    print("\nMenu:")
    print("1. Tambah Tugas")
    print("2. Lihat Daftar Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")
    
    choice = input("Pilih opsi: ")
    
    if choice == "1":
        namaTask = input("Masukkan nama tugas: ")
        tambahTask(namaTask)
    elif choice == "2":
        lihatTasks()
    elif choice == "3":
        try:
            task_id = int(input("Masukkan ID tugas yang ingin dihapus: "))
            hapusTask(task_id)
        except ValueError:
            print("Masukkan ID yang valid!")
    elif choice == "4":
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")