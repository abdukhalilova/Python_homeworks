# 1. is_prime(n) funksiyasini hosil qiling(n>0). Agar n soni tub bolsa true, aks holsa False qiymat qaytarsin.
def is_prime(n):
    if n%2==1:
        return True
    else:
        return False
print(is_prime(int(input("Enter a number: "))))

# 2. k sonining raqamlari yig'indisini hisoblovchi digit_sum(k) rekursiv funksiya tuzing
def digit_sum(k):
    dsum = 0
    for i in k:
        dsum +=int(i)
    return dsum
print(digit_sum((input("Enter a number: "))))

# 3. It is required to print all integer powers of two (that is, numbers of the form 2**k) that do not exceed the number N.
def power_of_2(a):
    i = 1
    while True:
        if 2**i<=a:
           print (2**i)
        else:
            break
        i+=1
power_of_2(int(input("Enter a number: ")))


