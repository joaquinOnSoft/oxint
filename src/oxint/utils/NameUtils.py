class NameUtils:

    @staticmethod
    def get_first_name_from_full_name(full_name: str) -> str:
        first_name = None

        if full_name is not None:
            tokens = full_name.split(" ")
            num_tokens = len(tokens)
            if num_tokens == 3:
                first_name = tokens[0]
            elif num_tokens >= 4:
                first_name = tokens[0] + " " + tokens[1]

        return first_name

    @staticmethod
    def get_last_name_from_full_name(full_name: str) -> str:
        last_name = None

        if full_name is not None:
            tokens = full_name.split(" ")
            num_tokens = len(tokens)
            if num_tokens == 3:
                last_name = tokens[1] + " " + tokens[2]
            elif num_tokens >= 4:
                last_name = ""
                for count in range(2, num_tokens):
                    last_name += tokens[count]
                    if count < (num_tokens -1):
                        last_name += " "

        return last_name

    @staticmethod
    def get_party_name_from_title(title: str) -> str:
        name = None

        if title is not None:
            index_parenthesis = title.find("(")
            if index_parenthesis > 0:
                name = title[0: index_parenthesis].strip()

        return name

    @staticmethod
    def get_party_abbrev_from_title(title: str) -> str:
        name = None

        if title is not None:
            index_parenthesis = title.find("(") + 1
            if index_parenthesis > 0:
                name = title[index_parenthesis:].replace(")", "")

        return name

