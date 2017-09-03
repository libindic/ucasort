from .core import Sort

def ucasort_sort(text):
    sobject = Sort()
    return sobject.sort(text)

def sort():
    return [ucasort_sort, str, {str: [str]}]

