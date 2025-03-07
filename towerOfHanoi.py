r1 = [1,2,3,4,5]
r2 = []
r3 = []

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        # Move a single disk from source to destination
        disk = source.pop()
        destination.append(disk)
        print(f"Move disk {disk} from {source} to {destination}")
    else:
        # Move n-1 disks from source to auxiliary rod using destination as auxiliary
        tower_of_hanoi(n-1, source, destination, auxiliary)

        # Move the nth disk from source to destination
        disk = source.pop()
        destination.append(disk)
        print(f"Move disk {disk} from {source} to {destination}")

        # Move the n-1 disks from auxiliary to destination using source as auxiliary
        tower_of_hanoi(n-1, auxiliary, source, destination)
tower_of_hanoi(5,r1,r2,r3)
print(r1,r2,r3)
