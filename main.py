import itertools


def subset_sum(weigths, target, partial=None, res=None):
    if res is None:
        res = []
    if partial is None:
        partial = {}
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


def get_disjoint_two_set(all_combinations_):
    dis_comb = []
    for i, j in itertools.combinations(all_combinations_, 2):
        # an empty set is True, a nonempty set is False
        if not set(i).intersection(set(j)):
            dis_comb.append((i, j))
    return dis_comb

def get_eurecom_grades(comb, subject_grade_):
    first_weighted_sum_ = {k: comb[0].get(k, 0) * subject_grade_.get(k, 0) for k in set(comb[0]) & set(subject_grade_)}
    second_weighted_sum_ = {k: comb[1].get(k, 0) * subject_grade_.get(k, 0) for k in set(comb[1]) & set(subject_grade_)}
    first_block_ = sum(first_weighted_sum_.values()) / sum(comb[0].values())
    second_block_ = sum(second_weighted_sum_.values()) / sum(comb[1].values())
    return first_block_, second_block_

def get_poli_grades(comb, subject_grade_):
    first_block_, second_block_ = get_eurecom_grades(comb, subject_grade_)
    poli_first_block = first_block_ * 1.8
    poli_second_block = second_block_ * 1.8
    if poli_first_block > 30:
        poli_first_block = 30
    if poli_second_block > 30:
        poli_second_block = 30
    return poli_first_block, poli_second_block

def get_maximum_score(filtered_comb_, subject_grade_):
    best_first = 0
    best_second = 0
    best_ = filtered_comb_[0]
    list_best = []
    min_diff = 30
    for comb in filtered_comb_:
        poli_first_block, poli_second_block = get_poli_grades(comb, subject_grade_)
        if round(poli_first_block) + round(poli_second_block) > best_first + best_second:
            best_first = round(poli_first_block)
            best_second = round(poli_second_block)
            best_ = comb

    # second round
    for comb in filtered_comb_:
        poli_first_block, poli_second_block = get_poli_grades(comb, subject_grade_)
        if round(poli_first_block) == best_first and round(poli_second_block) == best_second:
            list_best.append(comb)

    # balance
    for comb in list_best:
        first_block_, second_block_ = get_eurecom_grades(comb, subject_grade_)
        if (second_block_ - first_block_) < min_diff:
            best_ = comb
            min_diff = second_block_ - first_block_

    return best_


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


