def get_statistics(numbers: list[int]) -> dict:
    stat_dict: dict = {
    }
    stat_dict.update({"SUM": sum(numbers)})
    stat_dict.update({"MIN": min(numbers)})
    stat_dict.update({"MAX": max(numbers)})
    avg: float = sum(numbers) / len(numbers)
    stat_dict.update({"AVG": avg})
    return stat_dict


print(f"Statistics are: {get_statistics([30, 40, 2, 100, 33])}")
