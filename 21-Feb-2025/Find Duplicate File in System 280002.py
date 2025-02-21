# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict

class Solution:
    def find_duplicate_files(self, paths):
        content_to_paths = defaultdict(list)

        for path in paths:
            parts = path.split(' ')
            dir_path = parts[0]

            for file in parts[1:]:
                file_name, file_content = file.split('(')
                file_content = file_content[:-1]
                full_file_path = dir_path + "/" + file_name

                content_to_paths[file_content].append(full_file_path)

        return [file_paths for file_paths in content_to_paths.values() if len(file_paths) > 1]
