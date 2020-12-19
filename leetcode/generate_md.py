import sys
from os.path import isfile


class LeetcodeProblem:
    __slots__ = '__name', '__name_link', '__link', '__solution'

    def __init__(self, name: str = "", name_link: str = "", link: str = "", solution: str = ""):
        self.__name = name
        self.__name_link = name_link
        self.__link = link
        self.__solution = solution

    def read_raw(self, filename: str):
        with open(filename) as file:
            lines = file.readlines()
            # 'task_number. task_name' to 'task_name' only
            name_clean = lines[0][lines[0].index(" ")+1:].replace('\n', '')
            self.__name = name_clean
            self.__name_link = name_clean.lower().replace(" ", "-")
            self.__link = lines[1].replace('\n', '')
            self.__solution = "".join(lines[2:])

    def write_to_file(self, filename: str):
        header = f"# {filename.capitalize().replace('.md', '')} \n\n"
        clickable_link = f"+ [{self.__name}](#{self.__name_link})\n\n"
        raw_name_and_link = f"## {self.__name}\n\n{self.__link}\n\n"
        code = f"```python\n{self.__solution}\n```\n"
        if isfile(filename):
            with open(filename) as file:
                lines = file.readlines()
                index_for_clickable_link = 0
                for i, line in enumerate(lines):
                    if line.startswith("##"):
                        index_for_clickable_link = i
                        break
                lines[index_for_clickable_link-1] = clickable_link
                lines.extend(['\n', raw_name_and_link, code])
        else:
            lines = [header, clickable_link, raw_name_and_link, code]
        with open(filename, 'w') as file:
            file.writelines(lines)


if __name__ == "__main__":
    changing_file_name = sys.argv[1]
    print(changing_file_name)
    problem = LeetcodeProblem()
    problem.read_raw('source_leetcode_data.txt')
    problem.write_to_file(f'{changing_file_name}.md')
