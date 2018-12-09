import pandas as pd

def get_url_list():
    main = "adadf"
    page_n = 30
    out = []
    for i in range(page_n):
        out.append(main + str(i))
    return out


def main_parse(url_list,
               path_to_save):
    # parse
    final_output = []
    for single_url in url_list:
        single_output = single_page(single_url)
        final_output.extend(single_output)

    # save to csv
    df = pd.DataFrame(final_output, columns=[])
    df.to_csv(path_to_save)


def single_page(url):
    """ parse single page """

    output = [
        [price, feature_1, feature_2, feature_3],
        [price, feature_1, feature_2, feature_3],
        .....
    ]
    return output



if __name__ == '__main__':
    url_list = get_url_list()
    main_parse(url_list,
               "./output.csv")