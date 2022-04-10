seq_len = 200
features = []
for review in review_ints:
    review_len = len(review)
    len_diff = seq_len - review_len
    if len_diff <= 0:
        features.append(review[:seq_len])
        print(review[:seq_len])
    else:
        padding = [0] * len_diff
        padded_feature = padding + review
        features.append(padded_feature)
print()
features = np.asarray(features)
