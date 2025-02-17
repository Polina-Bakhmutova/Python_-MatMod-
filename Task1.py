a01 = 445423
c1 = 90474281
M = 2**31
beta1 = max(c1, M - c1)

a02 = 275803775
c2 = 42062397
beta2 = max(c2, M - c2)

K = 160

# Мультипликативный конгруэнтный метод
def mkm(a0, beta, M, n):
    sequence = [0] * n  
    sequence[0] = a0
    for i in range(1, n):
        sequence[i] = (sequence[i-1] * beta) % M
    return sequence

# Метод Макларена-Марсальи
def maclaren_marsaglia(D1, D2, K, n):
    R = [0] * K  
    sequence = [0] * n  
    for i in range(K):
        R[i] = D1[i]
    for i in range(n):
        j = D2[i] % K
        sequence[i] = R[j]
        if i + K < len(D1):
            R[j] = D1[i + K]
        else:
            R[j] = D2[i + K - len(D1)]
    return sequence


def main():
    n = 1000

    sequence_mkm1 = mkm(a01, beta1, M, n)
    sequence_mkm2 = mkm(a02, beta2, M, n)

    sequence_maclaren_marsaglia = maclaren_marsaglia(sequence_mkm1, sequence_mkm2, K, n)

    mkm_results = sequence_mkm1[99], sequence_mkm1[899], sequence_mkm1[999]
    marsaglia_results = sequence_maclaren_marsaglia[99], sequence_maclaren_marsaglia[899], sequence_maclaren_marsaglia[999]

    print("МКМ результаты:")
    print(f"100-й элемент: {mkm_results[0]}")
    print(f"900-й элемент: {mkm_results[1]}")
    print(f"1000-й элемент: {mkm_results[2]}")

    print("\nМетод Макларена-Марсальи результаты:")
    print(f"100-й элемент: {marsaglia_results[0]}")
    print(f"900-й элемент: {marsaglia_results[1]}")
    print(f"1000-й элемент: {marsaglia_results[2]}")

if __name__ == "__main__":
    main()
