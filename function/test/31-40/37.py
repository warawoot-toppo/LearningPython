def find_mean_median_mode(listA):
    import statistics
    meanA = statistics.mean(listA)
    medianA = statistics.median(listA)
    modeA = statistics.mode(listA)
    return meanA ,medianA, modeA

print(find_mean_median_mode([20, 50, 60, 80, 40, 40, 50, 30, 20, 20 ,10]))