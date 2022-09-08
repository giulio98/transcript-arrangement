import itertools


def subset_sum(weigths, target, partial={}, res=[]):
    s = sum(partial.values())

    # check if the partial sum is equals to target
    if s == target:
        res.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(weigths.values())):
        n = dict(itertools.islice(weigths.items(), i, len(weigths.values()), len(weigths.values())))
        remaining = dict(itertools.islice(weigths.items(), i + 1, len(weigths.values()), 1))
        new = {}
        for d in (partial, n):
            new.update(d)
        subset_sum(remaining, target, new, res)


def get_disjoint_two_set(all_combinations):
    dis_comb = []
    for i, j in itertools.combinations(all_combinations, 2):
        # an empty set is True, a nonempty set is False
        if not set(i).intersection(set(j)):
            dis_comb.append((i, j))
    return dis_comb


def get_maximum_score(filtered_comb, subject_grade, num_ects_per_block=25):
    best = filtered_comb[0]
    best_score = 0
    for comb in filtered_comb:
        first_weighted_sum = {k: comb[0].get(k, 0) * subject_grade.get(k, 0) for k in set(comb[0]) & set(subject_grade)}
        second_weighted_sum = {k: comb[1].get(k, 0) * subject_grade.get(k, 0) for k in set(comb[1]) & set(subject_grade)}
        first_block = sum(first_weighted_sum.values()) / sum(comb[0].values())
        second_block = sum(second_weighted_sum.values()) / sum(comb[1].values())
        poli_first_block = first_block * 1.8
        poli_second_block = second_block * 1.8
        if poli_first_block > 30:
            poli_first_block = 30
        if poli_second_block > 30:
            poli_second_block = 30
        if round(poli_first_block) + round(poli_second_block) > best_score:
            best_score = round(poli_first_block) + round(poli_second_block)
            best = comb
    return best


if __name__ == '__main__':
    # {<subject_name> : <ects_weight>}
    subject_weight = {'clouds': 5, 'malis': 5, 'dbsys': 5, 'stats': 2.5, 'quantis': 2.5, 'optim': 2.5,
                      'aml': 2.5, 'improc': 2.5, 'semproj': 10, 'asi': 5, 'deep': 2.5, 'malcom': 5}
    # insert below your eurecom grades(20esimi)
    # {<subject_name> : <grade>}
    subject_grade = {'clouds': 0, 'malis': 0, 'dbsys': 0, 'stats': 0, 'quantis': 0, 'optim': 0,
                     'aml': 0, 'improc': 0, 'semproj': 0, 'asi': 0, 'deep': 0, 'malcom': 0}
    credits_per_block = 25
    all_combinations = []
    subset_sum(subject_weight, credits_per_block, res=all_combinations)
    filtered_comb = get_disjoint_two_set(all_combinations)
    best = get_maximum_score(filtered_comb, subject_grade)
    print("The best arrangement is:")
    print("===============================================")
    print("FIRST BLOCK")
    for key, value in best[0].items():
        print(key)
    weighted_sum = {k: best[0].get(k, 0) * subject_grade.get(k, 0) for k in set(best[0]) & set(subject_grade)}
    first_block = sum(weighted_sum.values()) / sum(best[0].values())
    print("===============================================")
    print("EURECOM average: ", first_block)
    print("Poli average: ", first_block * 1.8, ", which round up to: ", round(first_block * 1.8))
    print("===============================================")
    print("===============================================")
    print("SECOND BLOCK")
    for key, value in best[1].items():
        print(key)
    second_weighted_sum = {k: best[1].get(k, 0) * subject_grade.get(k, 0) for k in set(best[1]) & set(subject_grade)}
    second_block = sum(second_weighted_sum.values()) / sum(best[1].values())
    print("===============================================")
    print("EURECOM average: ", second_block)
    print("Poli average: ", second_block * 1.8, ", which round up to: ", round(second_block * 1.8))
    print("===============================================")


