"""
Utility methods for form_network.py
Generating graph content
Writing results files
Initing results files
"""

from constants import RESULT_PREFIX
import xlwt as xlwt
import xlrd

def generate_graph(graph, datasheet):
    """
    columns are 6 and 10, 14 for actor2 and actor1 and actor 3 respectively
    """
    for row in range(1, datasheet.nrows):
        data = datasheet.row_slice(row)
        actor1 = data[6].value
        actor2 = data[10].value
        actor3 = data[14].value
        graph.add_edges_from([(actor1, actor2), (actor1, actor3)])
        graph.add_edges_from([(actor2, actor3)])


def generate_rank_dict(datasheet):
    """
    columns 10 for actor, column 25 for imdb score
    """
    rank_dict = {}
    without_one_movie_stars = {}
    rank = 0
    count = 0
    target_column = 10     # This example only has 1 column, and it is 0 indexed
    temp_actor = "Lauri"

    data = [datasheet.row_values(i) for i in range(datasheet.nrows)]
    labels = data[0]    # Don't sort our headers
    data = data[1:]     # Data begins on the second row
    data.sort(key=lambda x: x[target_column])

    bk = xlwt.Workbook()
    sheet = bk.add_sheet(datasheet.name)

    for idx, label in enumerate(labels):
        sheet.write(0, idx, label)

    for idx_r, row in enumerate(data):
        for idx_c, value in enumerate(row):
            sheet.write(idx_r+1, idx_c, value)
    
    bk.save('results/results.xls')

    datasheet = xlrd.open_workbook('results/results.xls')
    datasheet = datasheet.sheet_by_index(0)
    for row in range(1, datasheet.nrows):
        data = datasheet.row_slice(row)
        actor = data[10].value
        data = data[25].value
        data = data.replace(" ", "")
        if actor not in rank_dict.keys():
            if temp_actor != actor:
                if count == 0:
                    count = 1
                rank_dict[temp_actor] = rank / count
                if count > 3:
                    without_one_movie_stars[temp_actor] = rank / count
                #print(temp_actor, " ", rank_dict[temp_actor])
                rank = 0
                count = 0
        rank = rank + float(data)
        #print(actor, " ", rank)
        count = count + 1
        temp_actor = actor
    rank_dict.pop('Lauri', None)

    print(
        "Top 10 rated actors: ",
        {
            k: v
            for k, v in sorted(
                #rank_dict.items(), key=lambda item: item[1], reverse=True
                without_one_movie_stars.items(), key=lambda item: item[1], reverse=True
            )[:10]
        },
    )
    print(
        "Bottom 10 rated actors: ",
        {
            k: v
            for k, v in sorted(
                #rank_dict.items(), key=lambda item: item[1], reverse=False
                without_one_movie_stars.items(), key=lambda item: item[1], reverse=False
            )[:10]
        },
    )
    print("\n\n", rank_dict)
    return rank_dict


def generate_genre_graph(graph, datasheet):
    """
    Columns used for generating genre graphs are:
    11, for Movie title, 6, 10 and 14 for actors
    """
    for row in range(1, datasheet.nrows):
        data = datasheet.row_slice(row)
        movie = data[11].value
        actor1 = data[6].value
        actor2 = data[10].value
        actor3 = data[14].value
        graph.add_edges_from([(movie, actor1), (movie, actor2), (movie, actor3)])


def write_result(output_file, content):
    """
    Writes the outcome of processing into a file
    """

    with open(RESULT_PREFIX + output_file, "a") as file_out:
        if type(content) == dict:
            for key, value in content.items():
                file_out.write("%s: %s " % (key, value))
        else:
            file_out.write(content)


def init_result(inited_file, content):
    """
    Empties the result files
    """
    with open(RESULT_PREFIX + inited_file, "w") as file_init:
        file_init.write(content)


def sort_centralities(dictionary):
    """
    Sorts the given centrality dictionary by descending order
    source of the implementation:
    https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    """
    sorted_dict = ""
    sorted_dict = {
        key: value
        for key, value in sorted(
            dictionary.items(), key=lambda item: item[1], reverse=True
        )
    }
    return sorted_dict

def normalize(something):
            xmin = min(something)
            xmax = max(something)
            for i, x in enumerate(something):
                something[i] = (x-xmin) / (xmax-xmin) 
            return something