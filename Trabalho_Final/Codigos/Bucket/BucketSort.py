
@profile
def bucket_sort(floats):
    buckets = [ [] for _ in range(len(floats)) ]
    for num in floats:
        i = int(len(floats) * num)
        print(buckets)
        buckets[i].append(num)

    result = []
    for bucket in buckets:
        bucket.sort() # INSERTION_SORT(bucket)
        result += bucket
    return result

#print(bucket_sort([0.112, 0.3, 0.008, 0.07, 0.9, 0.8, 0.43, 0.29]))
