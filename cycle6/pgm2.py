fn = open("D:\FILE.txt", "r")

fn1 = open("D:\ newfile.txt", "w")

cont = fn.readlines()
type(cont)
print(len(cont))
for i in range(0, len(cont), 2):
    fn1.write(cont[i])

fn1.close()

fn1 = open("D:\ newfile.txt", 'r')
print (fn1.read())


fn.close()
fn1.close()