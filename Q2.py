def perform_action(action):
    actions_dict = {
        "add": "Adding item",
        "delete": "Deleting item",
        "update": "Updating item"

    }
    return actions_dict.get(action, "Unknown action")

    
result = perform_action("add")
print(result)
