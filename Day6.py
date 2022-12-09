# A floppy disc shows 'f' bytes free and 'u' bytes used. If you delete a file of size 'o' bytes and create a new file of size 'n' bytes,
# then how many free bytes will the floppy disc have?
# f, u, o, n are user entered values.

#Solution:

f=int(input("Enter free disk size in bytes: "))
u=int(input("Enter used disk size in bytes: "))
o=int(input("Enter old file size in bytes: "))
n=int(input("Enter new file size in bytes: "))

totalDiskSize = f+u
currentUsedDiskSize = u-o
currentUsedDiskSize = currentUsedDiskSize + n
currentFreeDiskSize = totalDiskSize - currentUsedDiskSize 

print("Free space available ",currentFreeDiskSize,"bytes")
