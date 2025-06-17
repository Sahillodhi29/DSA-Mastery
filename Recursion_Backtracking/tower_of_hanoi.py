def hanoi(n, src, helper, dest):
    if n == 1:
        print("move disk 1 from",src," to ",dest)
        return

    hanoi(n-1,src,dest,helper)
    
    print(f"Move disk {n} from {src} to {dest}")
    
    hanoi(n-1,helper,src, dest)
    
hanoi(3,'A','B','C')