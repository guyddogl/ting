def exists_word(word, instance):
    result = []
    for index in range(len(instance)):
        file_data = instance.search(index)
        lines = file_data["linhas_do_arquivo"]
        file_name = file_data["nome_do_arquivo"]
        occurrences = [
            {"linha": index + 1}
            for index in range(len(lines))
            if word.lower() in lines[index].lower()
        ]
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                }
            )
    return result


def search_by_word(word, instance):
    result = []
    for file_index in range(len(instance)):
        data = instance.search(file_index)
        lines = data["linhas_do_arquivo"]
        occurrences = [
            {"linha": index + 1, "conteudo": line}
            for index, line in enumerate(lines)
            if word.lower() in line.lower()
        ]
        if len(occurrences):
            result.append(
                {
                    "palavra": word,
                    "arquivo": data["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return result
