from urllib.parse import urlparse

def get_schemes_helper(input):
    output = [urlparse(x)[0] for x in input]
    return output

def get_domains_helper(input):
    output = [urlparse(x)[1] for x in input]
    return output

def get_paths_helper(input):
    # output = input.apply(lambda x: urlparse(x)[2]) # 14k rows - 0.28s
    output = [urlparse(x)[2] for x in input] # 14k rows - 0.44s
    return output

def get_params_helper(input):
    output = [urlparse(x)[3] for x in input]
    return output

def get_queries_helper(input):
    output = [urlparse(x)[4] for x in input]
    return output

def get_directories_from_path_helper(paths):
    # function splits the “path” column into a list of directories.
    output = [x.strip('/').split('/') for x in paths]
    # output = paths.str.strip('/').str.split('/')
    return output    
