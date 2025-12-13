from time import sleep
import subprocess

# UUID of the SSD
TARGET_UUID = "8EE1-24E9"
TARGET_MOUNTPOINT = "/mnt/tseven"

def get_uuids():
    try:
        output = subprocess.check_output(['lsblk', '-o', 'UUID', '-nr'], text = True)
        if TARGET_UUID in output:
            return output
        else:
            print(f"USB Mass Device: {TARGET_UUID} Not Found!")
    except subprocess.CalledProcessError as e:
        print(f"Error While Checking UUIDs: {e}")
        return False
        
def is_mounted():
    if TARGET_MOUNTPOINT in subprocess.check_output(['lsblk', '-o', 'MOUNTPOINT', '-nr'], text = True):
        return True
    else:
        return False


def mount_usb_mass_device():
    uuids = get_uuids()
    if TARGET_UUID in uuids:
        try:
            subprocess.run(['sudo' ,'mount' ,'/mnt/tseven'], check = True)
            return True
        except subprocess.CalledProcessError:
            return False
    else:
        print(f"USB Mass Device: {TARGET_UUID} Not Found!")
        return False

def main():
    while True:
        if not is_mounted():
            if mount_usb_mass_device():
                print(f"USB Mass Device: {TARGET_UUID} Mounted Successfully at mountpoint: /mnt/tseven. Next check in 90s.")
                sleep(90)
            else:
                print(f"USB Mass Device: {TARGET_UUID} Mount Failed! Next check in 10s.")
                sleep(10)
        else:
            print(f"USB Mass Device: {TARGET_UUID} Already Mounted at {TARGET_MOUNTPOINT}. Next check in 90s.")
            sleep(90)

if __name__ == "__main__":
    main()
