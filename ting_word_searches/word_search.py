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
    """Aqui irá sua implementação"""
